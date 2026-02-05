from __future__ import annotations

import json
import os
import sqlite3
from dataclasses import dataclass
from typing import Any, Dict, Iterator, List, Optional, Sequence, Tuple


@dataclass(frozen=True)
class LedgerRow:
    seq: int
    event_id: str
    event_type: str
    protocol: int
    issued_by: str
    issued_at: int
    payload_hash: str
    payload: Dict[str, Any]
    previous_hash: str | None
    event_hash: str


class LedgerReadError(RuntimeError):
    pass


def _db_connect(db_path: str) -> sqlite3.Connection:
    os.makedirs(os.path.dirname(db_path) or ".", exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def _parse_payload(payload_text: str) -> Dict[str, Any]:
    try:
        obj = json.loads(payload_text)
        if not isinstance(obj, dict):
            raise LedgerReadError("payload must be a JSON object")
        return obj
    except json.JSONDecodeError as e:
        raise LedgerReadError(f"invalid payload JSON: {e}") from e


def tail_events(db_path: str, limit: int = 50) -> List[LedgerRow]:
    if limit <= 0 or limit > 1000:
        raise LedgerReadError("limit must be between 1 and 1000")

    conn = _db_connect(db_path)
    try:
        rows = conn.execute(
            """
            SELECT seq, event_id, event_type, protocol, issued_by, issued_at,
                   payload_hash, payload, previous_hash, event_hash
            FROM ledger_events
            ORDER BY seq DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()

        out: List[LedgerRow] = []
        for r in rows:
            out.append(
                LedgerRow(
                    seq=int(r["seq"]),
                    event_id=str(r["event_id"]),
                    event_type=str(r["event_type"]),
                    protocol=int(r["protocol"]),
                    issued_by=str(r["issued_by"]),
                    issued_at=int(r["issued_at"]),
                    payload_hash=str(r["payload_hash"]),
                    payload=_parse_payload(str(r["payload"])),
                    previous_hash=None if r["previous_hash"] is None else str(r["previous_hash"]),
                    event_hash=str(r["event_hash"]),
                )
            )
        return out
    finally:
        conn.close()


def iter_events(
    db_path: str,
    *,
    start_seq: int = 1,
    end_seq: Optional[int] = None,
    types: Optional[Sequence[str]] = None,
) -> Iterator[LedgerRow]:
    if start_seq < 1:
        raise LedgerReadError("start_seq must be >= 1")
    if end_seq is not None and end_seq < start_seq:
        raise LedgerReadError("end_seq must be >= start_seq")

    conn = _db_connect(db_path)
    try:
        params: List[Any] = [start_seq]
        where = ["seq >= ?"]

        if end_seq is not None:
            where.append("seq <= ?")
            params.append(end_seq)

        if types:
            placeholders = ",".join(["?"] * len(types))
            where.append(f"event_type IN ({placeholders})")
            params.extend(list(types))

        sql = f"""
            SELECT seq, event_id, event_type, protocol, issued_by, issued_at,
                   payload_hash, payload, previous_hash, event_hash
            FROM ledger_events
            WHERE {' AND '.join(where)}
            ORDER BY seq ASC
        """

        cur = conn.execute(sql, tuple(params))
        for r in cur:
            yield LedgerRow(
                seq=int(r["seq"]),
                event_id=str(r["event_id"]),
                event_type=str(r["event_type"]),
                protocol=int(r["protocol"]),
                issued_by=str(r["issued_by"]),
                issued_at=int(r["issued_at"]),
                payload_hash=str(r["payload_hash"]),
                payload=_parse_payload(str(r["payload"])),
                previous_hash=None if r["previous_hash"] is None else str(r["previous_hash"]),
                event_hash=str(r["event_hash"]),
            )
    finally:
        conn.close()


def get_event_by_id(db_path: str, event_id: str) -> Optional[LedgerRow]:
    if not event_id:
        raise LedgerReadError("event_id is required")

    conn = _db_connect(db_path)
    try:
        r = conn.execute(
            """
            SELECT seq, event_id, event_type, protocol, issued_by, issued_at,
                   payload_hash, payload, previous_hash, event_hash
            FROM ledger_events
            WHERE event_id = ?
            LIMIT 1
            """,
            (event_id,),
        ).fetchone()

        if r is None:
            return None

        return LedgerRow(
            seq=int(r["seq"]),
            event_id=str(r["event_id"]),
            event_type=str(r["event_type"]),
            protocol=int(r["protocol"]),
            issued_by=str(r["issued_by"]),
            issued_at=int(r["issued_at"]),
            payload_hash=str(r["payload_hash"]),
            payload=_parse_payload(str(r["payload"])),
            previous_hash=None if r["previous_hash"] is None else str(r["previous_hash"]),
            event_hash=str(r["event_hash"]),
        )
    finally:
        conn.close()

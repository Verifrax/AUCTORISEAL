from __future__ import annotations

import hashlib
import json
import os
import sqlite3
import time
import uuid
from dataclasses import dataclass
from typing import Any, Dict, Optional, Tuple


@dataclass(frozen=True)
class LedgerEvent:
    event_id: str
    event_type: str
    protocol: int
    issued_by: str
    issued_at: int
    payload: Dict[str, Any]


class LedgerWriteError(RuntimeError):
    pass


def _sha256_hex(data: bytes) -> str:
    h = hashlib.sha256()
    h.update(data)
    return h.hexdigest()


def _canonical_json(obj: Any) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def _now_ms() -> int:
    return int(time.time() * 1000)


def _db_connect(db_path: str) -> sqlite3.Connection:
    os.makedirs(os.path.dirname(db_path) or ".", exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def _get_last_event_hash(conn: sqlite3.Connection) -> Optional[str]:
    row = conn.execute(
        "SELECT event_hash FROM ledger_events ORDER BY seq DESC LIMIT 1"
    ).fetchone()
    return None if row is None else str(row["event_hash"])


def _compute_event_hash(
    previous_hash: Optional[str],
    payload_hash: str,
    issued_at: int,
    event_type: str,
    issued_by: str,
    protocol: int,
    event_id: str,
) -> str:
    base = {
        "previous_hash": previous_hash or "",
        "payload_hash": payload_hash,
        "issued_at": issued_at,
        "event_type": event_type,
        "issued_by": issued_by,
        "protocol": protocol,
        "event_id": event_id,
    }
    return _sha256_hex(_canonical_json(base).encode("utf-8"))


def append_event(
    *,
    db_path: str,
    event_type: str,
    protocol: int,
    issued_by: str,
    payload: Dict[str, Any],
    issued_at: Optional[int] = None,
    event_id: Optional[str] = None,
) -> Tuple[int, str]:
    """
    Append a single event to the ledger.

    Returns: (seq, event_hash)

    Strict append-only posture:
    - no UPDATE
    - no DELETE
    - corrections via new events only
    """
    if protocol < 1:
        raise LedgerWriteError("protocol must be >= 1")

    eid = event_id or f"evt_{uuid.uuid4().hex}"
    ts = issued_at if issued_at is not None else _now_ms()

    payload_json = _canonical_json(payload)
    payload_hash = _sha256_hex(payload_json.encode("utf-8"))

    conn = _db_connect(db_path)
    try:
        with conn:
            prev_hash = _get_last_event_hash(conn)
            event_hash = _compute_event_hash(
                prev_hash, payload_hash, ts, event_type, issued_by, protocol, eid
            )

            conn.execute(
                """
                INSERT INTO ledger_events
                    (event_id, event_type, protocol, issued_by, issued_at,
                     payload_hash, payload, previous_hash, event_hash)
                VALUES
                    (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    eid,
                    event_type,
                    protocol,
                    issued_by,
                    ts,
                    payload_hash,
                    payload_json,
                    prev_hash,
                    event_hash,
                ),
            )

            seq = int(conn.execute("SELECT last_insert_rowid()").fetchone()[0])
            return seq, event_hash
    except sqlite3.IntegrityError as e:
        raise LedgerWriteError(f"integrity error appending event: {e}") from e
    finally:
        conn.close()


def build_event(
    *,
    event_type: str,
    protocol: int,
    issued_by: str,
    payload: Dict[str, Any],
    issued_at: Optional[int] = None,
    event_id: Optional[str] = None,
) -> LedgerEvent:
    """
    Construct an event object without writing it. Useful for previews/tests.
    """
    eid = event_id or f"evt_{uuid.uuid4().hex}"
    ts = issued_at if issued_at is not None else _now_ms()
    return LedgerEvent(
        event_id=eid,
        event_type=event_type,
        protocol=protocol,
        issued_by=issued_by,
        issued_at=ts,
        payload=payload,
    )

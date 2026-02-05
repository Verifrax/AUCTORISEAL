from __future__ import annotations

import hashlib
import json
import os
import sqlite3
from dataclasses import dataclass
from typing import Any, Dict, Optional, Tuple

from .reader import LedgerReadError, LedgerRow, iter_events


@dataclass(frozen=True)
class VerificationResult:
    ok: bool
    checked_events: int
    last_seq: int
    last_hash: Optional[str]
    error: Optional[str] = None


class LedgerVerificationError(RuntimeError):
    pass


def _sha256_hex(data: bytes) -> str:
    h = hashlib.sha256()
    h.update(data)
    return h.hexdigest()


def _canonical_json(obj: Any) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


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


def verify_ledger(db_path: str) -> VerificationResult:
    """
    Verify hash chaining across all ledger_events.

    This provides tamper-evidence, not tamper-prevention.
    Any failure MUST be treated as a critical integrity breach.
    """
    checked = 0
    last_seq = 0
    last_hash: Optional[str] = None

    try:
        prev: Optional[str] = None
        for row in iter_events(db_path, start_seq=1):
            expected = _compute_event_hash(
                previous_hash=prev,
                payload_hash=row.payload_hash,
                issued_at=row.issued_at,
                event_type=row.event_type,
                issued_by=row.issued_by,
                protocol=row.protocol,
                event_id=row.event_id,
            )
            if expected != row.event_hash:
                return VerificationResult(
                    ok=False,
                    checked_events=checked,
                    last_seq=row.seq,
                    last_hash=row.event_hash,
                    error=f"hash mismatch at seq={row.seq}: expected {expected} got {row.event_hash}",
                )

            if (row.previous_hash or "") != (prev or ""):
                return VerificationResult(
                    ok=False,
                    checked_events=checked,
                    last_seq=row.seq,
                    last_hash=row.event_hash,
                    error=f"previous_hash mismatch at seq={row.seq}: expected {prev} got {row.previous_hash}",
                )

            prev = row.event_hash
            checked += 1
            last_seq = row.seq
            last_hash = row.event_hash

        return VerificationResult(ok=True, checked_events=checked, last_seq=last_seq, last_hash=last_hash)
    except LedgerReadError as e:
        return VerificationResult(ok=False, checked_events=checked, last_seq=last_seq, last_hash=last_hash, error=str(e))

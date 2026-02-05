from __future__ import annotations

import os
import sqlite3
from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class FreezeState:
    active: bool
    freeze_id: Optional[str]
    issued_by: Optional[str]
    issued_at: Optional[int]
    protocol: Optional[int]


class LedgerRetentionError(RuntimeError):
    pass


def _db_connect(db_path: str) -> sqlite3.Connection:
    os.makedirs(os.path.dirname(db_path) or ".", exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def get_freeze_state(db_path: str) -> FreezeState:
    """
    Returns the currently active freeze state (if any).
    Freeze is modeled as a ledger record; if active=1 exists, issuance must be blocked.
    """
    conn = _db_connect(db_path)
    try:
        row = conn.execute(
            """
            SELECT freeze_id, issued_by, issued_at, protocol, active
            FROM freezes
            WHERE active = 1
            ORDER BY issued_at DESC
            LIMIT 1
            """
        ).fetchone()

        if row is None:
            return FreezeState(active=False, freeze_id=None, issued_by=None, issued_at=None, protocol=None)

        return FreezeState(
            active=bool(int(row["active"])),
            freeze_id=str(row["freeze_id"]),
            issued_by=str(row["issued_by"]),
            issued_at=int(row["issued_at"]),
            protocol=int(row["protocol"]),
        )
    finally:
        conn.close()


def require_not_frozen(db_path: str) -> None:
    """
    Raises if freeze is active. Call this at the start of any issuance/delegation path.
    """
    st = get_freeze_state(db_path)
    if st.active:
        raise LedgerRetentionError(
            f"authority is frozen (freeze_id={st.freeze_id}, issued_by={st.issued_by}, issued_at={st.issued_at})"
        )

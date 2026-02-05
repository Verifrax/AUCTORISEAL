from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from .verifier import VerificationResult, verify_ledger


@dataclass(frozen=True)
class IntegrityStatus:
    ok: bool
    checked_events: int
    last_seq: int
    last_hash: Optional[str]
    error: Optional[str] = None


def check_integrity(db_path: str) -> IntegrityStatus:
    """
    High-level integrity check entrypoint.

    This is the single call that downstream systems and the CLI should use.
    It intentionally fails closed on any inconsistency.
    """
    res: VerificationResult = verify_ledger(db_path)
    return IntegrityStatus(
        ok=res.ok,
        checked_events=res.checked_events,
        last_seq=res.last_seq,
        last_hash=res.last_hash,
        error=res.error,
    )

from __future__ import annotations

import time
import uuid
from dataclasses import dataclass
from typing import Any, Dict, Optional

from ..ledger.writer import append_event
from .formatter import canonicalize_revocation


@dataclass(frozen=True)
class RevokeRequest:
    revoked_seal_id: str
    revoked_by: str
    protocol: int = 1
    reason: str = ""
    notes: Optional[str] = None


@dataclass(frozen=True)
class RevokeResult:
    revocation_id: str
    seq: int
    event_hash: str


class SealRevocationError(RuntimeError):
    pass


def _now_ms() -> int:
    return int(time.time() * 1000)


def revoke_seal(
    *,
    db_path: str,
    req: RevokeRequest,
    revocation_id: Optional[str] = None,
    revoked_at: Optional[int] = None,
) -> RevokeResult:
    """
    Revokes an authority seal by appending an authority.seal_revoked event.
    Revocation is always allowed (even under freeze).
    """
    if req.protocol < 1:
        raise SealRevocationError("protocol must be >= 1")
    if not req.revoked_seal_id or not req.revoked_by:
        raise SealRevocationError("revoked_seal_id and revoked_by are required")

    rid = revocation_id or f"rev_{uuid.uuid4().hex}"
    ts = revoked_at if revoked_at is not None else _now_ms()

    rev_obj: Dict[str, Any] = {
        "revocation_id": rid,
        "revoked_seal_id": req.revoked_seal_id,
        "revoked_by": req.revoked_by,
        "revoked_at": ts,
        "protocol": req.protocol,
        "reason": req.reason,
        "metadata": {"notes": req.notes or ""},
    }

    rev_obj = canonicalize_revocation(rev_obj)

    payload: Dict[str, Any] = {"revocation": rev_obj}

    seq, event_hash = append_event(
        db_path=db_path,
        event_type="authority.seal_revoked",
        protocol=req.protocol,
        issued_by=req.revoked_by,
        payload=payload,
        issued_at=ts,
        event_id=f"evt_{rid}",
    )

    return RevokeResult(revocation_id=rid, seq=seq, event_hash=event_hash)

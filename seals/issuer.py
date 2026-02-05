from __future__ import annotations

import time
import uuid
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from ..ledger.retention import require_not_frozen
from ..ledger.writer import append_event
from .formatter import canonicalize_seal
from .fingerprints import seal_fingerprint_hex


@dataclass(frozen=True)
class IssueRequest:
    issued_by: str
    issued_to: str
    scope: List[str]
    constraints: Dict[str, Any]
    protocol: int = 1
    expires_at: Optional[int] = None
    notes: Optional[str] = None


@dataclass(frozen=True)
class IssueResult:
    seal_id: str
    seq: int
    event_hash: str
    fingerprint: str


class SealIssueError(RuntimeError):
    pass


def _now_ms() -> int:
    return int(time.time() * 1000)


def issue_seal(
    *,
    db_path: str,
    req: IssueRequest,
    seal_id: Optional[str] = None,
    issued_at: Optional[int] = None,
) -> IssueResult:
    """
    Issues an authority seal by appending an authority.seal_issued event.
    Strictly blocked while freeze is active.
    """
    if req.protocol < 1:
        raise SealIssueError("protocol must be >= 1")
    if not req.issued_by or not req.issued_to:
        raise SealIssueError("issued_by and issued_to are required")
    if not req.scope or any((not s or not isinstance(s, str)) for s in req.scope):
        raise SealIssueError("scope must be a non-empty list of non-empty strings")

    # Freeze gate: issuance forbidden while frozen.
    require_not_frozen(db_path)

    sid = seal_id or f"seal_{uuid.uuid4().hex}"
    ts = issued_at if issued_at is not None else _now_ms()

    seal_obj: Dict[str, Any] = {
        "seal_id": sid,
        "issued_by": req.issued_by,
        "issued_to": req.issued_to,
        "scope": sorted(list(set(req.scope))),
        "constraints": req.constraints or {},
        "issued_at": ts,
        "expires_at": req.expires_at,
        "protocol": req.protocol,
        "status": "active",
        "metadata": {
            "notes": req.notes or ""
        },
    }

    seal_obj = canonicalize_seal(seal_obj)
    fp = seal_fingerprint_hex(seal_obj)

    payload: Dict[str, Any] = {
        "seal": seal_obj,
        "fingerprint": fp,
    }

    seq, event_hash = append_event(
        db_path=db_path,
        event_type="authority.seal_issued",
        protocol=req.protocol,
        issued_by=req.issued_by,
        payload=payload,
        issued_at=ts,
        event_id=f"evt_{sid}",
    )

    return IssueResult(seal_id=sid, seq=seq, event_hash=event_hash, fingerprint=fp)

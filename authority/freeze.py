from __future__ import annotations

import time
import uuid
from dataclasses import dataclass
from typing import Optional

from ..ledger.writer import append_event


@dataclass(frozen=True)
class FreezeRequest:
    issued_by: str
    protocol: int = 1
    reason: str = ""


@dataclass(frozen=True)
class FreezeResult:
    freeze_id: str
    seq: int
    event_hash: str


class FreezeError(RuntimeError):
    pass


def _now_ms() -> int:
    return int(time.time() * 1000)


def issue_freeze(
    *,
    db_path: str,
    req: FreezeRequest,
    freeze_id: Optional[str] = None,
    issued_at: Optional[int] = None,
) -> FreezeResult:
    """
    Issue an authority freeze.
    A freeze halts issuance and delegation but allows revocation.
    """
    if req.protocol < 1:
        raise FreezeError("protocol must be >= 1")
    if not req.issued_by:
        raise FreezeError("issued_by is required")

    fid = freeze_id or f"freeze_{uuid.uuid4().hex}"
    ts = issued_at if issued_at is not None else _now_ms()

    payload = {
        "freeze": {
            "freeze_id": fid,
            "issued_by": req.issued_by,
            "issued_at": ts,
            "protocol": req.protocol,
            "active": True,
            "reason": req.reason,
        }
    }

    seq, event_hash = append_event(
        db_path=db_path,
        event_type="authority.freeze_issued",
        protocol=req.protocol,
        issued_by=req.issued_by,
        payload=payload,
        issued_at=ts,
        event_id=f"evt_{fid}",
    )

    return FreezeResult(freeze_id=fid, seq=seq, event_hash=event_hash)

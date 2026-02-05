from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Sequence

from ..ledger.reader import iter_events
from ..ledger.retention import get_freeze_state
from .fingerprints import seal_fingerprint_hex


@dataclass(frozen=True)
class ValidationInput:
    scope: str
    subject: str
    constraints: Dict[str, Any]
    at_ms: Optional[int] = None
    protocol: int = 1


@dataclass(frozen=True)
class ValidationDecision:
    allowed: bool
    reason: str
    seal_id: Optional[str] = None
    issuer: Optional[str] = None
    fingerprint: Optional[str] = None
    freeze_active: bool = False
    ledger_seq: Optional[int] = None


class SealValidationError(RuntimeError):
    pass


def _now_ms() -> int:
    return int(time.time() * 1000)


def _constraints_match(granted: Dict[str, Any], required: Dict[str, Any]) -> bool:
    """
    Conservative constraint matching:
    - If required specifies a key, granted must contain the same key with equal value.
    - Additional granted keys are allowed (they are further restrictions or metadata).
    """
    for k, v in (required or {}).items():
        if k not in granted:
            return False
        if granted[k] != v:
            return False
    return True


def _build_state(db_path: str) -> Dict[str, Any]:
    """
    Rebuild seal + revocation state from ledger events deterministically.
    This is intentionally simple and strict.
    """
    seals: Dict[str, Dict[str, Any]] = {}
    revoked: Dict[str, Dict[str, Any]] = {}

    for row in iter_events(db_path, start_seq=1):
        if row.event_type == "authority.seal_issued":
            seal = row.payload.get("seal")
            if isinstance(seal, dict) and "seal_id" in seal:
                seals[str(seal["seal_id"])] = seal
        elif row.event_type == "authority.seal_revoked":
            rev = row.payload.get("revocation")
            if isinstance(rev, dict) and "revoked_seal_id" in rev:
                revoked[str(rev["revoked_seal_id"])] = rev

    return {"seals": seals, "revoked": revoked}


def validate(
    db_path: str,
    vin: ValidationInput,
) -> ValidationDecision:
    """
    Validate whether a subject may perform a scope under required constraints
    at a given time, using only ledger truth.
    """
    if not vin.scope or not vin.subject:
        raise SealValidationError("scope and subject are required")

    at_ms = vin.at_ms if vin.at_ms is not None else _now_ms()

    freeze = get_freeze_state(db_path)
    # Freeze does not invalidate existing authority, but blocks issuance/delegation.
    # Consumers may optionally treat freeze as a policy signal.
    freeze_active = freeze.active

    st = _build_state(db_path)
    seals: Dict[str, Dict[str, Any]] = st["seals"]
    revoked: Dict[str, Dict[str, Any]] = st["revoked"]

    # Find candidate seals issued to subject that include scope.
    candidates: List[Dict[str, Any]] = []
    for sid, seal in seals.items():
        if str(seal.get("issued_to", "")) != vin.subject:
            continue
        if str(seal.get("status", "active")) != "active":
            continue
        if sid in revoked:
            continue
        if vin.scope not in list(seal.get("scope", [])):
            continue

        issued_at = int(seal.get("issued_at", 0))
        expires_at = seal.get("expires_at", None)
        if issued_at > at_ms:
            continue
        if expires_at is not None and int(expires_at) < at_ms:
            continue

        granted_constraints = seal.get("constraints", {}) or {}
        if not isinstance(granted_constraints, dict):
            continue
        if not _constraints_match(granted_constraints, vin.constraints or {}):
            continue

        candidates.append(seal)

    if not candidates:
        return ValidationDecision(
            allowed=False,
            reason="NO_VALID_AUTHORITY",
            freeze_active=freeze_active,
        )

    # Deterministic selection: choose the most recently issued seal.
    candidates.sort(key=lambda s: int(s.get("issued_at", 0)), reverse=True)
    chosen = candidates[0]
    sid = str(chosen["seal_id"])

    return ValidationDecision(
        allowed=True,
        reason="AUTHORIZED",
        seal_id=sid,
        issuer=str(chosen.get("issued_by", "")),
        fingerprint=seal_fingerprint_hex(chosen),
        freeze_active=freeze_active,
    )

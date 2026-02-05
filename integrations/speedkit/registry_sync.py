from __future__ import annotations

from typing import Any, Dict

from ...ledger.reader import iter_events
from ...seals.validator import ValidationInput, validate


class SpeedkitRegistrySyncError(RuntimeError):
    pass


def sync_registry_entry(
    *,
    db_path: str,
    system_id: str,
    authority_seal_id: str,
) -> Dict[str, Any]:
    """
    Synchronize a SPEEDKIT registry entry with AUCTORISEAL authority state.

    SPEEDKIT MUST NOT assert legitimacy independently.
    Legitimacy is derived exclusively from authority seals.
    """
    if not system_id:
        raise SpeedkitRegistrySyncError("system_id is required")
    if not authority_seal_id:
        raise SpeedkitRegistrySyncError("authority_seal_id is required")

    # Verify that the referenced seal exists and is active
    seal_found = False
    for row in iter_events(db_path, start_seq=1):
        if row.event_type == "authority.seal_issued":
            seal = row.payload.get("seal")
            if isinstance(seal, dict) and seal.get("seal_id") == authority_seal_id:
                seal_found = True
        if row.event_type == "authority.seal_revoked":
            rev = row.payload.get("revocation")
            if isinstance(rev, dict) and rev.get("revoked_seal_id") == authority_seal_id:
                raise SpeedkitRegistrySyncError("referenced seal is revoked")

    if not seal_found:
        raise SpeedkitRegistrySyncError("referenced seal does not exist")

    return {
        "system_id": system_id,
        "authority_seal_id": authority_seal_id,
        "status": "active",
        "source": "auctoriseal",
    }

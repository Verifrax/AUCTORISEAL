from __future__ import annotations

from typing import Any, Dict

from ...seals.validator import ValidationInput, validate
from ...authority.policy import enforce_mode_policy
from ...authority.modes import get_mode


class AdjutorixAuthorityError(RuntimeError):
    pass


def authorize_action(
    *,
    db_path: str,
    subject: str,
    action: str,
    constraints: Dict[str, Any],
    mode_name: str,
) -> Dict[str, Any]:
    """
    Hard authority gate for ADJUTORIX.

    This function MUST be called before any irreversible action.
    """
    mode = get_mode(mode_name)

    vin = ValidationInput(
        scope=action,
        subject=subject,
        constraints=constraints,
    )

    decision = validate(db_path, vin)

    if not decision.allowed:
        raise AdjutorixAuthorityError(decision.reason)

    policy = enforce_mode_policy(
        mode=mode,
        requested_action=action,
        allowed_scopes=[action],
    )

    if not policy.allowed:
        raise AdjutorixAuthorityError(policy.reason)

    return {
        "authorized": True,
        "seal_id": decision.seal_id,
        "issuer": decision.issuer,
        "fingerprint": decision.fingerprint,
        "freeze_active": decision.freeze_active,
    }

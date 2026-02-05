from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Set

from .modes import AuthorityMode


@dataclass(frozen=True)
class PolicyDecision:
    allowed: bool
    reason: str


class AuthorityPolicyError(RuntimeError):
    pass


def enforce_mode_policy(
    *,
    mode: AuthorityMode,
    requested_action: str,
    allowed_scopes: Iterable[str],
) -> PolicyDecision:
    """
    Enforce hard, non-configurable authority policy.

    Rules:
    - Writes are forbidden if mode.writes_allowed is False
    - Action must be explicitly present in allowed_scopes
    - No implicit expansion of authority
    """
    if not requested_action:
        return PolicyDecision(allowed=False, reason="INVALID_ACTION")

    scopes: Set[str] = set(allowed_scopes)

    if requested_action not in scopes:
        return PolicyDecision(allowed=False, reason="ACTION_OUT_OF_SCOPE")

    if not mode.writes_allowed and requested_action.endswith(":apply"):
        return PolicyDecision(allowed=False, reason="WRITES_FORBIDDEN_IN_MODE")

    return PolicyDecision(allowed=True, reason="POLICY_OK")

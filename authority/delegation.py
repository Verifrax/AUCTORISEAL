from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass(frozen=True)
class Delegation:
    authority_id: str
    issued_by: str
    issued_to: str
    scope: list[str]
    constraints: Dict[str, Any]
    delegation_allowed: bool
    issued_at: int
    expires_at: Optional[int]
    protocol: int


class DelegationError(RuntimeError):
    pass


def validate_delegation(parent: Delegation, child: Delegation) -> None:
    """
    Validate that a child delegation is strictly bounded by its parent authority.

    Rules:
    - Parent must allow delegation
    - Child scope ⊆ parent scope
    - Child constraints ⊇ parent constraints (never weaker)
    - Child expiry must be <= parent expiry (if any)
    - Protocol versions must match
    """
    if not parent.delegation_allowed:
        raise DelegationError("parent authority does not allow delegation")

    if parent.protocol != child.protocol:
        raise DelegationError("protocol mismatch in delegation chain")

    parent_scope = set(parent.scope)
    child_scope = set(child.scope)
    if not child_scope.issubset(parent_scope):
        raise DelegationError("child scope exceeds parent scope")

    for k, v in parent.constraints.items():
        if k not in child.constraints or child.constraints[k] != v:
            raise DelegationError(f"child constraints weaken parent constraint: {k}")

    if parent.expires_at is not None:
        if child.expires_at is None or child.expires_at > parent.expires_at:
            raise DelegationError("child expiry exceeds parent expiry")

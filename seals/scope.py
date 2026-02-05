from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, Tuple


@dataclass(frozen=True)
class ScopeCheck:
    ok: bool
    reason: str


class ScopeError(ValueError):
    pass


def normalize_scope(scope: Iterable[str]) -> List[str]:
    """
    Normalize a scope list:
    - strip
    - drop empties
    - unique
    - sorted
    """
    out = []
    seen = set()
    for s in scope:
        if not isinstance(s, str):
            raise ScopeError("scope entries must be strings")
        v = s.strip()
        if not v:
            continue
        if v in seen:
            continue
        seen.add(v)
        out.append(v)
    out.sort()
    return out


def scope_allows(granted_scope: Iterable[str], required_scope: str) -> ScopeCheck:
    """
    Strict scope match:
    - No wildcards
    - Required scope must be present exactly
    """
    if not isinstance(required_scope, str) or not required_scope.strip():
        return ScopeCheck(ok=False, reason="INVALID_REQUIRED_SCOPE")

    req = required_scope.strip()
    granted = set(normalize_scope(granted_scope))

    if req in granted:
        return ScopeCheck(ok=True, reason="SCOPE_ALLOWED")
    return ScopeCheck(ok=False, reason="SCOPE_DENIED")


def constraints_subset(granted: Dict[str, Any], required: Dict[str, Any]) -> ScopeCheck:
    """
    Conservative constraint matching:
    - Every required key must exist in granted with identical value.
    - Extra granted keys are allowed.
    """
    if required is None:
        required = {}
    if granted is None:
        granted = {}

    if not isinstance(required, dict) or not isinstance(granted, dict):
        return ScopeCheck(ok=False, reason="INVALID_CONSTRAINTS")

    for k, v in required.items():
        if k not in granted:
            return ScopeCheck(ok=False, reason=f"CONSTRAINT_MISSING:{k}")
        if granted[k] != v:
            return ScopeCheck(ok=False, reason=f"CONSTRAINT_MISMATCH:{k}")
    return ScopeCheck(ok=True, reason="CONSTRAINTS_OK")

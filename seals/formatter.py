from __future__ import annotations

import json
from typing import Any, Dict, List


def _canonical_json(obj: Any) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def _normalize_scope(scope: Any) -> List[str]:
    if scope is None:
        return []
    if not isinstance(scope, list):
        raise ValueError("scope must be a list")
    out: List[str] = []
    seen = set()
    for s in scope:
        if not isinstance(s, str):
            raise ValueError("scope entries must be strings")
        v = s.strip()
        if not v:
            continue
        if v in seen:
            continue
        seen.add(v)
        out.append(v)
    out.sort()
    return out


def canonicalize_seal(seal: Dict[str, Any]) -> Dict[str, Any]:
    """
    Canonicalize a seal object:
    - normalize scope
    - ensure constraints is an object
    - ensure status is present
    - stable metadata
    """
    obj = dict(seal)

    obj["scope"] = _normalize_scope(obj.get("scope"))
    constraints = obj.get("constraints", {})
    if constraints is None:
        constraints = {}
    if not isinstance(constraints, dict):
        raise ValueError("constraints must be an object")
    obj["constraints"] = constraints

    status = obj.get("status", "active")
    if status not in ("active", "revoked"):
        raise ValueError("status must be 'active' or 'revoked'")
    obj["status"] = status

    md = obj.get("metadata", {})
    if md is None:
        md = {}
    if not isinstance(md, dict):
        raise ValueError("metadata must be an object")
    obj["metadata"] = md

    return obj


def canonicalize_revocation(rev: Dict[str, Any]) -> Dict[str, Any]:
    obj = dict(rev)

    md = obj.get("metadata", {})
    if md is None:
        md = {}
    if not isinstance(md, dict):
        raise ValueError("metadata must be an object")
    obj["metadata"] = md

    # reason is optional but if present must be string
    if "reason" in obj and obj["reason"] is not None and not isinstance(obj["reason"], str):
        raise ValueError("reason must be a string")

    return obj

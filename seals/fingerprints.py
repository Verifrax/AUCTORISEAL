from __future__ import annotations

import hashlib
import json
from typing import Any, Dict


def _canonical_json(obj: Any) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def seal_fingerprint_hex(seal_obj: Dict[str, Any]) -> str:
    """
    Produce a stable fingerprint for a seal object.
    This is not a signature; it is a deterministic content identifier.
    """
    data = _canonical_json(seal_obj).encode("utf-8")
    return hashlib.sha256(data).hexdigest()

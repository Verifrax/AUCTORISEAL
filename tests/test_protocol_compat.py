from __future__ import annotations

import json
import os
from pathlib import Path


BASE = Path(__file__).resolve().parents[1]
PROTOCOL_DIR = BASE / "protocol"


def _load_json(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        obj = json.load(f)
    assert isinstance(obj, dict)
    return obj


def test_protocol_schemas_exist_and_are_valid_json() -> None:
    required = [
        "envelope.schema.json",
        "seal.schema.json",
        "authority.schema.json",
        "revocation.schema.json",
        "registry.schema.json",
        "error.schema.json",
    ]

    for name in required:
        p = PROTOCOL_DIR / name
        assert p.exists(), f"missing schema: {name}"
        _load_json(p)


def test_protocol_versions_are_positive_in_schemas() -> None:
    # Minimal sanity: ensure schemas declare integer protocol fields where applicable.
    seal = _load_json(PROTOCOL_DIR / "seal.schema.json")
    props = seal.get("properties", {})
    protocol = props.get("protocol", {})
    assert protocol.get("type") == "integer"
    assert protocol.get("minimum", 0) >= 1

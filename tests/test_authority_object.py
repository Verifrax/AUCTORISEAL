import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_authority_object_minimum():
    path = ROOT / "authorities/current/authority-object-0001.json"
    data = json.loads(path.read_text())
    published = json.loads((ROOT / "public/authority/AUTHORITY-0001.json").read_text())

    assert data["object_type"] == "AuthorityObject"
    assert data["status"] == "ACTIVE_TRUTH"
    assert data["canonical_publication_ref"] == "public/authority/AUTHORITY-0001.json"
    assert data["canonical_digest_ref"] == "public/authority/AUTHORITY-0001.digest.txt"
    assert data["canonical_verify_ref"] == "public/authority/AUTHORITY-0001.verify.txt"
    assert data["schema_ref"] == "protocol/authority.schema.json"
    assert data["seal_schema_ref"] == "protocol/seal.schema.json"
    assert data["revocation_schema_ref"] == "protocol/revocation.schema.json"
    assert data["historical_archive_ref"] == "authorities/history/"
    assert data["authority_id"] == published["authority_id"]
    assert data["authority_type"] == published["authority_type"]
    assert data["protocol"] == published["protocol"]
    assert data["schema_version"] == published["schema_version"]
    assert data["issued_by"] == published["issued_by"]
    assert data["issued_at"] == published["issued_at"]
    assert data["finality"] == published["finality"]

#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def need(cond, code):
    print(f"[VERIFY] {code}")
    if not cond:
        raise SystemExit(f"FAIL {code}")

authority_path = ROOT / "authorities/current/authority-object-0001.json"
index_path = ROOT / "authorities/current/index.json"
history_path = ROOT / "authorities/history/README.md"

need(authority_path.is_file(), "authority-object-present")
need(index_path.is_file(), "authority-index-present")
need(history_path.is_file(), "authority-history-present")

authority = json.loads(authority_path.read_text())
index = json.loads(index_path.read_text())

need(authority["object_type"] == "AuthorityObject", "authority-object-type")
need(authority["status"] == "ACTIVE_TRUTH", "authority-object-status")
need(authority["authority_id"] == "AUTHORITY-0001-VERIFRAX", "authority-id")
need(isinstance(authority.get("authority_digest"), str) and len(authority["authority_digest"]) > 0, "authority-digest")
need(isinstance(authority.get("governed_repositories"), list) and len(authority["governed_repositories"]) >= 5, "authority-governed-scope")
need(authority.get("governance_root_ref") == "https://github.com/Verifrax/.github", "authority-governance-root")
need(authority.get("history_ref") == "authorities/history/", "authority-history-ref")
need(authority.get("continuity_ref") == "https://github.com/Verifrax/VERIFRAX/blob/main/evidence/continuity/current/continuity-object-0001.json", "authority-continuity-ref")
need(authority.get("transfer_ref") == "https://github.com/Verifrax/VERIFRAX/blob/main/evidence/transfer/current/transfer-object-0001.json", "authority-transfer-ref")

need(index["object_type"] == "AuthorityIndex", "authority-index-type")
need(index["status"] == "ACTIVE_TRUTH", "authority-index-status")
need(index["historical"] is False, "authority-index-historical-false")
need(index["current_authority_object_ref"] == "authorities/current/authority-object-0001.json", "authority-index-binding")
need(index["entries"][0]["authority_id"] == "AUTHORITY-0001-VERIFRAX", "authority-index-entry-id")
need(index["entries"][0]["path"] == "authorities/current/authority-object-0001.json", "authority-index-entry-path")
need(index["entries"][0]["authority_digest"] == authority["authority_digest"], "authority-index-entry-digest-match")

print("[PASS] PHASE 3 / STEP 36 authority reconstructability minimum verified")

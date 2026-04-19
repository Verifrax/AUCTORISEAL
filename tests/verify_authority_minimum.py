#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

def need(cond, label):
    if cond:
        print(f"[VERIFY] {label}")
    else:
        errors.append(label)

readme_path = ROOT / "README.md"
authority_path = ROOT / "AUTHORITY.md"

need(readme_path.exists(), "readme-present")
need(authority_path.exists(), "authority-doc-present")
need((ROOT / "STATUS.md").exists(), "status-doc-present")
need((ROOT / "VERSION.md").exists(), "version-doc-present")
need((ROOT / "tests/test_authority_minimum.py").exists(), "authority-minimum-test-present")
need((ROOT / "tests/verify_authority_minimum.py").exists(), "authority-minimum-verifier-present")

for rel in [
    "api",
    "authorities",
    "authority",
    "cli",
    "docs",
    "evidence",
    "ledger",
    "public",
    "runtime",
    "seals",
    "tests",
]:
    need((ROOT / rel).is_dir(), f"dir-present {rel}")

readme = readme_path.read_text(encoding="utf-8") if readme_path.exists() else ""
authority = authority_path.read_text(encoding="utf-8") if authority_path.exists() else ""

for needle, label in [
    ("authority-issuance boundary", "readme-role-surface"),
    ("does not author constitutional law", "readme-not-law"),
    ("does not hold canonical world-state", "readme-not-state"),
    ("does not perform reconciliation", "readme-not-reconciliation"),
    ("does not perform sovereign cognition", "readme-not-cognition"),
    ("does not execute", "readme-not-execution"),
    ("does not verify", "readme-not-verification"),
    ("does not publish proof as proof authority", "readme-not-proof-authority"),
    ("does not operate intake", "readme-not-intake"),
    ("not terminal recognition", "readme-not-recognition"),
    ("not terminal recourse", "readme-not-recourse"),
]:
    need(needle in readme, label)

need("AUCTORISEAL" in authority, "authority-doc-names-surface")
need("authority" in authority.lower(), "authority-doc-authority-language")

if errors:
    print("\n[FAIL] AUCTORISEAL authority minimum verification failed")
    for e in errors:
        print(" -", e)
    sys.exit(1)

print("\n[PASS] AUCTORISEAL authority minimum verified")

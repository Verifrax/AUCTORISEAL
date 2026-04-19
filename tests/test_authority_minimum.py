from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_authority_minimum_surface_present():
    required = [
        "README.md",
        "AUTHORITY.md",
        "STATUS.md",
        "VERSION.md",
        "tests/test_authority_minimum.py",
        "tests/verify_authority_minimum.py",
    ]
    for rel in required:
        assert (ROOT / rel).exists(), rel

def test_authority_minimum_repo_shape_present():
    required_dirs = [
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
    ]
    for rel in required_dirs:
        assert (ROOT / rel).is_dir(), rel

def test_authority_minimum_boundary_lock_present():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    authority = (ROOT / "AUTHORITY.md").read_text(encoding="utf-8")

    required_readme = [
        "authority-issuance boundary",
        "does not author constitutional law",
        "does not hold canonical world-state",
        "does not perform reconciliation",
        "does not perform sovereign cognition",
        "does not execute",
        "does not verify",
        "does not publish proof as proof authority",
        "does not operate intake",
        "not terminal recognition",
        "not terminal recourse",
    ]
    for needle in required_readme:
        assert needle in readme, needle

    authority_needles = [
        "AUCTORISEAL",
        "authority",
    ]
    for needle in authority_needles:
        assert needle in authority, needle

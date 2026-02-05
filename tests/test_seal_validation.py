from __future__ import annotations

import tempfile
import os

from auctoriseal.cli.inspect_ledger import _apply_migrations
from auctoriseal.seals.issuer import IssueRequest, issue_seal
from auctoriseal.seals.validator import ValidationInput, validate


def _init_db(tmpdir: str) -> str:
    db = os.path.join(tmpdir, "ledger.sqlite")
    _apply_migrations(db)
    return db


def test_seal_allows_scope() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        db = _init_db(tmp)

        issue_seal(
            db_path=db,
            req=IssueRequest(
                issued_by="root.primary",
                issued_to="service.alpha",
                scope=["adjutorix:apply"],
                constraints={},
            ),
        )

        decision = validate(
            db,
            ValidationInput(
                subject="service.alpha",
                scope="adjutorix:apply",
                constraints={},
            ),
        )

        assert decision.allowed is True
        assert decision.seal_id is not None


def test_seal_denies_wrong_subject() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        db = _init_db(tmp)

        issue_seal(
            db_path=db,
            req=IssueRequest(
                issued_by="root.primary",
                issued_to="service.alpha",
                scope=["adjutorix:apply"],
                constraints={},
            ),
        )

        decision = validate(
            db,
            ValidationInput(
                subject="service.beta",
                scope="adjutorix:apply",
                constraints={},
            ),
        )

        assert decision.allowed is False
        assert decision.reason == "NO_VALID_AUTHORITY"

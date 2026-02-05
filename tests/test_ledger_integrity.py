from __future__ import annotations

import os
import tempfile

from auctoriseal.cli.inspect_ledger import _apply_migrations
from auctoriseal.ledger.integrity import check_integrity
from auctoriseal.seals.issuer import IssueRequest, issue_seal


def _init_db(tmpdir: str) -> str:
    db = os.path.join(tmpdir, "ledger.sqlite")
    _apply_migrations(db)
    return db


def test_integrity_ok_after_events() -> None:
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

        res = check_integrity(db)
        assert res.ok is True
        assert res.checked_events >= 1

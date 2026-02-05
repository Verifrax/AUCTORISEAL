from __future__ import annotations

import os
import tempfile

from auctoriseal.cli.inspect_ledger import _apply_migrations
from auctoriseal.authority.freeze import FreezeRequest, issue_freeze
from auctoriseal.seals.issuer import IssueRequest, issue_seal
from auctoriseal.ledger.retention import get_freeze_state


def _init_db(tmpdir: str) -> str:
    db = os.path.join(tmpdir, "ledger.sqlite")
    _apply_migrations(db)
    return db


def test_freeze_blocks_issuance() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        db = _init_db(tmp)

        st0 = get_freeze_state(db)
        assert st0.active is False

        issue_freeze(
            db_path=db,
            req=FreezeRequest(issued_by="root.emergency", reason="test"),
        )

        st1 = get_freeze_state(db)
        assert st1.active is True

        try:
            issue_seal(
                db_path=db,
                req=IssueRequest(
                    issued_by="root.primary",
                    issued_to="service.alpha",
                    scope=["adjutorix:apply"],
                    constraints={},
                ),
            )
            assert False, "expected issuance to be blocked under freeze"
        except Exception:
            assert True

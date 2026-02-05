from __future__ import annotations

import os
import tempfile

from auctoriseal.cli.inspect_ledger import _apply_migrations
from auctoriseal.seals.issuer import IssueRequest, issue_seal
from auctoriseal.seals.revoker import RevokeRequest, revoke_seal
from auctoriseal.seals.validator import ValidationInput, validate


def _init_db(tmpdir: str) -> str:
    db = os.path.join(tmpdir, "ledger.sqlite")
    _apply_migrations(db)
    return db


def test_revocation_invalidates_seal() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        db = _init_db(tmp)

        issued = issue_seal(
            db_path=db,
            req=IssueRequest(
                issued_by="root.primary",
                issued_to="service.alpha",
                scope=["adjutorix:apply"],
                constraints={},
            ),
        )

        before = validate(
            db,
            ValidationInput(subject="service.alpha", scope="adjutorix:apply", constraints={}),
        )
        assert before.allowed is True
        assert before.seal_id == issued.seal_id

        revoke_seal(
            db_path=db,
            req=RevokeRequest(
                revoked_seal_id=issued.seal_id,
                revoked_by="root.primary",
                reason="test",
            ),
        )

        after = validate(
            db,
            ValidationInput(subject="service.alpha", scope="adjutorix:apply", constraints={}),
        )
        assert after.allowed is False
        assert after.reason == "NO_VALID_AUTHORITY"

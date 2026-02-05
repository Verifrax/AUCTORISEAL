from __future__ import annotations

from auctoriseal.authority.delegation import Delegation, validate_delegation


def test_child_scope_must_be_subset() -> None:
    parent = Delegation(
        authority_id="auth_parent",
        issued_by="root.primary",
        issued_to="team.alpha",
        scope=["adjutorix:apply", "adjutorix:deploy"],
        constraints={"mode": "managed"},
        delegation_allowed=True,
        issued_at=1,
        expires_at=10,
        protocol=1,
    )

    child = Delegation(
        authority_id="auth_child",
        issued_by="team.alpha",
        issued_to="service.alpha",
        scope=["adjutorix:apply"],
        constraints={"mode": "managed"},
        delegation_allowed=False,
        issued_at=2,
        expires_at=9,
        protocol=1,
    )

    validate_delegation(parent, child)


def test_child_constraints_cannot_weaken() -> None:
    parent = Delegation(
        authority_id="auth_parent",
        issued_by="root.primary",
        issued_to="team.alpha",
        scope=["adjutorix:apply"],
        constraints={"mode": "managed", "env": "prod"},
        delegation_allowed=True,
        issued_at=1,
        expires_at=10,
        protocol=1,
    )

    child = Delegation(
        authority_id="auth_child",
        issued_by="team.alpha",
        issued_to="service.alpha",
        scope=["adjutorix:apply"],
        constraints={"mode": "managed"},  # weakened: missing env
        delegation_allowed=False,
        issued_at=2,
        expires_at=9,
        protocol=1,
    )

    try:
        validate_delegation(parent, child)
        assert False, "expected DelegationError"
    except Exception:
        assert True

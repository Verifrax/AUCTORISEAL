from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class AuthorityMode:
    """
    Defines the operational mode under which authority may be exercised.
    """
    name: str
    writes_allowed: bool
    delegation_allowed: bool
    description: str


# Canonical authority modes
EXTERNAL = AuthorityMode(
    name="external",
    writes_allowed=False,
    delegation_allowed=False,
    description="Read-only authority; no mutation or delegation permitted.",
)

MANAGED = AuthorityMode(
    name="managed",
    writes_allowed=True,
    delegation_allowed=True,
    description="Managed authority with controlled mutation and delegation.",
)

AUTO = AuthorityMode(
    name="auto",
    writes_allowed=False,
    delegation_allowed=False,
    description="Planner/automation mode; may propose but never mutate.",
)


MODES = {
    EXTERNAL.name: EXTERNAL,
    MANAGED.name: MANAGED,
    AUTO.name: AUTO,
}


class AuthorityModeError(RuntimeError):
    pass


def get_mode(name: str) -> AuthorityMode:
    if name not in MODES:
        raise AuthorityModeError(f"unknown authority mode: {name}")
    return MODES[name]

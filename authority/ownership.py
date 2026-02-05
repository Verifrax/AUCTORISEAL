from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Ownership:
    """
    Represents ownership context for authority.

    Ownership defines *who* holds authority, not *what* they can do.
    """
    owner_id: str
    owner_type: str  # "individual" | "organization" | "system"
    verified: bool
    verified_at: Optional[int] = None


class OwnershipError(RuntimeError):
    pass


def validate_ownership(ownership: Ownership) -> None:
    """
    Validate ownership record.

    Rules:
    - owner_id must be present
    - owner_type must be explicit
    - verification is required for authority issuance
    """
    if not ownership.owner_id:
        raise OwnershipError("owner_id is required")

    if ownership.owner_type not in ("individual", "organization", "system"):
        raise OwnershipError("invalid owner_type")

    if not ownership.verified:
        raise OwnershipError("ownership must be verified before authority can be issued")

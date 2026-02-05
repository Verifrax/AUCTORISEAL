from __future__ import annotations

import hmac
import os
from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class AuthConfig:
    """
    Minimal auth configuration.

    The public AUCTORISEAL API is read-only by design; auth exists primarily for:
    - rate-limiting identity
    - internal deployments
    - access logging correlation
    """
    api_key: Optional[str] = None


class AuthError(RuntimeError):
    pass


def load_auth_config() -> AuthConfig:
    return AuthConfig(api_key=os.environ.get("AUCTORISEAL_API_KEY"))


def verify_api_key(provided: Optional[str], cfg: AuthConfig) -> bool:
    """
    Constant-time API key check.
    If no key is configured, authentication is treated as disabled.
    """
    if cfg.api_key is None or cfg.api_key == "":
        return True
    if provided is None:
        return False
    return hmac.compare_digest(provided, cfg.api_key)

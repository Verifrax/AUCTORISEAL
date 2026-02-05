from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class RateLimitConfig:
    requests: int = 120
    window_seconds: int = 60


class RateLimitError(RuntimeError):
    pass


class InMemoryRateLimiter:
    """
    Minimal in-memory rate limiter.

    This is intentionally simple and is not a distributed rate limiter.
    Suitable for local/dev and single-instance deployments.
    """

    def __init__(self, cfg: Optional[RateLimitConfig] = None) -> None:
        self.cfg = cfg or RateLimitConfig()
        self._buckets: Dict[str, Dict[str, float]] = {}

    def allow(self, key: str) -> bool:
        now = time.time()
        bucket = self._buckets.get(key)
        if bucket is None:
            self._buckets[key] = {"reset": now + self.cfg.window_seconds, "count": 1}
            return True

        if now >= bucket["reset"]:
            bucket["reset"] = now + self.cfg.window_seconds
            bucket["count"] = 1
            return True

        if bucket["count"] >= self.cfg.requests:
            return False

        bucket["count"] += 1
        return True

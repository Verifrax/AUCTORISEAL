from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass(frozen=True)
class ErrorResponse:
    error: str
    code: Optional[str] = None
    details: Optional[Dict[str, Any]] = None

    def to_dict(self) -> Dict[str, Any]:
        out: Dict[str, Any] = {"error": self.error}
        if self.code is not None:
            out["code"] = self.code
        if self.details is not None:
            out["details"] = self.details
        return out


@dataclass(frozen=True)
class OkResponse:
    ok: bool = True
    data: Optional[Dict[str, Any]] = None

    def to_dict(self) -> Dict[str, Any]:
        out: Dict[str, Any] = {"ok": self.ok}
        if self.data is not None:
            out["data"] = self.data
        return out

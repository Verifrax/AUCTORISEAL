from __future__ import annotations

import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Any, Dict, Optional
from urllib.parse import parse_qs, urlparse

from ..ledger.reader import tail_events
from ..seals.validator import ValidationInput, validate
from ..ledger.retention import get_freeze_state


class ApiError(Exception):
    def __init__(self, status: int, message: str):
        self.status = status
        self.message = message
        super().__init__(message)


class AuctorisealApiHandler(BaseHTTPRequestHandler):
    server_version = "AUCTORISEAL/1.0"

    def _send(self, status: int, body: Dict[str, Any]) -> None:
        data = json.dumps(body, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _read_json(self) -> Dict[str, Any]:
        length = int(self.headers.get("Content-Length", "0"))
        if length <= 0:
            raise ApiError(400, "missing request body")
        raw = self.rfile.read(length)
        try:
            obj = json.loads(raw.decode("utf-8"))
        except Exception:
            raise ApiError(400, "invalid json body")
        if not isinstance(obj, dict):
            raise ApiError(400, "json body must be an object")
        return obj

    def _handle_health(self) -> None:
        self._send(200, {"ok": True})

    def _handle_protocol(self) -> None:
        self._send(
            200,
            {
                "protocol": 1,
                "schemas": [
                    "envelope.schema.json",
                    "seal.schema.json",
                    "authority.schema.json",
                    "revocation.schema.json",
                    "registry.schema.json",
                    "error.schema.json",
                ],
            },
        )

    def _handle_ledger_tail(self, qs: Dict[str, Any]) -> None:
        limit = int(qs.get("limit", ["50"])[0])
        events = []
        for row in tail_events(self.server.db_path, limit=limit):
            events.append(
                {
                    "seq": row.seq,
                    "event_id": row.event_id,
                    "event_type": row.event_type,
                    "issued_by": row.issued_by,
                    "issued_at": row.issued_at,
                    "payload": row.payload,
                    "event_hash": row.event_hash,
                }
            )
        self._send(200, {"events": events})

    def _handle_validate(self) -> None:
        body = self._read_json()
        subject = body.get("subject")
        scope = body.get("scope")
        constraints = body.get("constraints", {})
        at_ms = body.get("at_ms")

        decision = validate(
            self.server.db_path,
            ValidationInput(
                subject=subject,
                scope=scope,
                constraints=constraints,
                at_ms=at_ms,
            ),
        )

        self._send(
            200,
            {
                "allowed": decision.allowed,
                "reason": decision.reason,
                "seal_id": decision.seal_id,
                "issuer": decision.issuer,
                "fingerprint": decision.fingerprint,
                "freeze_active": decision.freeze_active,
            },
        )

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        qs = parse_qs(parsed.query)

        try:
            if parsed.path == "/health":
                self._handle_health()
            elif parsed.path == "/protocol":
                self._handle_protocol()
            elif parsed.path == "/ledger/tail":
                self._handle_ledger_tail(qs)
            else:
                raise ApiError(404, "not found")
        except ApiError as e:
            self._send(e.status, {"error": e.message})

    def do_POST(self) -> None:
        parsed = urlparse(self.path)
        try:
            if parsed.path == "/validate":
                self._handle_validate()
            else:
                raise ApiError(404, "not found")
        except ApiError as e:
            self._send(e.status, {"error": e.message})


class AuctorisealHttpServer(HTTPServer):
    def __init__(self, addr: str, port: int, db_path: str):
        super().__init__((addr, port), AuctorisealApiHandler)
        self.db_path = db_path


def main() -> None:
    addr = os.environ.get("AUCTORISEAL_BIND", "127.0.0.1")
    port = int(os.environ.get("AUCTORISEAL_PORT", "8080"))
    db_path = os.environ.get("AUCTORISEAL_DB", "./ledger.sqlite")

    srv = AuctorisealHttpServer(addr, port, db_path)
    print(f"AUCTORISEAL API listening on http://{addr}:{port}")
    srv.serve_forever()


if __name__ == "__main__":
    main()

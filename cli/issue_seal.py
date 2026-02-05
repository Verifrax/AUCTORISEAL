from __future__ import annotations

import argparse
import json
import sys
from typing import Any, Dict

from ..seals.issuer import IssueRequest, issue_seal


def _parse_kv_pairs(pairs: list[str]) -> Dict[str, Any]:
    out: Dict[str, Any] = {}
    for p in pairs:
        if "=" not in p:
            raise ValueError(f"invalid constraint format: {p} (expected key=value)")
        k, v = p.split("=", 1)
        out[k] = v
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description="Issue an AUCTORISEAL authority seal")
    parser.add_argument("--db", required=True, help="Path to ledger database")
    parser.add_argument("--issued-by", required=True, help="Issuing authority ID")
    parser.add_argument("--issued-to", required=True, help="Subject receiving authority")
    parser.add_argument("--scope", action="append", required=True, help="Authorized scope (repeatable)")
    parser.add_argument("--constraint", action="append", default=[], help="Constraint key=value (repeatable)")
    parser.add_argument("--expires-at", type=int, help="Expiration timestamp (ms)")
    parser.add_argument("--protocol", type=int, default=1, help="Protocol version")
    parser.add_argument("--notes", help="Optional notes")

    args = parser.parse_args()

    try:
        req = IssueRequest(
            issued_by=args.issued_by,
            issued_to=args.issued_to,
            scope=args.scope,
            constraints=_parse_kv_pairs(args.constraint),
            expires_at=args.expires_at,
            protocol=args.protocol,
            notes=args.notes,
        )

        res = issue_seal(db_path=args.db, req=req)

        print(json.dumps({
            "seal_id": res.seal_id,
            "seq": res.seq,
            "event_hash": res.event_hash,
            "fingerprint": res.fingerprint,
        }, indent=2))
    except Exception as e:
        print(f"error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

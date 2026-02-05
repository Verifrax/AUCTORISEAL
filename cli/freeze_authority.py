from __future__ import annotations

import argparse
import json
import sys

from ..authority.freeze import FreezeRequest, issue_freeze


def main() -> None:
    parser = argparse.ArgumentParser(description="Issue an AUCTORISEAL authority freeze")
    parser.add_argument("--db", required=True, help="Path to ledger database")
    parser.add_argument("--issued-by", required=True, help="Issuing authority ID")
    parser.add_argument("--reason", default="", help="Human-readable reason")
    parser.add_argument("--protocol", type=int, default=1, help="Protocol version")

    args = parser.parse_args()

    try:
        res = issue_freeze(
            db_path=args.db,
            req=FreezeRequest(issued_by=args.issued_by, reason=args.reason, protocol=args.protocol),
        )

        print(json.dumps({
            "freeze_id": res.freeze_id,
            "seq": res.seq,
            "event_hash": res.event_hash,
        }, indent=2))
    except Exception as e:
        print(f"error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

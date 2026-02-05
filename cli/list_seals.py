from __future__ import annotations

import argparse
import json
import sys
from typing import Any, Dict, List, Optional

from ..ledger.reader import iter_events


def main() -> None:
    parser = argparse.ArgumentParser(description="List AUCTORISEAL authority seals (ledger-derived)")
    parser.add_argument("--db", required=True, help="Path to ledger database")
    parser.add_argument("--status", choices=["active", "revoked"], help="Filter by status (derived)")
    parser.add_argument("--issued-to", help="Filter by issued_to")
    parser.add_argument("--scope", help="Filter by scope membership (exact)")
    parser.add_argument("--limit", type=int, default=200, help="Max seals to print (default 200)")

    args = parser.parse_args()

    try:
        seals: Dict[str, Dict[str, Any]] = {}
        revoked: Dict[str, Dict[str, Any]] = {}

        for row in iter_events(args.db, start_seq=1):
            if row.event_type == "authority.seal_issued":
                seal = row.payload.get("seal")
                if isinstance(seal, dict) and "seal_id" in seal:
                    seals[str(seal["seal_id"])] = seal
            elif row.event_type == "authority.seal_revoked":
                rev = row.payload.get("revocation")
                if isinstance(rev, dict) and "revoked_seal_id" in rev:
                    revoked[str(rev["revoked_seal_id"])] = rev

        out: List[Dict[str, Any]] = []
        for sid, seal in seals.items():
            status = "revoked" if sid in revoked else "active"

            if args.status and status != args.status:
                continue
            if args.issued_to and str(seal.get("issued_to", "")) != args.issued_to:
                continue
            if args.scope and args.scope not in list(seal.get("scope", [])):
                continue

            obj = dict(seal)
            obj["status"] = status
            if sid in revoked:
                obj["revocation"] = revoked[sid]
            out.append(obj)

        out.sort(key=lambda s: int(s.get("issued_at", 0)), reverse=True)
        out = out[: max(0, int(args.limit))]

        print(json.dumps({"seals": out}, indent=2))
    except Exception as e:
        print(f"error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

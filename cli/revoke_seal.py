from __future__ import annotations

import argparse
import json
import sys

from ..seals.revoker import RevokeRequest, revoke_seal


def main() -> None:
    parser = argparse.ArgumentParser(description="Revoke an AUCTORISEAL authority seal")
    parser.add_argument("--db", required=True, help="Path to ledger database")
    parser.add_argument("--revoked-seal-id", required=True, help="Seal ID to revoke")
    parser.add_argument("--revoked-by", required=True, help="Revoking authority ID")
    parser.add_argument("--reason", default="", help="Human-readable reason")
    parser.add_argument("--protocol", type=int, default=1, help="Protocol version")
    parser.add_argument("--notes", help="Optional notes")

    args = parser.parse_args()

    try:
        req = RevokeRequest(
            revoked_seal_id=args.revoked_seal_id,
            revoked_by=args.revoked_by,
            reason=args.reason,
            protocol=args.protocol,
            notes=args.notes,
        )

        res = revoke_seal(db_path=args.db, req=req)

        print(json.dumps({
            "revocation_id": res.revocation_id,
            "seq": res.seq,
            "event_hash": res.event_hash,
        }, indent=2))
    except Exception as e:
        print(f"error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

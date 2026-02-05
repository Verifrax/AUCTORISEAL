from __future__ import annotations

import argparse
import json
import sys

from ..ledger.integrity import check_integrity


def main() -> None:
    parser = argparse.ArgumentParser(description="Verify AUCTORISEAL ledger integrity (hash chain)")
    parser.add_argument("--db", required=True, help="Path to ledger database")
    args = parser.parse_args()

    try:
        res = check_integrity(args.db)
        print(json.dumps({
            "ok": res.ok,
            "checked_events": res.checked_events,
            "last_seq": res.last_seq,
            "last_hash": res.last_hash,
            "error": res.error,
        }, indent=2))
        if not res.ok:
            sys.exit(2)
    except Exception as e:
        print(f"error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

from __future__ import annotations

import argparse
import os
import sqlite3
import sys
from typing import List

from ..ledger.reader import tail_events


MIGRATIONS_DIR = os.path.join(os.path.dirname(__file__), "..", "ledger", "migrations")


def _db_connect(db_path: str) -> sqlite3.Connection:
    os.makedirs(os.path.dirname(db_path) or ".", exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def _read_sql_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def _list_migrations() -> List[str]:
    files = []
    for name in os.listdir(MIGRATIONS_DIR):
        if name.endswith(".sql"):
            files.append(name)
    files.sort()
    return files


def _apply_migrations(db_path: str) -> None:
    migs = _list_migrations()
    if not migs:
        raise RuntimeError("no migrations found")

    conn = _db_connect(db_path)
    try:
        with conn:
            for m in migs:
                sql = _read_sql_file(os.path.join(MIGRATIONS_DIR, m))
                conn.executescript(sql)
    finally:
        conn.close()


def main() -> None:
    parser = argparse.ArgumentParser(description="Inspect or initialize the AUCTORISEAL ledger")
    parser.add_argument("--db", required=True, help="Path to ledger database")
    parser.add_argument("--init", action="store_true", help="Initialize ledger by applying migrations")
    parser.add_argument("--tail", type=int, default=0, help="Print last N events")
    args = parser.parse_args()

    try:
        if args.init:
            _apply_migrations(args.db)
            print("ok: migrations applied")

        if args.tail > 0:
            rows = tail_events(args.db, limit=args.tail)
            for r in rows:
                print(f"{r.seq} {r.event_type} {r.event_id} {r.issued_by} {r.issued_at}")
    except Exception as e:
        print(f"error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

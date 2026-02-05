#!/bin/sh
set -e

DB_PATH="${AUCTORISEAL_DB:-./ledger.sqlite}"
BIND="${AUCTORISEAL_BIND:-0.0.0.0}"
PORT="${AUCTORISEAL_PORT:-8080}"

if [ ! -f "$DB_PATH" ]; then
  echo "[auctoriseal] initializing ledger"
  python -m auctoriseal.cli.inspect_ledger --db "$DB_PATH" --init
fi

echo "[auctoriseal] starting API on ${BIND}:${PORT}"
exec python -m auctoriseal.api.server

-- 0001_init.sql
-- Initial AUCTORISEAL ledger schema
-- This migration establishes the append-only authority ledger.

BEGIN;

PRAGMA foreign_keys = ON;

-- =========================
-- Ledger Metadata
-- =========================
CREATE TABLE ledger_meta (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL
);

INSERT INTO ledger_meta (key, value) VALUES
    ('protocol_version', '1'),
    ('ledger_version', '1');

-- =========================
-- Ledger Events
-- =========================
CREATE TABLE ledger_events (
    seq INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id TEXT NOT NULL UNIQUE,
    event_type TEXT NOT NULL,
    protocol INTEGER NOT NULL,
    issued_by TEXT NOT NULL,
    issued_at INTEGER NOT NULL,
    payload_hash TEXT NOT NULL,
    payload TEXT NOT NULL,
    previous_hash TEXT,
    event_hash TEXT NOT NULL
);

CREATE INDEX idx_ledger_events_type
    ON ledger_events(event_type);

-- =========================
-- Authority Seals
-- =========================
CREATE TABLE seals (
    seal_id TEXT PRIMARY KEY,
    issued_by TEXT NOT NULL,
    issued_to TEXT NOT NULL,
    scope TEXT NOT NULL,
    constraints TEXT NOT NULL,
    issued_at INTEGER NOT NULL,
    expires_at INTEGER,
    protocol INTEGER NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('active', 'revoked'))
);

CREATE INDEX idx_seals_status
    ON seals(status);

COMMIT;

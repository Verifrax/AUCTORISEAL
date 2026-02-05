-- AUCTORISEAL LEDGER SCHEMA
-- Append-only authority ledger
-- No UPDATE. No DELETE. Ever.

PRAGMA foreign_keys = ON;

-- =========================
-- Ledger Metadata
-- =========================
CREATE TABLE IF NOT EXISTS ledger_meta (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL
);

-- =========================
-- Ledger Events
-- =========================
CREATE TABLE IF NOT EXISTS ledger_events (
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

-- =========================
-- Authority Seals
-- =========================
CREATE TABLE IF NOT EXISTS seals (
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

-- =========================
-- Revocations
-- =========================
CREATE TABLE IF NOT EXISTS revocations (
    revocation_id TEXT PRIMARY KEY,
    seal_id TEXT NOT NULL,
    revoked_by TEXT NOT NULL,
    revoked_at INTEGER NOT NULL,
    protocol INTEGER NOT NULL,
    reason TEXT,
    FOREIGN KEY (seal_id) REFERENCES seals(seal_id)
);

-- =========================
-- Freeze Events
-- =========================
CREATE TABLE IF NOT EXISTS freezes (
    freeze_id TEXT PRIMARY KEY,
    issued_by TEXT NOT NULL,
    issued_at INTEGER NOT NULL,
    protocol INTEGER NOT NULL,
    active INTEGER NOT NULL CHECK (active IN (0, 1))
);

-- =========================
-- Integrity Constraints
-- =========================
CREATE INDEX IF NOT EXISTS idx_ledger_events_type
    ON ledger_events(event_type);

CREATE INDEX IF NOT EXISTS idx_seals_status
    ON seals(status);

CREATE INDEX IF NOT EXISTS idx_revocations_seal
    ON revocations(seal_id);

-- =========================
-- Invariant Enforcement Notes
-- =========================
-- 1. This schema is append-only by policy.
-- 2. Application code MUST NOT issue UPDATE or DELETE.
-- 3. Corrections occur only via new ledger_events.
-- 4. event_hash SHOULD be computed over:
--    (previous_hash || payload_hash || issued_at || event_type)
-- 5. Any integrity failure MUST cause validation to fail closed.

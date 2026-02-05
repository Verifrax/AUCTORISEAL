-- 0002_add_revocation.sql
-- Add revocation and freeze support to AUCTORISEAL ledger

BEGIN;

PRAGMA foreign_keys = ON;

-- =========================
-- Revocations
-- =========================
CREATE TABLE revocations (
    revocation_id TEXT PRIMARY KEY,
    seal_id TEXT NOT NULL,
    revoked_by TEXT NOT NULL,
    revoked_at INTEGER NOT NULL,
    protocol INTEGER NOT NULL,
    reason TEXT,
    FOREIGN KEY (seal_id) REFERENCES seals(seal_id)
);

CREATE INDEX idx_revocations_seal
    ON revocations(seal_id);

-- =========================
-- Freeze Events
-- =========================
CREATE TABLE freezes (
    freeze_id TEXT PRIMARY KEY,
    issued_by TEXT NOT NULL,
    issued_at INTEGER NOT NULL,
    protocol INTEGER NOT NULL,
    active INTEGER NOT NULL CHECK (active IN (0, 1))
);

COMMIT;

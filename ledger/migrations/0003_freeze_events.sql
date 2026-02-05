-- 0003_freeze_events.sql
-- Enforce single active freeze invariant and strengthen freeze semantics

BEGIN;

PRAGMA foreign_keys = ON;

-- =========================
-- Enforce single active freeze
-- =========================
CREATE UNIQUE INDEX IF NOT EXISTS idx_freezes_single_active
    ON freezes(active)
    WHERE active = 1;

-- =========================
-- Ledger meta update
-- =========================
INSERT OR REPLACE INTO ledger_meta (key, value)
VALUES ('ledger_version', '3');

COMMIT;

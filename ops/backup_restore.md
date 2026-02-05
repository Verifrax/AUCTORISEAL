# BACKUP & RESTORE

This document defines the **mandatory backup and restore procedures** for AUCTORISEAL.

Because authority is recorded, **loss or corruption of the ledger is catastrophic**.
Backups exist to preserve **finality**, not convenience.

---

## Backup Scope

The following assets MUST be backed up:

- Ledger database (`ledger.sqlite` or equivalent)
- Ledger migration files
- Runtime configuration (excluding secrets where applicable)
- Version metadata (`VERSION`)

Source code alone is insufficient.

---

## Backup Principles

- Backups MUST be **immutable once written**
- Backups MUST be **verifiable**
- Backups MUST preserve **ordering and integrity**
- Backups MUST be stored **off-host**

Partial backups are unacceptable.

---

## Backup Frequency

Minimum requirements:

- Ledger: after every authority-changing operation (or continuous)
- Configuration: on every change
- Full snapshot: daily

Higher frequency is encouraged for high-stakes deployments.

---

## Backup Verification

Every backup MUST be verified by:

1. Restoring to an isolated environment
2. Running `verify_integrity`
3. Confirming ledger sequence continuity
4. Confirming protocol version compatibility

Unverified backups are considered nonexistent.

---

## Restore Procedure

1. **Stop all services**
2. **Restore ledger database**
3. **Restore configuration**
4. **Verify integrity**
5. **Start in read-only mode**
6. **Manually confirm authority state**
7. **Resume normal operation**

Skipping any step invalidates the restore.

---

## Restore Constraints

- Restores MUST NOT merge ledgers
- Restores MUST NOT reorder events
- Restores MUST NOT skip migrations
- Restores MUST NOT alter history

If a restore requires modification, it is a failure.

---

## Disaster Recovery

If all backups are lost:

- Authority history is unrecoverable
- All existing authority MUST be treated as invalid
- A new authority epoch MUST be established explicitly

There is no silent recovery path.

---

## Testing

Backup and restore MUST be tested:

- at least quarterly
- after schema changes
- after protocol version changes

Untested recovery is not recovery.

---

## Final Invariant

> **If authority history cannot be restored intact, authority cannot be trusted.**

Nothing overrides this rule.

# DECOMMISSION

This document defines the **formal decommissioning procedure** for an AUCTORISEAL instance.

Decommissioning is not deletion.  
It is the controlled **end of authority issuance** with preserved history.

---

## Purpose

Decommissioning exists to ensure that:

- authority evolution stops cleanly
- history remains intact and verifiable
- no implicit authority survives shutdown
- downstream systems can transition safely

An undeclared shutdown is a governance failure.

---

## Preconditions

Before decommissioning:

- [ ] No active incident is in progress
- [ ] Ledger integrity verifies cleanly
- [ ] All operators are notified
- [ ] Downstream systems are prepared for authority loss

If these conditions are not met, decommissioning MUST NOT proceed.

---

## Decommission Procedure

1. **Issue a freeze**
   - Halt all new authority issuance and delegation
2. **Revoke active authority (optional but recommended)**
   - Explicitly revoke remaining active seals
3. **Verify final ledger state**
   - Run `verify_integrity`
4. **Create final backup**
   - Immutable, verified snapshot
5. **Mark instance as decommissioned**
   - Record decommission intent in governance records
6. **Shut down services**
   - Stop API and operator interfaces

All steps must be performed in order.

---

## Post-Decommission State

After decommissioning:

- No authority may be issued
- No delegation may occur
- Ledger remains readable
- Validation remains possible
- History remains final

Read-only access is preserved indefinitely where feasible.

---

## Downstream Responsibilities

Downstream systems MUST:

- treat authority from this instance as frozen
- not assume replacement authority implicitly
- transition to a new authority instance explicitly if required

Silent migration is forbidden.

---

## Ledger Preservation

The ledger MUST be preserved:

- unmodified
- intact
- verifiable
- accessible for audit

Deletion of the ledger is prohibited.

---

## Legal / Organizational Notes

Decommissioning may coincide with:

- organizational shutdown
- product retirement
- authority migration
- governance change

AUCTORISEAL does not enforce legal procedures, but requires authority clarity.

---

## Final Rule

> **Authority may end, but history must not.**

Decommissioning without preserved history invalidates legitimacy.

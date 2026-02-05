# REVOCATION

This document defines the **revocation model** of AUCTORISEAL.

Revocation is the mechanism by which authority **ceases to exist**.
There is no suspension, soft-disable, or grace period.

---

## Purpose

Revocation exists to answer one question:

> **How does authority stop?**

Stopping authority must be:
- explicit
- immediate
- recorded
- irreversible in history

---

## Core Rules

### 1. Revocation Overrides Grant

A revocation event **immediately invalidates** the referenced authority seal.

No prior grant survives revocation.
No future validation may treat a revoked seal as valid.

---

### 2. Revocation Is Explicit

Authority never expires silently.

Authority ends only by:
- explicit revocation
- explicit freeze followed by revocation
- explicit scope exhaustion (if defined)

If none occur, authority remains valid.

---

### 3. Revocation Is Recorded

Every revocation:
- is written to the append-only ledger
- references the revoked seal
- records issuer, timestamp, and reason

Unrecorded revocation does not exist.

---

### 4. Revocation Is Immediate

Revocation takes effect at the moment it is recorded.

There is:
- no delay
- no propagation window
- no eventual consistency

Consumers must fail closed if revocation state is uncertain.

---

### 5. Revocation Is Deterministic

Given the same ledger state:
- a seal is either revoked or not
- validation must always yield the same result

Interpretation is forbidden.

---

## Who May Revoke

A seal may be revoked by:
- the original issuer
- any ancestor authority in the delegation chain
- a root authority
- an emergency freeze authority (where applicable)

No other entity may revoke authority.

---

## Revocation Scope

Revocation applies to:
- the specific seal referenced
- all actions authorized by that seal

Revocation does **not** automatically revoke:
- sibling seals
- child delegations (unless explicitly chained)

Delegated authority must be revoked separately unless delegation rules specify otherwise.

---

## Freeze Interaction

When a freeze is active:
- new authority issuance is forbidden
- delegation is forbidden
- revocation remains allowed

Freeze exists to **enable safe revocation under uncertainty**.

---

## Error Conditions

Revocation MUST fail if:
- the referenced seal does not exist
- the revoker lacks authority
- the ledger is in an invalid state

Failure to revoke must be explicit and visible.

---

## Audit Requirements

Every revocation record must include:
- revoked seal identifier
- revoking authority identifier
- timestamp
- reason (free-text, non-normative)

Auditability is mandatory.

---

## Non-Goals

Revocation does not:
- judge intent
- assess correctness
- prevent future re-issuance
- erase history

Revocation only ends authority.

---

## Final Invariant

> **Authority ends only when revocation is recorded.**

Anything else is narrative.

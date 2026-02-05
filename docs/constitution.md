# CONSTITUTION

This document defines the **unchanging principles** of AUCTORISEAL.  
It is the highest-level normative text in this repository.

If any implementation, policy, or document contradicts this constitution, **the constitution prevails**.

---

## Purpose

AUCTORISEAL exists to make **authority explicit, prior, bounded, and recorded** before irreversible actions are allowed.

Its purpose is not safety, speed, or automation.

Its purpose is **legitimacy**.

---

## Core Principles

### 1. Authority Must Be Explicit

No authority is assumed.  
No authority is inferred.  
No authority exists unless it is **explicitly issued and recorded**.

If authority is not sealed, it does not exist.

---

### 2. Authority Must Precede Action

Authority must exist **before** any action that requires it.

Post-hoc justification is invalid.

If authority is granted after an action, the action is unauthorized by definition.

---

### 3. Authority Must Be Bounded

Every authority grant must specify:

- scope
- constraints
- duration (explicit or implicit)
- issuer

Unbounded authority is prohibited.

---

### 4. Authority Must Be Recorded

All authority grants, revocations, freezes, and delegations are:

- recorded in an append-only ledger
- immutable once recorded
- verifiable deterministically

There is no private authority.

---

### 5. Revocation Overrides Grant

Revocation immediately invalidates authority.

There is no grace period.
There is no implied continuation.

If authority is revoked, it no longer exists.

---

### 6. Finality Is Required

Authority records are final.

History is not rewritten.
Records are not erased.
Corrections occur only through new records.

Finality is a feature, not a flaw.

---

### 7. Determinism Over Interpretation

Given the same ledger state and protocol version, authority validation must produce the same result.

Human interpretation does not override recorded facts.

---

### 8. Legitimacy Is Ecosystem-Scoped

Authority asserted by AUCTORISEAL applies only to:

- systems that explicitly defer to it
- scopes explicitly defined in seals

No external legitimacy is implied.

---

### 9. Authority Is Not Decision-Making

AUCTORISEAL does not decide outcomes.

It records:
- who was allowed to decide
- under what conditions

Responsibility for decisions remains with the authority holder.

---

### 10. Emergency Powers Are Explicit

Emergency actions (freezes) must be:

- explicit
- recorded
- reversible only by defined authority

There are no implicit emergencies.

---

## Invariants

The following must never change:

- No implicit authority
- No silent mutation
- No unrecorded action
- No deletion of history
- No authority without scope

Any change that violates an invariant invalidates AUCTORISEAL.

---

## Evolution

This constitution may evolve only if:

1. a new constitution version is authored
2. the change is recorded in the ledger
3. the protocol version is incremented

Silent evolution is forbidden.

---

## Final Rule

> **If authority is not explicit, prior, bounded, and recorded, it does not exist.**

This rule has no exception.

# AUCTORISEAL → ADJUTORIX Integration

This module defines the **hard authority boundary** between **AUCTORISEAL** and **ADJUTORIX**.

ADJUTORIX MUST defer to AUCTORISEAL for all authority decisions involving:
- irreversible actions
- disk mutation
- deployment
- freeze-sensitive operations

There are no exceptions.

---

## Purpose

The purpose of this integration is to ensure:

> **No action occurs unless it is explicitly authorized by a valid authority seal.**

ADJUTORIX enforces execution.  
AUCTORISEAL defines legitimacy.

---

## Contract

ADJUTORIX MUST:

1. Call `authorize_action()` **before** any irreversible operation
2. Pass:
   - subject (who is acting)
   - action (what is being requested)
   - constraints (execution context)
   - authority mode (external / managed / auto)
3. Treat any failure as **hard stop**

A failure to authorize MUST abort the operation.

---

## Adapter Responsibilities

The adapter:

- validates authority via AUCTORISEAL ledger
- enforces mode-based policy
- returns seal provenance on success
- raises on any ambiguity or denial

It does **not**:
- decide execution logic
- retry authorization
- degrade authority requirements

---

## Failure Semantics

If authorization fails:

- the action is unauthorized
- ADJUTORIX must not proceed
- the failure reason must be surfaced to the operator

Failing open is forbidden.

---

## Freeze Semantics

When a freeze is active:

- issuance and delegation are blocked
- existing seals remain valid
- ADJUTORIX may optionally surface freeze state to operators

Freeze is a governance signal, not a bypass.

---

## Invariant

> **If ADJUTORIX acts without a valid seal, the system is compromised.**

This integration exists to prevent that state.

---

## Final Note

This adapter is intentionally small and strict.

Complexity belongs in:
- the authority system (AUCTORISEAL)
- the execution engine (ADJUTORIX)

Not in the boundary between them.

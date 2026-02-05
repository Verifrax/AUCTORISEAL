# PROTOCOL

This document defines the **AUCTORISEAL authority protocol**.
The protocol is the **binding contract** between AUCTORISEAL and all systems that defer to it.

If implementation behavior conflicts with this document or the schemas it references,  
**the protocol prevails**.

---

## Purpose

The protocol exists to ensure that:

- authority is explicit
- authority is validated deterministically
- authority evolution is auditable
- authority failure is detectable

The protocol does not define business logic or outcomes.

---

## Protocol Versioning

- The protocol version is a **single integer**.
- The version applies to:
  - envelopes
  - seals
  - authority grants
  - revocations
  - registry references
  - errors
- Version is recorded in every protocol object.

### Compatibility Rules

- **Minor changes are forbidden**.
- Any semantic change requires a **version increment**.
- Consumers MUST reject objects with unsupported protocol versions.

There is no implicit backward compatibility.

---

## Canonical Schemas

The protocol consists of the following canonical schemas:

- `envelope.schema.json`
- `seal.schema.json`
- `authority.schema.json`
- `revocation.schema.json`
- `registry.schema.json`
- `error.schema.json`

All schemas are authoritative.

---

## Envelope Rules

- Every message MUST be wrapped in an envelope.
- Envelopes define:
  - message type
  - protocol version
  - trace context
  - session context
  - payload
- Payloads without envelopes are invalid.

---

## Authority Rules

- Authority exists only when represented by a valid seal.
- Validation MUST:
  - evaluate delegation chains
  - evaluate scope
  - evaluate constraints
  - evaluate revocation state
- Validation MUST be deterministic.

If validation result is ambiguous, it MUST fail closed.

---

## Revocation Rules

- Revocation overrides all grants.
- Revocation is immediate.
- Revocation state MUST be checked during every validation.

Caching revocation state without verification is forbidden.

---

## Registry Rules

- Registry entries derive legitimacy from authority seals.
- Registry status MUST reflect seal status.
- Registry implementations MUST NOT assert authority independently.

---

## Error Semantics

- Errors are protocol objects.
- Errors MUST include:
  - machine-readable code
  - human-readable message
  - protocol version
- Errors MUST NOT imply authority or legitimacy.

---

## Determinism Requirement

Given:
- identical protocol version
- identical ledger state
- identical input

Validation MUST produce identical output.

Non-deterministic behavior is a protocol violation.

---

## Failure Posture

On protocol violation:
- validation MUST fail
- no authority is granted
- no fallback behavior is allowed

Failing open is forbidden.

---

## Evolution

Protocol evolution requires:
1. protocol version increment
2. schema updates
3. explicit documentation
4. ledger recording (where applicable)

Silent evolution is forbidden.

---

## Final Rule

> **If it is not defined by this protocol, it is not authoritative.**

There are no exceptions.

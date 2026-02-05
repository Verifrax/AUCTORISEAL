# THREAT MODEL

This document defines the **explicit threat model** for AUCTORISEAL.

AUCTORISEAL is an **authority and legitimacy system**.  
Threats are evaluated based on their ability to **forge, corrupt, bypass, or obscure authority**.

---

## Security Objective

The primary objective is:

> **Prevent silent or undetectable misuse of authority.**

Secondary objectives:
- detect authority forgery
- detect history tampering
- ensure revocation is effective
- ensure validation is deterministic

Availability, performance, and convenience are **explicitly secondary**.

---

## Assets

The following assets are critical:

- Authority Seals
- Ledger integrity
- Delegation chains
- Revocation records
- Freeze records
- Protocol schemas
- Validation logic

Compromise of any of these compromises legitimacy.

---

## Adversaries

### External Adversary
- No trusted access
- Attempts to forge seals
- Attempts to replay or inject records
- Attempts to misrepresent authority

### Insider Adversary
- Has legitimate access
- Attempts to exceed granted scope
- Attempts to hide or rewrite actions
- Attempts to bypass revocation

### Operator Error
- Mis-issuance of authority
- Accidental revocation
- Misconfiguration
- Incorrect delegation

Operator error is assumed to be inevitable.

---

## In-Scope Threats

- Forged authority seals
- Unauthorized delegation
- Scope escalation
- Constraint bypass
- Ledger modification
- Ledger truncation
- Replay with altered context
- Validation inconsistencies
- Silent revocation failure
- Authority persistence after revocation
- Ambiguous authority interpretation

---

## Out-of-Scope Threats

- AI model hallucination
- Downstream system bugs
- Network-level attacks outside deployment assumptions
- Physical compromise of host hardware
- Legal or regulatory disputes
- Business logic failures in products

---

## Trust Assumptions

AUCTORISEAL assumes:

- Ledger storage is durable
- Cryptographic primitives (if enabled) are not broken
- Root authority identifiers are protected
- Operators follow documented procedures

Violation of these assumptions degrades trust but does not invalidate recorded history.

---

## Mitigations

### Authority Forgery
- Deterministic seal schema
- Issuer validation against ledger
- Delegation chain verification

### History Tampering
- Append-only ledger
- Integrity verification
- Hash chaining or fingerprints

### Scope Abuse
- Strict scope matching
- Constraint evaluation
- No wildcard expansion

### Revocation Failure
- Revocation precedence
- Immediate invalidation
- Validation checks include revocation state

### Ambiguity
- Protocol schemas override interpretation
- Deterministic validation rules
- Explicit error states

---

## Residual Risk

Residual risks accepted by design:

- Misuse of legitimately granted authority
- Malicious but authorized actions
- Delayed detection outside the system

AUCTORISEAL does not attempt to prevent misuse of valid authority.

---

## Failure Posture

On detection of integrity failure:

- Validation MUST fail closed
- System enters read-only mode
- No new authority is issued
- Operators must investigate

Failing open is forbidden.

---

## Final Statement

> **AUCTORISEAL treats unclear authority as a critical failure.  
Silence is considered compromise.**

This threat model is binding.

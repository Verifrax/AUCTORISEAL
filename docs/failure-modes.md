# FAILURE MODES

This document enumerates **explicit failure modes** of AUCTORISEAL and the required system posture for each.

AUCTORISEAL treats failure as **normal and expected**.  
What matters is that failure is **detectable, bounded, and final**.

---

## Classification

Failure modes are grouped by impact on **authority legitimacy**.

Priority order:
1. Authority ambiguity
2. Authority forgery
3. Authority persistence after revocation
4. History corruption
5. Availability loss

If multiple failures occur, the highest-priority posture applies.

---

## FM-01: Missing Authority

**Description**  
An action requiring authority occurs without a corresponding valid seal.

**Detection**  
- Validation returns `NO_VALID_AUTHORITY`

**Posture**  
- Action is declared unauthorized
- Downstream systems MUST reject the action
- No remediation inside AUCTORISEAL

**Severity**  
Critical

---

## FM-02: Ambiguous Authority

**Description**  
Multiple seals appear to authorize an action with conflicting scope or constraints.

**Detection**  
- Validation detects non-deterministic outcome

**Posture**  
- Validation MUST fail closed
- Action is unauthorized
- Operator investigation required

**Severity**  
Critical

---

## FM-03: Forged or Invalid Seal

**Description**  
A seal fails schema, issuer, delegation, or integrity validation.

**Detection**  
- Seal validation failure
- Delegation chain invalid

**Posture**  
- Seal rejected
- Event logged
- No authority granted

**Severity**  
Critical

---

## FM-04: Revocation Ignored

**Description**  
A revoked seal continues to be treated as valid by a consumer.

**Detection**  
- Validation mismatch against ledger state

**Posture**  
- Seal invalidated
- Consumer considered non-compliant
- Incident response initiated

**Severity**  
Critical

---

## FM-05: Ledger Integrity Failure

**Description**  
Ledger verification detects tampering, truncation, or inconsistency.

**Detection**  
- Hash / fingerprint mismatch
- Migration inconsistency
- Verification failure

**Posture**  
- System enters read-only mode
- No new seals issued
- Only inspection allowed

**Severity**  
Critical

---

## FM-06: Freeze State Active

**Description**  
A freeze event is active in the ledger.

**Detection**  
- Active freeze record present

**Posture**  
- Issuance forbidden
- Delegation forbidden
- Revocation allowed

**Severity**  
High (intentional)

---

## FM-07: Operator Error

**Description**  
Authority incorrectly issued, scoped, or revoked by an operator.

**Detection**  
- Human review
- Post-incident analysis

**Posture**  
- Correct via revocation
- Issue new seal if required
- Record correction explicitly

**Severity**  
Medium

---

## FM-08: Protocol Mismatch

**Description**  
Consumer uses an incompatible protocol version.

**Detection**  
- Version validation failure

**Posture**  
- Validation fails
- No authority granted

**Severity**  
High

---

## FM-09: Availability Loss

**Description**  
AUCTORISEAL instance is temporarily unavailable.

**Detection**  
- Service unreachable

**Posture**  
- Existing seals remain valid
- No new authority can be issued
- Consumers must degrade safely

**Severity**  
Medium

---

## FM-10: Stale Consumer Cache

**Description**  
Consumer validates authority using stale ledger data.

**Detection**  
- Ledger sequence mismatch

**Posture**  
- Validation fails
- Consumer must refresh state

**Severity**  
High

---

## Non-Failures (By Design)

The following are **not** failures:

- Authorized misuse within scope
- Bad decisions by authority holders
- Undesired outcomes of authorized actions
- Downstream system bugs

AUCTORISEAL does not judge outcomes.

---

## Failure Invariant

> **When authority is unclear, the system must stop.**

Any behavior that continues under ambiguity is a defect.

---

## Final Rule

> **Failure must reduce power, never expand it.**

This rule is absolute.

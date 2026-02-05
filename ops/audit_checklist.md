# AUDIT CHECKLIST

This checklist defines what an auditor, reviewer, or investigator must be able to verify
when assessing an AUCTORISEAL deployment.

If any item cannot be verified, **authority legitimacy is compromised**.

---

## 1. Ledger Integrity

- [ ] Ledger storage is append-only
- [ ] No UPDATE or DELETE statements exist in application code
- [ ] Hash chaining is enabled and verifiable
- [ ] `verify_integrity` passes with no errors
- [ ] Ledger sequence numbers are continuous
- [ ] Ledger replay is deterministic

---

## 2. Protocol Compliance

- [ ] All protocol objects include a protocol version
- [ ] Protocol version is supported by consumers
- [ ] Unsupported protocol versions are rejected
- [ ] Schemas match deployed code behavior
- [ ] No undocumented fields are treated as authoritative

---

## 3. Authority Seals

- [ ] Every seal has a unique seal_id
- [ ] Issuer identity is explicit
- [ ] Subject identity is explicit
- [ ] Scope is explicit and non-empty
- [ ] Constraints are explicit
- [ ] Seal issuance is recorded in the ledger
- [ ] Seal fingerprints are deterministic

---

## 4. Revocation

- [ ] Revocation events are explicit and recorded
- [ ] Revocation overrides prior grants immediately
- [ ] Revoked seals are never treated as valid
- [ ] Revocation authority is validated
- [ ] Revocation reasons are recorded (non-normative)

---

## 5. Freeze Semantics

- [ ] Freeze events are explicit and recorded
- [ ] Only one active freeze exists at a time
- [ ] Issuance and delegation are blocked under freeze
- [ ] Revocation remains allowed under freeze
- [ ] Freeze state is surfaced to operators

---

## 6. Validation Behavior

- [ ] Validation is deterministic
- [ ] Ambiguous authority fails closed
- [ ] Missing authority fails closed
- [ ] Expired authority is rejected
- [ ] Constraint mismatches are rejected
- [ ] Scope mismatches are rejected

---

## 7. Integration Boundaries

- [ ] ADJUTORIX defers all irreversible actions to AUCTORISEAL
- [ ] SPEEDKIT derives registry legitimacy from AUCTORISEAL
- [ ] No downstream system self-authorizes
- [ ] Authority checks occur before execution

---

## 8. Operational Controls

- [ ] Operator actions are explicit
- [ ] Operator identity is recorded
- [ ] No background or automatic issuance exists
- [ ] Configuration changes are auditable
- [ ] Backups preserve ledger integrity

---

## 9. Failure Handling

- [ ] Integrity failures force read-only mode
- [ ] Authority ambiguity halts execution
- [ ] Errors are explicit and surfaced
- [ ] No silent fallback behavior exists

---

## 10. Documentation Consistency

- [ ] Constitution exists and is unmodified
- [ ] Governance document is present
- [ ] Threat model is present
- [ ] Failure modes are documented
- [ ] This checklist matches deployed behavior

---

## Final Assertion

> **If this checklist cannot be completed without exceptions,  
> authority legitimacy cannot be asserted.**

There are no partial passes.

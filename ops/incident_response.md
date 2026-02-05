# INCIDENT RESPONSE

This document defines the **mandatory response procedure** for incidents involving
AUCTORISEAL authority, integrity, or legitimacy.

Speed is secondary to correctness.  
Ambiguity is treated as failure.

---

## Incident Definition

An incident is any event where:

- authority may have been forged
- authority may have been bypassed
- authority may have persisted after revocation
- ledger integrity may have been compromised
- protocol behavior may have been violated
- actions occurred under unclear authority

If authority is unclear, it is an incident.

---

## Severity Levels

### Critical
- Ledger integrity failure
- Undetected authority bypass
- Revocation ignored
- Protocol mismatch causing false authorization

### High
- Incorrect issuance
- Incorrect delegation
- Freeze failure
- Stale authority usage

### Medium
- Operator error with clear remediation
- Temporary availability loss

---

## Immediate Actions (All Incidents)

1. **Stop authority issuance**
   - Issue a freeze immediately if not already active
2. **Preserve evidence**
   - Snapshot ledger database
   - Preserve logs and configs
3. **Fail closed**
   - Downstream systems must halt irreversible actions
4. **Notify operators**
   - Human notification is mandatory

---

## Investigation Procedure

1. Verify ledger integrity (`verify_integrity`)
2. Identify affected seals and scopes
3. Trace delegation chains
4. Identify first invalid or ambiguous event
5. Determine blast radius (systems, actions, time)

Ledger records are the primary source of truth.

---

## Containment

- Revoke affected seals explicitly
- Do not delete or modify records
- Record all containment actions in the ledger

Containment actions must themselves be auditable.

---

## Recovery

- Re-issue authority only after:
  - root cause is identified
  - governance approval (if applicable)
  - protocol compatibility is confirmed
- Lift freeze only when authority clarity is restored

Recovery must not rewrite history.

---

## Communication

- Use precise language
- Do not speculate beyond recorded facts
- Distinguish between:
  - unauthorized actions
  - authorized misuse
  - system failures

Narrative without evidence is prohibited.

---

## Post-Incident Review

Required outputs:

- incident timeline (ledger-backed)
- root cause analysis
- remediation steps
- preventive controls
- governance updates (if needed)

Reviews must reference ledger sequence numbers.

---

## Non-Goals

Incident response does not:

- assign legal blame
- determine business liability
- judge intent
- guarantee future safety

It restores authority clarity.

---

## Final Rule

> **When authority is in doubt, stop everything.**

Resumption without clarity is forbidden.

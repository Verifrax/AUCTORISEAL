# GOVERNANCE

This document defines **who may issue authority**, **how authority evolves**, and **how final decisions are made** within AUCTORISEAL.

AUCTORISEAL governance is intentionally **explicit, minimal, and slow**.

---

## Purpose

Governance exists to answer one question:

> **Who is allowed to grant, revoke, or freeze authority — and under what record?**

All other questions are secondary.

---

## Governance Scope

This document governs:

- Authority roots
- Authority delegation
- Seal issuance
- Seal revocation
- Emergency freezes
- Governance evolution

It does **not** govern:
- Downstream system behavior
- Product business logic
- Legal compliance
- AI model decisions

---

## Authority Roots

### Root Authority

- AUCTORISEAL has one or more **Root Authorities**.
- Root Authorities are defined in `authority/roots.yaml`.
- Root Authorities may:
  - issue authority seals
  - revoke authority seals
  - delegate authority
  - initiate freeze events

Root Authorities are **explicitly named** and **versioned**.

There is no implicit root.

---

## Delegated Authority

- Root Authorities may delegate authority to named delegates.
- Delegation must specify:
  - scope
  - constraints
  - duration
- Delegation chains are finite and must be verifiable.

Delegates may only act **within the granted scope**.

Delegation does not imply permanence.

---

## Seal Issuance

- Authority is granted by issuing an **Authority Seal**.
- Every seal issuance:
  - is explicit
  - is recorded in the ledger
  - references its issuing authority
  - includes scope and constraints

Issuance is **never automatic**.

---

## Seal Revocation

- Any seal may be revoked by:
  - its issuer
  - an ancestor authority in the delegation chain
- Revocation:
  - is explicit
  - is recorded in the ledger
  - takes effect immediately upon validation

Revocation overrides all prior grants.

---

## Freeze Semantics

A **Freeze** is an emergency governance action.

When a freeze is issued:
- no new authority may be granted
- no delegation may occur
- only revocation is allowed

Freeze events are:
- explicit
- rare
- recorded
- reversible only by Root Authority

---

## Governance Evolution

Governance rules may evolve only by:

1. issuing a governance change record
2. recording the change in the ledger
3. bumping the authority protocol version

Governance changes are **never implicit**.

Backward compatibility is not guaranteed across governance versions.

---

## Dispute Resolution

If there is disagreement about authority:

- the ledger record is final
- seal validity is determined deterministically
- human interpretation does not override recorded facts

AUCTORISEAL does not arbitrate disputes beyond validating records.

---

## Transparency

- Governance rules are public.
- Root authority identifiers are public.
- Seal metadata is public.
- Private keys and credentials are never public.

Opacity is considered a governance failure.

---

## Non-Claims

AUCTORISEAL governance does **not** claim:
- regulatory authority
- legal enforceability
- certification status

It defines authority **only within systems that explicitly defer to it**.

---

## Final Rule

> **If authority is not recorded, it does not exist.**

There are no exceptions.

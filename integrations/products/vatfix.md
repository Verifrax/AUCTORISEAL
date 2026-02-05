# VATFIX

VATFIX is a **domain product built on governed execution** and backed by **AUCTORISEAL authority**.

It exists to demonstrate **authority-backed financial logic execution** where ambiguity is unacceptable.

---

## Role in the Ecosystem

- **AUCTORISEAL** — records who is allowed to authorize actions
- **ADJUTORIX** — enforces execution under authority
- **VATFIX** — applies governed logic in a financial domain

VATFIX does not self-authorize.  
It consumes authority.

---

## Authority Dependency

VATFIX MUST require valid authority seals for:

- data mutation
- rule application
- report finalization
- deployment of logic changes

All execution flows MUST pass through ADJUTORIX.

---

## Financial Integrity Posture

VATFIX assumes:

- authority errors are worse than availability loss
- ambiguity must halt execution
- revocation must invalidate pending actions immediately

Failing closed is mandatory.

---

## Audit & Traceability

VATFIX MUST be able to emit:

- authority seal ID
- issuing authority
- execution timestamp
- ADJUTORIX job reference
- ledger sequence number

These records are non-optional.

---

## Failure Semantics

If authority is missing, expired, or revoked:

- processing halts
- outputs are marked invalid
- no partial results are accepted

---

## Non-Claims

VATFIX does not claim:

- legal compliance
- tax correctness
- regulatory approval

It proves only that actions were executed under explicit authority.

---

## Invariant

> **If VATFIX produces output without authority, the output is invalid.**

There are no exceptions.

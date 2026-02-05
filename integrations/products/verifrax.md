# VERIFRAX

VERIFRAX is a **product built on top of the AUCTORISEAL authority layer** and enforced by **ADJUTORIX**.

It exists as **evidence**, not theory.

---

## Role in the Ecosystem

- **AUCTORISEAL** — defines and records authority
- **ADJUTORIX** — enforces governed execution
- **VERIFRAX** — demonstrates authority-backed operation in a real product

VERIFRAX does not implement its own authority logic.

---

## Authority Dependency

VERIFRAX MUST:

- defer all irreversible actions to ADJUTORIX
- require valid authority seals for:
  - state mutation
  - deployments
  - verification finalization
- surface seal provenance in audit outputs

If authority is missing or revoked, VERIFRAX must halt.

---

## Legitimacy Model

VERIFRAX legitimacy is derived from:

- an active authority seal
- recorded provenance in the AUCTORISEAL ledger
- enforcement via ADJUTORIX

There is no standalone legitimacy.

---

## Failure Posture

If authority validation fails:

- execution stops
- verification is marked invalid
- operators are notified

Failing open is forbidden.

---

## Auditability

VERIFRAX MUST be able to produce:

- seal identifiers
- issuing authority
- validation timestamps
- ledger sequence references

Auditability is a first-class requirement.

---

## Non-Claims

VERIFRAX does not claim:

- regulatory approval
- legal certification
- absolute correctness

It proves only that actions occurred under explicit authority.

---

## Invariant

> **If VERIFRAX runs without authority, the system is compromised.**

This invariant is non-negotiable.

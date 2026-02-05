# AUCTORISEAL

## Authority of Record for Governed Systems

**AUCTORISEAL** is an authority-of-record system.
It exists to define, record, and verify **who is allowed to authorize actions** in systems capable of irreversible or externally meaningful effects.

> **Use everything freely but if it matters, you must be able to prove who authorized it before execution.**

Execution can be automated.
Decisions that create responsibility cannot.

---

## What AUCTORISEAL Is

* An **authority layer**, not an execution engine
* An **append-only ledger** of authorization decisions
* A **pre-execution legitimacy system**, not post-incident logging
* A **deterministic source of truth** for audits, investigations, and replay

AUCTORISEAL answers one question only:

> **Who was authorized to allow this action, and under what scope, before it happened?**

---

## What AUCTORISEAL Is Not

AUCTORISEAL is **not**:

* an AI system
* a workflow engine
* a policy document
* a compliance checklist
* a monitoring or logging tool

It does not decide *what* to do.
It decides **who may allow something to be done**.

---

## Core Invariant

Any system that can:

* mutate state
* deploy code
* produce financial impact
* generate externally relied-upon outputs

**MUST be able to prove who authorized the action prior to execution.**

Post-hoc approval is invalid.
Implicit authorization is invalid.
"The system decided" is invalid.

If this proof does not exist, the output is **non-legitimate by definition**.

---

## Scope

AUCTORISEAL records and verifies:

* authority grants (seals)
* scope and constraints
* revocations
* freezes
* protocol versioning

All records are:

* append-only
* tamper-evident
* replayable
* auditable

---

## Relationship to Execution

AUCTORISEAL does **not** execute actions.

Execution systems (for example, automation engines or AI-driven workflows) may:

* run freely
* experiment
* fail

However, **legitimacy is separate from execution**.

Execution without authority may succeed technically, but it is:

* non-defensible
* non-compliant
* non-repudiable

---

## Open vs Authoritative Use

The code in this repository is open and may be used freely.

However:

* **Self-hosted use does not create authority-of-record**
* **Authority-of-record requires continuity, governance, and retention guarantees**

This distinction is intentional.

---

## Repository Posture

This repository is:

* conservative
* slow-moving
* intentionally boring

Changes are limited to:

* security fixes
* protocol evolution
* governance updates

If you are looking for rapid iteration, demos, or experimentation, this is not the correct layer.

---

## Governance and Trust

Authority is defined by:

* explicit governance
* published doctrine
* immutable history

See:

* `docs/constitution.md`
* `GOVERNANCE.md`
* `SECURITY.md`

Trust is earned through **clarity and restraint**, not features.

---

## Final Statement

AUCTORISEAL does not promise safety.
It does not promise correctness.
It does not promise compliance.

It promises one thing only:

> **If an action mattered, you can prove who was allowed to authorize it — or prove that no one was.**

Everything else builds on that.

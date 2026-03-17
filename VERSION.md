# VERSION

**SYSTEM:** AUCTORISEAL  
**VERSIONING MODEL:** EXPLICIT / FORWARD-ONLY / NON-RETROACTIVE

---

## CURRENT VERSION POSTURE

AUCTORISEAL currently exposes canonical published authority surfaces and recorded release boundaries.

Current declared posture:

- **Current published release version:** `v0.1.2`
- **State:** `NON-FINAL`
- **Authority posture:** `PUBLISHED`
- **Seal posture:** `GENESIS PRESENT`
- **Compatibility:** `NOT GUARANTEED`
- **Repository release boundary directory:** `.verifrax/tags/`

That means AUCTORISEAL has published release declarations, but repository publication alone must not be confused with protocol finality, downstream activation, or irreversible seal legitimacy.

---

## VERSION PRINCIPLES

AUCTORISEAL versioning is governed by the following rules:

- versions must be explicit
- versions are forward-only
- published release declarations are immutable once recorded
- prior release boundaries remain historical record
- repository visibility alone does not redefine the last recorded release boundary
- no consumer may infer a new version from repository drift alone

If a repository state is newer than the last recorded boundary, that newer state is not a new declared release until an explicit new release boundary is published.

---

## RELEASE BOUNDARY RELATION

Canonical release declarations are recorded under:

- `.verifrax/tags/`

Those files define the published release boundary states of AUCTORISEAL.

They are release declarations, not implicit claims that every later repository commit is a new published version.

A repository commit may exist after the latest recorded release boundary.
That does not automatically create a new version.

---

## CURRENT ASSERTION

At the currently published posture:

- AUCTORISEAL has explicit published release boundaries
- the latest recorded published release boundary is `v0.1.2`
- AUCTORISEAL remains **NON-FINAL**
- compatibility is **NOT GUARANTEED**
- downstream systems must consume explicit release and authority surfaces rather than infer version truth from repository visibility alone

---

## VERSION CHANGE RULE

AUCTORISEAL version may change only when all of the following occur together:

1. an explicit new release boundary is recorded
2. the new version identifier is declared on canonical published surfaces
3. the change is committed and published through governed review
4. downstream consumers can inspect the new boundary explicitly

No silent version transition is valid.

---

## NON-CLAIMS

AUCTORISEAL versioning does not claim:

- downstream finality
- downstream seal activation
- automatic compatibility
- legal or regulatory certification
- implicit version transition by repository publication alone

---

## FINAL RULE

> **If a version is not explicitly declared on canonical published surfaces, it must not be treated as published.**

There are no implicit version transitions.

---

## DECLARATION

This file defines the canonical published version posture of AUCTORISEAL.

If this file is missing, altered, or ambiguous,  
**AUCTORISEAL MUST BE TREATED AS VERSION-AMBIGUOUS UNTIL LEGIBILITY IS RESTORED.**

# AUTHORITY

**SYSTEM:** AUCTORISEAL  
**AUTHORITY MODEL:** ROOTED / EXPLICIT / FAIL-CLOSED

---

## CURRENT AUTHORITY POSTURE

AUCTORISEAL is currently published as the canonical authority-layer repository of the VERIFRAX stack.

Current declared posture:

- **State:** `NON-FINAL`
- **Authority posture:** `PUBLISHED`
- **Seal posture:** `HISTORICAL GENESIS MATERIAL PRESENT / NON-CANONICAL FOR CURRENT SEAL BASIS`
- **Governance posture:** `EXPLICIT`
- **Compatibility:** `NOT GUARANTEED`
- **Repository release boundary:** `.verifrax/tags/`

That means AUCTORISEAL publishes canonical authority objects, authority digests, schemas, revocation surfaces, and governance rules that downstream systems may defer to, but historical genesis material must not be confused with the current canonical authority basis.

---

## AUTHORITY SOURCE

AUCTORISEAL is the root authority-definition component of the VERIFRAX stack.

Within its own system boundary, authority is grounded in explicit published surfaces, including:

- `authority/roots.yaml`
- `public/authority/AUTHORITY-0001.json`
- `public/authority/AUTHORITY-0001.digest.txt`
- `public/authority/AUTHORITY-0001.verify.txt`
- `authorities/current/authority-object-0001.json`
- `authority-ledger.json` (historical material)
- `public/genesis/SEAL-0001.json` (historical material)
- `protocol/authority.schema.json`
- `protocol/seal.schema.json`
- `protocol/revocation.schema.json`

If authority is not represented through those canonical published surfaces, it must not be treated as valid.

Current authority-object entry surface:

- `authorities/current/authority-object-0001.json`

Historical authority-object entry surfaces must live only under `authorities/history/`.

---

## WHAT AUCTORISEAL MAY AUTHORITATIVELY DEFINE

AUCTORISEAL may authoritatively define, publish, and evolve:

- authority roots
- seal issuance semantics
- seal revocation semantics
- delegation semantics
- freeze semantics
- authority object schemas
- authority ledger structure
- canonical authority publication surfaces

It does not authoritatively determine truth of evidence bundles.
It does not authoritatively determine downstream business logic.
It does not authoritatively convert publication alone into downstream execution legitimacy.

---

## ROOT AUTHORITY BOUNDARY

Authority roots must be explicit.

There is no implicit root authority.

Any claim of authority must resolve to published root material and valid ledger-visible or seal-visible authority state.

If an authority chain cannot be traced to explicit canonical roots under published rules, it must be treated as invalid.

---

## SEAL AUTHORITY BOUNDARY

Seals are valid only when they are:

- issued under explicit root or delegated authority
- structurally valid under canonical schemas
- compatible with ledger and revocation state
- within scope and constraint rules
- not superseded by freeze or revocation conditions

AUCTORISEAL may publish seal-validity doctrine.
Downstream consumers must still validate that doctrine against published artifacts.

---

## REVOCATION AND FREEZE AUTHORITY

AUCTORISEAL may define and publish:

- who may revoke prior authority
- how revocation becomes effective
- how freeze blocks further authority evolution
- what downstream consumers must treat as authority-invalidating conditions

Revocation and freeze are authority surfaces, not optional annotations.

If revocation or freeze state is ambiguous, consumers should fail closed.

---

## DOWNSTREAM AUTHORITY RELATION

AUCTORISEAL may be deferred to by downstream systems such as:

- **VERIFRAX** for authority conditions in verification
- **CORPIFORM** for authority-gated execution
- integrations that consume canonical authority artifacts

But no downstream system inherits authority merely by naming AUCTORISEAL.

Downstream legitimacy still requires:

- correct artifact consumption
- correct validation behavior
- correct enforcement of revocation and freeze semantics

---

## NON-CLAIMS

AUCTORISEAL does not claim:

- truth authorship
- legal supremacy
- automatic downstream activation
- automatic downstream finality
- implicit legitimacy by repository visibility alone

It defines authority only within systems that explicitly defer to its published canonical surfaces.

---

## FAILURE CONSEQUENCE

If authority publication becomes illegible, inconsistent, or materially drifted across canonical surfaces:

- consumers should fail closed
- seals should not be assumed valid
- downstream systems should refuse authority-dependent actions
- repository publication must not be treated as a substitute for valid authority state

---

## FINAL RULE

> **If authority is not explicit on canonical published surfaces, it does not exist.**

There are no implicit authority exceptions.

---

## DECLARATION

This file defines the canonical published authority posture of AUCTORISEAL.

If this file is missing, altered, or ambiguous,  
**AUCTORISEAL MUST BE TREATED AS A DEGRADED AUTHORITY SURFACE UNTIL LEGIBILITY IS RESTORED.**

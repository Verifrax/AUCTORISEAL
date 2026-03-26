# STATUS

**SYSTEM:** AUCTORISEAL  
**CLASS:** AUTHORITY SEALING COMPONENT  
**CURRENT STATE:** NON-FINAL / ACTIVE AUTHORITY SURFACE

---

## CURRENT POSTURE

AUCTORISEAL is currently published as the canonical authority-layer repository of the VERIFRAX stack.

Current declared posture:

- **State:** `NON-FINAL`
- **Authority posture:** `PUBLISHED`
- **Seal posture:** `HISTORICAL GENESIS MATERIAL PRESENT / NON-CANONICAL FOR CURRENT SEAL BASIS`
- **Governance posture:** `EXPLICIT`
- **Compatibility:** `NOT GUARANTEED`
- **Repository release boundary:** `.verifrax/tags/`

That means AUCTORISEAL publicly exposes canonical authority-object surfaces, schemas, revocation semantics, and governance doctrine, while genesis seal material and ledger material remain historical and must not be treated as the current canonical seal basis.

---

## STATE DEFINITIONS

- **ACTIVE AUTHORITY SURFACE**  
  Canonical authority artifacts are published and inspectable.  
  Authority state may be consumed by downstream systems.

- **FROZEN**  
  New authority issuance is blocked except where freeze doctrine explicitly allows narrower actions such as revocation.

- **DEGRADED**  
  Integrity, legibility, or publication consistency is impaired.  
  Consumers should fail closed.

- **DEAD**  
  The repository is no longer a valid live authority surface for new legitimacy.

---

## CURRENT ASSERTION

This published instance of **AUCTORISEAL** is an **ACTIVE AUTHORITY SURFACE** in a **NON-FINAL** posture.

Therefore:

- authority surfaces may be inspected and consumed
- governance remains explicit and public
- revocation and freeze semantics remain authoritative within the system boundary
- publication alone does not imply that downstream components are sealed or final
- downstream activation still depends on valid authority material and correct consumer enforcement

---

## CANONICAL AUTHORITY SURFACES

The minimum canonical authority surfaces include:

- `public/authority/AUTHORITY-0001.json`
- `public/authority/AUTHORITY-0001.digest.txt`
- `public/authority/AUTHORITY-0001.verify.txt`
- `authority/roots.yaml`
- `protocol/authority.schema.json`
- `protocol/seal.schema.json`
- `protocol/revocation.schema.json`
- `GOVERNANCE.md`
- `SECURITY.md`
- `DISCLAIMER.md`
- `evidence/README.md`
- `authority-ledger.json` (historical material)
- `public/genesis/SEAL-0001.json` (historical material)

If these surfaces drift materially from one another, consumers should treat the authority surface as degraded.

---

## DOWNSTREAM RELATION

AUCTORISEAL does not determine truth.

AUCTORISEAL determines and publishes authority state that downstream systems may defer to.

That means:

- **VERIFRAX** may verify bundles using AUCTORISEAL authority conditions
- **CORPIFORM** may gate execution using AUCTORISEAL-issued authority
- integrations may consume authority artifacts without gaining authority of their own

No downstream repository may silently substitute itself for AUCTORISEAL authority state.

---

## FAILURE CONSEQUENCE

If integrity, publication consistency, or authority legibility fails:

- consumers should fail closed
- downstream execution systems should refuse if required authority cannot be validated
- repository publication must not be treated as a substitute for valid authority material

---

## DECLARATION

This file defines the canonical published status posture of AUCTORISEAL.

If this file is missing, altered, or ambiguous,  
**AUCTORISEAL MUST BE TREATED AS A DEGRADED AUTHORITY SURFACE UNTIL LEGIBILITY IS RESTORED.**

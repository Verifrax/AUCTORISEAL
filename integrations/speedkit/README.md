# AUCTORISEAL → SPEEDKIT Integration

This module defines how **SPEEDKIT** derives **registry legitimacy** from **AUCTORISEAL**.

SPEEDKIT is a **truth registry**.  
It does not decide authority.  
It reflects authority that already exists.

---

## Purpose

The purpose of this integration is to ensure:

> **No system is considered legitimate unless backed by an explicit authority seal.**

AUCTORISEAL defines authority.  
SPEEDKIT records truth.

---

## Contract

SPEEDKIT MUST:

1. Accept registry entries only when:
   - a referenced authority seal exists
   - the seal is active (not revoked)
2. Reflect authority status faithfully:
   - active seal → active registry entry
   - revoked seal → revoked registry entry
3. Treat AUCTORISEAL as the **single source of legitimacy**

SPEEDKIT MUST NOT:
- infer authority
- cache legitimacy beyond seal validity
- override revocation

---

## Registry Sync

The `registry_sync.py` adapter:

- verifies seal existence via the ledger
- detects revocation deterministically
- returns registry status derived from authority
- never mutates authority state

All registry entries sourced from AUCTORISEAL MUST record:
- `authority_seal_id`
- `source = auctoriseal`

---

## Failure Semantics

If authority cannot be verified:

- the registry entry MUST NOT be activated
- the system is treated as untrusted
- no fallback legitimacy is allowed

Failing open is forbidden.

---

## Invariant

> **Truth without authority is noise.  
> Authority without truth is inert.**

This integration binds the two.

---

## Final Note

This adapter is intentionally minimal.

Any complexity added here risks corrupting the authority boundary.

If authority is unclear, SPEEDKIT must remain silent.

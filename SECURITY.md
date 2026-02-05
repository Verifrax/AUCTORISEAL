# SECURITY

AUCTORISEAL is an **authority and legitimacy system**.  
Security here is about **integrity, finality, and non-repudiation**, not convenience.

This document defines how security is handled, what is in scope, and how issues are disclosed.

---

## Security Model (Summary)

AUCTORISEAL assumes:

- Attackers may read public data.
- Attackers may attempt to forge authority.
- Attackers may attempt to corrupt history.
- Attackers may attempt to bypass revocation.
- Operators may make mistakes.

AUCTORISEAL is designed so that **authority cannot be forged silently** and **history cannot be altered without detection**.

---

## In Scope

The following are **security-critical** and in scope:

- Authority Seal issuance
- Authority Seal validation
- Authority Seal revocation
- Ledger append integrity
- Ledger replay determinism
- Protocol schema correctness
- Scope and constraint enforcement
- Delegation chain validation
- Freeze and emergency revocation semantics
- Public API correctness (read-only guarantees)

---

## Out of Scope

The following are **explicitly out of scope**:

- AI model behavior
- Downstream system bugs
- Business logic of products using AUCTORISEAL
- Regulatory compliance guarantees
- User interface vulnerabilities in third-party integrations
- Availability guarantees beyond stated deployment posture

AUCTORISEAL does not guarantee safety, correctness, or compliance of systems that defer to it.

---

## Threat Model

### Considered Threats

- Forged authority seals
- Silent modification of historical records
- Replay attacks with altered context
- Scope escalation via malformed constraints
- Unauthorized delegation
- Partial ledger corruption
- Operator error during issuance or revocation

### Explicit Non-Goals

- Preventing all misuse of granted authority
- Detecting malicious intent by authorized actors
- Preventing misuse outside defined scope by downstream systems

---

## Integrity Guarantees

AUCTORISEAL provides:

- **Append-only ledger**: no update or delete operations
- **Deterministic verification**: identical inputs yield identical validation results
- **Cryptographic fingerprints** (where enabled) for seals and ledger entries
- **Explicit revocation events** that override prior grants
- **Freeze events** that halt authority evolution

If integrity verification fails, the system must enter a **degraded read-only mode**.

---

## Disclosure Policy

If you discover a security vulnerability:

1. **Do not** open a public issue.
2. **Do not** exploit the vulnerability beyond proof of existence.
3. Contact the maintainer privately.

### Preferred Contact
- Email: `security@auctoriseal.org` (if configured)
- Otherwise: direct maintainer contact as listed in `GOVERNANCE.md`

Provide:
- clear description
- reproduction steps
- affected components
- potential impact

---

## Response Expectations

- Acknowledgement within **72 hours**
- Assessment and severity classification
- Fix or mitigation plan for critical issues
- Public disclosure only after mitigation (if appropriate)

There is **no bug bounty program** unless explicitly stated elsewhere.

---

## Responsible Disclosure Statement

AUCTORISEAL prioritizes **integrity over speed**.  
Some fixes may require protocol changes and version bumps.

Security reports that demand secrecy beyond reasonable mitigation windows will not be accepted.

---

## Final Note

Security in AUCTORISEAL is inseparable from authority.

If a security issue allows:
- forged authority
- silent history alteration
- undetectable revocation bypass

it is considered **critical**.

Everything else is secondary.

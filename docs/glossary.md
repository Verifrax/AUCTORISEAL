# GLOSSARY

This glossary defines **normative terms** used by AUCTORISEAL.  
If a term is used elsewhere with a conflicting meaning, **this glossary prevails**.

---

## Authority
The explicit permission granted to an entity to authorize specific actions within a defined scope and constraints.

Authority does not imply execution.  
Authority does not imply correctness.

---

## Authority Seal
A recorded assertion that grants authority.

An Authority Seal specifies:
- issuer
- subject (issued to)
- scope
- constraints
- issuance time
- status

If a seal does not exist, authority does not exist.

---

## Issuer
The authority entity that issues a seal.

An issuer must itself possess valid authority to issue the seal.

---

## Subject
The entity to which authority is granted.

A subject may be:
- an organization
- a system
- a service
- a delegated authority

---

## Scope
The precise set of actions that the authority permits.

Examples:
- `adjutorix:apply`
- `adjutorix:deploy`
- `registry:register`

Anything outside scope is unauthorized.

---

## Constraints
Additional conditions attached to a scope.

Examples:
- environment limitations
- mode restrictions
- time bounds
- file or path restrictions

Constraints narrow authority; they never expand it.

---

## Delegation
The act of granting a subset of one’s authority to another entity.

Delegation:
- must be explicit
- must be recorded
- must be bounded
- is revocable

---

## Delegation Chain
The ordered sequence of authority grants leading back to a root authority.

Delegation chains must be finite and verifiable.

---

## Root Authority
An authority defined as an origin point for delegation.

Root authorities are explicitly declared and versioned.

There is no implicit root.

---

## Revocation
A recorded event that invalidates an existing authority seal.

Revocation:
- is explicit
- is immediate
- overrides all prior grants

---

## Freeze
An emergency governance action that halts the issuance of new authority.

During a freeze:
- issuance is forbidden
- delegation is forbidden
- revocation remains allowed

---

## Ledger
An append-only record of all authority-related events.

The ledger is the source of truth.

---

## Append-Only
A property of the ledger where records may be added but never modified or deleted.

Corrections occur only through new records.

---

## Finality
The guarantee that once recorded, authority events cannot be erased or rewritten.

Finality is required for legitimacy.

---

## Validation
The deterministic process of evaluating whether a seal is valid given the current ledger state and protocol version.

---

## Determinism
The property that identical inputs always yield identical validation results.

Human interpretation does not override determinism.

---

## Legitimacy
The state of being authorized according to recorded authority.

Legitimacy is ecosystem-scoped and voluntary.

---

## Ecosystem
The set of systems that explicitly defer to AUCTORISEAL for authority validation.

---

## Protocol
The versioned set of schemas and rules governing how authority is represented and validated.

Protocol definitions override implementation behavior.

---

## Operator
The human or legal entity responsible for running an AUCTORISEAL instance.

Operators do not gain authority by default.

---

## Non-Repudiation
The inability to deny having issued, delegated, or revoked authority once it is recorded.

---

## Unauthorized Action
Any action that occurs without a valid authority seal covering its scope and constraints.

---

## Final Definition

> **Authority exists only where it is explicitly sealed, recorded, and valid.**

All other claims are narrative.

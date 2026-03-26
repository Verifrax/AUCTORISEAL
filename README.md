# AUCTORISEAL

![CI](https://img.shields.io/github/actions/workflow/status/Verifrax/AUCTORISEAL/auctoriseal-ci.yml?branch=main\&label=CI)
![Determinism](https://img.shields.io/github/actions/workflow/status/Verifrax/AUCTORISEAL/determinism-check.yml?branch=main\&label=determinism)
![Identity](https://img.shields.io/github/actions/workflow/status/Verifrax/AUCTORISEAL/identity.yml?branch=main\&label=identity)
![License](https://img.shields.io/badge/license-Apache--2.0-blue)
![npm](https://img.shields.io/npm/v/@verifrax/auctoriseal)
![npm downloads](https://img.shields.io/npm/dm/@verifrax/auctoriseal)
![Node](https://img.shields.io/badge/node-%3E%3D20-brightgreen)
![Protocol](https://img.shields.io/badge/protocol-Verifrax-black)

Authority sealing primitive for the **VERIFRAX protocol stack**.

AUCTORISEAL publishes canonical authority objects, authority digests, and governance-visible authority artifacts used by verifiers to establish protocol-level authority boundaries.

This repository defines the **authority layer** of the VERIFRAX ecosystem.

---

# Overview

AUCTORISEAL exists to make **authority explicit, inspectable, and reproducible**.

Instead of implicit repository trust or opaque governance decisions, authority is represented through **public artifacts** such as:

* canonical authority object
* authority digest and verification procedure
* authority schemas
* historical genesis seal material
* historical ledger material
* governance documentation

These artifacts are published so that downstream systems — including **VERIFRAX verifiers** — can determine whether authority conditions are satisfied.

**AUCTORISEAL does not assert truth — it publishes the canonical authority surfaces that VERIFRAX verifiers use to determine whether protocol authority conditions are satisfied.**

---

# Position in the VERIFRAX stack

The Verifrax architecture separates responsibility across layers:

| Layer            | Responsibility                                  |
| ---------------- | ----------------------------------------------- |
| **AUCTORISEAL**  | Defines and publishes authority state           |
| **VERIFRAX**     | Verifies evidence bundles and protocol outcomes |
| **Integrations** | Consume verified authority state                |

AUCTORISEAL does **not determine truth**.

It defines the **authority surfaces required for truth verification**.

---

# Core authority artifacts

The repository exposes several canonical authority artifacts.

## Historical ledger material

```
authority-ledger.json
```

Retained as historical inspectable material. It is not the current canonical authority surface for artifact-0005.

## Canonical authority object

```
public/authority/AUTHORITY-0001.json
```

Defines the published governed repository authority object used as the canonical public authority surface.

## Authority digest

```
public/authority/AUTHORITY-0001.digest.txt
public/authority/AUTHORITY-0001.verify.txt
```

Publishes the reproducible digest and exact verification procedure for the canonical authority object.

## Historical genesis seal material

```
public/genesis/SEAL-0001.json
```

Retained as historical inspectable material. It is not the current canonical authority basis for artifact-0005.

## Authority schemas

```
protocol/authority.schema.json
protocol/seal.schema.json
```

Formal schema definitions for authority objects and seals.

## Governance documentation

```
GOVERNANCE.md
DISCLAIMER.md
SECURITY.md
```

Documents governance structure, operational assumptions, and disclosure policies.

---

# npm package

The npm package mirrors the public repository boundary so that authority artifacts can be consumed as a dependency.

Install:

```
npm install @verifrax/auctoriseal
```

This package includes:

* authority ledger
* genesis seal
* protocol schemas
* CLI utilities
* governance documents
* integration adapters
* verifier evidence samples

The npm package is **not a runtime authority server**.

It is a **distribution surface for authority artifacts**.

---

# Repository structure

```
.verifrax/
api/
authority/
cli/
docs/
evidence/
integrations/
ledger/
ops/
protocol/
public/genesis/
runtime/
seals/
tests/
```

Additional root materials:

```
README.md
LICENSE
SECURITY.md
GOVERNANCE.md
CONTRIBUTING.md
DISCLAIMER.md
CITATION.cff
```

---

# Example usage

Inspect the historical ledger material:

```
cat authority-ledger.json
```

Inspect the canonical authority object:

```
cat public/authority/AUTHORITY-0001.json
cat public/authority/AUTHORITY-0001.digest.txt
cat public/authority/AUTHORITY-0001.verify.txt
```

Inspect the historical genesis seal material:

```
cat public/genesis/SEAL-0001.json
```

Review authority schemas:

```
cat protocol/authority.schema.json
cat protocol/seal.schema.json
```

Run repository checks:

```
npm test
npm run build
npm run pack:check
```

---

# Authority visibility principle

AUCTORISEAL follows a strict rule:

> Authority must be observable through published artifacts.

Consumers should never rely on:

* hidden governance
* undocumented authority changes
* implicit repository trust

Authority state must be verifiable through:

* ledger presence
* seal presence
* schema compatibility
* repository publication surfaces

---

# Security model

Security is based on **public inspectability**.

Consumers should verify:

* authority ledger presence
* genesis seal integrity
* schema compatibility
* release boundary consistency

Sensitive vulnerabilities should not be disclosed publicly.

Security contact:

```
security@verifrax.net
```

---

# Development

Clone the repository:

```
git clone https://github.com/Verifrax/AUCTORISEAL.git
cd AUCTORISEAL
```

Run checks:

```
npm test
npm run build
npm run pack:check
```

---

# Governance

See:

```
GOVERNANCE.md
```

---

# Contributing

See:

```
CONTRIBUTING.md
```

---

# Disclaimer

See:

```
DISCLAIMER.md
```

---

# License

Licensed under the **Apache License 2.0**.

See `LICENSE` for the full license text.

---

# Repository

[https://github.com/Verifrax/AUCTORISEAL](https://github.com/Verifrax/AUCTORISEAL)

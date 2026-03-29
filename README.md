# AUCTORISEAL

![License](https://img.shields.io/badge/license-Apache--2.0-blue)
![Role](https://img.shields.io/badge/role-authority%20surface-111111)
![npm](https://img.shields.io/npm/v/@verifrax/auctoriseal)
![CI](https://github.com/Verifrax/AUCTORISEAL/actions/workflows/auctoriseal-ci.yml/badge.svg?branch=main)
![Identity](https://github.com/Verifrax/AUCTORISEAL/actions/workflows/identity.yml/badge.svg?branch=main)
![Determinism](https://github.com/Verifrax/AUCTORISEAL/actions/workflows/determinism-check.yml/badge.svg?branch=main)
![Deploy](https://github.com/Verifrax/AUCTORISEAL/actions/workflows/pages-deploy.yml/badge.svg?branch=main)
![Host](https://img.shields.io/badge/host-auctoriseal.verifrax.net-1f6feb)

Authority issuance and authority reference surface for the governed Verifrax system.

## Status

* Layer: Authority
* Repository class: governed authority surface
* Public host ownership: `auctoriseal.verifrax.net`
* npm package: `@verifrax/auctoriseal`
* Package surface: authority issuance implementation surface
* License: Apache License Version 2.0

## One-sentence role

AUCTORISEAL records, publishes, and verifies the authority objects that define who may authorize governed Verifrax execution before CORPIFORM runs and before VERIFRAX or public verifier surfaces evaluate the resulting evidence.

## What this repository is

This repository is the authority layer of the Verifrax stack.

It exists to provide:

* authority object issuance
* authority object publication
* authority digest publication
* authority verification material
* authority/governance linkage
* revocation and freeze reference material where declared
* public authority artifacts that downstream systems can inspect without hidden trust

This repository is the place where authority becomes explicit.

## What this repository is not

This repository is not:

* the authored protocol repository
* the derived specification publication surface
* the governed execution runtime
* the public proof publication surface
* the public verifier UI
* the intake surface
* the commercial landing surface
* the evidence root for artifact registration
* a generic trust claim by prose alone

AUCTORISEAL does not:

* execute governed runtime actions
* produce CORPIFORM receipts
* verify final truth claims by itself
* replace VERIFRAX evidence judgment
* publish marketing copy as authority

Authority here means authorization boundary, not truth verdict.

## Authority model

AUCTORISEAL defines who may authorize governed actions and under what scope.

Its outputs are meant to be machine-checkable.

The required authority direction across the governed system is:

* VERIFRAX authors normative source material.
* VERIFRAX-SPEC publishes derived specification artifacts from VERIFRAX.
* Derived artifacts are not upstream authority.
* Governance authority is external and bound through AUCTORISEAL plus the governed repo set in `.github`.

AUCTORISEAL publishes authority artifacts used by:

* `.github` governance linkage surfaces
* CORPIFORM execution admission and receipt binding
* VERIFRAX evidence and chain interpretation
* VERIFRAX-verify and other verifier surfaces where authority references must be inspectable

## Stack position

Read the authority path in this order:

1. `.github` — governed repository boundary and governance linkage
2. `AUCTORISEAL` — authority issuance and authority publication
3. `CORPIFORM` — governed execution under recorded authority
4. `VERIFRAX` — evidence root, verification boundary, and artifact chain
5. `VERIFRAX-verify` — public verification surface

AUCTORISEAL sits above execution and below evidence interpretation.

## Public host ownership

This repository owns the authority reference surface for:

* `https://auctoriseal.verifrax.net/`

That surface must remain authority-only.

It must not become:

* API execution
* proof publication
* verifier UI
* intake flow
* commercial landing
* generic docs mirror

## Public artifact surface

Authority artifacts published from this repository must be sufficient for an outsider to:

* fetch the current authority object
* inspect the governed boundary it declares
* recompute the published authority digest
* compare the published digest with the raw authority object
* inspect the authority version/schema reference

At minimum, the repository must keep authority publication material aligned across:

* repository paths under the public authority surface
* `.github/governance/AUTHORITY_CURRENT.txt`
* `.github/governance/AUTHORITY_DIGEST.txt`
* `.github/governance/AUTHORITY_VERSION.txt`
* any VERIFRAX evidence entry that binds execution to authority

## Artifact-0005 alignment

AUCTORISEAL is load-bearing for artifact-0005.

For artifact-0005 to remain truthful, this repository must provide a public canonical authority object and reproducible authority digest that can be bound to:

* `.github` governed repository manifests
* the exact governed execution run by CORPIFORM
* the recorded receipt referenced by VERIFRAX evidence
* matching verifier interpretation across maintained verification surfaces

AUCTORISEAL must not describe artifact-0005 as sealed, complete, or broader than the VERIFRAX evidence root proves.

AUCTORISEAL must make the authority part of artifact-0005 inspectable.

## Inputs and outputs

### Inputs

This repository consumes:

* governance boundary truth from `.github`
* declared authority scope and issuer inputs
* schema and implementation constraints required for authority publication

### Outputs

This repository produces:

* authority objects
* authority digests
* authority verification instructions
* revocation/freeze/reference material where declared
* public authority reference artifacts

It does not produce:

* governed execution receipts
* verifier verdicts
* proof certificates
* evidence-chain registration entries

## Verifier relationship

Verifier surfaces must be able to inspect authority without trusting a maintainer statement.

That means AUCTORISEAL must remain legible to both:

* `VERIFRAX` as the evidence and verification boundary
* `VERIFRAX-verify` as the public verification surface

If a verifier cannot discover which authority object governed an execution boundary, the authority layer is incomplete.

## Repository reading rule

Read this repository for authority scope and authority publication.

Read these neighboring repositories for the rest of the path:

* [`.github`](https://github.com/Verifrax/.github) — governance root
* [`CORPIFORM`](https://github.com/Verifrax/CORPIFORM) — governed execution and receipts
* [`VERIFRAX`](https://github.com/Verifrax/VERIFRAX) — evidence root and artifact chain
* [`VERIFRAX-verify`](https://github.com/Verifrax/VERIFRAX-verify) — public verification surface
* [`VERIFRAX-SPEC`](https://github.com/Verifrax/VERIFRAX-SPEC) — derived specification publication
* [`VERIFRAX-DOCS`](https://github.com/Verifrax/VERIFRAX-DOCS) — documentation/reference surface

## CI and integrity expectations

Any CI described here must be real and load-bearing.

At minimum, the repository should enforce real checks for:

* identity alignment
* package/version alignment where a package exists
* authority-example digest reproducibility
* published authority-path integrity
* documentation/path consistency for authority artifacts

This README must not use badge theater to imply checks that do not actually verify authority properties.


## Verifrax system path labels

The governed Verifrax path that this README must stay compatible with is:

1. `.github` — organization governance and governed repository boundary
2. `AUCTORISEAL` — authority issuance and public authority reference
3. `CORPIFORM` — governed execution and receipt emission
4. `VERIFRAX` — authored protocol, evidence root, and artifact-chain registration boundary
5. `VERIFRAX-SPEC` — derived specification publication surface
6. `VERIFRAX-PROFILES` — deterministic profile-constraint surface
7. `VERIFRAX-SAMPLES` — pinned sample and reproducibility surface
8. `VERIFRAX-verify` — public verification repository and UI boundary
9. `VERIFRAX-DOCS` — explanatory documentation surface
10. `cicullis` — enforcement boundary
11. `proof` — proof publication surface
12. `SIGILLARIUM` — seal and archive reference surface
13. `apply` — intake surface

The live host-label map that must remain explicit and non-contradictory is:

* `https://api.verifrax.net/` — execution surface
* `https://proof.verifrax.net/` — proof publication surface
* `https://auctoriseal.verifrax.net/` — authority issuance and authority reference surface
* `https://corpiform.verifrax.net/` — runtime and receipt reference surface
* `https://cicullis.verifrax.net/` — enforcement reference surface
* `https://verify.verifrax.net/` — public verification surface
* `https://sigillarium.verifrax.net/` — seal and archive reference surface
* `https://apply.verifrax.net/` — intake surface
* `https://docs.verifrax.net/` — documentation surface

This README must remain compatible with `artifact-0005` as the load-bearing authority → execution → verification → evidence boundary without claiming that this repository alone authors, proves, seals, or registers `artifact-0005` unless that role is actually true for this repository.


## Security

Do not disclose private keys, signing material, revocation secrets, unpublished emergency procedures, or hidden authority inputs in public issues.

Authority compromise is not a documentation bug. It is a system event and must be handled through the declared security and governance process.

## Contributing

Changes to this repository change how execution legitimacy is established.

A contribution is wrong if it:

* blurs authority with truth judgment
* makes authority depend on prose alone
* breaks digest reproducibility
* weakens governance linkage
* creates ambiguity between current and historical authority material
* introduces future-state claims as present truth

## License

Apache License Version 2.0. See `LICENSE`.

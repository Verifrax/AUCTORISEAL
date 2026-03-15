# AUCTORISEAL Evidence Index

This directory is the public evidence surface for AUCTORISEAL.

It exists so that any reviewer, claimant, challenger, auditor, or adversarial reader can inspect what authority state was claimed, what publication surfaces were observed, what issuance evidence exists, what was re-executed, and what boundary the current evidence actually proves.

This index is not a substitute for the evidence objects themselves. It is the canonical navigation surface for those objects.

---

## Current boundary

The evidence currently published here establishes a bounded public authority surface for AUCTORISEAL.

Currently indexed from this root:

1. authority readiness evidence
2. issued authority subject evidence
3. re-execution evidence after authority publication became present

That means this evidence tree currently proves a narrower boundary than VERIFRAX.

It is focused on AUCTORISEAL authority publication and issuance visibility, not on the full VERIFRAX bootstrap chain.

---

## How to read this evidence

Read this tree in the following order.

### 1. Authority readiness

Start here if you want to inspect whether AUCTORISEAL had real published authority artifacts rather than only implementation surfaces.

- `artifact-0002/`

Primary file:

- `artifact-0002/artifact-0002.json`

This artifact is the readiness boundary for authority publication.

It is the place to inspect:

- whether a canonical authority ledger was present
- whether a genesis seal was present
- whether public authority objects existed as inspectable artifacts
- whether the evidence distinguished real publication from code-only surfaces

Supporting examples:

- `artifact-0002/authority-surface-files.txt`
- `artifact-0002/ledger-presence.txt`
- `artifact-0002/seal-presence.txt`
- `artifact-0002/issued-object-search.txt`
- `artifact-0002/live-reference-search.txt`
- `artifact-0002/ledger-tree.txt`
- `artifact-0002/seals-tree.txt`

### 2. Issued subject evidence

Read this next if you want the direct evidence for the published issuance subject.

- `artifact-0003/`

Primary file:

- `artifact-0003/artifact-0003.json`

This artifact is the direct publication-and-subject boundary.

It is the place to inspect:

- whether the authority ledger was present
- whether the genesis seal was present
- whether the claimed issued subject existed as a public inspectable object

Supporting examples:

- `artifact-0003/authority-ledger-presence.txt`
- `artifact-0003/seal-0001-presence.txt`
- `artifact-0003/issued-object-search.txt`
- `artifact-0003/EXECUTION_STATUS.txt`

### 3. Re-execution evidence

Read this if you want to inspect whether the published subject was re-executed after authority publication was in place.

- `artifact-0003-reexecution/`

This surface matters because it preserves the difference between:

- an authority claim that merely exists on paper
- an authority subject that became executable after public publication

Key files:

- `artifact-0003-reexecution/EXECUTION_STATUS.txt`
- `artifact-0003-reexecution/authority-ledger-presence.txt`
- `artifact-0003-reexecution/seal-0001-presence.txt`
- `artifact-0003-reexecution/issued-object-search.txt`
- `artifact-0003-reexecution/object-hashes.txt`

---

## Evidence map

### `artifact-0002/`

Purpose:

- authority readiness evidence for AUCTORISEAL publication surfaces

Use this when checking:

- whether authority publication was real
- whether canonical authority artifacts existed
- whether readiness was based on public objects rather than implementation code alone

Primary file:

- `artifact-0002/artifact-0002.json`

### `artifact-0003/`

Purpose:

- issued authority subject evidence

Use this when checking:

- whether the authority ledger was present
- whether the genesis seal was present
- whether the issuance subject existed in public inspectable form

Primary file:

- `artifact-0003/artifact-0003.json`

### `artifact-0003-reexecution/`

Purpose:

- re-execution evidence after the authority subject became publicly present

Use this when checking:

- whether the subject moved from absent to present
- whether re-execution evidence was recorded after publication
- whether the post-publication boundary is materially stronger than the earlier state

Primary file for quick entry:

- `artifact-0003-reexecution/EXECUTION_STATUS.txt`

---

## Adversarial reading rule

This evidence surface must be readable by a hostile reader, not only a friendly one.

That means this tree must allow an external reader to answer all of the following without guessing:

- what was claimed
- what exact object was being discussed
- what supporting files were collected
- whether the subject was present or absent
- what changed between readiness and issuance
- what boundary is proven now
- what boundary is not claimed here

If a reader cannot answer those questions from this root plus the referenced files, the evidence surface is incomplete.

This index exists to reduce that ambiguity.

---

## Entry points

If you are entering this tree for the first time, start here:

- authority readiness object: `artifact-0002/artifact-0002.json`
- issued subject object: `artifact-0003/artifact-0003.json`
- re-execution summary: `artifact-0003-reexecution/EXECUTION_STATUS.txt`

---

## Scope boundary

This index covers the evidence currently published under `AUCTORISEAL/evidence`.

It does not claim that every possible future authority artifact already exists.
It claims that the evidence that does exist is now navigable from a single public root.

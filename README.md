`markdown
# AUCTORISEAL

**AUCTORISEAL is the authority and legitimacy layer of the ADJUTORIX ecosystem.**  
It issues, records, and revokes **Authority Seals** that define **who is allowed to authorize irreversible actions** (e.g., apply, deploy, freeze) under explicit scope and constraints.

AUCTORISEAL is intentionally **boring**, **strict**, and **auditable**.

---

## What AUCTORISEAL Is

AUCTORISEAL provides:

- **Authority Seals**: explicit, prior grants of permission with scope + constraints.
- **Append-only ledger**: every seal issuance and revocation is recorded.
- **Deterministic validation**: given the same ledger state, validation yields the same result.
- **Revocation**: authority can be revoked immediately and verifiably.
- **Integration contracts**: systems (SPEEDKIT, ADJUTORIX, products) defer to AUCTORISEAL for legitimacy.

---

## What AUCTORISEAL Is Not

AUCTORISEAL is **not**:

- a government, regulator, or standards body
- a compliance certification authority
- an AI system or autonomous agent
- a workflow engine for code execution
- a “safety” guarantee

It does not decide *what* should happen.  
It records and enforces **who is allowed to authorize** what happens.

---

## The Core Invariant

> If an action required authority, and the authority was not sealed, then the action was **unauthorized**.

---

## Ecosystem Map

- **AUCTORISEAL** — authority & legitimacy (seals, revocation, ledger)
- **SPEEDKIT** — registry of systems (truth surface)
- **ADJUTORIX** — governed execution engine (law / enforcement)
- **Products** — deployed systems (evidence of operation)
- **Primitives** — libraries/tools (implementation)

---

## Repository Layout

- `docs/` — constitution, glossary, threat model, trust model
- `protocol/` — versioned schemas and compatibility rules
- `ledger/` — append-only ledger schema, migrations, integrity verification
- `seals/` — seal lifecycle logic (issue/validate/revoke)
- `authority/` — roots, delegation, modes, freeze semantics
- `integrations/` — adapters for ADJUTORIX/SPEEDKIT and product references
- `api/` — read-only public interface (OpenAPI, server)
- `cli/` — operator tools (explicit issuance, revocation, inspections)
- `ops/` — audit checklist, incident response, backup/restore, decommission
- `tests/` — protocol compatibility + integrity tests (legitimacy requires tests)

---

## Quickstart (Local)

### 1) Prerequisites
- Python 3.11+
- SQLite 3
- (Optional) Docker

### 2) Install
bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
`

### 3) Initialize Ledger

bash
python -m auctoriseal.cli.inspect_ledger --init


### 4) Issue a Seal (Operator Action)

bash
python -m auctoriseal.cli.issue_seal \
  --issued-to "example-org" \
  --scope "adjutorix:apply" \
  --constraints "mode=managed" \
  --notes "Initial managed apply authority"


### 5) Validate a Seal

bash
python -m auctoriseal.cli.verify_integrity
python -m auctoriseal.cli.list_seals --active


### 6) Run Read-only API

bash
python -m auctoriseal.api.server --config runtime/config.example.yaml


---

## Public Contract

The public contract is defined in:

* `protocol/envelope.schema.json`
* `protocol/seal.schema.json`
* `protocol/authority.schema.json`
* `protocol/revocation.schema.json`
* `protocol/registry.schema.json`
* `protocol/error.schema.json`
* `protocol/protocol.md`

If code contradicts protocol, **protocol wins**.

---

## Operational Posture

* Ledger is **append-only**.
* Seals are **revocable**.
* Public API is **read-only**.
* Issuance and revocation are **explicit operator actions**.
* Integrations must treat AUCTORISEAL as a **hard dependency** for legitimacy.

---

## Legal / Non-Claims

See:

* `DISCLAIMER.md` (mandatory)
* `GOVERNANCE.md`
* `SECURITY.md`

---

## License

See `LICENSE`.


::contentReference[oaicite:0]{index=0}


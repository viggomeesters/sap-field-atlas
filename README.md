# SAP Field Atlas

Project id: `sap-field-atlas`  
Recommended public-facing name: **SAP Field Atlas** (`sap-field-atlas`).

SAP Field Atlas is a bare-bones, agent-ready knowledge base for SAP data migration consultants. It models the practical objects consultants use every day: SAP GUI transactions, Fiori apps, tables, fields, labels/aliases, relationships, value sources, and SAP Migration Cockpit template mappings.

## Problem

SAP data migration work constantly moves between ECC, S/4HANA, Fiori, SAP GUI, table exports, and Migration Cockpit templates. The same concept can appear as a table-field (`MARA-MATNR`), a business term (Material Number), a template field (Product Number), or language/context-specific labels. Consultants often keep this knowledge in personal notes; agents need it in structured contracts.

## Audience

- SAP data migration consultants
- Functional consultants who need quick table/field/transaction explanations
- AI agents that need a cloneable SAP data model context pack

## Agent-ready approach

The repository is intentionally data-first. YAML files under `data/` hold the knowledge. Python validation and tests make the contracts safe to consume. A cloned repo should be enough for an agent to answer questions such as:

- Explain `SE16N`.
- Explain `MARA-MATNR`.
- Which labels can refer to Material Number / Product Number?
- Which table/field does a Migration Cockpit template field map to?

## Public safety

This is **not official SAP documentation** and does not mirror proprietary SAP content. Use source references and confidence labels. Do not add client names, customer exports, screenshots, internal URLs, project-specific mappings, or data copied from customer systems.

## Current status

Skeleton initialized locally in WSL at `/home/viggo/github/sap-field-atlas`. Public repository: <https://github.com/viggomeesters/sap-field-atlas>. The local project id/package name remains `sap-field-atlas`; the public-facing repository name is `sap-field-atlas`.

## How to feed this repo to an agent

Clone or open the repo and give the agent this instruction:

```text
Use this repository as SAP Field Atlas context. For questions about transaction codes, tables, TABLE-FIELD ids, Fiori apps, Migration Cockpit labels, aliases, and SAP value sources, inspect data/*.yaml first. Use skills/explain-sap-object.md as the answer contract. Distinguish technical names from business/template labels and surface confidence/needs_verification instead of guessing.
```

Lookup pattern:

- transaction code → `data/transactions.yaml`
- `TABLE-FIELD` → `data/fields.yaml`
- table name → `data/tables.yaml`
- template label → `data/migration_templates.yaml` + field labels
- value source/customizing → `data/domains.yaml`
- graph context → `data/relationships.yaml`

Examples:

- `examples/explain-se16n.md`
- `examples/explain-mara-matnr.md`

## Commands

```bash
uv run sap-field-atlas validate
uv run sap-field-atlas audit-completeness
uv run pytest -q
```

## Layout

```text
data/           YAML knowledge contracts
schemas/        human-readable schema contracts
examples/       example agent answers
skills/         agent prompt/skill snippets
scripts/        helper scripts
src/            validator/CLI
tests/          regression tests
```

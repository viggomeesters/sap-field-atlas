# Architecture

SAP Field Atlas is intentionally small and data-first.

## Surfaces

- `data/*.yaml` — machine-readable knowledge contracts.
- `schemas/*.schema.yaml` — human-readable schema contracts.
- `src/sap_field_atlas/validation.py` — executable integrity checks across collections.
- `src/sap_field_atlas/cli.py` — small CLI wrapper for validation/audit commands.
- `skills/explain-sap-object.md` — agent answer contract.
- `examples/*.md` — example agent outputs.

## Runtime model

There is no server, database, secret store, or external runtime. A clone of the repository plus Python/uv is enough.

## Data model

The core collections are:

- transactions;
- Fiori apps;
- tables;
- fields;
- Migration Cockpit templates;
- domains/value sources;
- relationships.

Relationships form a lightweight graph across SAP objects. Confidence and source references are first-class because the repo starts from practical consultant knowledge and should gradually become more source-backed.

## Non-goals

- Not official SAP documentation.
- Not a customer-project knowledge base.
- Not the SAP FO Knowledge Base.
- Not a mirror of proprietary SAP help content.

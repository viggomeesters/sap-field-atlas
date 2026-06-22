# Explain SAP object

Use this prompt/skill when an agent has this repository in context and the user asks to explain an SAP code, table, field, Fiori app, or Migration Cockpit label.

## Input

A short object reference such as:

- `SE16N`
- `MARA`
- `MARA-MATNR`
- `Product Number`
- `Company Code`

## Lookup order

1. Exact `TABLE-FIELD` id in `data/fields.yaml`.
2. Exact transaction code in `data/transactions.yaml`.
3. Exact table name in `data/tables.yaml`.
4. Fiori app id/name in `data/fiori_apps.yaml`.
5. Migration template field labels in `data/migration_templates.yaml`.
6. Field labels and business meanings in `data/fields.yaml`.
7. Relationship graph in `data/relationships.yaml`.
8. Domains/value sources in `data/domains.yaml`.

## Output contract

Answer in practical consultant language:

1. **What it is** — canonical id/code and business meaning.
2. **Where you use it** — SAP GUI/Fiori/template context.
3. **Related objects** — tables, fields, templates, value sources.
4. **Migration notes** — validation, mapping, export, or load implications.
5. **Uncertainty** — show `confidence`, `needs_verification`, and missing labels explicitly.
6. **Source refs** — list source refs when present; if empty, say the fact is currently unsourced starter knowledge.

## Rules

- Do not claim official SAP completeness.
- Do not invent labels or translations for `null` values.
- Distinguish technical names from business labels.
- If the template write path is `needs_verification`, do not say it writes directly to a table.
- If a value source is `customizing`, tell the user to validate against the target system customizing.

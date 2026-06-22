# Atlas Fill Loop

The Atlas Fill Loop is the repeatable workflow for growing SAP Field Atlas from sparse seed knowledge into a source-aware, validated knowledge graph.

It is designed for agents and maintainers. The loop starts with a **gap**, adds the smallest useful SAP object slice, validates it, reviews confidence/source quality, and then selects the next gap.

## Loop shape

```text
GAP → SCOPE → COLLECT → MODEL → LINK → VALIDATE → EXPLAIN → REVIEW → SHIP → NEXT GAP
```

## 0. Inputs

A loop run should start from one of these inputs:

- a missing SAP object: transaction, table, field, template, domain/value source, relationship, or Fiori app;
- a weak fact: `confidence: needs_verification`;
- a sparse object: missing labels, source refs, relationships, common transactions, or value-source detail;
- a consultant question that the atlas cannot answer yet.

Generate a current gap report with:

```bash
make gap-report
```

## 1. GAP — choose the smallest useful gap

Pick one small vertical slice. Good slices:

- one transaction + tables it commonly opens;
- one table + key fields + text/check/customizing relationships;
- one Migration Cockpit template field + canonical table-field mapping;
- one field + labels + value source + related fields;
- one `needs_verification` object promoted to `verified` with source refs.

Bad slices:

- “add all Material Master”; too broad;
- copied SAP documentation;
- customer/project-specific mappings;
- facts without confidence labels.

## 2. SCOPE — define the contract before editing

Write down:

- target object ids;
- collections to touch under `data/`;
- expected relationships;
- confidence target: `verified`, `known_from_experience`, or `needs_verification`;
- public source refs, if available;
- explicit non-goals.

Use `docs/templates/atlas-fill-task.md` for this.

## 3. COLLECT — gather source-safe evidence

Allowed sources:

- public SAP pages or public community pages when they support a small factual claim;
- public package/repo-local fixtures;
- consultant experience, but only as `known_from_experience` or `needs_verification`;
- synthetic examples that contain no customer data.

Do not add customer exports, screenshots, internal URLs, tickets, client names, or proprietary mappings.

## 4. MODEL — add or update YAML contracts

Use the existing collections:

- `data/transactions.yaml`
- `data/fiori_apps.yaml`
- `data/tables.yaml`
- `data/fields.yaml`
- `data/migration_templates.yaml`
- `data/domains.yaml`
- `data/relationships.yaml`

Rules:

- use stable ids (`TABLE-FIELD`, lowercase relationship ids, explicit template ids);
- every item gets `confidence` and `source_refs`;
- `verified` requires at least one source ref;
- if uncertain, prefer `needs_verification` over guessing.

## 5. LINK — make the graph useful

For every new object, ask:

- which table/field/domain/template/transaction is it related to?
- is the relationship a primary key, foreign key, check table, customizing lookup, text table, semantic equivalent, transaction access, or template mapping?
- does the relation belong in `related_fields`, `related_tables`, `common_transactions`, or `data/relationships.yaml`?

An object with no relationships is usually not agent-ready yet.

## 6. VALIDATE — run deterministic gates

Run:

```bash
make check
make gap-report
```

`make check` is the hard gate. `make gap-report` is the planning/coverage signal.

## 7. EXPLAIN — prove agent usefulness

If the slice changes user-facing knowledge, update or add an example under `examples/` and check that an agent can answer:

- what is this SAP object?
- how is it used in migration work?
- which labels/aliases can refer to it?
- what confidence/source caveat should be surfaced?
- what should not be assumed?

Use `skills/explain-sap-object.md` as the answer contract.

## 8. REVIEW — source, safety, and graph review

Before shipping, review:

- no customer/project/private data;
- no proprietary SAP doc copy;
- confidence labels match evidence;
- `verified` facts have source refs;
- graph links resolve and are useful;
- README/docs/examples stay current if public behavior changed.

## 9. SHIP — commit one small slice

Commit message pattern:

```text
feat(data): add <sap-object-slice>
```

Examples:

```text
feat(data): add material type value source
feat(data): map product base unit field
feat(data): verify SE16N transaction metadata
```

## 10. NEXT GAP — feed the loop again

After shipping, run:

```bash
make gap-report
```

Pick the next highest-value gap:

1. `needs_verification` facts with high reuse;
2. key fields without value-source detail;
3. tables with no common transactions;
4. template fields without canonical mapping;
5. relationships missing around already-used objects;
6. language/export/template labels missing for common fields.

## Stop conditions

Stop and ask/record a blocker when:

- the next fact needs customer-specific evidence;
- only proprietary SAP documentation would support the claim;
- source confidence is unclear and the claim would be misleading;
- a relationship cannot be modelled with current schema;
- the slice is too broad for one safe commit.

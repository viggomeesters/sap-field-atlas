# Source and confidence policy

SAP Field Atlas is allowed to start from practical consultant knowledge, but every fact must be honest about confidence and source status.

## Confidence levels

- `verified` — backed by a specific public source, repo-local fixture, or verified system observation that can be checked again.
- `known_from_experience` — common SAP consultant knowledge that is useful but not yet source-complete.
- `needs_verification` — plausible seed or mapping that must not be treated as authoritative.

## Source references

Use `source_refs` as a list. Accepted starter forms:

- public URL to SAP Help/API/Fiori Apps Library/community docs when legally usable;
- local source id for repo-owned examples/fixtures;
- empty list only when confidence is `known_from_experience` or `needs_verification`.

Do not use generic SAP home/help root URLs as high-specificity evidence for an important claim. Prefer the exact page or keep confidence lower.

## Public data boundary

Never add:

- customer/client names;
- screenshots or exports from customer SAP systems;
- internal URLs, ticket ids, project ids, names, or proprietary mappings;
- literal copied chunks of proprietary SAP documentation.

Prefer short factual statements plus source references.

## MVP vs later

MVP is data-consultant-first:

1. transactions;
2. tables;
3. fields;
4. field labels/aliases;
5. relationships;
6. Migration Cockpit template mappings;
7. value sources/domains/customizing hints.

Later extension points:

- Fiori apps beyond starter links;
- BAPIs;
- function modules;
- broader module/domain packs;
- richer source-specific release/applicability metadata.

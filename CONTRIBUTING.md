# Contributing

SAP Field Atlas is public-safe and source-aware.

## Hard rules

- Do not add client/customer data.
- Do not add screenshots or exports from customer SAP systems.
- Do not add internal URLs, project IDs, tickets, names, or proprietary mappings.
- Do not claim this is official SAP documentation.
- Do not mirror proprietary SAP documentation. Add source references and short factual notes instead.

## Confidence labels

- `verified`: backed by a specific public source, repo-local fixture, or verified system observation that can be checked again.
- `known_from_experience`: common consultant knowledge, useful but not source-complete.
- `needs_verification`: plausible/seed information that must not be treated as authoritative.

See `docs/source-confidence-policy.md` for the full policy.

## Source refs

Use exact public URLs or repo-local evidence ids where possible. Empty `source_refs: []` is acceptable only for `known_from_experience` or `needs_verification` starter knowledge. Do not use generic SAP root URLs as strong evidence for important claims.

## Scope now vs later

MVP focuses on transactions, tables, fields, labels/aliases, relationships, Migration Cockpit mappings, and value sources/domains/customizing hints. Fiori apps, BAPIs, function modules, and broader coverage are later extension points unless a specific task adds them.

## Adding knowledge

1. Add or edit YAML under `data/`.
2. Include `confidence` and `source_refs` where the contract supports it.
3. Follow `CODE_OF_CONDUCT.md` and `SUPPORT.md` for public interaction boundaries.
4. Run the full gate:

```bash
make check
```

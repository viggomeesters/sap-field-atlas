# Fill Atlas Gap Loop

Use this when an agent is asked to grow SAP Field Atlas.

## Instruction

Follow `docs/ATLAS_FILL_LOOP.md` exactly. If invoked through Viggo's `go-loop`, treat `go-loop` as the execution orchestrator and this skill as the SAP Field Atlas domain protocol.

For multi-slice campaigns, use `docs/templates/go-loop-atlas-campaign.md` and keep AW Lite/go-loop runtime state outside this repo.

Work in one small vertical slice:

1. Run `make gap-report`.
2. Select or confirm one gap.
3. Scope the smallest useful object slice.
4. Add/update YAML under `data/`.
5. Add relationships and value-source detail.
6. Add/update examples when the slice changes agent answers.
7. Run `make check` and `make gap-report`.
8. Review source confidence and public-data safety.
9. Commit one focused slice.

## Rules

- Do not add customer data, SAP screenshots/exports, internal URLs, tickets, or proprietary mappings.
- Do not copy proprietary SAP documentation.
- `verified` requires concrete source refs.
- Prefer `needs_verification` over guessing.
- No repo-local `.go-workflow` or durable run state.
- No GitHub Actions unless explicitly requested.

## Pass condition

A fill slice is done only when:

- `make check` passes;
- `make gap-report` reflects the expected improvement or documents remaining gaps;
- the new/updated objects are linked into the graph;
- source/confidence/public-safety review has no blocking finding.

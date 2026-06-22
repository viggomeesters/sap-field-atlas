# Agent Instructions — SAP Field Atlas

SAP Field Atlas is a **public, generic, agent-ready SAP data migration knowledge base**. Keep it separate from any SAP FO Knowledge Base or customer-specific McCoy/FO work.

## Repo identity

- Public repo: `viggomeesters/sap-field-atlas`
- Local WSL path: `/home/viggo/github/sap-field-atlas`
- Python package: `sap-field-atlas`
- Python module: `sap_field_atlas`
- CLI: `sap-field-atlas`

Do not reintroduce old FO-KB project/package/CLI slugs into this repo; `scripts/validate_repository.py` enforces the exact blocked strings.

## Public data boundary

Allowed:

- generic SAP transaction/table/field/template knowledge;
- public source references;
- explicitly confidence-labelled consultant knowledge;
- synthetic examples that contain no customer data.

Forbidden:

- customer/client names;
- screenshots or exports from SAP systems;
- internal URLs, tickets, project IDs, proprietary mappings;
- copied proprietary SAP documentation.

## Workflow

1. Inspect `git status --short --branch` and `git remote -v` before editing.
2. Keep changes data-first and source/confidence labelled.
3. Run:
   ```bash
   make check
   ```
4. Commit focused changes and push only after gates pass.
5. For durable planning, use Viggo's vault-first Agent Workflow Lite outside this repo. Do **not** add repo-local `.go-workflow`, `go_workflow`, or generated `tasks.md` runtime state.

## Validation contract

`make check` must run:

- repository identity/safety guard;
- YAML knowledge validation;
- completeness audit;
- pytest regression tests;
- git whitespace diff check.

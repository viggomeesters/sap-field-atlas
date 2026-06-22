# Repo-complete checklist

Applied from Viggo's `viggo-agent-skills` operating conventions to this public repo.

## Identity

- [x] Public repo name, package name, module name, CLI name, README, and remote agree on `sap-field-atlas`.
- [x] Explicitly separated from SAP FO Knowledge Base.
- [x] `AGENTS.md` tells agents not to add repo-local workflow runtime state.

## Safety

- [x] Public-data boundary documented in `README.md`, `CONTRIBUTING.md`, `SECURITY.md`, and `AGENTS.md`.
- [x] Source/confidence policy exists.
- [x] Verified facts require `source_refs` in the validator.
- [x] Repository guard rejects old FO-KB identity strings and repo-local workflow remnants.

## Operations

- [x] `Makefile` exposes one command: `make check`.
- [x] PR template includes validation and public-data checklist.
- [x] CODEOWNERS routes review to `@viggomeesters`.

## Agent usability

- [x] Agent instructions in `AGENTS.md`.
- [x] Explain skill in `skills/explain-sap-object.md`.
- [x] Example outputs in `examples/`.
- [x] Architecture and roadmap docs in `docs/`.

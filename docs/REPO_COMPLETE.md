# Repo-complete checklist

Applied from Viggo's `viggo-agent-skills` operating conventions to this public repo.

## Identity

- [x] Public repo name, package name, module name, CLI name, README, and remote agree on `sap-field-atlas`.
- [x] Explicitly separated from SAP FO Knowledge Base.
- [x] `AGENTS.md` tells agents not to add repo-local workflow runtime state.

## Public GitHub surface

- [x] Repository About/description is useful and specific.
- [x] Repository topics are set for discoverability.
- [x] README has a professional hero, badges, problem statement, quick start, examples, package/release section, safety boundary, and contributors link.
- [x] `assets/repo-hero.svg` gives the repo a visual identity.
- [x] `docs/HERO_GUIDELINES.md` defines visual QA requirements: crisp at README scale, not zoomed out, not busy, no text overflow, no fuzzy filters/shadows.
- [x] `CONTRIBUTORS.md` exists.

## Release and package

- [x] `v0.1.0` release exists.
- [x] Python wheel and source distribution are built and attached to the release.
- [x] `docs/PACKAGE.md` documents build/install/verify flow.
- [x] `Makefile` exposes `make package`.

## Safety

- [x] Public-data boundary documented in `README.md`, `CONTRIBUTING.md`, `SECURITY.md`, and `AGENTS.md`.
- [x] Source/confidence policy exists.
- [x] Verified facts require `source_refs` in the validator.
- [x] Repository guard rejects old FO-KB identity strings and repo-local workflow remnants.

## Operations

- [x] `Makefile` exposes one full local gate: `make check`.
- [x] PR template includes validation and public-data checklist.
- [x] CODEOWNERS routes review to `@viggomeesters`.
- [x] No GitHub Actions workflow is included by default; local `make check` is canonical unless CI is explicitly requested.

## Agent usability

- [x] Agent instructions in `AGENTS.md`.
- [x] Explain skill in `skills/explain-sap-object.md`.
- [x] Example outputs in `examples/`.
- [x] Architecture and roadmap docs in `docs/`.

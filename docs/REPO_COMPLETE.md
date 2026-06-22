# Repo-complete checklist

Applied from Viggo's `viggo-agent-skills` operating conventions to this public repo.

## Identity

- [x] Public repo name, package name, module name, CLI name, README, and remote agree on `sap-field-atlas`.
- [x] Explicitly separated from SAP FO Knowledge Base.
- [x] `AGENTS.md` tells agents not to add repo-local workflow runtime state.

## Public GitHub surface

- [x] Repository About/description is useful and specific.
- [x] Repository topics are set for discoverability.
- [x] README has a professional hero, badges, problem statement, quick start, examples, package/release section, safety boundary, project status, and contributors link.
- [x] `assets/repo-hero.svg` gives the repo a visual identity.
- [x] `docs/HERO_GUIDELINES.md` defines visual QA requirements: crisp at README scale, not zoomed out, not busy, no text overflow, no fuzzy filters/shadows.
- [x] `CONTRIBUTORS.md` exists.

## Governance and community hygiene

- [x] `CHANGELOG.md` records public release history.
- [x] `SUPPORT.md` defines support scope and no-SLA expectations.
- [x] `CODE_OF_CONDUCT.md` defines contributor behavior and safety boundaries.
- [x] `NOTICE.md` states SAP trademark/non-affiliation and public-data limitations.
- [x] `.github/ISSUE_TEMPLATE/config.yml` disables blank issues and routes users to source/safety docs.
- [x] `docs/MAINTAINER_CHECKLIST.md` gives a release/readiness checklist.

## Release and package

- [x] `v0.1.0` release exists.
- [x] Python wheel and source distribution are built and attached to the release.
- [x] `docs/PACKAGE.md` documents build/install/verify flow.
- [x] `Makefile` exposes `make package`.

## Safety

- [x] Public-data boundary documented in `README.md`, `CONTRIBUTING.md`, `SECURITY.md`, `SUPPORT.md`, and `AGENTS.md`.
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
- [x] Fill-loop skill in `skills/fill-atlas-gap-loop.md`.
- [x] Example outputs in `examples/`.
- [x] `docs/ATLAS_FILL_LOOP.md` defines gap → scope → collect → model → link → validate → explain → review → ship → next gap.
- [x] `docs/templates/atlas-fill-task.md` gives a small-slice task template.
- [x] `docs/templates/go-loop-atlas-campaign.md` gives a go-loop designer/campaign brief for multi-slice runs.
- [x] `.github/ISSUE_TEMPLATE/fill-atlas-gap.md` captures public-safe gap requests.
- [x] `make gap-report` provides the next-loop planning signal.
- [x] Architecture, roadmap, package, hero, source-confidence, and maintainer docs in `docs/`.

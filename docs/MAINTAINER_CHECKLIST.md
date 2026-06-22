# Maintainer checklist

Use this checklist before tagging a public release or calling the repository complete.

## Local gates

```bash
make check
make package
```

## Public surface

- README is clear, professional, and current.
- Hero passes `docs/HERO_GUIDELINES.md`.
- About/description, topics, and homepage are useful.
- `CONTRIBUTORS.md`, `SUPPORT.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `NOTICE.md`, and `CHANGELOG.md` are present.
- Release notes exist under `docs/releases/`.

## Data safety

- No customer names, screenshots, exports, system dumps, tickets, credentials, internal URLs, or project-specific mappings.
- New `verified` facts have specific `source_refs`.
- `known_from_experience` and `needs_verification` facts are not presented as authoritative.

## Release

- Version/tag is correct.
- Wheel and source distribution are built.
- Release notes mention schema/data/CLI impact.
- GitHub release assets are attached when no package registry is used.
- Remote `main` and release tag point at the intended commit.

## No default CI

Do not add GitHub Actions as part of repo-complete unless explicitly requested. Local `make check` is the canonical gate.

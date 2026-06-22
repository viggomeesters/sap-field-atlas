# Scripts

## `validate_repository.py`

Repository identity, public-safety, public-surface, and repo-complete guard.

Run via:

```bash
make check
```

## `atlas_gap_report.py`

Heuristic coverage report for the Atlas Fill Loop. It summarizes collection counts, confidence mix, and likely next gaps such as `needs_verification` facts, missing labels, unknown value sources, sparse relationships, and template fields without canonical mappings.

Run via:

```bash
make gap-report
```

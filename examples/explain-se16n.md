# Explain `SE16N`

## What it is

`SE16N` is modelled as a SAP GUI transaction for general table display / practical table browsing.

- Canonical object: `SE16N`
- Category: `data_viewer`
- Systems: ECC, S/4
- Confidence: `known_from_experience`
- Source refs: none yet

## Where you use it

Consultants commonly use `SE16N` to inspect table data, run quick lookups, and make exports when they have the right authorization.

## Related objects

- Related table in this starter seed: `MARA`
- Relationship: `se16n-displays-mara`

## Migration notes

Useful for quick data checks and export-style analysis during migration work. Do not treat an export label as the canonical SAP technical field name; use field ids such as `MARA-MATNR` for canonical references.

## Uncertainty

The exact official transaction title can vary by SAP release/context and should be verified against the target system. This repo currently stores `SE16N` as practical consultant knowledge, not official SAP documentation.

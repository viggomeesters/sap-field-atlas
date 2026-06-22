# Explain `MARA-MATNR`

## What it is

`MARA-MATNR` is the canonical table-field id for the material number field in table `MARA`.

- Table: `MARA`
- Field: `MATNR`
- Business meaning: Material Number
- Key field: yes
- Confidence: `known_from_experience`
- Source refs: none yet

## Labels and aliases

Known starter labels:

- SAP EN short: `Material`
- SAP EN long: `Material Number`
- Export label: `Material Number`
- Migration Cockpit label: `Product Number`
- NL labels: not verified yet

## Related objects

- Table: `MARA` — general material data / Material Master anchor
- Migration template seed: `s4-product-initial-seed`
- Relationship: `product-number-template-maps-to-mara-matnr`

## Migration notes

In S/4 and Migration Cockpit context, a user may see “Product Number” where the canonical technical field is still modelled here as `MARA-MATNR`. Treat “Product Number” as a template/business label until the exact template write path is verified.

## Uncertainty

The starter seed does not yet verify datatype, length, language-specific labels, or direct table-write behavior. Do not claim the Product template writes directly to `MARA` unless a source/system check proves it.

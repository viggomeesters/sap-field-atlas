# Label, alias, relationship, and value-source model

SAP Field Atlas treats technical field ids, labels, aliases, and value sources as separate facts. Agents should not collapse them into one name.

## Label contexts

A field can have multiple labels:

- canonical technical id: `TABLE-FIELD`, e.g. `MARA-MATNR`
- technical field name: `MATNR`
- business meaning: Material Number
- SAP GUI short/long labels per logon language
- export labels
- SAP Migration Cockpit template labels such as Product Number

When explaining a field, answer with the canonical id first, then list known labels with confidence and unknown labels as `needs_verification` or `null`.

## Value sources

Use `value_source.kind` to distinguish:

- `identifier`: generated or governed identifier such as material number
- `customizing`: target-system customizing value such as Company Code (`BUKRS`)
- `domain` / `check_table` / `lookup_table`: constrained values
- `free_text`: unconstrained text
- `unknown`: not modelled yet

## Example: label ambiguity

If an agent is asked “What is Product Number?”, it should say:

1. In this starter seed, Product Number is a Migration Cockpit label mapped to `MARA-MATNR`.
2. The canonical SAP table-field is `MARA-MATNR`.
3. Business meaning: Material Number.
4. Known labels include Material Number and Product Number; language-specific labels are incomplete until verified.
5. The write path of the template is `needs_verification`, so do not claim it writes directly to MARA.

## Example: customizing-managed value

`T001-BUKRS` / Company Code is modelled as `customizing` because valid values are maintained in the target SAP system. Migration work should validate source values against target customizing instead of treating them as arbitrary text.

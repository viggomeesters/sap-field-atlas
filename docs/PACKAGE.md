# Package

SAP Field Atlas ships as a small Python package that provides the `sap-field-atlas` validation CLI.

## Build

```bash
make package
```

This creates:

- `dist/sap_field_atlas-0.1.0-py3-none-any.whl`
- `dist/sap_field_atlas-0.1.0.tar.gz`

## Install from GitHub

```bash
python -m pip install git+https://github.com/viggomeesters/sap-field-atlas.git@v0.1.0
```

## Install from release artifact

Download the wheel from the `v0.1.0` GitHub release and run:

```bash
python -m pip install sap_field_atlas-0.1.0-py3-none-any.whl
```

## Verify

```bash
sap-field-atlas validate --root /path/to/sap-field-atlas
sap-field-atlas audit-completeness --root /path/to/sap-field-atlas
```

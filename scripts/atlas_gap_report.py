#!/usr/bin/env python3
from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
COLLECTIONS = {
    "transactions": "transactions.yaml",
    "fiori_apps": "fiori_apps.yaml",
    "tables": "tables.yaml",
    "fields": "fields.yaml",
    "migration_templates": "migration_templates.yaml",
    "domains": "domains.yaml",
    "relationships": "relationships.yaml",
}


def read_yaml(name: str) -> list[dict[str, Any]]:
    path = DATA / COLLECTIONS[name]
    if not path.exists():
        return []
    value = yaml.safe_load(path.read_text()) or []
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, dict)]


def identity(item: dict[str, Any]) -> str:
    for key in ("id", "code", "name", "template_id"):
        value = item.get(key)
        if isinstance(value, str) and value:
            return value
    return "<unknown>"


def is_empty_label(value: Any) -> bool:
    return value in (None, "", [])


def main() -> int:
    data = {name: read_yaml(name) for name in COLLECTIONS}
    print("# SAP Field Atlas gap report")
    print()
    print("## Coverage counts")
    for name, items in data.items():
        print(f"- {name}: {len(items)}")

    print()
    print("## Confidence mix")
    confidence = Counter()
    for items in data.values():
        for item in items:
            confidence[item.get("confidence", "<missing>")] += 1
    for label in ("verified", "known_from_experience", "needs_verification", "<missing>"):
        if confidence[label]:
            print(f"- {label}: {confidence[label]}")

    gaps: list[str] = []

    for name, items in data.items():
        if not items:
            gaps.append(f"empty collection: {name}")
        for item in items:
            ident = identity(item)
            if item.get("confidence") == "needs_verification":
                gaps.append(f"needs verification: {name} {ident}")
            if item.get("confidence") == "verified" and not item.get("source_refs"):
                gaps.append(f"verified without source refs: {name} {ident}")

    table_ids = {identity(item) for item in data["tables"]}
    fields_by_table: dict[str, list[dict[str, Any]]] = {table: [] for table in table_ids}
    for field in data["fields"]:
        fields_by_table.setdefault(str(field.get("table")), []).append(field)
        labels = field.get("labels") or {}
        for label_key in ("sap_en_short", "sap_en_long", "export_label", "migration_cockpit_label"):
            if is_empty_label(labels.get(label_key)):
                gaps.append(f"missing label {label_key}: fields {identity(field)}")
        value_source = field.get("value_source") or {}
        if value_source.get("kind") in (None, "unknown"):
            gaps.append(f"unknown value source: fields {identity(field)}")
        if not field.get("related_fields"):
            gaps.append(f"no related fields listed: fields {identity(field)}")

    for table in data["tables"]:
        ident = identity(table)
        if not fields_by_table.get(ident):
            gaps.append(f"table has no fields: tables {ident}")
        if not table.get("common_transactions"):
            gaps.append(f"table has no common transactions: tables {ident}")
        if not table.get("related_tables"):
            gaps.append(f"table has no related tables: tables {ident}")

    relationship_pairs = {(rel.get("from"), rel.get("to"), rel.get("relationship_type")) for rel in data["relationships"]}
    for field in data["fields"]:
        table = field.get("table")
        ident = identity(field)
        if table and (table, ident, "primary_key") not in relationship_pairs and field.get("is_key"):
            gaps.append(f"key field lacks primary_key relationship: {table} -> {ident}")

    for template in data["migration_templates"]:
        for field in template.get("fields") or []:
            if isinstance(field, dict) and not field.get("canonical_field"):
                label = field.get("template_field") or field.get("label") or "<unknown>"
                gaps.append(f"template field without canonical mapping: {identity(template)} {label}")

    print()
    print("## Prioritized gaps")
    if not gaps:
        print("- none detected by heuristic gap report")
    else:
        for idx, gap in enumerate(gaps[:40], start=1):
            print(f"{idx}. {gap}")
        if len(gaps) > 40:
            print(f"- ... {len(gaps) - 40} more")

    print()
    print("## Suggested next loop input")
    if gaps:
        print(f"- Fill gap: {gaps[0]}")
    else:
        print("- Choose a new SAP object slice and create an atlas fill task.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

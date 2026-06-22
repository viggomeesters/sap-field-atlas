from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

COLLECTIONS = {
    "transactions": "transactions.yaml",
    "fiori_apps": "fiori_apps.yaml",
    "tables": "tables.yaml",
    "fields": "fields.yaml",
    "migration_templates": "migration_templates.yaml",
    "domains": "domains.yaml",
    "relationships": "relationships.yaml",
}
CONFIDENCE = {"verified", "known_from_experience", "needs_verification"}
VALUE_SOURCE_KINDS = {"free_text", "identifier", "customizing", "domain", "check_table", "lookup_table", "unknown"}
RELATIONSHIP_TYPES = {
    "primary_key",
    "foreign_key",
    "text_table",
    "customizing_lookup",
    "domain",
    "check_table",
    "semantic_equivalent",
    "transaction_access",
    "template_mapping",
}
REQUIRED = {
    "transactions": ["code", "purpose", "category", "systems", "relevant_for", "confidence", "source_refs"],
    "fiori_apps": ["id", "name", "purpose", "confidence", "source_refs"],
    "tables": ["name", "business_object", "description", "key_fields", "confidence", "source_refs"],
    "fields": ["id", "table", "field", "business_meaning", "is_key", "labels", "value_source", "confidence", "source_refs"],
    "migration_templates": ["template_id", "object", "variant", "source_system", "target_system", "fields", "confidence", "source_refs"],
    "domains": ["id", "kind", "description", "confidence", "source_refs"],
    "relationships": ["id", "from", "relationship_type", "description", "confidence", "source_refs"],
}


class ValidationError(Exception):
    pass


def _read_yaml(path: Path) -> Any:
    if not path.exists():
        return []
    try:
        value = yaml.safe_load(path.read_text())
    except yaml.YAMLError as exc:
        raise ValidationError(f"invalid YAML in {path}: {exc}") from exc
    return [] if value is None else value


def _as_list(value: Any, collection: str) -> list[dict[str, Any]]:
    if not isinstance(value, list):
        raise ValidationError(f"data/{COLLECTIONS[collection]} must contain a YAML list")
    for item in value:
        if not isinstance(item, dict):
            raise ValidationError(f"{collection} contains a non-object item")
    return value


def load_knowledge(root: Path) -> dict[str, list[dict[str, Any]]]:
    data_dir = root / "data"
    return {name: _as_list(_read_yaml(data_dir / filename), name) for name, filename in COLLECTIONS.items()}


def _identity(collection: str, item: dict[str, Any]) -> str:
    for key in ("id", "code", "name", "template_id"):
        value = item.get(key)
        if isinstance(value, str) and value:
            return value
    raise ValidationError(f"{collection} item lacks id/code/name/template_id: {item}")


def _require_fields(collection: str, item: dict[str, Any], ident: str) -> None:
    for key in REQUIRED[collection]:
        if key not in item:
            raise ValidationError(f"{collection} {ident} missing required field: {key}")
    confidence = item.get("confidence")
    if confidence not in CONFIDENCE:
        raise ValidationError(f"invalid confidence for {ident}: {confidence}")
    refs = item.get("source_refs")
    if not isinstance(refs, list):
        raise ValidationError(f"source_refs must be a list for {ident}")
    if confidence == "verified" and not refs:
        raise ValidationError(f"verified item requires at least one source_ref: {ident}")


def _object_ids(ids: dict[str, set[str]]) -> set[str]:
    return set().union(*ids.values()) if ids else set()


def validate_knowledge(data: dict[str, list[dict[str, Any]]]) -> list[str]:
    ids: dict[str, set[str]] = {}
    for collection, items in data.items():
        seen: set[str] = set()
        for item in items:
            ident = _identity(collection, item)
            if ident in seen:
                raise ValidationError(f"duplicate {collection} id: {ident}")
            seen.add(ident)
            _require_fields(collection, item, ident)
        ids[collection] = seen

    table_ids = ids["tables"]
    field_ids = ids["fields"]
    transaction_ids = ids["transactions"]

    for field in data["fields"]:
        ident = _identity("fields", field)
        table = field.get("table")
        if table not in table_ids:
            raise ValidationError(f"field {ident} points at missing table: {table}")
        if not isinstance(field.get("is_key"), bool):
            raise ValidationError(f"field {ident} is_key must be boolean")
        labels = field.get("labels")
        if not isinstance(labels, dict):
            raise ValidationError(f"field {ident} labels must be an object")
        value_source = field.get("value_source")
        if not isinstance(value_source, dict):
            raise ValidationError(f"field {ident} value_source must be an object")
        kind = value_source.get("kind")
        if kind not in VALUE_SOURCE_KINDS:
            raise ValidationError(f"field {ident} invalid value_source.kind: {kind}")
        lookup = value_source.get("lookup_table")
        if lookup and lookup not in table_ids:
            raise ValidationError(f"field {ident} lookup_table missing: {lookup}")
        for related in field.get("related_fields", []) or []:
            if related not in field_ids:
                raise ValidationError(f"field {ident} related field missing: {related}")

    for table in data["tables"]:
        ident = _identity("tables", table)
        for field_id in table.get("key_fields", []) or []:
            if field_id not in field_ids:
                raise ValidationError(f"table {ident} key field missing: {field_id}")
        for code in table.get("common_transactions", []) or []:
            if code not in transaction_ids:
                raise ValidationError(f"table {ident} transaction missing: {code}")
        for related in table.get("related_tables", []) or []:
            if related not in table_ids:
                raise ValidationError(f"table {ident} related table missing: {related}")

    all_ids = _object_ids(ids)
    for domain in data["domains"]:
        ident = _identity("domains", domain)
        if domain.get("kind") not in VALUE_SOURCE_KINDS - {"unknown"}:
            raise ValidationError(f"domain {ident} invalid kind: {domain.get('kind')}")
        for key in ("table", "field"):
            value = domain.get(key)
            if value and value not in all_ids:
                raise ValidationError(f"domain {ident} {key} missing: {value}")

    for rel in data["relationships"]:
        rel_id = _identity("relationships", rel)
        start = rel.get("from")
        end = rel.get("to")
        if rel.get("relationship_type") not in RELATIONSHIP_TYPES:
            raise ValidationError(f"relationship {rel_id} invalid type: {rel.get('relationship_type')}")
        if start not in all_ids:
            raise ValidationError(f"relationship {rel_id} from missing: {start}")
        if end and end not in all_ids:
            raise ValidationError(f"relationship {rel_id} to missing: {end}")

    for template in data["migration_templates"]:
        ident = _identity("migration_templates", template)
        fields = template.get("fields")
        if not isinstance(fields, list):
            raise ValidationError(f"template {ident} fields must be a list")
        for field in fields:
            if not isinstance(field, dict):
                raise ValidationError(f"template {ident} field mapping must be an object")
            canonical = field.get("canonical_field")
            if canonical and canonical not in field_ids:
                raise ValidationError(f"template {ident} canonical field missing: {canonical}")
            confidence = field.get("confidence")
            if confidence and confidence not in CONFIDENCE:
                raise ValidationError(f"template {ident} invalid field confidence: {confidence}")

    return []


def audit_completeness(data: dict[str, list[dict[str, Any]]]) -> list[str]:
    validate_knowledge(data)
    findings: list[str] = []
    if not any(data.values()):
        findings.append("starter skeleton: no SAP knowledge items yet")
    required = ["transactions", "tables", "fields"]
    for collection in required:
        if not data[collection]:
            findings.append(f"starter gap: no {collection} yet")
    return findings

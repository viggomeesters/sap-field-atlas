import pytest

from sap_field_atlas.validation import ValidationError, validate_knowledge


def empty_data():
    return {
        "transactions": [],
        "fiori_apps": [],
        "tables": [],
        "fields": [],
        "migration_templates": [],
        "domains": [],
        "relationships": [],
    }


def test_duplicate_ids_fail():
    data = empty_data()
    item = {"code": "SE16N", "purpose": "View data", "category": "data_viewer", "systems": ["ECC"], "relevant_for": ["analysis"], "confidence": "known_from_experience", "source_refs": []}
    data["transactions"] = [item, dict(item)]
    with pytest.raises(ValidationError, match="duplicate"):
        validate_knowledge(data)


def test_field_requires_existing_table():
    data = empty_data()
    data["fields"] = [{"id": "MARA-MATNR", "table": "MARA", "field": "MATNR", "business_meaning": "Material Number", "is_key": True, "labels": {}, "value_source": {"kind": "identifier"}, "confidence": "known_from_experience", "source_refs": []}]
    with pytest.raises(ValidationError, match="missing table"):
        validate_knowledge(data)


def test_relationship_requires_known_objects():
    data = empty_data()
    data["relationships"] = [{"id": "rel-1", "from": "MARA-MATNR", "to": "MAKT-MATNR", "relationship_type": "semantic_equivalent", "description": "x", "confidence": "needs_verification", "source_refs": []}]
    with pytest.raises(ValidationError, match="from missing"):
        validate_knowledge(data)


def test_verified_requires_source_ref():
    data = empty_data()
    data["transactions"] = [{"code": "SE16N", "purpose": "View data", "category": "data_viewer", "systems": ["ECC"], "relevant_for": ["analysis"], "confidence": "verified", "source_refs": []}]
    with pytest.raises(ValidationError, match="verified item requires"):
        validate_knowledge(data)


def test_invalid_confidence_fails():
    data = empty_data()
    data["transactions"] = [{"code": "SE16N", "purpose": "View data", "category": "data_viewer", "systems": ["ECC"], "relevant_for": ["analysis"], "confidence": "sure", "source_refs": []}]
    with pytest.raises(ValidationError, match="invalid confidence"):
        validate_knowledge(data)

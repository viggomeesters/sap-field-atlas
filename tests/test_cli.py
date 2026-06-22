from pathlib import Path

from sap_field_atlas.validation import audit_completeness, load_knowledge, validate_knowledge


def test_repository_knowledge_validates():
    data = load_knowledge(Path('.'))
    assert validate_knowledge(data) == []
    assert audit_completeness(data) == []

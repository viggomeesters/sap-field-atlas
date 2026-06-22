.PHONY: check validate audit test guard diff-check

check: guard validate audit test diff-check

guard:
	python3 scripts/validate_repository.py

validate:
	uv run sap-field-atlas validate

audit:
	uv run sap-field-atlas audit-completeness

test:
	uv run pytest -q

diff-check:
	git diff --check

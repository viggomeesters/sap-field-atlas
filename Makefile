.PHONY: check validate audit test guard package gap-report diff-check

check: guard validate audit test diff-check

guard:
	python3 scripts/validate_repository.py

validate:
	uv run sap-field-atlas validate

audit:
	uv run sap-field-atlas audit-completeness

test:
	uv run pytest -q

package:
	uv build

gap-report:
	python3 scripts/atlas_gap_report.py

diff-check:
	git diff --check

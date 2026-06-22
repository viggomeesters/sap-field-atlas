#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

import tomllib
import yaml

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "project_name": "sap-field-atlas",
    "module_dir": ROOT / "src" / "sap_field_atlas",
    "cli_name": "sap-field-atlas",
    "github_remote": "viggomeesters/sap-field-atlas",
}
TEXT_SUFFIXES = {".md", ".py", ".toml", ".yaml", ".yml", ".txt", ".gitignore", ""}
FORBIDDEN_IDENTITY_STRINGS = [
    "sap-fo-knowledge-base",
    "sap_fo_knowledge_base",
    "sap-fo-kb",
]
FORBIDDEN_PATHS = [
    ".go-workflow",
    "go_workflow",
    "tasks.md",
]
REQUIRED_PUBLIC_REPO_FILES = [
    "AGENTS.md",
    "CONTRIBUTORS.md",
    "SECURITY.md",
    "Makefile",
    "assets/repo-hero.svg",
    "docs/ARCHITECTURE.md",
    "docs/HERO_GUIDELINES.md",
    "docs/PACKAGE.md",
    "docs/REPO_COMPLETE.md",
    "docs/ROADMAP.md",
    ".github/pull_request_template.md",
    ".github/CODEOWNERS",
]
ALLOW_SELF = {Path("scripts/validate_repository.py")}


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_pyproject() -> dict:
    with (ROOT / "pyproject.toml").open("rb") as fh:
        return tomllib.load(fh)


def iter_text_files():
    skip_parts = {".git", ".venv", ".pytest_cache", "__pycache__"}
    for path in ROOT.rglob("*"):
        rel = path.relative_to(ROOT)
        if path.is_dir() or skip_parts.intersection(rel.parts):
            continue
        if path.suffix in TEXT_SUFFIXES or path.name in {"Makefile", "CODEOWNERS"}:
            yield rel, path


def check_identity() -> None:
    pyproject = read_pyproject()
    project = pyproject.get("project", {})
    if project.get("name") != EXPECTED["project_name"]:
        fail(f"pyproject project.name must be {EXPECTED['project_name']!r}")
    scripts = project.get("scripts", {})
    if EXPECTED["cli_name"] not in scripts:
        fail(f"missing CLI script {EXPECTED['cli_name']!r}")
    if not EXPECTED["module_dir"].is_dir():
        fail("missing src/sap_field_atlas module")
    readme = (ROOT / "README.md").read_text()
    if "SAP Field Atlas" not in readme or "sap-field-atlas" not in readme:
        fail("README does not advertise SAP Field Atlas identity")


def check_yaml_contracts() -> None:
    data_dir = ROOT / "data"
    required = {
        "transactions.yaml",
        "fiori_apps.yaml",
        "tables.yaml",
        "fields.yaml",
        "migration_templates.yaml",
        "domains.yaml",
        "relationships.yaml",
    }
    missing = [name for name in sorted(required) if not (data_dir / name).exists()]
    if missing:
        fail(f"missing data files: {', '.join(missing)}")
    for path in sorted(data_dir.glob("*.yaml")):
        value = yaml.safe_load(path.read_text())
        if value is not None and not isinstance(value, list):
            fail(f"{path.relative_to(ROOT)} must contain a YAML list")


def check_public_boundary() -> None:
    for rel in REQUIRED_PUBLIC_REPO_FILES:
        if not (ROOT / rel).exists():
            fail(f"missing repo-complete public file: {rel}")
    readme = (ROOT / "README.md").read_text()
    for required_phrase in ("![SAP Field Atlas repository hero]", "## Package and release", "## Contributors"):
        if required_phrase not in readme:
            fail(f"README missing professional public surface section: {required_phrase}")
    hero = (ROOT / "assets" / "repo-hero.svg").read_text()
    forbidden_hero_fragments = ("<filter", "feGaussianBlur", "stdDeviation=", "dropShadow", "filter=")
    for fragment in forbidden_hero_fragments:
        if fragment in hero:
            fail(f"repo hero uses fuzzy/blur-prone SVG fragment: {fragment}")
    if "width=\"1000\"" not in hero or "height=\"360\"" not in hero:
        fail("repo hero must use the crisp README-scale 1000x360 canvas")
    for rel, path in iter_text_files():
        if rel in ALLOW_SELF:
            continue
        text = path.read_text(errors="ignore")
        for forbidden in FORBIDDEN_IDENTITY_STRINGS:
            if forbidden in text:
                fail(f"forbidden old identity string {forbidden!r} in {rel}")
    for forbidden in FORBIDDEN_PATHS:
        if (ROOT / forbidden).exists():
            fail(f"forbidden repo-local workflow remnant exists: {forbidden}")


def main() -> int:
    check_identity()
    check_yaml_contracts()
    check_public_boundary()
    print("repository guard ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

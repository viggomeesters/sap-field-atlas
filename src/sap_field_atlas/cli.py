from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .validation import ValidationError, audit_completeness, load_knowledge, validate_knowledge


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="sap-field-atlas")
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("validate", "audit-completeness"):
        p = sub.add_parser(name)
        p.add_argument("--root", default=".")
    args = parser.parse_args(argv)
    root = Path(args.root)
    try:
        data = load_knowledge(root)
        if args.command == "validate":
            findings = validate_knowledge(data)
        else:
            findings = audit_completeness(data)
    except ValidationError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    if findings:
        for finding in findings:
            print(finding)
    else:
        print("ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

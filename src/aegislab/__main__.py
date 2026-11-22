"""CLI entry point: python -m aegislab analyze --input FILE --source-id ID."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .ssh_incident import InputError, analyze, human_summary


def main() -> int:
    parser = argparse.ArgumentParser(description="Bounded, offline SSH auth evidence triage")
    commands = parser.add_subparsers(dest="command", required=True)
    scan = commands.add_parser("analyze", help="Analyze source-declared JSONL envelopes")
    scan.add_argument("--input", type=Path, required=True, help="Local JSONL input")
    scan.add_argument("--source-id", required=True, help="Stable human-supplied source identity")
    scan.add_argument("--source-kind", choices=("synthetic", "unverified_import"),
                      default="synthetic", help="Declared source kind, not an attestation")
    scan.add_argument("--json", action="store_true", help="Print full machine-readable report")
    args = parser.parse_args()
    try:
        report = analyze(args.input, source_id=args.source_id, source_kind=args.source_kind)
    except InputError as exc:
        print(f"Input not assessed: {exc}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print(human_summary(report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""CLI entry point: python -m aegislab analyze --input FILE --source-id ID."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .ssh_incident import InputError, analyze, human_summary
from .investigator_context import prepare_context
from .investigator import investigate
from .local_inference import LocalConfig


def main() -> int:
    parser = argparse.ArgumentParser(description="Bounded, offline SSH auth evidence triage")
    commands = parser.add_subparsers(dest="command", required=True)
    scan = commands.add_parser("analyze", help="Analyze source-declared JSONL envelopes")
    scan.add_argument("--input", type=Path, required=True, help="Local JSONL input")
    scan.add_argument("--source-id", required=True, help="Stable human-supplied source identity")
    scan.add_argument("--source-kind", choices=("synthetic", "unverified_import"),
                      default="synthetic", help="Declared source kind, not an attestation")
    output = scan.add_mutually_exclusive_group()
    output.add_argument("--json", action="store_true", help="Print full machine-readable report")
    output.add_argument("--prepare-context", action="store_true",
                        help="Preview provisional bounded AI context; no inference")
    output.add_argument("--probe-investigator", action="store_true",
                        help="Experimental local AI on synthetic evidence only; unadjudicated output")
    scan.add_argument("--finding-id", help="Select a finding for context or probe")
    scan.add_argument("--model", help="Local model ID for experimental probe")
    scan.add_argument("--local-port", type=int, help="Loopback API port for experimental probe")
    scan.add_argument("--deadline", type=float, help="Overall inference worker wait budget in seconds")
    scan.add_argument("--socket-timeout", type=float, help="Individual socket I/O timeout in seconds")
    args = parser.parse_args()
    if args.finding_id is not None and not (args.prepare_context or args.probe_investigator):
        parser.error("--finding-id requires context preview or investigator probe")
    if not args.probe_investigator and any(v is not None for v in (args.model, args.local_port, args.deadline, args.socket_timeout)):
        parser.error("Local inference options require --probe-investigator")
    if args.probe_investigator:
        try:
            config = LocalConfig(model=args.model if args.model is not None else LocalConfig.model,
                                 port=args.local_port if args.local_port is not None else LocalConfig.port,
                                 timeout=args.socket_timeout if args.socket_timeout is not None else LocalConfig.timeout,
                                 deadline=args.deadline if args.deadline is not None else LocalConfig.deadline)
        except ValueError as exc:
            parser.error(str(exc))
    try:
        report = analyze(args.input, source_id=args.source_id, source_kind=args.source_kind)
    except InputError as exc:
        print(f"Input not assessed: {exc}", file=sys.stderr)
        return 2
    if args.probe_investigator:
        print(json.dumps(investigate(report, config, finding_id=args.finding_id), indent=2, sort_keys=True))
    elif args.prepare_context:
        print(json.dumps({"baseline": report,
                          "preparation": prepare_context(report, finding_id=args.finding_id)},
                         indent=2, sort_keys=True))
    elif args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print(human_summary(report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

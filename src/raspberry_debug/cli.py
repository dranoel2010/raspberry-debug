"""CLI entry point for raspberry-debug."""

from __future__ import annotations

import argparse
from pathlib import Path

from .parser import analyze_log, format_findings


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="raspberry-debug",
        description="Analysiert Raspberry-Pi Logs und zeigt wahrscheinliche Ursachen.",
    )
    parser.add_argument("logfile", type=Path, help="Pfad zur Log-Datei")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if not args.logfile.exists():
        parser.error(f"Datei nicht gefunden: {args.logfile}")

    report = format_findings(analyze_log(args.logfile.read_text(encoding="utf-8")))
    print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

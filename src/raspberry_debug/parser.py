"""Simple parser for Raspberry Pi related log snippets."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True, slots=True)
class Finding:
    """Detected issue within a log stream."""

    title: str
    severity: str
    evidence: str
    recommendation: str


_RULES: tuple[tuple[str, Finding], ...] = (
    (
        "under-voltage detected",
        Finding(
            title="Unterspannung erkannt",
            severity="high",
            evidence="Kernel meldet 'under-voltage detected'",
            recommendation="Netzteil prüfen (mind. 5V/3A), Kabelqualität verbessern.",
        ),
    ),
    (
        "mmc0: timeout",
        Finding(
            title="SD-Karten-Timeout",
            severity="medium",
            evidence="I/O Timeout auf mmc0",
            recommendation="SD-Karte testen/ersetzen und Dateisystem prüfen.",
        ),
    ),
    (
        "kernel panic",
        Finding(
            title="Kernel Panic",
            severity="critical",
            evidence="Kernel Panic gefunden",
            recommendation="Letzte Kernel-/Treiberänderungen zurücknehmen und Crash-Log analysieren.",
        ),
    ),
)


def analyze_log(log_text: str) -> list[Finding]:
    """Analyze log text and return matching findings.

    Matching is case-insensitive and returns de-duplicated findings in rule order.
    """

    haystack = log_text.lower()
    findings: list[Finding] = []
    seen_titles: set[str] = set()

    for needle, finding in _RULES:
        if needle in haystack and finding.title not in seen_titles:
            findings.append(finding)
            seen_titles.add(finding.title)

    return findings


def format_findings(findings: Iterable[Finding]) -> str:
    """Render findings to a simple textual report."""

    entries = list(findings)
    if not entries:
        return "Keine bekannten Probleme erkannt."

    lines = []
    for idx, finding in enumerate(entries, start=1):
        lines.extend(
            [
                f"{idx}. [{finding.severity.upper()}] {finding.title}",
                f"   Evidenz: {finding.evidence}",
                f"   Empfehlung: {finding.recommendation}",
            ]
        )
    return "\n".join(lines)

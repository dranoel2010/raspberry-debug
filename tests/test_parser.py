from raspberry_debug.parser import analyze_log, format_findings


def test_analyze_log_detects_multiple_findings_once() -> None:
    log = """
    random line
    Under-Voltage detected!
    MMC0: timeout waiting for hardware interrupt
    under-voltage detected
    """

    findings = analyze_log(log)

    assert [f.title for f in findings] == ["Unterspannung erkannt", "SD-Karten-Timeout"]


def test_format_findings_empty() -> None:
    assert format_findings([]) == "Keine bekannten Probleme erkannt."

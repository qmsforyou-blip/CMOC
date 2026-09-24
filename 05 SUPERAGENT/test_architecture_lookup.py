#!/usr/bin/env python3
"""Acceptance tests for ARCHITECTURE LOOKUP v0.4."""

from __future__ import annotations

import tempfile
from pathlib import Path

from architecture_lookup import lookup

def _write(root: Path, rel: str, text: str) -> None:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def _paths(result: dict, role: str) -> list[str]:
    return [item["path"] for item in result["artifacts"][role]]

def test_p9_positive_resolution() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _write(root, "05 SUPERAGENT/P9-PRODUCTION-E2E-RECOVERY-BOUNDARY-001.md", "# P9\nStatus: ACCEPTED\nThis is an integration boundary composed from existing runtime components.")
        _write(root, "05 SUPERAGENT/test_runtime_p9_production_e2e_recovery.py", "# P9 test")
        _write(root, "05 SUPERAGENT/p9_runtime.py", "# P9 implementation")
        _write(root, "05 SUPERAGENT/EVIDENCE-RUNTIME-P9-PRODUCTION-E2E-RECOVERY-001.md", "# Evidence\nStatus: ACCEPTED")
        result = lookup("P9", root)
        assert result["gaps"] == []
        assert result["summary"]["realization_mode"] == "COMPOSITE"
        assert all(_paths(result, role) for role in ("contract", "implementation", "test", "evidence"))

def test_p10_positive_resolution() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _write(root, "05 SUPERAGENT/P10-PRODUCTION-READINESS-GATE-001.md", "# P10 — PRODUCTION READINESS GATE\nStatus: ACCEPTED\nP10 is the final production-readiness gate.\nP10 is therefore an audit/gate, not another execution stage.\nREADY_WITH_LIMITATIONS")
        _write(root, "05 SUPERAGENT/test_p10_production_readiness_gate.py", "# P10 test")
        _write(root, "05 SUPERAGENT/p10_gate.py", "# P10 implementation")
        _write(root, "05 SUPERAGENT/EVIDENCE-RUNTIME-P10-PRODUCTION-READINESS-GATE-001.md", "# Evidence\nStatus: ACCEPTED")
        result = lookup("P10", root)
        assert result["gaps"] == []
        assert result["summary"]["realization_mode"] == "GATE"
        assert result["summary"]["evidence_count"] == 1
        # An unlabelled state is not proof of an actual gate result.
        assert result["artifacts"]["contract"][0]["observed_results"] == ()

def test_p7_multiple_evidence_is_allowed() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _write(root, "05 SUPERAGENT/P7-PRODUCTION-CMOC-WRITE-BOUNDARY-001.md", "# P7\nStatus: ACCEPTED")
        _write(root, "05 SUPERAGENT/production_cmoc_writer.py", "# P7 implementation")
        _write(root, "05 SUPERAGENT/test_p7_production_cmoc_write.py", "# P7 test")
        _write(root, "05 SUPERAGENT/EVIDENCE-P7-PRODUCTION-CMOC-WRITE-001.md", "# Evidence\nStatus: ACCEPTED")
        _write(root, "05 SUPERAGENT/EVIDENCE-RUNTIME-P7-PRODUCTION-CMOC-WRITE-001.md", "# Evidence\nStatus: ACCEPTED")
        result = lookup("P7", root)
        assert result["gaps"] == []
        assert result["summary"]["evidence_count"] == 2

def test_missing_role_is_reported_without_inference() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _write(root, "05 SUPERAGENT/P9-PRODUCTION-E2E-RECOVERY-BOUNDARY-001.md", "# P9\nStatus: ACCEPTED")
        result = lookup("P9", root)
        assert "MISSING_IMPLEMENTATION" in result["gaps"]
        assert "MISSING_TEST" in result["gaps"]
        assert "MISSING_EVIDENCE" in result["gaps"]

def test_subject_scope_rejects_cross_references() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _write(root, "05 SUPERAGENT/P7-PRODUCTION-CMOC-WRITE-BOUNDARY-001.md", "# P7 — PRODUCTION CMOC WRITE BOUNDARY\nStatus: DESIGN / ARCHITECTURE CANDIDATE")
        _write(root, "05 SUPERAGENT/P9-PRODUCTION-E2E-RECOVERY-BOUNDARY-001.md", "# P9\nThis references P7 as an upstream component.")
        _write(root, "05 SUPERAGENT/P9.1-RUNTIME-PRODUCTION-E2E-INTEGRATION-BOUNDARY-001.md", "# P9.1\nThis references P7.")
        _write(root, "05 SUPERAGENT/unrelated_review.md", "# Review\nP7 is mentioned here but is not the subject.")
        result = lookup("P7", root)
        paths = _paths(result, "contract")
        assert "05 SUPERAGENT/P7-PRODUCTION-CMOC-WRITE-BOUNDARY-001.md" in paths
        assert "05 SUPERAGENT/P9-PRODUCTION-E2E-RECOVERY-BOUNDARY-001.md" not in paths
        assert "05 SUPERAGENT/P9.1-RUNTIME-PRODUCTION-E2E-INTEGRATION-BOUNDARY-001.md" not in paths
        assert "05 SUPERAGENT/unrelated_review.md" not in paths


def test_status_is_not_collected_from_body_mentions() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _write(root, "05 SUPERAGENT/P7-PRODUCTION-CMOC-WRITE-BOUNDARY-001.md", "# P7\nStatus: DESIGN / ARCHITECTURE CANDIDATE\nThe evidence is NOT ACCEPTED in another scenario.\nMISSING is not the current state.")
        result = lookup("P7", root)
        artifact = result["artifacts"]["contract"][0]
        assert artifact["status"] == ("DESIGN / ARCHITECTURE CANDIDATE",)
        assert artifact["observed_results"] == ()


def test_read_only_and_deterministic_shape() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _write(root, "05 SUPERAGENT/P7-PRODUCTION-CMOC-WRITE-BOUNDARY-001.md", "# P7\nStatus: ACCEPTED")
        before = sorted(str(p.relative_to(root)) for p in root.rglob("*"))
        first = lookup("P7", root)
        second = lookup("P7", root)
        after = sorted(str(p.relative_to(root)) for p in root.rglob("*"))
        assert before == after
        assert first["artifacts"] == second["artifacts"]
        assert first["gaps"] == second["gaps"]

def test_realistic_ownership_and_modes() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _write(root, "P7-WRITE-BOUNDARY.md", "# P7 write\n**Status:** DESIGN / ARCHITECTURE CANDIDATE\nP10 is a readiness gate.")
        _write(root, "P9-RECOVERY-BOUNDARY.md", "# P9 recovery\n**Status:** ACCEPTED\nP9 binds the following previously accepted boundaries:\n- P7\n- P8")
        _write(root, "P9.1-INTEGRATION-BOUNDARY.md", "# P9.1\nRealization mode: GATE")
        _write(root, "P10-READINESS-GATE.md", "# P10 — PRODUCTION READINESS GATE\n**Status:** DESIGN / ARCHITECTURE CANDIDATE\n## States\n- READY_WITH_LIMITATIONS\n- NOT_READY")
        _write(root, "PROD-001-RUNTIME-BOUNDARY.md", "# PROD-001\nP7 is a readiness gate.\nP9 is a readiness gate.")
        _write(root, "POST-P10-ARCHITECTURE-REVIEW.md", "# POST-P10\nRealization mode: COMPOSITE")
        _write(root, "production_cmoc_writer.py", '\"\"\"P7 production CMOC writer.\"\"\"\nclass Result:\n    status: str\n')
        _write(root, "unrelated.py", 'x = 1\n# P7 implementation\n')
        for subject, expected in (("P7", "DIRECT"), ("P9", "COMPOSITE"), ("P10", "GATE")):
            result = lookup(subject, root)
            assert result["summary"]["realization_mode"] == expected
            assert result["summary"]["contract_count"] == 1
        assert _paths(lookup("P7", root), "implementation") == ["production_cmoc_writer.py"]
        assert lookup("P7", root)["artifacts"]["implementation"][0]["status"] == ()
        assert lookup("P10", root)["artifacts"]["contract"][0]["observed_results"] == ()


def test_exact_status_and_actual_results() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _write(root, "EVIDENCE-P10-001.md", "# Evidence\n**Status:** TESTED / NOT ACCEPTED\n**Result:** READY_WITH_LIMITATIONS\n## Possible states\n- NOT_READY\n- EVIDENCE_INCOMPLETE\n## Example\n```text\nStatus: ACCEPTED\nResult: NOT_READY\n```\n")
        item = lookup("P10", root)["artifacts"]["evidence"][0]
        assert item["status"] == ("TESTED / NOT ACCEPTED",)
        assert item["observed_results"] == ("READY_WITH_LIMITATIONS",)
        _write(root, "EVIDENCE-RUNTIME-P10-002.md", "# Evidence\n**Status:** ACCEPTED\n## 1. Result\n```text\nstatus: READY_WITH_LIMITATIONS\n```\nEvidence status: ACCEPTED.\n")
        items = lookup("P10", root)["artifacts"]["evidence"]
        assert all(item["observed_results"] == ("READY_WITH_LIMITATIONS",) for item in items)
        assert items[1]["status"] == ("ACCEPTED",)


def test_ambiguities_are_not_hidden() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _write(root, "P9-A-BOUNDARY.md", "# P9\nStatus: ACCEPTED\nStatus: DESIGN / ARCHITECTURE CANDIDATE\nRealization mode: GATE")
        _write(root, "P9-B-BOUNDARY.md", "# P9\nRealization mode: COMPOSITE")
        result = lookup("P9", root)
        assert result["summary"]["realization_mode"] is None
        assert "AMBIGUOUS_CONTRACT" in result["gaps"]
        assert "AMBIGUOUS_STATUS" in result["gaps"]
        assert "MISSING_IMPLEMENTATION" in result["gaps"]
        assert "SCOPE_INSUFFICIENT" in lookup("P99", root)["gaps"]


if __name__ == "__main__":
    tests = [value for name, value in sorted(globals().items()) if name.startswith("test_") and callable(value)]
    for test in tests:
        test()
    print(f"ARCHITECTURE LOOKUP ACCEPTANCE: PASS ({len(tests)} tests)")

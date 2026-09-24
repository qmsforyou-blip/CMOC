#!/usr/bin/env python3
"""Acceptance tests for ARCHITECTURE LOOKUP v0.2."""

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

if __name__ == "__main__":
    test_p9_positive_resolution()
    test_p10_positive_resolution()
    test_p7_multiple_evidence_is_allowed()
    test_missing_role_is_reported_without_inference()
    test_read_only_and_deterministic_shape()
    print("ARCHITECTURE LOOKUP ACCEPTANCE: PASS")

"""M07 must not accept a relation citing absent or mismatched evidence."""

import unittest
import json
import tempfile
from pathlib import Path
from unittest.mock import patch

from m07_llm import M07LLMError, build_relation_candidates
from run_superagent import load_source_package


class RelationEvidenceGuardTest(unittest.TestCase):
    def test_full_run_rejects_unbound_evidence_before_llm(self):
        with tempfile.TemporaryDirectory() as tmp:
            package = Path(tmp) / "package.json"
            package.write_text(json.dumps({"package_id": "X", "source_id": "SRC-X",
                "source_name": "X", "fragments": [{"location": "p1", "text": "X"}],
                "source_package_status": "PARTIAL", "relation_evidence": []}), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "REQUIRES_PERSISTED_RUN"):
                load_source_package(str(package))

    def test_rejects_missing_or_wrong_endpoint_evidence(self):
        passports = [{"id": x, "source_id": "SRC-TEST"} for x in ("PAS-001", "PAS-002", "PAS-003")]
        result = {"evaluated_scope": [p["id"] for p in passports], "records": [{
            "id": "REL-001", "source_id": "SRC-TEST",
            "from_passport_id": "PAS-001", "to_passport_id": "PAS-003",
            "relation_type": "PART_OF", "status": "RELATION_CANDIDATE",
            "epistemic_status": "PROVISIONAL", "basis_refs": ["EVID-001"],
            "evidence_gap": None,
        }]}
        evidence = [{"evidence_id": "EVID-001", "supports": ["PAS-001", "PAS-002"]}]
        with patch("m07_llm._request_json", return_value=result):
            with self.assertRaisesRegex(M07LLMError, "both endpoints"):
                build_relation_candidates(passports, evidence)
            with self.assertRaisesRegex(M07LLMError, "unavailable evidence"):
                build_relation_candidates(passports, [])


if __name__ == "__main__":
    unittest.main()

"""Source-bound relation evidence must bind only to current-run passports."""

import unittest
from unittest.mock import patch

from machine_source_001 import MachineSource001Superagent, bind_relation_evidence
from m07_llm import M07LLMError, build_relation_candidates


class RelationEvidenceHandoffTest(unittest.TestCase):
    def setUp(self):
        self.text = "Manager A reports to the weekly review of stream B."
        self.source = {
            "package_id": "SOURCE-TEST",
            "source_id": "SRC-TEST",
            "fragments": [{"location": "p6", "text": self.text}],
            "relation_evidence": [{
                "evidence_id": "EVID-001", "location": "p6", "text": self.text,
                "supports_terms": ["Manager A", "Weekly review B"],
            }],
        }
        self.passports = [
            {"id": "PAS-001", "term": "Manager A", "source_id": "SRC-TEST"},
            {"id": "PAS-002", "term": "Weekly review B", "source_id": "SRC-TEST"},
        ]

    def test_passes_bound_evidence_to_existing_m07(self):
        runner = MachineSource001Superagent(self.source)
        batch = runner.new_batch("SRC-TEST", "M07", "test")
        inp = {"records": self.passports, "traceability": {"source_package": "SOURCE-TEST"}}
        with patch("machine_source_001.build_relation_candidates", return_value=[]) as m07:
            result = runner._m07_with_evidence(inp, batch)
        evidence = m07.call_args.args[1]
        self.assertEqual(evidence[0]["supports"], ["PAS-001", "PAS-002"])
        self.assertEqual(result["relation_evidence"], evidence)

    def test_rejects_stale_or_unsupported_binding(self):
        for change in (
            {"supports_terms": ["Manager A", "Missing passport"]},
            {"text": "Unrelated text"},
            {"location": "another page"},
        ):
            source = {**self.source, "relation_evidence": [{**self.source["relation_evidence"][0], **change}]}
            with self.subTest(change=change), self.assertRaises(ValueError):
                bind_relation_evidence(source, self.passports)

    def test_default_remains_no_evidence(self):
        source = {**self.source, "relation_evidence": []}
        self.assertEqual(bind_relation_evidence(source, self.passports), [])

    def test_m07_rejects_relation_with_missing_or_wrong_endpoint_evidence(self):
        third = {"id": "PAS-003", "term": "Other", "source_id": "SRC-TEST"}
        records = self.passports + [third]
        result = {"evaluated_scope": [p["id"] for p in records], "records": [{
            "id": "REL-001", "source_id": "SRC-TEST",
            "from_passport_id": "PAS-001", "to_passport_id": "PAS-003",
            "relation_type": "PART_OF", "status": "RELATION_CANDIDATE",
            "epistemic_status": "PROVISIONAL", "basis_refs": ["EVID-001"],
            "evidence_gap": None,
        }]}
        evidence = bind_relation_evidence(self.source, records)
        with patch("m07_llm._request_json", return_value=result):
            with self.assertRaisesRegex(M07LLMError, "both endpoints"):
                build_relation_candidates(records, evidence)
            with self.assertRaisesRegex(M07LLMError, "unavailable evidence"):
                build_relation_candidates(records, [])


if __name__ == "__main__":
    unittest.main()

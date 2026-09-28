import json
import sqlite3
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from pilot_003_m08_probe import probe


class ReviewedM08ProbeTest(unittest.TestCase):
    def test_validates_reviewed_subset_and_never_writes_run(self):
        fragment = {"location": "p6", "text": "A weekly meeting reviews measures and problems."}
        original = {"package_id": "SOURCE-OLD", "source_id": "SRC-005", "fragments": [fragment]}
        controlled = {"package_id": "SOURCE-NEW", "source_id": "SRC-005", "fragments": [fragment],
            "relation_evidence": [
                {"evidence_id": "EVID-2", "location": "p6", "text": fragment["text"]},
                {"evidence_id": "EVID-3", "location": "p6", "text": fragment["text"]},
            ]}
        passports = [{"id": f"PAS-00{i}", "source_id": "SRC-005", "term": f"term-{i}",
                      "working_class": "ACTIVITY", "source_basis": [f"FORM-{i:03d}"]}
                     for i in range(1, 5)]
        binding = {"run_id": "RUN-003", "source_id": "SRC-005", "source_package_id": "SOURCE-OLD",
            "evidence_package_id": "SOURCE-NEW",
            "passports": {p["id"]: {"working_class": p["working_class"], "source_basis": p["source_basis"]}
                          for p in passports},
            "evidence_pairs": {"EVID-2": ["PAS-002", "PAS-003"],
                               "EVID-3": ["PAS-002", "PAS-004"]}}
        transcript = {"run_id": "RUN-003", "source_id": "SRC-005",
            "source_package_id": "SOURCE-OLD", "evidence_package_id": "SOURCE-NEW",
            "excluded_relation": {"id": "REL-001", "reason": "type unresolved"},
            "records": [{"id": f"REL-00{i}", "source_id": "SRC-005",
                         "from_passport_id": f"PAS-00{i+1}", "to_passport_id": "PAS-002",
                         "relation_type": "ACTIVITY_OCCURS_WITHIN_ACTIVITY",
                         "status": "RELATION_CANDIDATE", "epistemic_status": "PROVISIONAL",
                         "basis_refs": [f"EVID-{i}"], "evidence_gap": None}
                        for i in (2, 3)]}
        discovery = {"discovery": {"source_package_id": "SOURCE-OLD",
            "results": [{"type": "PASSPORT_RECORDS", "source_id": "SRC-005", "records": passports}]}}
        with tempfile.TemporaryDirectory() as tmp:
            db = Path(tmp) / "run.sqlite"
            with sqlite3.connect(db) as conn:
                conn.execute("CREATE TABLE adapter_results (run_id TEXT, stage_id TEXT, payload_json TEXT)")
                conn.execute("INSERT INTO adapter_results VALUES (?, ?, ?)",
                             ("RUN-003", "DISCOVERY", json.dumps(discovery)))
            before = db.read_bytes()
            with patch("pilot_003_m08_probe.decide") as no_llm:
                checked = probe(db, "RUN-003", original, controlled, binding, transcript, validate_only=True)
            no_llm.assert_not_called()
            self.assertEqual(checked["status"], "M08_INPUT_VALIDATED")
            with patch("pilot_003_m08_probe.decide", return_value={"records": []}) as m08:
                output = probe(db, "RUN-003", original, controlled, binding, transcript)
            self.assertEqual([r["id"] for r in m08.call_args.args[1]], ["REL-002", "REL-003"])
            self.assertEqual(output["status"], "READ_ONLY_M08_PROBE")
            self.assertEqual(db.read_bytes(), before)
            wrong = {**transcript, "records": [{**transcript["records"][0], "to_passport_id": "PAS-001"},
                                                transcript["records"][1]]}
            with self.assertRaisesRegex(ValueError, "ENDPOINT_MISMATCH"):
                probe(db, "RUN-003", original, controlled, binding, wrong, validate_only=True)


if __name__ == "__main__":
    unittest.main()

import json
import sqlite3
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from pilot_003_relation_probe import inspect


class PersistedRelationProbeTest(unittest.TestCase):
    def test_reuses_passports_without_mutating_database(self):
        fragment = {"location": "p6", "text": "Manager meets team weekly."}
        original = {"package_id": "SOURCE-OLD", "source_id": "SRC-005", "fragments": [fragment]}
        controlled = {
            "package_id": "SOURCE-NEW", "source_id": "SRC-005", "fragments": [fragment],
            "relation_evidence": [{"evidence_id": "EVID-001", "location": "p6",
                                   "text": fragment["text"], "supports_terms": ["old wording", "old wording B"]}],
        }
        passports = [{"id": "PAS-001", "term": "New wording A", "source_id": "SRC-005", "working_class": "ROLE", "source_basis": ["FORM-001"]},
                     {"id": "PAS-002", "term": "New wording B", "source_id": "SRC-005", "working_class": "ACTIVITY", "source_basis": ["FORM-002"]}]
        binding = {"run_id": "RUN-003", "source_id": "SRC-005", "source_package_id": "SOURCE-OLD",
                   "evidence_package_id": "SOURCE-NEW", "passports": {
                       "PAS-001": {"working_class": "ROLE", "source_basis": ["FORM-001"]},
                       "PAS-002": {"working_class": "ACTIVITY", "source_basis": ["FORM-002"]}},
                   "evidence_pairs": {"EVID-001": ["PAS-001", "PAS-002"]}}
        result = {"discovery": {"source_package_id": "SOURCE-OLD", "results": [
            {"type": "PASSPORT_RECORDS", "source_id": "SRC-005", "records": passports}
        ]}}
        with tempfile.TemporaryDirectory() as tmp:
            db = Path(tmp) / "run.sqlite"
            with sqlite3.connect(db) as conn:
                conn.execute("CREATE TABLE adapter_results (run_id TEXT, stage_id TEXT, payload_json TEXT)")
                conn.execute("INSERT INTO adapter_results VALUES (?, ?, ?)",
                             ("RUN-003", "DISCOVERY", json.dumps(result)))
            before = db.read_bytes()
            with patch("pilot_003_relation_probe.build_relation_candidates", return_value=[]) as m07:
                output = inspect(db, "RUN-003", original, controlled, binding)
            self.assertEqual(m07.call_args.args[1][0]["supports"], ["PAS-001", "PAS-002"])
            self.assertEqual(output["status"], "READ_ONLY_RELATION_PROBE")
            self.assertEqual(db.read_bytes(), before)
            with patch("pilot_003_relation_probe.build_relation_candidates") as no_llm:
                checked = inspect(db, "RUN-003", original, controlled, binding, validate_only=True)
            no_llm.assert_not_called()
            self.assertEqual(checked["status"], "RUN_BINDING_VALIDATED")

            for changed in (
                {**binding, "run_id": "OTHER-RUN"},
                {**binding, "evidence_pairs": {"EVID-001": ["PAS-001", "PAS-999"]}},
                {**binding, "passports": {**binding["passports"], "PAS-001": {"working_class": "ROLE", "source_basis": ["FORM-999"]}}},
            ):
                with self.subTest(changed=changed), self.assertRaises(ValueError):
                    inspect(db, "RUN-003", original, controlled, changed)
            self.assertEqual(db.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()

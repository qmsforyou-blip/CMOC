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
                                   "text": fragment["text"], "supports_terms": ["A", "B"]}],
        }
        passports = [{"id": "PAS-001", "term": "A"}, {"id": "PAS-002", "term": "B"}]
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
                output = inspect(db, "RUN-003", original, controlled)
            self.assertEqual(m07.call_args.args[1][0]["supports"], ["PAS-001", "PAS-002"])
            self.assertEqual(output["status"], "READ_ONLY_RELATION_PROBE")
            self.assertEqual(db.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()

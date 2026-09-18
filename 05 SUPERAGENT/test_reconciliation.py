import unittest
from pathlib import Path

from cmoc_query import load_index
from reconciliation import reconcile


BASE = Path(__file__).parent


class TestReconciliation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index = load_index(BASE / "cmoc_query_index.json")

    def test_existing_equivalent(self):
        records = [{
            "record_id": "NOM-TEST-001",
            "value": "Управляемость",
            "target_object_type": "TERM",
            "traceability": "SRC-TEST:p1",
        }]
        r = reconcile(self.index, "SRC-TEST", "BATCH-TEST-001",
                      "NOMENCLATURE", records, ["TERMS"])
        self.assertEqual(r[0]["match_result"], "EXISTING_EQUIVALENT")
        self.assertEqual(r[0]["cmoc_object_id"], "T-0001")

    def test_source_candidate_not_declared_new(self):
        records = [{
            "record_id": "NOM-TEST-002",
            "value": "FAST_RESPONSE",
            "target_object_type": "TERM",
            "traceability": "SRC-002:p2",
        }]
        r = reconcile(self.index, "SRC-002", "BATCH-SRC-002-REC-001",
                      "NOMENCLATURE", records, ["TERMS"])
        self.assertEqual(r[0]["match_result"], "NEEDS_REVIEW")
        self.assertIsNone(r[0]["cmoc_object_id"])

    def test_structural_candidate_needs_review(self):
        records = [{
            "record_id": "NOM-TEST-003",
            "value": "Организационная",
            "target_object_type": "TERM",
            "traceability": "SRC-TEST:p1",
        }]
        r = reconcile(self.index, "SRC-TEST", "BATCH-TEST-002",
                      "NOMENCLATURE", records, ["TERMS"])
        self.assertEqual(r[0]["match_result"], "NEEDS_REVIEW")
        self.assertIsNotNone(r[0]["cmoc_object_id"])

    def test_traceability_survives(self):
        records = [{
            "record_id": "NOM-TEST-004",
            "value": "FAST_RESPONSE",
            "target_object_type": "TERM",
            "traceability": "SRC-002:BATCH-SRC-002-M04-001:NOM-001",
        }]
        r = reconcile(self.index, "SRC-002", "BATCH-SRC-002-M04-001",
                      "NOMENCLATURE", records, ["TERMS"])
        self.assertEqual(r[0]["traceability"],
                         "SRC-002:BATCH-SRC-002-M04-001:NOM-001")


if __name__ == "__main__":
    unittest.main()

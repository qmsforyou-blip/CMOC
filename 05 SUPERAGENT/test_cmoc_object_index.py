import json
import unittest
from pathlib import Path

BASE = Path(__file__).parent
INDEX = BASE / "cmoc_object_index.json"

FORBIDDEN = {
    "semantic_summary", "definition", "interpretation", "meaning",
    "semantic_similarity", "equivalence", "conflict",
    "reconciliation_decision", "canonical_status",
    "NEW", "EXISTING_EQUIVALENT", "EXISTING_RELATED", "NEEDS_REVIEW",
}

class TestCMOCObjectIndexV02(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(INDEX.read_text(encoding="utf-8"))

    def test_schema_and_version(self):
        self.assertEqual(self.data["schema"], "CMOC-OBJECT-INDEX-001")
        self.assertEqual(self.data["version"], "0.2")
        self.assertEqual(self.data["source_inventory"], "CMOC-INVENTORY-001@2026-09-18")

    def test_representation_count(self):
        self.assertEqual(
            self.data["representation_record_count"],
            len(self.data["records"]),
        )
        self.assertEqual(
            self.data["representation_kind_counts"]["OBJECT_FILE"], 732
        )
        self.assertEqual(
            self.data["representation_kind_counts"]["REGISTRY_RECORD"], 669
        )

    def test_expected_object_classes(self):
        expected = {
            "TERM", "DISTINCTION", "GM_FORMULATION", "MACHINE",
            "PATTERN", "CHAIN", "LAW", "OBSERVATION",
            "ORGANIZATIONAL_CONSTRUCTION", "INVARIANT",
        }
        self.assertTrue(expected.issubset(self.data["object_type_counts"]))

    def test_representation_contract(self):
        allowed = {"OBJECT_FILE", "REGISTRY_RECORD", "OTHER_ADDRESSABLE"}
        for r in self.data["records"]:
            self.assertIn(r["representation"]["kind"], allowed)
            self.assertTrue(r["representation"]["container"])
            self.assertTrue(r["representation"]["location"] is not None)
            self.assertTrue(r["provenance"]["repository"])
            self.assertTrue(r["provenance"]["git_sha"])
            self.assertTrue(r["provenance"]["inventory_snapshot"])
            self.assertIn(r["count_basis"], {
                "OBJECT_FILE", "REGISTRY_RECORD",
                "OTHER_ADDRESSABLE", "UNKNOWN"
            })

    def test_duplicate_object_ids_are_allowed(self):
        ids = [r["object_id"] for r in self.data["records"]]
        self.assertLess(len(set(ids)), len(ids))

    def test_no_semantic_payload(self):
        def walk(v):
            if isinstance(v, dict):
                for k, value in v.items():
                    self.assertNotIn(k, FORBIDDEN)
                    walk(value)
            elif isinstance(v, list):
                for value in v:
                    walk(value)
        walk(self.data)

    def test_index_is_read_only_artifact(self):
        self.assertIn("Read-only", self.data["purpose"])
        self.assertIn("No semantic reconciliation", self.data["purpose"])

if __name__ == "__main__":
    unittest.main()

import json
import tempfile
import unittest
from pathlib import Path

from cmoc_query import load_object_index, query

BASE = Path(__file__).parent


class TestCMOCQueryV03(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records = load_object_index(BASE / "cmoc_object_index.json")

    def test_q001_exact_term(self):
        r = query(self.records, "Q-001", "EXACT", "TERM", "T-0001", ["TERMS"])
        self.assertEqual(r["match_status"], "MATCH")
        self.assertEqual(r["results"][0]["object_id"], "T-0001")

    def test_q002_exact_distinction(self):
        r = query(self.records, "Q-002", "EXACT", "DISTINCTION", "DIS-000001", ["DISTINCTIONS"])
        self.assertEqual(r["match_status"], "MATCH")
        self.assertEqual(r["results"][0]["object_id"], "DIS-000001")

    def test_q003_duplicate_physical_representations_preserved(self):
        r = query(
            self.records, "Q-003", "EXACT", "DISTINCTION", "DIS-0155", ["DISTINCTIONS"]
        )
        self.assertEqual(r["match_status"], "AMBIGUOUS")
        self.assertEqual(len(r["results"]), 2)
        addresses = {
            (x["representation"]["container"], x["representation"]["location"]["line"])
            for x in r["results"]
        }
        self.assertEqual(addresses, {
            ("08 CMOC Core/LAB-002 Реестр различений.md", 1473),
            ("08 CMOC Core/LAB-002 Реестр различений.md", 1501),
        })

    def test_q004_unknown_name_preserved(self):
        r = query(self.records, "Q-004", "EXACT", "INVARIANT", "INV-0009", ["INVARIANTS"])
        self.assertEqual(r["match_status"], "MATCH")
        self.assertEqual(r["results"][0]["object_id"], "INV-0009")
        self.assertIsNone(
            self.records[
                next(i for i, x in enumerate(self.records) if x["object_id"] == "INV-0009")
            ]["object_name"]
        )
        self.assertIsNone(r["results"][0]["representation"].get("object_name"))

    def test_q005_scope_insufficient(self):
        r = query(
            self.records, "Q-005", "EXACT", "MACHINE", "MC-CAND-096-01", ["TERMS"]
        )
        self.assertEqual(r["match_status"], "SCOPE_INSUFFICIENT")
        self.assertEqual(r["results"], [])

    def test_q006_no_match_is_not_new(self):
        r = query(
            self.records, "Q-006", "EXACT", "TERM", "TERM-NOT-IN-CMOC", ["TERMS"]
        )
        self.assertEqual(r["match_status"], "NO_MATCH")
        self.assertEqual(r["results"], [])
        self.assertNotIn("NEW", json.dumps(r, ensure_ascii=False))

    def test_q007_structural_candidate(self):
        r = query(
            self.records,
            "Q-007",
            "STRUCTURAL",
            "TERM",
            {"fields_present": ["id", "name"]},
            ["TERMS"],
        )
        self.assertEqual(r["match_status"], "CANDIDATE")
        self.assertTrue(r["results"])
        self.assertTrue(all(x["match_status"] == "CANDIDATE" for x in r["results"]))

    def test_q008_read_only(self):
        index_path = BASE / "cmoc_object_index.json"
        before = index_path.read_bytes()
        query(self.records, "Q-008", "EXACT", "TERM", "T-0001", ["TERMS"])
        after = index_path.read_bytes()
        self.assertEqual(before, after)

    def test_result_contract(self):
        r = query(self.records, "Q-CONTRACT", "EXACT", "TERM", "T-0001", ["TERMS"])
        result = r["results"][0]
        for key in (
            "object_id",
            "object_type",
            "match_mode",
            "match_status",
            "match_basis",
            "indexed_attributes",
            "representation",
            "traceability",
        ):
            self.assertIn(key, result)

    def test_load_rejects_wrong_index(self):
        with tempfile.NamedTemporaryFile("w", suffix=".json", encoding="utf-8") as f:
            json.dump({"objects": []}, f)
            f.flush()
            with self.assertRaises(ValueError):
                load_object_index(f.name)


if __name__ == "__main__":
    unittest.main()

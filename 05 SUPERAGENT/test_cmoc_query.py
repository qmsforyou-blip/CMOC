import json
import unittest
from pathlib import Path

from cmoc_query import load_index, query


BASE = Path(__file__).parent


class TestCMOCQuery(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index = load_index(BASE / "cmoc_query_index.json")

    def test_exact_existing_term(self):
        r = query(self.index, "Q-001", "EXACT", "TERM", "Управляемость", ["TERMS"])
        self.assertEqual(r["match_status"], "MATCH")
        self.assertEqual(r["results"][0]["object_id"], "T-0001")

    def test_exact_existing_by_id(self):
        r = query(self.index, "Q-002", "EXACT", "TERM", "T-0002", ["TERMS"])
        self.assertEqual(r["match_status"], "MATCH")

    def test_exact_new_candidate(self):
        r = query(self.index, "Q-003", "EXACT", "TERM", "FAST_RESPONSE", ["TERMS"])
        self.assertEqual(r["match_status"], "NO_MATCH")
        self.assertEqual(r["results"], [])

    def test_structural_candidate(self):
        r = query(self.index, "Q-004", "STRUCTURAL", "TERM", "организационная", ["TERMS"])
        self.assertEqual(r["match_status"], "CANDIDATE")
        self.assertTrue(r["results"])

    def test_scope_insufficient(self):
        r = query(self.index, "Q-005", "EXACT", "DISTINCTION", "Управляемость", ["TERMS"])
        self.assertEqual(r["match_status"], "SCOPE_INSUFFICIENT")

    def test_query_is_read_only(self):
        before = (BASE / "cmoc_query_index.json").read_bytes()
        query(self.index, "Q-006", "EXACT", "TERM", "Решение", ["TERMS"])
        after = (BASE / "cmoc_query_index.json").read_bytes()
        self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main()

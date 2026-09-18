import unittest
from pathlib import Path
from cmoc_query import load_objects, query

BASE=Path(__file__).parent

class TestCMOCQueryV02(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.inventory,cls.objects=load_objects(BASE/"cmoc_inventory.json")

    def test_exact_term(self):
        r=query(self.objects,"Q-001","EXACT","TERM","T-0001",["TERMS"])
        self.assertEqual(r["match_status"],"MATCH")
        self.assertEqual(r["results"][0]["object_id"],"T-0001")

    def test_exact_machine(self):
        r=query(cls.objects,"Q-002","EXACT","MACHINE","MC-CAND-096-01",["MACHINES"])
        self.assertEqual(r["match_status"],"MATCH")

    def test_structural_distinction(self):
        r=query(cls.objects,"Q-003","STRUCTURAL","DISTINCTION","решение",["DISTINCTIONS"])
        self.assertEqual(r["match_status"],"CANDIDATE")
        self.assertTrue(r["results"])

    def test_scope_insufficient(self):
        r=query(cls.objects,"Q-004","EXACT","MACHINE","MC-CAND-096-01",["TERMS"])
        self.assertEqual(r["match_status"],"SCOPE_INSUFFICIENT")

    def test_no_match_is_not_new(self):
        r=query(cls.objects,"Q-005","EXACT","TERM","TERM-NOT-IN-CMOC",["TERMS"])
        self.assertEqual(r["match_status"],"NO_MATCH")
        self.assertEqual(r["results"],[])

    def test_traceability(self):
        r=query(cls.objects,"Q-006","EXACT","TERM","T-0001",["TERMS"])
        self.assertIn("traceability",r["results"][0])
        self.assertEqual(r["results"][0]["traceability"]["inventory_schema"],"CMOC-INVENTORY-001")

if __name__=="__main__": unittest.main()

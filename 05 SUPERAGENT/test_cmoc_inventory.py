import json
import unittest
from pathlib import Path


class CMOCInventoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        path = Path(__file__).with_name("cmoc_inventory.json")
        cls.inventory = json.loads(path.read_text(encoding="utf-8"))

    def test_inventory_schema_and_snapshot(self):
        inv = self.inventory
        self.assertEqual(inv["schema"], "CMOC-INVENTORY-001")
        self.assertEqual(inv["version"], "0.1")
        self.assertEqual(inv["repository"], "qmsforyou-blip/CMOC")
        self.assertEqual(inv["branch"], "main")
        self.assertEqual(len(inv["records"]), 1303)

    def test_key_object_counts(self):
        counts = self.inventory["object_counts"]
        self.assertEqual(counts["TERM"], 125)
        self.assertEqual(counts["DISTINCTION"], 544)
        self.assertEqual(counts["GM_FORMULATION"], 49)
        self.assertEqual(counts["MACHINE"], 8)
        self.assertEqual(counts["PATTERN"], 1)
        self.assertEqual(counts["CHAIN"], 2)

    def test_paths_are_unique(self):
        paths = [r["path"] for r in self.inventory["records"]]
        self.assertEqual(len(paths), len(set(paths)))

    def test_required_metadata_present(self):
        for record in self.inventory["records"]:
            self.assertIn("path", record)
            self.assertIn("class", record)
            self.assertIn("size_bytes", record)
            self.assertIn("git_sha", record)


if __name__ == "__main__":
    unittest.main()

import json
import unittest
import subprocess
import hashlib
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class CMOCInventoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        path = Path(__file__).with_name("cmoc_inventory.json")
        cls.inventory = json.loads(path.read_text(encoding="utf-8"))

    def test_inventory_schema_and_snapshot(self):
        inv = self.inventory
        self.assertEqual(inv["schema"], "CMOC-INVENTORY-001")
        self.assertEqual(inv["version"], "0.3")
        self.assertEqual(inv["repository"], "qmsforyou-blip/CMOC")
        self.assertEqual(inv["branch"], subprocess.check_output(["git", "branch", "--show-current"], cwd=ROOT, text=True).strip())
        self.assertEqual(inv["source_commit"], subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip())
        self.assertTrue(inv["generated_at"])
        self.assertTrue(inv["records"])

    def test_key_object_counts(self):
        records = self.inventory["records"]
        self.assertEqual(self.inventory["object_counts"], dict(Counter(r["object_type"] for r in records if r.get("object_type"))))
        self.assertEqual(self.inventory["file_class_counts"], dict(Counter(r["class"] for r in records)))
        self.assertTrue({"TERM", "DISTINCTION", "GM_FORMULATION", "MACHINE", "PATTERN", "CHAIN"}.issubset(self.inventory["object_counts"]))

    def test_all_source_files_are_accounted_for(self):
        tracked = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT).decode("utf-8").split("\0")
        derived = {"05 SUPERAGENT/cmoc_inventory.json", "05 SUPERAGENT/cmoc_object_index.json"}
        expected = {p for p in tracked if p and p not in derived and (ROOT / p).is_file()}
        recorded = {r["path"] for r in self.inventory["records"]}
        errors = self.inventory["structural_errors"]
        self.assertEqual(expected, recorded | {e["path"] for e in errors})
        for error in errors:
            self.assertTrue(error["type"])
            self.assertIn(error["path"], expected)

    def test_paths_are_unique(self):
        paths = [r["path"] for r in self.inventory["records"]]
        self.assertEqual(len(paths), len(set(paths)))

    def test_required_metadata_present(self):
        for record in self.inventory["records"]:
            self.assertIn("path", record)
            self.assertIn("class", record)
            self.assertIn("size_bytes", record)
            self.assertIn("git_sha", record)
            data = (ROOT / record["path"]).read_bytes()
            self.assertEqual(record["size_bytes"], len(data))
            self.assertEqual(record["git_sha"], hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest())


if __name__ == "__main__":
    unittest.main()

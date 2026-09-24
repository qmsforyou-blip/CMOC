import json
import unittest
from collections import Counter
from pathlib import Path

BASE = Path(__file__).parent
INDEX = BASE / "cmoc_object_index.json"
INVENTORY = BASE / "cmoc_inventory.json"

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
        cls.inventory = json.loads(INVENTORY.read_text(encoding="utf-8"))
        cls.inventory_by_path = {
            item["path"]: item["git_sha"] for item in cls.inventory["records"]
        }

    def test_schema_and_version(self):
        self.assertEqual(self.data["schema"], "CMOC-OBJECT-INDEX-001")
        self.assertEqual(self.data["version"], "0.2")
        self.assertEqual(self.data["source_inventory"], f'{self.inventory["schema"]}@{self.inventory["generated_at"]}')
        for key in ("repository", "branch", "source_commit", "generated_at"):
            self.assertEqual(self.data[key], self.inventory[key])

    def test_representation_count(self):
        self.assertEqual(
            self.data["representation_record_count"],
            len(self.data["records"]),
        )
        records = self.data["records"]
        expected = Counter(r["representation"]["kind"] for r in records)
        self.assertEqual(self.data["representation_kind_counts"], {
            kind: expected[kind] for kind in ("OBJECT_FILE", "REGISTRY_RECORD", "OTHER_ADDRESSABLE")
        })
        expected_paths = {r["path"] for r in self.inventory["records"] if r.get("object_type")}
        indexed_paths = {r["representation"]["container"] for r in records if r["representation"]["kind"] == "OBJECT_FILE"}
        self.assertEqual(indexed_paths, expected_paths)
        self.assertEqual(expected["OBJECT_FILE"], len(expected_paths))

    def test_expected_object_classes(self):
        expected = {
            "TERM", "DISTINCTION", "GM_FORMULATION", "MACHINE",
            "PATTERN", "CHAIN", "LAW", "OBSERVATION",
            "ORGANIZATIONAL_CONSTRUCTION", "INVARIANT",
        }
        self.assertTrue(expected.issubset(self.data["object_type_counts"]))

    def test_count_views(self):
        records = self.data["records"]
        expected = {}
        for object_type in {r["object_type"] for r in records}:
            selected = [r for r in records if r["object_type"] == object_type]
            expected[object_type] = {
                "representations": len(selected),
                "object_files": sum(r["representation"]["kind"] == "OBJECT_FILE" for r in selected),
                "registry_records": sum(r["representation"]["kind"] == "REGISTRY_RECORD" for r in selected),
                "unique_object_ids": len({r["object_id"] for r in selected}),
            }
        self.assertEqual(self.data["count_views"]["by_object_type"], expected)
        self.assertEqual(self.data["object_type_counts"], dict(Counter(r["object_type"] for r in records)))
        self.assertEqual(self.data["count_views"]["unique_object_ids"], len({r["object_id"] for r in records}))

    def test_registry_container_counts(self):
        counts = {}
        for r in self.data["records"]:
            if r["representation"]["kind"] != "REGISTRY_RECORD":
                continue
            container = r["representation"]["container"]
            counts[container] = counts.get(container, 0) + 1
        self.assertEqual(counts, {
            "08 CMOC Core/LAB-000 Опись терминов ОН.md": 110,
            "08 CMOC Core/LAB-002 Реестр различений.md": 623,
            "08 CMOC Core/LAB-004 Инварианты.md": 11,
            "08 CMOC Core/LAB-005 Опись организационных конструкций.md": 478,
        })

    def test_unique_full_addresses(self):
        addresses = []
        for r in self.data["records"]:
            addresses.append((
                r["object_type"],
                r["representation"]["kind"],
                r["representation"]["container"],
                json.dumps(r["representation"]["location"], sort_keys=True, ensure_ascii=False),
            ))
        self.assertEqual(len(addresses), len(set(addresses)))

    def test_provenance_matches_inventory(self):
        for r in self.data["records"]:
            container = r["representation"]["container"]
            self.assertIn(container, self.inventory_by_path)
            self.assertEqual(
                r["provenance"]["git_sha"],
                self.inventory_by_path[container],
                msg=container,
            )

    def test_actual_object_structure_is_indexed(self):
        by_id = {(r["object_type"], r["object_id"]): r for r in self.data["records"]
                 if r["representation"]["kind"] == "OBJECT_FILE"}
        term = by_id[("TERM", "T-0001")]
        self.assertIn("id", term["structure"]["fields_present"])
        self.assertIn("name", term["structure"]["fields_present"])
        self.assertIn("type", term["structure"]["fields_present"])
        self.assertIn("tags", term["structure"]["fields_present"])
        self.assertIn("Формулировки", term["structure"]["sections_present"])

        distinction = by_id[("DISTINCTION", "DIS-000001")]
        for field in ("id", "status", "source", "basis", "patch", "tags"):
            self.assertIn(field, distinction["structure"]["fields_present"])
        self.assertIn("Связи", distinction["structure"]["sections_present"])

    def test_object_id_is_not_guessed_from_arbitrary_content(self):
        from build_cmoc_object_index import explicit_object_id
        self.assertIsNone(
            explicit_object_id(
                "# Notes\nReference to T-9999 appears here.\n",
                "some/untitled.md",
            )
        )

    def test_representation_contract(self):
        allowed = {"OBJECT_FILE", "REGISTRY_RECORD", "OTHER_ADDRESSABLE"}
        for r in self.data["records"]:
            self.assertIn(r["representation"]["kind"], allowed)
            self.assertTrue(r["representation"]["container"])
            self.assertTrue(r["representation"]["location"] is not None)
            if r["representation"]["kind"] == "OBJECT_FILE":
                self.assertEqual(r["representation"]["location"], "FILE")
            elif r["representation"]["kind"] == "REGISTRY_RECORD":
                self.assertIsInstance(r["representation"]["location"], dict)
                self.assertIn("record_id", r["representation"]["location"])
                self.assertIn("line", r["representation"]["location"])
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

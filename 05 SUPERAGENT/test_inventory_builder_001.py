"""Production acceptance test for INVENTORY-BUILDER-001."""

from __future__ import annotations

import hashlib
import json
import tempfile
from pathlib import Path

from inventory_builder import build_inventory, write_inventory


def _hash_tree(root: Path) -> dict[str, str]:
    return {
        p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in sorted(root.rglob("*"))
        if p.is_file()
    }


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)

        (root / "T-0001.md").write_text(
            "---\n"
            "id: T-0001\n"
            "type: term\n"
            "status: active\n"
            "title: Test term\n"
            "source: TEST\n"
            "created: 2026-09-24\n"
            "tags:\n"
            "  - test\n"
            "inventory_class: TERM_FILE\n"
            "---\n"
            "# Test term\n",
            encoding="utf-8",
        )

        (root / "MC-TEST-001.md").write_text(
            "---\n"
            "machine_id: MC-TEST-001\n"
            "type: machine\n"
            "status: active\n"
            "title: Test machine\n"
            "source: TEST\n"
            "created: 2026-09-24\n"
            "tags:\n"
            "  - test\n"
            "inventory_class: MACHINE\n"
            "---\n"
            "# Test machine\n",
            encoding="utf-8",
        )

        registry = root / "08 CMOC Core"
        registry.mkdir()
        for name in (
            "LAB-000 Опись терминов ОН.md",
            "LAB-002 Реестр различений.md",
            "LAB-004 Инварианты.md",
            "LAB-005 Опись организационных конструкций.md",
        ):
            (registry / name).write_text(f"# {name}\n", encoding="utf-8")

        excluded = root / "03_MACHINE-CATALOG/MACHINES"
        excluded.mkdir(parents=True)
        (excluded / "MACHINE-CANDIDATES.md").write_text(
            "# MACHINE-CANDIDATES\n", encoding="utf-8"
        )

        (root / "notes.md").write_text(
            "# ordinary repository file\n", encoding="utf-8"
        )

        before = _hash_tree(root)

        snapshot = build_inventory(
            root,
            repository="TEST/CMOC",
            state="work/discovery-result-builder",
            source_commit="TEST-COMMIT-001",
            generated_at="2026-09-24T00:00:00+03:00",
        )

        assert snapshot["schema"] == "CMOC-INVENTORY-001"
        assert snapshot["version"] == "0.2"
        assert snapshot["repository"] == "TEST/CMOC"
        assert snapshot["branch"] == "work/discovery-result-builder"
        assert snapshot["source_commit"] == "TEST-COMMIT-001"
        assert snapshot["builder_version"] == "INVENTORY-BUILDER-001-v0.1"

        objects = [
            r for r in snapshot["records"]
            if r.get("representation", {}).get("kind") == "OBJECT_FILE"
        ]
        registries = [
            r for r in snapshot["records"]
            if r.get("representation", {}).get("kind") == "REGISTRY_RECORD"
        ]

        assert {r["object_id"] for r in objects} == {"T-0001", "MC-TEST-001"}
        assert {r["object_type"] for r in objects} == {"TERM", "MACHINE"}
        assert {r["object_id"] for r in registries} == {
            "LAB-000", "LAB-002", "LAB-004", "LAB-005"
        }

        assert any(
            r.get("path") == "03_MACHINE-CATALOG/MACHINES/MACHINE-CANDIDATES.md"
            and r.get("class") == "EXCLUDED"
            for r in snapshot["records"]
        )
        assert any(
            r.get("path") == "notes.md"
            and r.get("class") == "REPOSITORY_OTHER"
            for r in snapshot["records"]
        )
        assert snapshot["structural_errors"] == []

        repeat = build_inventory(
            root,
            repository="TEST/CMOC",
            state="work/discovery-result-builder",
            source_commit="TEST-COMMIT-001",
            generated_at="2026-09-24T00:00:00+03:00",
        )
        assert snapshot["records"] == repeat["records"]
        assert snapshot["structural_errors"] == repeat["structural_errors"]

        output = root / "inventory.json"
        write_inventory(snapshot, output)
        assert json.loads(output.read_text(encoding="utf-8")) == snapshot

        after = _hash_tree(root)
        for path, digest in before.items():
            assert after[path] == digest

        assert "decision" not in snapshot
        assert "match_result" not in snapshot
        assert "cmoc_write" not in snapshot
        assert "object_index" not in snapshot

    print("INVENTORY-BUILDER-001 PRODUCTION ACCEPTANCE TEST: PASS")


if __name__ == "__main__":
    main()

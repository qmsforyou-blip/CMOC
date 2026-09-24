"""Compatibility acceptance test: INVENTORY-BUILDER-001 -> CMOC-OBJECT-INDEX-001."""

from __future__ import annotations

import hashlib
import json
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from inventory_builder import build_inventory, write_inventory
from build_cmoc_object_index import build as build_object_index


def _hash_tree(root: Path) -> dict[str, str]:
    return {
        p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in sorted(root.rglob("*"))
        if p.is_file()
    }


def _write_object(path: Path, identity_key: str, identity: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "---\n"
        f"{identity_key}: {identity}\n"
        "name: Test object\n"
        "source: TEST\n"
        "---\n"
        "# Test object\n",
        encoding="utf-8",
    )


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)

        _write_object(
            root / "000 База/01 Термины/T-0001 Test term.md",
            "id",
            "T-0001",
        )
        _write_object(
            root / "03_MACHINE-CATALOG/MACHINES/MC-TEST-001 Test machine.md",
            "machine_id",
            "MC-TEST-001",
        )

        registry = root / "08 CMOC Core"
        registry.mkdir(parents=True)

        (registry / "LAB-000 Опись терминов ОН.md").write_text(
            "# LAB-000\nT-0002 Registry term\n",
            encoding="utf-8",
        )
        (registry / "LAB-002 Реестр различений.md").write_text(
            "| DIS-0001 | Registry distinction |\n",
            encoding="utf-8",
        )
        (registry / "LAB-004 Инварианты.md").write_text(
            "# INV-0001 Registry invariant\n",
            encoding="utf-8",
        )
        (registry / "LAB-005 Опись организационных конструкций.md").write_text(
            "| C-0001 | Registry construction |\n",
            encoding="utf-8",
        )

        (root / "notes.md").write_text(
            "# ordinary repository file\n",
            encoding="utf-8",
        )

        generated_at = "2026-09-24T15:20:00+03:00"
        source_commit = "TEST-COMMIT-COMPAT-001"

        before = _hash_tree(root)

        inventory = build_inventory(
            root,
            repository="TEST/CMOC",
            state="work/discovery-result-builder",
            source_commit=source_commit,
            generated_at=generated_at,
        )
        inventory_path = root / "cmoc_inventory.json"
        write_inventory(inventory, inventory_path)

        index = build_object_index(
            repository_root=root,
            inventory_path=inventory_path,
        )

        assert index["schema"] == "CMOC-OBJECT-INDEX-001"
        assert index["version"] == "0.2"
        assert index["repository"] == inventory["repository"]
        assert index["branch"] == inventory["branch"]
        assert index["generated_at"] == inventory["generated_at"]
        assert index["source_commit"] == inventory["source_commit"]
        assert index["source_inventory"] == (
            f'{inventory["schema"]}@{inventory["generated_at"]}'
        )

        records = index["records"]
        assert records

        for record in records:
            assert record["provenance"]["repository"] == inventory["repository"]
            assert record["provenance"]["inventory_snapshot"] == (
                f'{inventory["schema"]}@{inventory["generated_at"]}/{inventory["source_commit"]}'
            )

        object_files = [
            r for r in records
            if r["representation"]["kind"] == "OBJECT_FILE"
        ]
        registry_records = [
            r for r in records
            if r["representation"]["kind"] == "REGISTRY_RECORD"
        ]

        assert {r["object_id"] for r in object_files} == {
            "T-0001",
            "MC-TEST-001",
        }
        assert {r["object_id"] for r in registry_records} == {
            "T-0002",
            "DIS-0001",
            "INV-0001",
            "C-0001",
        }

        assert all(
            r["git_sha"] is not None
            for r in inventory["records"]
            if r["path"].startswith("08 CMOC Core/")
        )
        assert all(r["provenance"]["git_sha"] for r in records)

        after = _hash_tree(root)
        assert before == {
            path: digest for path, digest in after.items()
            if path != "cmoc_inventory.json"
        }

        assert not (root / "cmoc_object_index.json").exists()

        serialized = json.dumps(index, ensure_ascii=False)
        assert "2026-09-18" not in serialized
        assert "fd12c417358723b97205730084b87e9068a37854" not in serialized

    print("INVENTORY -> OBJECT INDEX COMPATIBILITY TEST: PASS")


if __name__ == "__main__":
    main()

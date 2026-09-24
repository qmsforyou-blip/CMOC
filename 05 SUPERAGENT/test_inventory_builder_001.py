"""Production acceptance test for INVENTORY-BUILDER-001."""

from __future__ import annotations

import hashlib
import json
import tempfile
from pathlib import Path

from inventory_builder import (
    BUILDER_VERSION,
    CLASSIFICATION_RULES_VERSION,
    build_inventory,
    write_inventory,
)


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
        registry.mkdir()
        for name in (
            "LAB-000 Опись терминов ОН.md",
            "LAB-002 Реестр различений.md",
            "LAB-004 Инварианты.md",
            "LAB-005 Опись организационных конструкций.md",
        ):
            (registry / name).write_text(f"# {name}\n", encoding="utf-8")

        excluded = root / "03_MACHINE-CATALOG/MACHINES"
        (excluded / "MACHINE-CANDIDATES.md").write_text(
            "# MACHINE-CANDIDATES\n", encoding="utf-8"
        )

        (root / "00 Стандарты CMOC/STD-TEST.md").parent.mkdir(
            parents=True, exist_ok=True
        )
        (root / "00 Стандарты CMOC/STD-TEST.md").write_text(
            "# standard\n", encoding="utf-8"
        )
        (root / "04 PATCH/PATCH-TEST.md").parent.mkdir(
            parents=True, exist_ok=True
        )
        (root / "04 PATCH/PATCH-TEST.md").write_text(
            "# patch\n", encoding="utf-8"
        )
        (root / "05 SUPERAGENT/test.txt").parent.mkdir(
            parents=True, exist_ok=True
        )
        (root / "05 SUPERAGENT/test.txt").write_text(
            "runtime\n", encoding="utf-8"
        )

        (root / "02 Машинки/runtime.py").parent.mkdir(
            parents=True, exist_ok=True
        )
        (root / "02 Машинки/runtime.py").write_text(
            "runtime\n", encoding="utf-8"
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
        assert snapshot["version"] == "0.3"
        assert snapshot["repository"] == "TEST/CMOC"
        assert snapshot["branch"] == "work/discovery-result-builder"
        assert snapshot["source_commit"] == "TEST-COMMIT-001"
        assert snapshot["builder_version"] == BUILDER_VERSION
        assert snapshot["classification_rules_version"] == CLASSIFICATION_RULES_VERSION

        assert all("git_sha" in r and "size_bytes" in r and r["type"] == "file" for r in snapshot["records"])

        objects = [
            r for r in snapshot["records"]
            if r.get("representation", {}).get("kind") == "OBJECT_FILE"
        ]
        registries = [
            r for r in snapshot["records"]
            if r.get("representation", {}).get("kind") == "REGISTRY_CONTAINER"
        ]

        assert {r["object_id"] for r in objects} == {"T-0001", "MC-TEST-001"}
        assert {r["object_type"] for r in objects} == {"TERM", "MACHINE"}
        assert {r["path"] for r in registries} == {
            "08 CMOC Core/LAB-000 Опись терминов ОН.md",
            "08 CMOC Core/LAB-002 Реестр различений.md",
            "08 CMOC Core/LAB-004 Инварианты.md",
            "08 CMOC Core/LAB-005 Опись организационных конструкций.md",
        }

        assert any(
            r.get("path") == "03_MACHINE-CATALOG/MACHINES/MACHINE-CANDIDATES.md"
            and r.get("class") == "EXCLUDED"
            for r in snapshot["records"]
        )
        assert any(
            r.get("path") == "00 Стандарты CMOC/STD-TEST.md"
            and r.get("class") == "STANDARD"
            for r in snapshot["records"]
        )
        assert any(
            r.get("path") == "04 PATCH/PATCH-TEST.md"
            and r.get("class") == "PATCH"
            for r in snapshot["records"]
        )
        assert any(
            r.get("path") == "05 SUPERAGENT/test.txt"
            and r.get("class") == "SUPERAGENT"
            for r in snapshot["records"]
        )
        assert any(
            r.get("path") == "02 Машинки/runtime.py"
            and r.get("class") == "MACHINE_RUNTIME"
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
            generated_at="2026-09-25T00:00:00+03:00",
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

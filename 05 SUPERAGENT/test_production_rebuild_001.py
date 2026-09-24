"""Acceptance test for PROD-REBUILD-001."""

from __future__ import annotations

import json
import subprocess
import tempfile
from pathlib import Path

from rebuild_inventory_object_index import rebuild


def _git(root: Path, *args: str) -> str:
    return subprocess.run(
        ["git", "-C", str(root), *args],
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=True,
    ).stdout.strip()


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)

        _write(
            root / "000 База/01 Термины/T-0001 Test term.md",
            "---\nid: T-0001\nsource: TEST\n---\n# Test\n",
        )
        _write(
            root / "03_MACHINE-CATALOG/MACHINES/MC-TEST-001 Test machine.md",
            "---\nmachine_id: MC-TEST-001\nsource: TEST\n---\n# Test\n",
        )
        _write(
            root / "08 CMOC Core/LAB-000 Опись терминов ОН.md",
            "T-0002 Registry term\n",
        )
        _write(
            root / "08 CMOC Core/LAB-002 Реестр различений.md",
            "| DIS-0001 | Registry distinction |\n",
        )
        _write(
            root / "08 CMOC Core/LAB-004 Инварианты.md",
            "# INV-0001 Registry invariant\n",
        )
        _write(
            root / "08 CMOC Core/LAB-005 Опись организационных конструкций.md",
            "| C-0001 | Registry construction |\n",
        )
        _write(root / "notes.md", "# clean repository\n")

        _git(root, "init")
        _git(root, "config", "user.email", "test@example.invalid")
        _git(root, "config", "user.name", "CMOC Test")
        _git(root, "add", ".")
        _git(root, "commit", "-m", "test production rebuild")
        head = _git(root, "rev-parse", "HEAD")

        first = rebuild(root)
        assert first["status"] == "PRODUCTION_REBUILD_COMPLETED"
        assert first["source_commit"] == head
        assert first["inventory_errors"] == 0

        inventory_path = root / "05 SUPERAGENT/cmoc_inventory.json"
        index_path = root / "05 SUPERAGENT/cmoc_object_index.json"
        assert inventory_path.exists()
        assert index_path.exists()

        inventory_1 = json.loads(inventory_path.read_text(encoding="utf-8"))
        index_1 = json.loads(index_path.read_text(encoding="utf-8"))

        assert not any(
            r["path"] in {
                "05 SUPERAGENT/cmoc_inventory.json",
                "05 SUPERAGENT/cmoc_object_index.json",
            }
            for r in inventory_1["records"]
        )
        assert not any(r["path"].startswith(".git/") for r in inventory_1["records"])

        second = rebuild(root)
        inventory_2 = json.loads(inventory_path.read_text(encoding="utf-8"))
        index_2 = json.loads(index_path.read_text(encoding="utf-8"))

        assert second["source_commit"] == head
        assert inventory_1["records"] == inventory_2["records"]
        assert inventory_1["structural_errors"] == inventory_2["structural_errors"]
        assert index_1["records"] == index_2["records"]

        _write(root / "notes.md", "# dirty repository\n")
        try:
            rebuild(root)
        except RuntimeError as exc:
            assert str(exc).startswith("PRODUCTION_REBUILD_BLOCKED:")
        else:
            raise AssertionError("Dirty repository was not blocked")

    print("PROD-REBUILD-001 ACCEPTANCE TEST: PASS")


if __name__ == "__main__":
    main()

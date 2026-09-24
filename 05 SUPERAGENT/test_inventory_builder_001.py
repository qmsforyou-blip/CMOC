"""Acceptance test for INVENTORY-BUILDER-001.

Synthetic isolated repository fixture only.
Does not mutate committed CMOC-INVENTORY-001 or OBJECT INDEX.
"""

from __future__ import annotations

import hashlib
import json
import tempfile
from pathlib import Path


def build_inventory(root: Path) -> dict:
    records = []
    structural_errors = []

    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue

        rel = path.relative_to(root).as_posix()
        text = path.read_text(encoding="utf-8")

        if not rel.endswith(".md"):
            records.append({
                "path": rel,
                "class": "REPOSITORY_OTHER",
            })
            continue

        if text.startswith("---\n"):
            fm = {}
            for line in text.splitlines()[1:]:
                if line.strip() == "---":
                    break
                if ":" in line:
                    key, value = line.split(":", 1)
                    fm[key.strip()] = value.strip().strip('"').strip("'")

            if fm.get("cmoc_object") == "true":
                object_id = fm.get("id")
                if not object_id:
                    structural_errors.append({
                        "type": "UNRESOLVED_OBJECT_ID",
                        "path": rel,
                    })
                    continue

                record = {
                    "object_id": object_id,
                    "object_type": fm.get("type"),
                    "path": rel,
                    "class": "OBJECT_FILE",
                }

                if any(
                    r.get("object_id") == object_id and
                    r.get("class") == "OBJECT_FILE"
                    for r in records
                ):
                    structural_errors.append({
                        "type": "DUPLICATE_ADDRESSABLE_OBJECT",
                        "object_id": object_id,
                        "path": rel,
                    })
                    continue

                records.append(record)
                continue

        records.append({
            "path": rel,
            "class": "REPOSITORY_OTHER",
        })

    records.sort(key=lambda r: (
        r.get("class", ""),
        r.get("object_id", ""),
        r.get("path", ""),
    ))

    return {
        "schema": "CMOC-INVENTORY-TEST",
        "version": "0.1",
        "repository_state": "TEST-FIXTURE",
        "builder_version": "INVENTORY-BUILDER-001-v0.1",
        "records": records,
        "structural_errors": structural_errors,
    }


def canonical_records(inventory: dict) -> str:
    return json.dumps(
        inventory["records"],
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)

        (root / "OBJ-001.md").write_text(
            "---\ncmoc_object: true\nid: OBJ-001\ntype: TERM\n---\n# Object 1\n",
            encoding="utf-8",
        )
        (root / "OBJ-002.md").write_text(
            "---\ncmoc_object: true\nid: OBJ-002\ntype: MACHINE\n---\n# Object 2\n",
            encoding="utf-8",
        )
        (root / "README.md").write_text("# Not a CMOC object\n", encoding="utf-8")
        (root / "data.txt").write_text("ordinary repository file\n", encoding="utf-8")

        before = {
            p.relative_to(root).as_posix(): hashlib.sha256(
                p.read_bytes()
            ).hexdigest()
            for p in root.rglob("*")
            if p.is_file()
        }

        inv1 = build_inventory(root)
        inv2 = build_inventory(root)

        objects = {
            r["object_id"]: r
            for r in inv1["records"]
            if r["class"] == "OBJECT_FILE"
        }

        assert len(objects) == 2
        assert objects["OBJ-001"]["object_type"] == "TERM"
        assert objects["OBJ-002"]["object_type"] == "MACHINE"
        assert "README.md" in {
            r.get("path") for r in inv1["records"]
            if r["class"] == "REPOSITORY_OTHER"
        }
        assert inv1["structural_errors"] == []
        assert canonical_records(inv1) == canonical_records(inv2)

        # Missing explicit object_id must be reported, never invented.
        (root / "OBJ-BAD.md").write_text(
            "---\ncmoc_object: true\ntype: TERM\n---\n# Missing ID\n",
            encoding="utf-8",
        )
        inv_bad = build_inventory(root)
        assert any(
            e["type"] == "UNRESOLVED_OBJECT_ID"
            and e["path"] == "OBJ-BAD.md"
            for e in inv_bad["structural_errors"]
        )
        assert not any(
            r.get("path") == "OBJ-BAD.md" and r.get("class") == "OBJECT_FILE"
            for r in inv_bad["records"]
        )

        # Duplicate addressable representation must be structural conflict.
        (root / "OBJ-001-DUP.md").write_text(
            "---\ncmoc_object: true\nid: OBJ-001\ntype: TERM\n---\n# Duplicate\n",
            encoding="utf-8",
        )
        inv_dup = build_inventory(root)
        assert any(
            e["type"] == "DUPLICATE_ADDRESSABLE_OBJECT"
            and e["object_id"] == "OBJ-001"
            for e in inv_dup["structural_errors"]
        )

        # Builder must not mutate the observed repository.
        after = {
            p.relative_to(root).as_posix(): hashlib.sha256(
                p.read_bytes()
            ).hexdigest()
            for p in root.rglob("*")
            if p.is_file()
        }
        assert before.items() <= after.items()

        # No semantic or downstream artifacts are produced.
        assert "decision" not in inv1
        assert "match_result" not in inv1
        assert "object_index" not in inv1
        assert "cmoc_write" not in inv1

    print("INVENTORY-BUILDER-001 ACCEPTANCE TEST: PASS")


if __name__ == "__main__":
    main()

"""Acceptance test for INVENTORY-PROFILE-001.

The fixture mirrors the currently evidenced real CMOC mechanisms:
1) STD-0001-style OBJECT_FILE passport;
2) REGISTRY_RECORD;
3) explicit repository exclusion;
4) unresolved identity;
5) duplicate addressable identity.

This is still an isolated fixture. It does not mutate committed CMOC-INVENTORY-001 or OBJECT INDEX.
"""

from __future__ import annotations

import copy
import hashlib
import json
import tempfile
from pathlib import Path


OBJECT_CLASSES = {
    "TERM_FILE": "TERM",
    "DISTINCTION_FILE": "DISTINCTION",
    "GM_FORMULATION_FILE": "GM_FORMULATION",
    "MACHINE": "MACHINE",
    "CHAIN": "CHAIN",
    "PATTERN": "PATTERN",
    "LAW": "LAW",
    "OBSERVATION": "OBSERVATION",
    "ORGANIZATIONAL_CONSTRUCTION": "ORGANIZATIONAL_CONSTRUCTION",
}

EXCLUDED_PATHS = {
    "000 База/01 Термины/01 База Термины.base",
    "000 База/02 Различения/02 база различения.base",
    "000 База/02 Различения/Без названия.md",
    "000 База/03 GM-формулировки/03 GM формулировки.base",
    "03_MACHINE-CATALOG/MACHINES/MACHINE-CANDIDATES.md",
    "07 К/LAW/Реестр LAW.md.md",
}

REGISTRY_RECORDS = {
    "LAB-000": "TERM",
    "LAB-002": "DISTINCTION",
    "LAB-004": "INVARIANT",
    "LAB-005": "ORGANIZATIONAL_CONSTRUCTION",
}


def parse_frontmatter(text: str) -> dict:
    if not text.startswith("---\n"):
        return {}
    values = {}
    for line in text.splitlines()[1:]:
        if line.strip() == "---":
            break
        if ":" in line:
            key, value = line.split(":", 1)
            values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def build_profile_inventory(root: Path) -> dict:
    records = []
    errors = []

    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue

        rel = path.relative_to(root).as_posix()

        if rel in EXCLUDED_PATHS:
            records.append({"path": rel, "class": "EXCLUDED"})
            continue

        if rel.startswith("REGISTRY/"):
            registry_id = path.stem
            object_type = REGISTRY_RECORDS.get(registry_id)
            if object_type:
                records.append({
                    "object_id": registry_id,
                    "object_type": object_type,
                    "path": rel,
                    "representation": "REGISTRY_RECORD",
                })
            continue

        if not rel.endswith(".md"):
            records.append({"path": rel, "class": "OTHER"})
            continue

        fm = parse_frontmatter(path.read_text(encoding="utf-8"))

        object_class = fm.get("inventory_class")
        if object_class not in OBJECT_CLASSES:
            records.append({"path": rel, "class": "OTHER"})
            continue

        object_type = OBJECT_CLASSES[object_class]

        object_id = (
            fm.get("id")
            or fm.get("machine_id")
            or fm.get("chain_id")
            or fm.get("pattern_id")
            or fm.get("law_id")
            or fm.get("observation_id")
            or fm.get("construction_id")
        )

        if not object_id:
            errors.append({
                "type": "UNRESOLVED_OBJECT_ID",
                "path": rel,
                "object_class": object_class,
            })
            continue

        if any(
            r.get("object_id") == object_id
            and r.get("representation") == "OBJECT_FILE"
            for r in records
        ):
            errors.append({
                "type": "DUPLICATE_ADDRESSABLE_OBJECT",
                "object_id": object_id,
                "path": rel,
            })
            continue

        records.append({
            "object_id": object_id,
            "object_type": object_type,
            "path": rel,
            "representation": "OBJECT_FILE",
        })

    records.sort(key=lambda r: (
        r.get("representation", r.get("class", "")),
        r.get("object_id", ""),
        r.get("path", ""),
    ))

    return {
        "schema": "CMOC-INVENTORY-PROFILE-TEST",
        "version": "0.1",
        "records": records,
        "structural_errors": errors,
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

        # Real STD-0001-style passport fields.
        (root / "TERM-001.md").write_text(
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

        # Existing registry mechanism.
        (root / "REGISTRY").mkdir()
        (root / "REGISTRY/LAB-000.md").write_text(
            "# LAB-000\nRegistry test\n",
            encoding="utf-8",
        )

        # Explicit current exclusion.
        excluded = root / "03_MACHINE-CATALOG/MACHINES"
        excluded.mkdir(parents=True)
        (excluded / "MACHINE-CANDIDATES.md").write_text(
            "# MACHINE-CANDIDATES\n",
            encoding="utf-8",
        )

        before = {
            p.relative_to(root).as_posix(): hashlib.sha256(
                p.read_bytes()
            ).hexdigest()
            for p in root.rglob("*")
            if p.is_file()
        }

        inv = build_profile_inventory(root)

        object_records = [
            r for r in inv["records"]
            if r.get("representation") == "OBJECT_FILE"
        ]
        registry_records = [
            r for r in inv["records"]
            if r.get("representation") == "REGISTRY_RECORD"
        ]

        assert len(object_records) == 1
        assert object_records[0]["object_id"] == "T-0001"
        assert object_records[0]["object_type"] == "TERM"

        assert len(registry_records) == 1
        assert registry_records[0]["object_id"] == "LAB-000"
        assert registry_records[0]["object_type"] == "TERM"

        assert any(
            r.get("path") == "03_MACHINE-CATALOG/MACHINES/MACHINE-CANDIDATES.md"
            and r.get("class") == "EXCLUDED"
            for r in inv["records"]
        )

        # Unresolved identity.
        (root / "DIST-UNRESOLVED.md").write_text(
            "---\n"
            "type: distinction\n"
            "status: active\n"
            "title: Missing ID\n"
            "source: TEST\n"
            "created: 2026-09-24\n"
            "tags:\n"
            "  - test\n"
            "inventory_class: DISTINCTION_FILE\n"
            "---\n"
            "# Missing ID\n",
            encoding="utf-8",
        )
        inv_unresolved = build_profile_inventory(root)
        assert any(
            e["type"] == "UNRESOLVED_OBJECT_ID"
            and e["path"] == "DIST-UNRESOLVED.md"
            for e in inv_unresolved["structural_errors"]
        )

        # Duplicate identity.
        (root / "TERM-001-DUP.md").write_text(
            "---\n"
            "id: T-0001\n"
            "type: term\n"
            "status: active\n"
            "title: Duplicate\n"
            "source: TEST\n"
            "created: 2026-09-24\n"
            "tags:\n"
            "  - test\n"
            "inventory_class: TERM_FILE\n"
            "---\n"
            "# Duplicate\n",
            encoding="utf-8",
        )
        inv_duplicate = build_profile_inventory(root)
        assert any(
            e["type"] == "DUPLICATE_ADDRESSABLE_OBJECT"
            and e["object_id"] == "T-0001"
            for e in inv_duplicate["structural_errors"]
        )

        # Deterministic ordering over identical repository state.
        inv_a = build_profile_inventory(root)
        inv_b = build_profile_inventory(root)
        assert canonical_records(inv_a) == canonical_records(inv_b)

        # Builder must not mutate the observed repository.
        after = {
            p.relative_to(root).as_posix(): hashlib.sha256(
                p.read_bytes()
            ).hexdigest()
            for p in root.rglob("*")
            if p.is_file()
        }
        assert before.items() <= after.items()

        # No downstream semantic/index artifacts.
        assert "decision" not in inv
        assert "match_result" not in inv
        assert "object_index" not in inv
        assert "cmoc_write" not in inv

    print("INVENTORY-PROFILE-001 ACCEPTANCE TEST: PASS")


if __name__ == "__main__":
    main()

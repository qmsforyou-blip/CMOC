"""Production structural CMOC Inventory Builder.

Builds a deterministic inventory snapshot from the observed CMOC repository.
It performs structural discovery only and does not mutate CMOC or OBJECT INDEX.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


CLASS_TO_TYPE = {
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

ID_PATTERNS = (
    re.compile(r"\bT-\d{4}\b"),
    re.compile(r"\bDIS-\d+\b"),
    re.compile(r"\bLAB-\d+\b"),
    re.compile(r"\bMC-[A-Z0-9-]+\b"),
    re.compile(r"\bCHAIN-[A-Z0-9-]+\b"),
    re.compile(r"\bMP-[A-Z0-9-]+\b"),
    re.compile(r"\bLAW-\d+\b"),
    re.compile(r"\bOBS-\d+\b"),
    re.compile(r"\bOC-\d+\b"),
)

NON_OBJECT_PATHS = {
    "000 База/01 Термины/01 База Термины.base",
    "000 База/02 Различения/02 база различения.base",
    "000 База/02 Различения/Без названия.md",
    "000 База/03 GM-формулировки/03 GM формулировки.base",
    "03_MACHINE-CATALOG/MACHINES/MACHINE-CANDIDATES.md",
    "07 К/LAW/Реестр LAW.md.md",
}

REGISTRY_SPECS = {
    "08 CMOC Core/LAB-000 Опись терминов ОН.md": ("TERM", "TERM"),
    "08 CMOC Core/LAB-002 Реестр различений.md": ("DISTINCTION", "DISTINCTION"),
    "08 CMOC Core/LAB-004 Инварианты.md": ("INVARIANT", "INVARIANT"),
    "08 CMOC Core/LAB-005 Опись организационных конструкций.md": (
        "ORGANIZATIONAL_CONSTRUCTION",
        "ORGANIZATIONAL_CONSTRUCTION",
    ),
}


def _frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    result: dict[str, str] = {}
    for line in text.splitlines()[1:]:
        if line.strip() == "---":
            break
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$", line)
        if match:
            result[match.group(1)] = match.group(2).strip().strip('"').strip("'")
    return result


def _explicit_object_id(text: str, path: str) -> str | None:
    fm = _frontmatter(text)
    for key in (
        "id",
        "machine_id",
        "chain_id",
        "pattern_id",
        "law_id",
        "observation_id",
        "construction_id",
    ):
        value = fm.get(key)
        if value and any(pattern.fullmatch(value) for pattern in ID_PATTERNS):
            return value

    for candidate in (Path(path).name, Path(path).stem):
        for pattern in ID_PATTERNS:
            match = pattern.search(candidate)
            if match:
                return match.group(0)
    return None


def _object_record(root: Path, path: str, object_type: str, object_class: str) -> dict[str, Any]:
    full = root / path
    text = full.read_text(encoding="utf-8")
    fm = _frontmatter(text)
    object_id = _explicit_object_id(text, path)
    if object_id is None:
        raise ValueError(f"UNRESOLVED_OBJECT_ID: {path}")
    return {
        "schema": "CMOC-INVENTORY-RECORD",
        "version": "0.1",
        "object_id": object_id,
        "object_type": object_type,
        "class": object_class,
        "path": path,
        "representation": {
            "kind": "OBJECT_FILE",
            "container": path,
            "location": "FILE",
        },
        "source": fm.get("source", "UNKNOWN"),
    }


def build_inventory(
    repository_root: str | Path,
    *,
    repository: str,
    state: str,
    source_commit: str,
    generated_at: str,
    builder_version: str = "INVENTORY-BUILDER-001-v0.1",
) -> dict[str, Any]:
    """Observe a CMOC repository and return a deterministic inventory snapshot."""
    root = Path(repository_root)
    if not root.is_dir():
        raise ValueError("repository_root must be an existing directory")

    records: list[dict[str, Any]] = []
    errors: list[dict[str, Any]] = []
    seen: dict[tuple[str, str], str] = {}

    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(root).as_posix()

        if rel in NON_OBJECT_PATHS:
            records.append({
                "path": rel,
                "class": "EXCLUDED",
            })
            continue

        if rel in REGISTRY_SPECS:
            object_type, object_class = REGISTRY_SPECS[rel]
            records.append({
                "schema": "CMOC-INVENTORY-RECORD",
                "version": "0.1",
                "object_id": Path(rel).name.split()[0],
                "object_type": object_type,
                "class": "CMOC_CORE_REGISTRY",
                "path": rel,
                "representation": {
                    "kind": "REGISTRY_RECORD",
                    "container": rel,
                    "location": "REGISTRY",
                },
            })
            continue

        if path.suffix.lower() != ".md":
            records.append({"path": rel, "class": "REPOSITORY_OTHER"})
            continue

        fm = _frontmatter(path.read_text(encoding="utf-8"))
        object_class = fm.get("inventory_class")
        if object_class not in CLASS_TO_TYPE:
            records.append({"path": rel, "class": "REPOSITORY_OTHER"})
            continue

        object_type = CLASS_TO_TYPE[object_class]
        try:
            record = _object_record(root, rel, object_type, object_class)
        except ValueError as exc:
            errors.append({"type": "UNRESOLVED_OBJECT_ID", "path": rel, "detail": str(exc)})
            continue

        key = (record["object_id"], "OBJECT_FILE")
        if key in seen:
            errors.append({
                "type": "DUPLICATE_ADDRESSABLE_OBJECT",
                "object_id": record["object_id"],
                "first_path": seen[key],
                "path": rel,
            })
            continue
        seen[key] = rel
        records.append(record)

    records.sort(key=lambda r: (
        r.get("representation", {}).get("kind", r.get("class", "")),
        r.get("object_id", ""),
        r.get("path", ""),
    ))

    return {
        "schema": "CMOC-INVENTORY-001",
        "version": "0.2",
        "generated_at": generated_at,
        "repository": repository,
        "branch": state,
        "source_commit": source_commit,
        "builder_version": builder_version,
        "purpose": "Full structural inventory snapshot. No semantic reconciliation or correction performed.",
        "records": records,
        "structural_errors": errors,
    }


def write_inventory(snapshot: dict[str, Any], output_path: str | Path) -> None:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(snapshot, ensure_ascii=False, indent=2, sort_keys=False) + "\n",
        encoding="utf-8",
    )

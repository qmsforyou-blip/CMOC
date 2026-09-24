"""Production structural CMOC Inventory Builder.

Builds CMOC-INVENTORY-001 from repository structure using explicit, versioned
structural classification rules. No semantic inference and no repository
mutation are performed.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


BUILDER_VERSION = "INVENTORY-BUILDER-001-v0.2"
CLASSIFICATION_RULES_VERSION = "INVENTORY-CLASSIFICATION-RULES-001-v0.1"

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


def _classify_path(rel: str) -> str:
    """Classify by explicit repository structure, not semantic content."""
    if rel in NON_OBJECT_PATHS:
        return "EXCLUDED"

    if rel.startswith("08 CMOC Core/"):
        return "CMOC_CORE_REGISTRY"

    if rel.startswith("00 Стандарты CMOC/"):
        return "STANDARD"

    if rel.startswith("04 PATCH/"):
        return "PATCH"

    if rel.startswith("05 SUPERAGENT/"):
        return "SUPERAGENT"

    if rel.startswith("000 База/01 Термины/"):
        return "TERM_FILE"

    if rel.startswith("000 База/02 Различения/"):
        return "DISTINCTION_FILE"

    if rel.startswith("000 База/03 GM-формулировки/"):
        return "GM_FORMULATION_FILE"

    if rel.startswith("03_MACHINE-CATALOG/CHAINS/"):
        return "CHAIN"

    if rel.startswith("03_MACHINE-CATALOG/PATTERNS/"):
        return "PATTERN"

    if rel.startswith("03_MACHINE-CATALOG/MACHINES/"):
        return "MACHINE"

    if rel.startswith("07 К/LAW/"):
        return "LAW"

    if rel.startswith("07 К/OBS/"):
        return "OBSERVATION"

    if rel.startswith("07 К/OC/"):
        return "ORGANIZATIONAL_CONSTRUCTION"

    return "REPOSITORY_OTHER"


def _object_record(
    root: Path,
    path: str,
    object_type: str,
    object_class: str,
) -> dict[str, Any]:
    full = root / path
    text = full.read_text(encoding="utf-8")
    fm = _frontmatter(text)
    object_id = _explicit_object_id(text, path)

    if object_id is None:
        raise ValueError(f"UNRESOLVED_OBJECT_ID: {path}")

    return {
        "schema": "CMOC-INVENTORY-RECORD",
        "version": "0.2",
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


def _registry_record(path: str) -> dict[str, Any]:
    return {
        "schema": "CMOC-INVENTORY-RECORD",
        "version": "0.2",
        "class": "CMOC_CORE_REGISTRY",
        "path": path,
        "representation": {
            "kind": "REGISTRY_CONTAINER",
            "container": path,
            "location": "REGISTRY",
        },
    }


def build_inventory(
    repository_root: str | Path,
    *,
    repository: str,
    state: str,
    source_commit: str,
    generated_at: str,
    builder_version: str = BUILDER_VERSION,
    classification_rules_version: str = CLASSIFICATION_RULES_VERSION,
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
        object_class = _classify_path(rel)

        if object_class == "EXCLUDED":
            records.append({"path": rel, "class": "EXCLUDED"})
            continue

        if object_class == "CMOC_CORE_REGISTRY":
            records.append(_registry_record(rel))
            continue

        if object_class == "REPOSITORY_OTHER":
            records.append({"path": rel, "class": object_class})
            continue

        if object_class in {"STANDARD", "PATCH", "SUPERAGENT"}:
            records.append({"path": rel, "class": object_class})
            continue

        if object_class not in CLASS_TO_TYPE:
            errors.append({
                "type": "UNSUPPORTED_CLASSIFICATION",
                "path": rel,
                "class": object_class,
            })
            continue

        object_type = CLASS_TO_TYPE[object_class]
        try:
            record = _object_record(root, rel, object_type, object_class)
        except (OSError, UnicodeError, ValueError) as exc:
            errors.append({
                "type": "UNRESOLVED_OBJECT_ID",
                "path": rel,
                "detail": str(exc),
            })
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

    object_counts: dict[str, int] = {}
    file_class_counts: dict[str, int] = {}

    for record in records:
        cls = record.get("class", "REPOSITORY_OTHER")
        file_class_counts[cls] = file_class_counts.get(cls, 0) + 1
        object_type = record.get("object_type")
        if object_type:
            object_counts[object_type] = object_counts.get(object_type, 0) + 1

    return {
        "schema": "CMOC-INVENTORY-001",
        "version": "0.2",
        "generated_at": generated_at,
        "repository": repository,
        "branch": state,
        "source_commit": source_commit,
        "builder_version": builder_version,
        "classification_rules_version": classification_rules_version,
        "purpose": "Full structural inventory snapshot. No semantic reconciliation or correction performed.",
        "object_counts": dict(sorted(object_counts.items())),
        "file_class_counts": dict(sorted(file_class_counts.items())),
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

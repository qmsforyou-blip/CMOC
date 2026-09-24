"""PROD-REBUILD-001 — deterministic local Inventory -> Object Index rebuild."""

from __future__ import annotations

import json
import os
import subprocess
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Any

from inventory_builder import BUILDER_VERSION, build_inventory
from build_cmoc_object_index import build as build_object_index


ROOT = Path(__file__).resolve().parents[1]
INVENTORY_OUTPUT = ROOT / "05 SUPERAGENT" / "cmoc_inventory.json"
OBJECT_INDEX_OUTPUT = ROOT / "05 SUPERAGENT" / "cmoc_object_index.json"
DERIVED_OUTPUTS = {
    INVENTORY_OUTPUT.relative_to(ROOT).as_posix(),
    OBJECT_INDEX_OUTPUT.relative_to(ROOT).as_posix(),
}


def _git(root: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(root), *args],
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=True,
    )
    return result.stdout.strip()


def git_state(root: Path) -> dict[str, str]:
    status = _git(root, "status", "--porcelain=v1", "--untracked-files=all")
    dirty_paths: list[str] = []
    for line in status.splitlines():
        if len(line) >= 4:
            path = line[3:]
            if " -> " in path:
                path = path.split(" -> ", 1)[-1]
            if path not in DERIVED_OUTPUTS:
                dirty_paths.append(path)

    if dirty_paths:
        raise RuntimeError(
            "PRODUCTION_REBUILD_BLOCKED: repository has uncommitted non-derived changes: "
            + ", ".join(dirty_paths)
        )

    return {
        "branch": _git(root, "branch", "--show-current"),
        "source_commit": _git(root, "rev-parse", "HEAD"),
    }


def _write_json_atomic(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(
        prefix=f".{path.name}.",
        suffix=".tmp",
        dir=str(path.parent),
    )
    tmp_path = Path(tmp_name)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as handle:
            json.dump(payload, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
        os.replace(tmp_path, path)
    finally:
        if tmp_path.exists():
            tmp_path.unlink()


def rebuild(root: str | Path = ROOT) -> dict[str, Any]:
    root = Path(root)
    state = git_state(root)
    generated_at = datetime.now().astimezone().isoformat(timespec="seconds")

    inventory = build_inventory(
        root,
        repository="qmsforyou-blip/CMOC",
        state=state["branch"],
        source_commit=state["source_commit"],
        generated_at=generated_at,
    )

    # Build Object Index from the in-memory Inventory before mutating either
    # derived output. The temporary Inventory is outside the repository.
    with tempfile.TemporaryDirectory() as tmp:
        temp_inventory = Path(tmp) / "cmoc_inventory.json"
        _write_json_atomic(temp_inventory, inventory)
        object_index = build_object_index(
            repository_root=root,
            inventory_path=temp_inventory,
        )

    _write_json_atomic(INVENTORY_OUTPUT if root == ROOT else root / "05 SUPERAGENT/cmoc_inventory.json", inventory)
    _write_json_atomic(OBJECT_INDEX_OUTPUT if root == ROOT else root / "05 SUPERAGENT/cmoc_object_index.json", object_index)

    return {
        "status": "PRODUCTION_REBUILD_COMPLETED",
        "repository": inventory["repository"],
        "branch": inventory["branch"],
        "source_commit": inventory["source_commit"],
        "builder_version": BUILDER_VERSION,
        "inventory_records": len(inventory["records"]),
        "inventory_errors": len(inventory["structural_errors"]),
        "object_index_records": object_index["representation_record_count"],
    }


def main() -> int:
    result = rebuild()
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

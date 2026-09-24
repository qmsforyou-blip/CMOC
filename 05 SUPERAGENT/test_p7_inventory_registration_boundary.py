"""Synthetic acceptance test for P7 -> Inventory Registration boundary.

This test deliberately uses an isolated temporary inventory representation.
It does not mutate CMOC-INVENTORY-001 or OBJECT INDEX.
"""

from __future__ import annotations

import copy
import json
import tempfile
from pathlib import Path


def register_inventory(p7_result: dict, inventory: dict) -> tuple[str, dict]:
    if p7_result.get("status") != "CMOC_WRITE_ACCEPTED":
        return "INVENTORY_REGISTRATION_REJECTED", inventory

    required = (
        "object_id",
        "object_type",
        "representation",
        "provenance",
        "traceability",
        "write_id",
    )
    missing = [key for key in required if not p7_result.get(key)]
    if missing:
        return "INVENTORY_REGISTRATION_REJECTED", inventory

    record = {
        "object_id": p7_result["object_id"],
        "object_type": p7_result["object_type"],
        "representation": p7_result["representation"],
        "provenance": p7_result["provenance"],
        "traceability": p7_result["traceability"],
        "write_id": p7_result["write_id"],
    }

    records = inventory.setdefault("records", {})
    existing = records.get(record["object_id"])

    if existing is None:
        records[record["object_id"]] = record
        return "INVENTORY_REGISTERED", inventory

    if existing == record:
        return "ALREADY_REGISTERED", inventory

    return "INVENTORY_REGISTRATION_CONFLICT", inventory


def main() -> None:
    base_inventory = {
        "schema": "CMOC-INVENTORY-REGISTRATION-TEST",
        "version": "0.1",
        "records": {},
    }
    original = copy.deepcopy(base_inventory)

    valid = {
        "status": "CMOC_WRITE_ACCEPTED",
        "object_id": "OBJ-TEST-001",
        "object_type": "TERM",
        "representation": {
            "kind": "OBJECT_FILE",
            "container": "000 База/01 Термины/OBJ-TEST-001.md",
            "location": "FILE",
        },
        "provenance": {"repository": "qmsforyou-blip/CMOC", "source": "TEST"},
        "traceability": {"run_id": "RUN-TEST-001", "source_id": "SRC-TEST"},
        "write_id": "WRITE-TEST-001",
    }

    status, inv = register_inventory(valid, copy.deepcopy(base_inventory))
    assert status == "INVENTORY_REGISTERED"
    assert inv["records"]["OBJ-TEST-001"]["object_id"] == "OBJ-TEST-001"

    status2, inv2 = register_inventory(valid, copy.deepcopy(inv))
    assert status2 == "ALREADY_REGISTERED"
    assert inv2 == inv

    changed = copy.deepcopy(valid)
    changed["representation"] = {
        "kind": "OBJECT_FILE",
        "container": "000 База/01 Термины/OBJ-TEST-001-CHANGED.md",
        "location": "FILE",
    }
    status3, _ = register_inventory(changed, copy.deepcopy(inv))
    assert status3 == "INVENTORY_REGISTRATION_CONFLICT"

    invalid = copy.deepcopy(valid)
    invalid["status"] = "CANONICALIZATION_READY"
    status4, _ = register_inventory(invalid, copy.deepcopy(base_inventory))
    assert status4 == "INVENTORY_REGISTRATION_REJECTED"

    missing = copy.deepcopy(valid)
    del missing["write_id"]
    status5, _ = register_inventory(missing, copy.deepcopy(base_inventory))
    assert status5 == "INVENTORY_REGISTRATION_REJECTED"

    # Boundary invariant: the committed/base snapshot and INDEX are not touched.
    assert base_inventory == original

    # Physical isolated artifact only, proving the representation is serializable/readable.
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "inventory_registration_test.json"
        path.write_text(json.dumps(inv, ensure_ascii=False, indent=2), encoding="utf-8")
        restored = json.loads(path.read_text(encoding="utf-8"))
        assert restored == inv

    # No semantic operations are part of this boundary.
    assert "decision" not in inv
    assert "match_result" not in inv
    assert "cmoc_write" not in inv
    assert "object_index" not in inv

    print("P7 -> INVENTORY REGISTRATION BOUNDARY TEST: PASS")


if __name__ == "__main__":
    main()

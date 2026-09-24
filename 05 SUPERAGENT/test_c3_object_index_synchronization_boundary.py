#!/usr/bin/env python3
"""Synthetic isolated acceptance test for C3 OBJECT INDEX boundary."""
from __future__ import annotations

import copy
import hashlib
import json


class C3Error(ValueError):
    pass


def c3_sync(payload, cmoc, index):
    if payload.get("status") != "CMOC_WRITE_ACCEPTED":
        raise C3Error("C3_REJECTED")
    for field in ("object_id", "provenance", "traceability", "write_verification"):
        if not payload.get(field):
            raise C3Error("C3_REJECTED")
    if payload["write_verification"] is not True:
        raise C3Error("C3_REJECTED")

    oid = payload["object_id"]
    persisted = cmoc.get(oid)
    if persisted is None:
        raise C3Error("PERSISTED_OBJECT_MISSING")

    if persisted.get("object_id") != oid:
        raise C3Error("OBJECT_ID_MISMATCH")

    derived = {
        "object_id": oid,
        "object_type": persisted["object_type"],
        "canonical_name": persisted["canonical_name"],
        "provenance": copy.deepcopy(persisted["provenance"]),
        "traceability": copy.deepcopy(persisted["traceability"]),
    }

    existing = index.get(oid)
    if existing is None:
        index[oid] = derived
        return "INDEX_SYNCHRONIZED"

    if existing == derived:
        return "ALREADY_SYNCHRONIZED"

    raise C3Error("INDEX_SYNCHRONIZATION_CONFLICT")


def test_valid_and_idempotent():
    cmoc = {
        "OBJ-001": {
            "object_id": "OBJ-001",
            "object_type": "REQUIREMENT",
            "canonical_name": "Example",
            "provenance": {"source_id": "SRC-001"},
            "traceability": {"run_id": "RUN-001"},
        }
    }
    index = {}
    payload = {
        "status": "CMOC_WRITE_ACCEPTED",
        "object_id": "OBJ-001",
        "provenance": {"source_id": "SRC-001"},
        "traceability": {"run_id": "RUN-001"},
        "write_verification": True,
    }
    assert c3_sync(payload, cmoc, index) == "INDEX_SYNCHRONIZED"
    before = copy.deepcopy(index)
    assert c3_sync(payload, cmoc, index) == "ALREADY_SYNCHRONIZED"
    assert index == before


def test_rejections():
    base = {
        "object_id": "OBJ-001",
        "provenance": {"source_id": "SRC-001"},
        "traceability": {"run_id": "RUN-001"},
        "write_verification": True,
    }
    cmoc = {"OBJ-001": {
        "object_id": "OBJ-001", "object_type": "REQUIREMENT",
        "canonical_name": "Example", "provenance": {"source_id": "SRC-001"},
        "traceability": {"run_id": "RUN-001"},
    }}
    index = {}
    for mutation in (
        {"status": "CANONICALIZATION_READY"},
        {"status": "CMOC_WRITE_REJECTED"},
        {"status": "CMOC_WRITE_ACCEPTED", "object_id": ""},
        {"status": "CMOC_WRITE_ACCEPTED", "traceability": ""},
        {"status": "CMOC_WRITE_ACCEPTED", "write_verification": False},
    ):
        p = {**base, **mutation}
        try:
            c3_sync(p, cmoc, index)
        except C3Error as exc:
            assert str(exc) == "C3_REJECTED"
        else:
            raise AssertionError("invalid C3 entry must be rejected")


def test_missing_and_conflict():
    cmoc = {"OBJ-001": {
        "object_id": "OBJ-001", "object_type": "REQUIREMENT",
        "canonical_name": "Example", "provenance": {"source_id": "SRC-001"},
        "traceability": {"run_id": "RUN-001"},
    }}
    payload = {
        "status": "CMOC_WRITE_ACCEPTED", "object_id": "OBJ-001",
        "provenance": {"source_id": "SRC-001"},
        "traceability": {"run_id": "RUN-001"}, "write_verification": True,
    }
    index = {}
    assert c3_sync(payload, cmoc, index) == "INDEX_SYNCHRONIZED"
    index["OBJ-001"]["canonical_name"] = "Different"
    try:
        c3_sync(payload, cmoc, index)
    except C3Error as exc:
        assert str(exc) == "INDEX_SYNCHRONIZATION_CONFLICT"
    else:
        raise AssertionError("different derived representation must conflict")


def test_identity_and_boundary_controls():
    cmoc = {"OBJ-001": {
        "object_id": "OBJ-001", "object_type": "REQUIREMENT",
        "canonical_name": "Example", "provenance": {"source_id": "SRC-001"},
        "traceability": {"run_id": "RUN-001"},
    }}
    payload = {
        "status": "CMOC_WRITE_ACCEPTED", "object_id": "OBJ-001",
        "provenance": {"source_id": "SRC-001"},
        "traceability": {"run_id": "RUN-001"}, "write_verification": True,
    }
    index = {}
    before_cmoc = copy.deepcopy(cmoc)
    before_payload = copy.deepcopy(payload)
    assert c3_sync(payload, cmoc, index) == "INDEX_SYNCHRONIZED"
    assert cmoc == before_cmoc
    assert payload == before_payload


if __name__ == "__main__":
    test_valid_and_idempotent()
    test_rejections()
    test_missing_and_conflict()
    test_identity_and_boundary_controls()
    print("C3 OBJECT INDEX SYNCHRONIZATION BOUNDARY TEST: PASS")

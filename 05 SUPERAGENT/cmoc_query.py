#!/usr/bin/env python3
"""SPEC-005 CMOC QUERY v0.3 — read-only retrieval over CMOC OBJECT INDEX v0.2."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

BASE = Path(__file__).parent
OBJECT_INDEX_DEFAULT = BASE / "cmoc_object_index.json"
LEGACY_QUERY_INDEX_DEFAULT = BASE / "cmoc_query_index.json"

TYPE_SCOPE = {
    "TERM": "TERMS",
    "DISTINCTION": "DISTINCTIONS",
    "GM_FORMULATION": "FORMULATIONS",
    "MACHINE": "MACHINES",
    "PATTERN": "PATTERNS",
    "CHAIN": "CHAINS",
    "LAW": "LAW",
    "OBSERVATION": "OBSERVATIONS",
    "ORGANIZATIONAL_CONSTRUCTION": "ORGANIZATIONAL_CONSTRUCTIONS",
    "INVARIANT": "INVARIANTS",
}

ALLOWED_QUERY_TYPES = {"EXACT", "ALIAS", "STRUCTURAL", "CANDIDATE"}
ALLOWED_STATUSES = {"MATCH", "NO_MATCH", "CANDIDATE", "AMBIGUOUS", "SCOPE_INSUFFICIENT"}


def norm(value: Any) -> str:
    value = str(value).lower().replace("ё", "е")
    return " ".join(re.sub(r"[^0-9a-zа-я]+", " ", value, flags=re.I).split())


def load_object_index(path: str | Path = OBJECT_INDEX_DEFAULT) -> list[dict]:
    """Load the normative OBJECT INDEX v0.2 records."""
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if data.get("schema") != "CMOC-OBJECT-INDEX-001" or data.get("version") != "0.2":
        raise ValueError("Not a CMOC OBJECT INDEX v0.2")
    records = data.get("records")
    if not isinstance(records, list):
        raise ValueError("OBJECT INDEX has no records list")
    return records


# Compatibility boundary for the pre-v0.3 RECONCILIATION MVP.
# It is deliberately not used by QUERY v0.3 runtime.
def load_index(path: str | Path) -> list[dict]:
    """Load the legacy SPEC-003 query index for existing reconciliation tests."""
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if "objects" in data:
        objects = data["objects"]
        for obj in objects:
            obj.setdefault("aliases", [])
        return objects
    raise ValueError("Legacy query index expected")


def _scope_names(query_scope: Any) -> set[str]:
    if query_scope is None:
        return set()
    if isinstance(query_scope, str):
        return {query_scope}
    return {str(x) for x in query_scope}


def _parse_structure_query(value: Any) -> dict:
    if isinstance(value, dict):
        return value
    if isinstance(value, str):
        try:
            parsed = json.loads(value)
        except json.JSONDecodeError as exc:
            raise ValueError("STRUCTURAL/CANDIDATE query_value must be a JSON object") from exc
        if isinstance(parsed, dict):
            return parsed
    raise ValueError("STRUCTURAL/CANDIDATE query_value must be a JSON object")


def _structure_matches(record: dict, criteria: dict) -> bool:
    structure = record.get("structure") or {}
    representation = record.get("representation") or {}
    indexed = record.get("indexed_attributes") or {}

    if "object_type" in criteria and record.get("object_type") != criteria["object_type"]:
        return False
    if "representation_kind" in criteria and representation.get("kind") != criteria["representation_kind"]:
        return False
    if "fields_present" in criteria:
        wanted = set(criteria["fields_present"])
        if not wanted.issubset(set(structure.get("fields_present") or [])):
            return False
    if "sections_present" in criteria:
        wanted = set(criteria["sections_present"])
        if not wanted.issubset(set(structure.get("sections_present") or [])):
            return False
    if "indexed_attributes" in criteria:
        for key, value in (criteria["indexed_attributes"] or {}).items():
            if indexed.get(key) != value:
                return False
    return True


def _result(record: dict, query_id: str, query_type: str, status: str, basis: str) -> dict:
    return {
        "query_id": query_id,
        "object_id": record.get("object_id"),
        "object_type": record.get("object_type"),
        "match_mode": query_type,
        "match_status": status,
        "match_basis": basis,
        "indexed_attributes": record.get("indexed_attributes", {}),
        "representation": record.get("representation"),
        "traceability": record.get("traceability", {}),
    }


def query(
    records: list[dict],
    qid: str,
    qtype: str,
    target: str | None,
    value: Any,
    scope: list[str] | None,
) -> dict:
    """Execute one read-only query against already-loaded OBJECT INDEX records."""
    if qtype not in ALLOWED_QUERY_TYPES:
        raise ValueError(f"Unsupported QUERY_TYPE: {qtype}")

    scope_set = _scope_names(scope)
    if target and TYPE_SCOPE.get(target) not in scope_set:
        return {
            "query_id": qid,
            "match_status": "SCOPE_INSUFFICIENT",
            "match_basis": f"TARGET_OBJECT_TYPE={target} outside QUERY_SCOPE",
            "scope_checked": sorted(scope_set),
            "results": [],
        }

    candidates = [
        r for r in records
        if (not target or r.get("object_type") == target)
        and (not scope_set or TYPE_SCOPE.get(r.get("object_type")) in scope_set)
    ]

    if qtype == "EXACT":
        raw = str(value).strip()
        normalized = norm(raw)

        # EXACT is deterministic by the strongest explicit address first:
        # object_id. If the requested ID has several physical representations,
        # preserve all of them and report AMBIGUOUS. Do not let a coincidental
        # match in another indexed field create additional hits.
        id_hits = [
            r for r in candidates
            if str(r.get("object_id", "")).upper() == raw.upper()
        ]
        if id_hits:
            hits = id_hits
            basis = "exact object_id"
        else:
            # If no object_id matches, an exact object_name match is allowed.
            # Other indexed attributes are deliberately not considered.
            hits = [
                r for r in candidates
                if r.get("object_name") is not None
                and norm(r["object_name"]) == normalized
            ]
            basis = "exact object_name"

        # OBJECT_FILE is the canonical addressable representation for an
        # object. Registry rows are additional physical representations.
        # Therefore one canonical OBJECT_FILE plus registry representation(s)
        # is still a resolved MATCH; multiple non-canonical representations
        # without a unique OBJECT_FILE remain AMBIGUOUS.
        object_files = [
            r for r in hits
            if (r.get("representation") or {}).get("kind") == "OBJECT_FILE"
        ]
        if len(object_files) == 1:
            status = "MATCH"
            basis += "; canonical OBJECT_FILE present"
        elif len(hits) == 1:
            status = "MATCH"
        else:
            status = "AMBIGUOUS" if hits else "NO_MATCH"
    elif qtype == "ALIAS":
        normalized = norm(value)
        hits = [
            r for r in candidates
            if normalized and any(
                norm(alias) == normalized
                for alias in (r.get("indexed_attributes") or {}).get("aliases", [])
            )
        ]
        status = "MATCH" if len(hits) == 1 else ("AMBIGUOUS" if hits else "NO_MATCH")
        basis = "explicit indexed alias"
    else:
        criteria = _parse_structure_query(value)
        hits = [r for r in candidates if _structure_matches(r, criteria)]
        status = "CANDIDATE" if hits else "NO_MATCH"
        basis = "indexed structural fields only"

    return {
        "query_id": qid,
        "match_status": status,
        "match_basis": basis,
        "scope_checked": sorted(scope_set),
        "results": [_result(r, qid, qtype, status, basis) for r in hits],
    }


def main() -> None:
    payload = json.load(sys.stdin)
    index_path = payload.get("object_index_path", str(OBJECT_INDEX_DEFAULT))
    records = load_object_index(index_path)
    result = query(
        records,
        payload["query_id"],
        payload["query_type"],
        payload.get("target_object_type"),
        payload.get("query_value"),
        payload.get("query_scope"),
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

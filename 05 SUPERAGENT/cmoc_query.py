#!/usr/bin/env python3
"""SPEC-003 CMOC QUERY — deterministic read-only MVP.

The query layer never mutates the CMOC. It searches a checked-in index
and returns evidence/traceability for RECONCILIATION.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path


def norm(value: str) -> str:
    value = value.lower().replace("ё", "е")
    value = re.sub(r"[^0-9a-zа-я]+", " ", value, flags=re.IGNORECASE)
    return " ".join(value.split())


def load_index(path: str | Path) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def exact(objects, value):
    q = norm(value)
    qid = value.strip().upper()
    return [o for o in objects if o["object_id"].upper() == qid or norm(o["name"]) == q]


def alias(objects, value):
    q = norm(value)
    out = []
    for o in objects:
        for a in o.get("aliases", []):
            if norm(a) == q:
                out.append(o)
    return out


def structural(objects, value, target_type=None):
    q_tokens = set(norm(value).split())
    out = []
    for o in objects:
        if target_type and o["object_type"] != target_type:
            continue
        overlap = q_tokens & set(norm(o["name"]).split())
        if overlap:
            out.append((len(overlap), o))
    out.sort(key=lambda x: (-x[0], x[1]["object_id"]))
    return [o for _, o in out]


def query(index: dict, query_id: str, query_type: str, target_type: str | None,
          value: str, scope: list[str]) -> dict:
    objects = index.get("objects", [])
    allowed = set(scope)
    if target_type:
        type_scope = {
            "TERM": "TERMS",
            "NOMENCLATURE": "TERMS",
            "DISTINCTION": "DISTINCTIONS",
        }.get(target_type, target_type)
        if type_scope not in allowed:
            return {
                "query_id": query_id,
                "match_status": "SCOPE_INSUFFICIENT",
                "match_basis": f"TARGET_OBJECT_TYPE={target_type} outside QUERY_SCOPE",
                "results": [],
            }

    candidates = [
        o for o in objects
        if (
            ("TERMS" in allowed and o["object_type"] == "TERM")
            or ("DISTINCTIONS" in allowed and o["object_type"] == "DISTINCTION")
        )
    ]

    if target_type:
        candidates = [o for o in candidates if o["object_type"] == target_type]

    if query_type == "EXACT":
        hits = exact(candidates, value)
        status = "MATCH" if hits else "NO_MATCH"
    elif query_type == "ALIAS":
        hits = alias(candidates, value)
        status = "MATCH" if hits else "NO_MATCH"
    elif query_type == "STRUCTURAL":
        hits = structural(candidates, value, target_type)
        status = "CANDIDATE" if hits else "NO_MATCH"
    elif query_type == "CANDIDATE":
        hits = structural(candidates, value, target_type)
        status = "CANDIDATE" if hits else "NO_MATCH"
    else:
        raise ValueError(f"Unsupported QUERY_TYPE: {query_type}")

    results = []
    for o in hits:
        results.append({
            "query_id": query_id,
            "object_id": o["object_id"],
            "object_type": o["object_type"],
            "match_mode": query_type,
            "match_status": status,
            "match_basis": "normalized exact/name" if query_type == "EXACT"
                else "registered alias" if query_type == "ALIAS"
                else "token overlap candidate",
            "object_status": o.get("status", "UNKNOWN"),
            "traceability": o["traceability"],
        })

    return {
        "query_id": query_id,
        "match_status": status,
        "results": results,
        "scope_checked": sorted(allowed),
    }


def main() -> None:
    payload = json.load(sys.stdin)
    index_path = payload.get(
        "index_path",
        str(Path(__file__).with_name("cmoc_query_index.json")),
    )
    result = query(
        load_index(index_path),
        payload["query_id"],
        payload["query_type"],
        payload.get("target_object_type"),
        payload["query_value"],
        payload.get("query_scope", ["TERMS"]),
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

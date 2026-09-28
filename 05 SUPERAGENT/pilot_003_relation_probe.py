"""Read-only M07 probe using persisted Discovery passports and controlled evidence.

The LLM request may incur a charge. This command does not change the RUN,
human decisions, CMOC, or OBJECT INDEX.
"""

from __future__ import annotations

import argparse
import json
import sqlite3
from pathlib import Path

from m07_llm import build_relation_candidates


def bind_evidence(run_id: str, original: dict, controlled: dict, passports: list[dict], binding: dict) -> list[dict]:
    """Verify a human-specified ID mapping against one persisted Discovery run."""
    if (binding.get("run_id") != run_id or
        binding.get("source_id") != original["source_id"] or
        binding.get("source_package_id") != original["package_id"] or
        binding.get("evidence_package_id") != controlled["package_id"]):
        raise ValueError("RUN_BINDING_MISMATCH")
    expected = binding.get("passports")
    if not isinstance(expected, dict) or set(expected) != {p["id"] for p in passports}:
        raise ValueError("PASSPORT_SET_MISMATCH")
    by_id = {p["id"]: p for p in passports}
    for passport_id, claim in expected.items():
        passport = by_id[passport_id]
        if (passport.get("source_id") != original["source_id"] or
            passport.get("working_class") != claim.get("working_class") or
            passport.get("source_basis") != claim.get("source_basis")):
            raise ValueError(f"PASSPORT_BINDING_MISMATCH: {passport_id}")
    fragments = {f["location"]: f["text"] for f in original["fragments"]}
    templates = {e["evidence_id"]: e for e in controlled.get("relation_evidence", [])}
    pairs = binding.get("evidence_pairs")
    if not isinstance(pairs, dict) or not pairs or set(pairs) != set(templates):
        raise ValueError("EVIDENCE_SET_MISMATCH")
    evidence = []
    for evidence_id, pair in pairs.items():
        template = templates[evidence_id]
        location = template.get("location")
        if location not in fragments or template.get("text") != fragments[location]:
            raise ValueError("EVIDENCE_SOURCE_MISMATCH")
        if not isinstance(pair, list) or len(pair) != 2 or pair[0] == pair[1] or any(p not in by_id for p in pair):
            raise ValueError("EVIDENCE_ENDPOINT_MISMATCH")
        evidence.append({"evidence_id": evidence_id, "locations": [location],
                         "text": template["text"], "supports": pair})
    return evidence


def inspect(db_path: Path, run_id: str, original: dict, controlled: dict, binding: dict) -> dict:
    if original["source_id"] != controlled["source_id"] or original["fragments"] != controlled["fragments"]:
        raise ValueError("SOURCE_MISMATCH: controlled evidence must use identical source fragments")
    with sqlite3.connect(f"file:{db_path.resolve()}?mode=ro", uri=True) as db:
        db.execute("PRAGMA query_only=ON")
        row = db.execute(
            "SELECT payload_json FROM adapter_results WHERE run_id=? AND stage_id='DISCOVERY' ORDER BY rowid DESC LIMIT 1",
            (run_id,),
        ).fetchone()
    if row is None:
        raise ValueError("COMPLETED_DISCOVERY_RESULT_NOT_FOUND")
    discovery = json.loads(row[0])["discovery"]
    if discovery["source_package_id"] != original["package_id"]:
        raise ValueError("SOURCE_PACKAGE_MISMATCH")
    m06 = next((x for x in discovery["results"] if x.get("type") == "PASSPORT_RECORDS"), None)
    if m06 is None or m06["source_id"] != original["source_id"]:
        raise ValueError("M06_PASSPORT_RECORDS_NOT_FOUND")
    evidence = bind_evidence(run_id, original, controlled, m06["records"], binding)
    records = build_relation_candidates(m06["records"], evidence)
    return {
        "status": "READ_ONLY_RELATION_PROBE",
        "run_id": run_id,
        "source_package_id": original["package_id"],
        "evidence_package_id": controlled["package_id"],
        "relation_evidence": evidence,
        "records": records,
        "boundary": "M07 diagnostic only; no RUN, decisions, CMOC, or OBJECT INDEX write",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", required=True, type=Path)
    parser.add_argument("--run-id", required=True)
    here = Path(__file__).resolve().parent
    parser.add_argument("--original", type=Path, default=here / "SOURCE-PACKAGE-SRC-005-IMAI-CH13-P6.example.json")
    parser.add_argument("--evidence", type=Path, default=here / "SOURCE-PACKAGE-SRC-005-IMAI-CH13-P6-REL.example.json")
    parser.add_argument("--binding", type=Path, default=here / "PILOT-003-SRC-005-RELATION-BINDING.json")
    args = parser.parse_args()
    original = json.loads(args.original.read_text(encoding="utf-8"))
    controlled = json.loads(args.evidence.read_text(encoding="utf-8"))
    binding = json.loads(args.binding.read_text(encoding="utf-8"))
    print(json.dumps(inspect(args.db, args.run_id, original, controlled, binding), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from admission import execute_c1_from_admission
from c1_canonization import canonize


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--admission", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    admission = json.loads(
        Path(args.admission).read_text(encoding="utf-8")
    )

    candidate = {
        "record_id": "PAS-009",
        "value": "Создание незаменимых организационных способностей предприятия",
        "object_type": "ORGANIZATIONAL_CAPABILITY",
        "canonical_name": "Создание незаменимых организационных способностей предприятия",
    }

    raw = json.dumps(
        candidate,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )

    approved_candidate = {
        "decision_result": "NEW_APPROVED",
        "candidate": candidate,
        "provenance": {
            "source_id": "SRC-012",
            "reconciliation_id": "RECON-5ac3eaa4180a87aa",
            "match_id": "MAT-PAS-009",
        },
        "traceability": {
            "source_id": "SRC-012",
            "match_id": "MAT-PAS-009",
            "passport_id": "PAS-009",
        },
        "approved_candidate_hash": hashlib.sha256(
            raw.encode("utf-8")
        ).hexdigest(),
        "new_evidence_ref": "PAS-009-FORM-025-027",
    }

    c1_input = execute_c1_from_admission(
        admission,
        approved_candidate,
    )
    result = canonize(c1_input)

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(json.dumps({
        "status": result["status"],
        "object_id": result["object_id"],
        "output": str(output),
        "cmoc_write": result["boundary"]["cmoc_write"],
        "object_index_write": result["boundary"]["object_index_write"],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from admission import execute_c1_from_admission
from c1_canonization import canonize
from production_cmoc_writer import ProductionCmocWriter


def sha256_json(value: dict) -> str:
    raw = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generic Admission -> C1 -> optional isolated C2 runner"
    )

    parser.add_argument("--admission", required=True)
    parser.add_argument("--output", required=True)

    parser.add_argument("--record-id", required=True)
    parser.add_argument("--value", required=True)
    parser.add_argument("--object-type", required=True)
    parser.add_argument("--canonical-name", required=True)

    parser.add_argument("--source-id", required=True)
    parser.add_argument("--reconciliation-id", required=True)
    parser.add_argument("--match-id", required=True)
    parser.add_argument("--passport-id", required=True)
    parser.add_argument("--new-evidence-ref", required=True)

    parser.add_argument("--c2-target")
    parser.add_argument("--run-id")
    parser.add_argument("--batch-id")
    parser.add_argument("--attempt-id")
    parser.add_argument("--result-id")

    args = parser.parse_args()

    admission = json.loads(
        Path(args.admission).read_text(encoding="utf-8")
    )

    candidate = {
        "record_id": args.record_id,
        "value": args.value,
        "object_type": args.object_type,
        "canonical_name": args.canonical_name,
    }

    approved_candidate = {
        "decision_result": "NEW_APPROVED",
        "candidate": candidate,
        "provenance": {
            "source_id": args.source_id,
            "reconciliation_id": args.reconciliation_id,
            "match_id": args.match_id,
        },
        "traceability": {
            "source_id": args.source_id,
            "match_id": args.match_id,
            "passport_id": args.passport_id,
        },
        "approved_candidate_hash": sha256_json(candidate),
        "new_evidence_ref": args.new_evidence_ref,
    }

    c1_input = execute_c1_from_admission(
        admission,
        approved_candidate,
    )

    c1_result = canonize(c1_input)

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(
            c1_result,
            ensure_ascii=False,
            indent=2,
        ) + "\n",
        encoding="utf-8",
    )

    result = {
        "c1_status": c1_result["status"],
        "object_id": c1_result["object_id"],
        "c1_output": str(output),
        "c2_status": "NOT_REQUESTED",
        "c2_target": None,
    }

    if args.c2_target:
        required_c2 = {
            "--run-id": args.run_id,
            "--batch-id": args.batch_id,
            "--attempt-id": args.attempt_id,
            "--result-id": args.result_id,
        }

        missing = [
            name
            for name, value in required_c2.items()
            if not value
        ]

        if missing:
            raise SystemExit(
                "C2_METADATA_REQUIRED: " + ", ".join(missing)
            )

        payload = {
            **c1_result,
            "run_id": args.run_id,
            "source_id": args.source_id,
            "batch_id": args.batch_id,
            "stage_id": "C2_CMOC_WRITE",
            "attempt_id": args.attempt_id,
            "result_id": args.result_id,
        }

        c2 = ProductionCmocWriter(
            Path(args.c2_target)
        ).write(payload)

        result["c2_status"] = c2.status
        result["c2_target"] = args.c2_target

    print(
        json.dumps(
            result,
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
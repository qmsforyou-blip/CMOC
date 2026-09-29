from __future__ import annotations

import argparse
import json
from pathlib import Path

from production_cmoc_writer import ProductionCmocWriter


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--c1", required=True)
    parser.add_argument("--target", required=True)
    args = parser.parse_args()

    c1 = json.loads(Path(args.c1).read_text(encoding="utf-8"))

    payload = {
        **c1,
        "run_id": "RUN-PILOT-010-SRC-010-LAB003-T0002-T0005-R2",
        "source_id": "SRC-010",
        "batch_id": "BATCH-SRC-010-C2-001",
        "stage_id": "C2_CMOC_WRITE",
        "attempt_id": "ATTEMPT-SRC-010-MAT-PAS-021-C2-001",
        "result_id": "RESULT-SRC-010-MAT-PAS-021-C2-001",
    }

    result = ProductionCmocWriter(Path(args.target)).write(payload)

    print(json.dumps({
        "status": result.status,
        "object_id": result.object_id,
        "basis": result.basis,
        "target": args.target,
        "boundary": {
            "semantic_decision": "NOT_PERFORMED",
            "cmoc_write": "PERFORMED" if result.status == "CMOC_WRITE_ACCEPTED" else "NOT_PERFORMED",
            "object_index_write": "NONE",
        },
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
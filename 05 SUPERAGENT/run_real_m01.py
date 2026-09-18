"""Run M01 on a SOURCE_PACKAGE JSON file using the live LLM adapter.

Usage:
  LLM_API_KEY=... LLM_MODEL=... python run_real_m01.py SOURCE-PACKAGE.json
Optional:
  LLM_BASE_URL=https://openrouter.ai/api/v1
""" 
from __future__ import annotations

import json
import sys

from m01_integration import build_m01_handler
from mvp_runner import Contract, Superagent


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python run_real_m01.py SOURCE-PACKAGE.json", file=sys.stderr)
        return 2

    with open(sys.argv[1], encoding="utf-8") as f:
        package = json.load(f)

    source_id = package["source_id"]
    contracts = {
        "M01": Contract(
            "M01",
            {"SOURCE_PACKAGE"},
            "EXTRACTION_RECORDS",
            {"source_id", "batch_id", "records", "traceability", "ref"},
        )
    }
    runner = Superagent(contracts, {"M01": build_m01_handler()})
    initial = {
        "type": "SOURCE_PACKAGE",
        "source_id": source_id,
        "source_package": package,
        "traceability": {
            "source_id": source_id,
            "package_id": package.get("package_id"),
            "work_scope": package.get("work_scope"),
        },
        "ref": package.get("package_id", "SOURCE_PACKAGE"),
    }
    result = runner.run_chain(
        "RUN-REAL-M01-001",
        {"source_id": source_id},
        initial,
        ["M01"],
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] == "ACCEPT" else 1


if __name__ == "__main__":
    raise SystemExit(main())

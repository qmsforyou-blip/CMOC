"""Production M01 handler for MVP-SUPERAGENT-001."""

from __future__ import annotations

from typing import Callable, Dict, Any

from m01_llm import extract


def build_m01_handler(extractor: Callable[[dict], list] = extract):
    """Return an M01 MACHINE handler suitable for mvp_runner.Superagent."""

    def m01(source_package_input: Dict[str, Any], batch) -> Dict[str, Any]:
        package = source_package_input["source_package"]
        records = extractor(package)
        return {
            "status": "ACCEPT",
            "type": "EXTRACTION_RECORDS",
            "source_id": batch.source_id,
            "batch_id": batch.batch_id,
            "records": records,
            "traceability": {
                "source_id": batch.source_id,
                "batch_id": batch.batch_id,
                "locations": [r["location"] for r in records],
                "source_package": package.get("package_id", "SOURCE_PACKAGE"),
            },
            "ref": f"{batch.batch_id}:OUTPUT",
        }

    return m01

"""Acceptance test: failed production stage -> resume -> completion."""

from __future__ import annotations

import json
import tempfile
from pathlib import Path

from production_adapter_runtime import ProductionAdapter, ProductionAdapterRegistry
from run_superagent import start_run


def package() -> dict:
    return {
        "package_id": "SOURCE-PACKAGE-FAILED-RECOVERY-001",
        "source_id": "SRC-FAILED-RECOVERY-001",
        "source_name": "FAILED RECOVERY TEST SOURCE",
        "source_package_status": "COMPLETE",
        "fragments": [{"fragment_id": "F-001", "ref": "fragment-001"}],
    }


def main() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        source_path = root / "source_package.json"
        db_path = root / "runtime.sqlite"
        source_path.write_text(json.dumps(package()), encoding="utf-8")

        registry = ProductionAdapterRegistry()
        calls: list[str] = []
        fail_once = {"value": True}

        def implementation(envelope):
            calls.append(envelope["attempt_id"])
            if fail_once["value"]:
                fail_once["value"] = False
                raise RuntimeError("SIMULATED_PRODUCTION_FAILURE")
            return {**envelope, "status": "ACCEPT"}

        registry.register(ProductionAdapter("DISCOVERY", implementation))

        first = start_run(
            str(source_path), str(db_path), "RUN-FAILED-RECOVERY-001", registry
        )
        assert first["status"] == "ADAPTER_EXECUTION_FAILED"

        resumed = start_run(
            str(source_path),
            str(db_path),
            "RUN-FAILED-RECOVERY-001",
            registry,
            resume=True,
        )
        assert resumed["status"] == "PIPELINE_COMPLETED"
        assert len(calls) == 2
        assert calls[0] == "ATTEMPT-DISCOVERY-RUN-FAILED-RECOVERY-001"
        assert calls[1].startswith("ATTEMPT-DISCOVERY-RUN-FAILED-RECOVERY-001-RESUME-")

    print("RUNTIME FAILED-RECOVERY TEST: PASS")


if __name__ == "__main__":
    main()

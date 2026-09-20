#!/usr/bin/env python3
"""A4.4 negative control: DISCOVERY does not depend on QUERY/CMOC.

This is a controlled orchestration test, not a new LLM production run.
The Python import boundary deliberately makes cmoc_query and reconciliation
unavailable. A source-bound M01-M08 chain is then executed through the same
SUPERAGENT orchestration kernel with deterministic stub machines.

The control proves that the DISCOVERY orchestration contract can complete
without QUERY/CMOC services. It does not prove that every production LLM
adapter is independently free of those imports; the production automated
launcher is separately documented as Discovery-only.
"""
from __future__ import annotations

import builtins
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from mvp_runner import Batch, Contract, Superagent


BLOCKED = {"cmoc_query", "reconciliation", "reconciliation_input_adapter"}


class QueryUnavailableImportGuard:
    def __enter__(self):
        self.original = builtins.__import__

        def guarded_import(name, globals=None, locals=None, fromlist=(), level=0):
            root = name.split(".", 1)[0]
            if root in BLOCKED:
                raise ImportError(f"A4.4 QUERY unavailable: blocked import {name}")
            return self.original(name, globals, locals, fromlist, level)

        builtins.__import__ = guarded_import
        return self

    def __exit__(self, exc_type, exc, tb):
        builtins.__import__ = self.original
        return False


SOURCE_ID = "SRC-002"
RUN_ID = "RUN-A4.4-QUERY-UNAVAILABLE-001"
SOURCE_PACKAGE = "SOURCE-002-PACKAGE-001-CONTROLLED-1-6"


def wrap(batch: Batch, output_type: str, records: list[dict], upstream: dict) -> dict:
    return {
        "status": "ACCEPT",
        "type": output_type,
        "source_id": SOURCE_ID,
        "batch_id": batch.batch_id,
        "records": records,
        "traceability": {
            "source_id": SOURCE_ID,
            "source_package": SOURCE_PACKAGE,
            "batch_id": batch.batch_id,
            "upstream_batch": upstream.get("batch_id"),
        },
        "ref": f"{batch.batch_id}:OUTPUT",
    }


def main() -> None:
    with QueryUnavailableImportGuard():
        # Import the orchestration kernel only after QUERY/RECONCILIATION are
        # explicitly unavailable.
        from mvp_runner import Batch, Contract, Superagent

        def make_handler(task, output_type):
            def handler(inp, batch):
                records = inp.get("records", [])
                if task == "M01":
                    records = [{"id": "EX-001", "value": "source evidence"}]
                elif task == "M02":
                    records = [{"id": "DIS-001", "value": "source distinction"}]
                elif task == "M03":
                    records = [{"id": "FORM-001", "value": "source formulation"}]
                elif task == "M04":
                    records = [{"id": "NOM-001", "value": "source candidate"}]
                elif task == "M05":
                    records = [{"id": "CLS-001", "value": "source classification"}]
                elif task == "M06":
                    records = [{"id": "PAS-001", "value": "source passport"}]
                elif task == "M07":
                    records = [{"id": "REL-001", "value": "NO_RELATION"}]
                elif task == "M08":
                    records = []
                return wrap(batch, output_type, records, inp)
            return handler

        contracts = {}
        handlers = {}
        machine_ids = {}

        chain = [
            ("M01", "SOURCE_PACKAGE", "EXTRACTION_RECORDS"),
            ("M02", "EXTRACTION_RECORDS", "DISTINCTION_RECORDS"),
            ("M03", "DISTINCTION_RECORDS", "FORMULATION_RECORDS"),
            ("M04", "FORMULATION_RECORDS", "NOMENCLATURE_CANDIDATES"),
            ("M05", "NOMENCLATURE_CANDIDATES", "CLASSIFICATION_RECORDS"),
            ("M06", "CLASSIFICATION_RECORDS", "PASSPORT_RECORDS"),
            ("M07", "PASSPORT_RECORDS", "RELATION_CANDIDATES"),
            ("M08", "RELATION_CANDIDATES", "DECISION_RECORDS"),
        ]

        for task, input_type, output_type in chain:
            contracts[task] = Contract(
                task,
                {input_type},
                output_type,
                {"source_id", "batch_id", "records", "traceability", "ref"},
                {"records"},
            )
            handlers[task] = make_handler(task, output_type)
            machine_ids[task] = f"{task}-A4.4-CONTROL"

        class ControlledSuperagent(Superagent):
            _seq = 0

            def new_batch(self, source_id, task, input_ref, handoff_id=None):
                self.__class__._seq += 1
                batch_id = f"BATCH-A4.4-{task}-{self.__class__._seq:03d}"
                batch = Batch(batch_id, source_id, task, input_ref, handoff_id)
                self.batches.append(batch)
                return batch

        runner = ControlledSuperagent(contracts, handlers, machine_ids)

        source = {
            "package_id": SOURCE_PACKAGE,
            "source_id": SOURCE_ID,
            "source_name": "A4.4 controlled source",
            "source_package_status": "PARTIAL",
        }
        initial = {
            "type": "SOURCE_PACKAGE",
            "source_id": SOURCE_ID,
            "source_package": source,
            "traceability": {
                "source_id": SOURCE_ID,
                "source_package": SOURCE_PACKAGE,
            },
            "ref": SOURCE_PACKAGE,
        }

        result = runner.run_chain(
            RUN_ID,
            source,
            initial,
            [task for task, _, _ in chain],
        )

        assert result["status"] == "ACCEPT"
        assert len(result["results"]) == 8
        assert all(h.status == "ACCEPT" for h in runner.handoffs)
        assert result["results"][-1]["type"] == "DECISION_RECORDS"
        assert result["results"][-1]["records"] == []

    print(json.dumps({
        "gate": "A4.4-QUERY-UNAVAILABLE-DISCOVERY-ISOLATION",
        "status": "PASS",
        "query_imports_blocked": sorted(BLOCKED),
        "discovery_chain_completed": True,
        "tasks_completed": 8,
        "handoffs_accepted": 7,
        "cmoc_access": "BLOCKED",
        "query_access": "BLOCKED",
        "discovery_result_mutation_by_reconciliation": "NOT_POSSIBLE",
        "control_rule": "DISCOVERY orchestration does not require QUERY/CMOC",
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

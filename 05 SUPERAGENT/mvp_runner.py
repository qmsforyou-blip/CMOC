"""MVP-SUPERAGENT-001 runner v0.1.

Deterministic orchestration kernel. It does not contain source-specific knowledge.
Semantic machine implementations are injected as handlers.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional
import json
import sys

STATUS_ACCEPT = "ACCEPT"
STATUS_REJECT = "REJECT"
STATUS_STOP = "STOP"
STATUS_ESCALATE = "ESCALATE"

@dataclass
class Contract:
    task: str
    accepted_inputs: set[str]
    output_type: str
    required_output_fields: set[str]
    required_input_fields: set[str] = field(default_factory=set)

@dataclass
class Batch:
    batch_id: str
    source_id: str
    task: str
    input_ref: str
    handoff_id: Optional[str] = None
    output: Optional[dict] = None

@dataclass
class Handoff:
    handoff_id: str
    source_id: str
    from_task: str
    to_task: str
    output_ref: str
    input_type: str
    traceability: dict
    status: str
    reason: str = ""

@dataclass
class JournalEntry:
    run_id: str
    source_id: str
    task: str
    batch_id: Optional[str]
    input_ref: str
    output_ref: Optional[str]
    status: str
    qc_result: str
    handoff_result: str
    reason: str = ""
    handoff_id: Optional[str] = None
    machine_id: Optional[str] = None

class Superagent:
    """Orchestration kernel; semantic production remains in injected MACHINE handlers."""
    def __init__(self, contracts: Dict[str, Contract], handlers: Dict[str, Callable[[dict, Batch], dict]], machine_ids: Optional[Dict[str, str]] = None):
        self.contracts = contracts
        self.handlers = handlers
        self.machine_ids = machine_ids or {task: f"{task}-DEMO" for task in handlers}
        self.journal: List[JournalEntry] = []
        self._batch_seq: Dict[str, int] = {}
        self._handoff_seq: Dict[str, int] = {}
        self.handoffs: List[Handoff] = []
        self.batches: List[Batch] = []

    def new_handoff_id(self, source_id: str, from_task: str, to_task: str) -> str:
        key = f"{source_id}-{from_task}-{to_task}"
        self._handoff_seq[key] = self._handoff_seq.get(key, 0) + 1
        return f"HANDOFF-{source_id}-{from_task}-{to_task}-{self._handoff_seq[key]:03d}"

    def new_batch(self, source_id: str, task: str, input_ref: str, handoff_id: Optional[str] = None) -> Batch:
        key = f"{source_id}-{task}"
        self._batch_seq[key] = self._batch_seq.get(key, 0) + 1
        batch = Batch(f"BATCH-{source_id}-{task}-{self._batch_seq[key]:03d}", source_id, task, input_ref, handoff_id)
        self.batches.append(batch)
        return batch

    def check_source_package(self, source_package: dict, source_id: str) -> tuple[bool, str]:
        required = {"package_id", "source_id", "source_name", "fragments"}
        missing = sorted(required - set(source_package))
        if missing:
            return False, f"MISSING_SOURCE_PACKAGE_FIELDS: {missing}"
        if source_package["source_id"] != source_id:
            return False, "SOURCE_PACKAGE_SOURCE_ID_MISMATCH"
        status = source_package.get("source_package_status", "UNKNOWN")
        if status not in {"COMPLETE", "PARTIAL", "UNKNOWN"}:
            return False, f"INVALID_SOURCE_PACKAGE_STATUS: {status}"
        if not isinstance(source_package["fragments"], list):
            return False, "SOURCE_PACKAGE_FRAGMENTS_NOT_LIST"
        return True, status

    def check_input(self, task: str, inp: dict) -> tuple[bool, str]:
        c = self.contracts.get(task)
        if not c:
            return False, "REQUEST_CONTRACT"
        typ = inp.get("type")
        if typ not in c.accepted_inputs:
            return False, f"TYPE_MISMATCH: {typ} -> {sorted(c.accepted_inputs)}"
        if not inp.get("source_id"):
            return False, "MISSING_SOURCE_ID"
        if not inp.get("traceability"):
            return False, "MISSING_TRACEABILITY"
        missing = sorted(c.required_input_fields - set(inp))
        if missing:
            return False, f"MISSING_REQUIRED_INPUT_FIELDS: {missing}"
        if "source_package" in c.required_input_fields:
            ok, reason = self.check_source_package(inp["source_package"], source["source_id"])
            if not ok:
                return False, reason
        if missing:
            return False, f"MISSING_REQUIRED_INPUT_FIELDS: {missing}"
        return True, "PASS"

    def check_output(self, task: str, out: dict) -> tuple[bool, str]:
        c = self.contracts[task]
        if out.get("type") != c.output_type:
            return False, f"OUTPUT_TYPE_MISMATCH: {out.get('type')} != {c.output_type}"
        missing = sorted(c.required_output_fields - set(out))
        if missing:
            return False, f"MISSING_REQUIRED_FIELDS: {missing}"
        if not out.get("traceability"):
            return False, "MISSING_TRACEABILITY"
        return True, "PASS"

    def create_handoff(self, run_id: str, source: dict, from_task: str, to_task: str, output: dict) -> Handoff:
        handoff_id = self.new_handoff_id(source["source_id"], from_task, to_task)
        contract = self.contracts.get(to_task)
        input_type = output.get("type", "UNKNOWN")
        traceability = output.get("traceability", {})
        output_ref = output.get("ref", "UNKNOWN")
        if not contract:
            handoff = Handoff(handoff_id, source["source_id"], from_task, to_task, output_ref,
                              input_type, traceability, STATUS_REJECT, "REQUEST_CONTRACT")
        elif input_type not in contract.accepted_inputs:
            handoff = Handoff(handoff_id, source["source_id"], from_task, to_task, output_ref,
                              input_type, traceability, STATUS_REJECT,
                              f"TYPE_MISMATCH: {input_type} -> {sorted(contract.accepted_inputs)}")
        elif not output.get("source_id"):
            handoff = Handoff(handoff_id, source["source_id"], from_task, to_task, output_ref,
                              input_type, traceability, STATUS_REJECT, "MISSING_SOURCE_ID")
        elif not traceability:
            handoff = Handoff(handoff_id, source["source_id"], from_task, to_task, output_ref,
                              input_type, traceability, STATUS_REJECT, "MISSING_TRACEABILITY")
        else:
            handoff = Handoff(handoff_id, source["source_id"], from_task, to_task, output_ref,
                              input_type, traceability, STATUS_ACCEPT, "READY")
        self.handoffs.append(handoff)
        self.journal.append(JournalEntry(run_id, source["source_id"], f"{from_task}->{to_task}",
                                         None, output_ref, output_ref, handoff.status,
                                         "PASS", handoff.status, handoff.reason, handoff.handoff_id))
        return handoff

    def execute(self, run_id: str, source: dict, task: str, inp: dict, handoff_id: Optional[str] = None) -> dict:
        ok, reason = self.check_input(task, inp)
        if not ok:
            self.journal.append(JournalEntry(run_id, source["source_id"], task, None,
                                             inp.get("ref","UNKNOWN"), None, STATUS_REJECT,
                                             "NOT_RUN", "NOT_CREATED", reason))
            return {"status": STATUS_REJECT, "reason": reason, "task": task, "batch_id": None}

        batch = self.new_batch(source["source_id"], task, inp.get("ref","INPUT"), handoff_id)
        handler = self.handlers.get(task)
        machine_id = self.machine_ids.get(task)
        if not handler:
            reason = "MACHINE_NOT_REGISTERED"
            self.journal.append(JournalEntry(run_id, source["source_id"], task, batch.batch_id,
                                             inp.get("ref","INPUT"), None, STATUS_REJECT,
                                             "NOT_RUN", "NOT_CREATED", reason))
            return {"status": STATUS_REJECT, "reason": reason, "task": task, "batch_id": batch.batch_id}

        out = handler(inp, batch)
        ok, reason = self.check_output(task, out)
        if not ok:
            self.journal.append(JournalEntry(run_id, source["source_id"], task, batch.batch_id,
                                             inp.get("ref","INPUT"), None, STATUS_REJECT,
                                             "FAIL", "STOP", reason, None, machine_id))
            return {"status": STATUS_REJECT, "reason": reason, "task": task, "batch_id": batch.batch_id}

        batch.output = out
        out["batch_id"] = batch.batch_id
        self.journal.append(JournalEntry(run_id, source["source_id"], task, batch.batch_id,
                                         inp.get("ref","INPUT"), out.get("ref"),
                                         STATUS_ACCEPT, "PASS", "READY", "", None, machine_id))
        return out

    def run_chain(self, run_id: str, source: dict, initial: dict, tasks: List[str]) -> dict:
        current = initial
        current_handoff_id = None
        results = []
        for i, task in enumerate(tasks):
            result = self.execute(run_id, source, task, current, current_handoff_id)
            results.append(result)
            if result.get("status") != STATUS_ACCEPT:
                return {"status": result.get("status"), "results": results, "journal": self.journal}
            if i < len(tasks) - 1:
                next_task = tasks[i + 1]
                handoff = self.create_handoff(run_id, source, task, next_task, result)
                if handoff.status != STATUS_ACCEPT:
                    return {"status": STATUS_REJECT, "results": results,
                            "journal": self.journal, "handoff": handoff}
                current_handoff_id = handoff.handoff_id
                current = {
                    **result,
                    "type": handoff.input_type,
                    "source_id": handoff.source_id,
                    "traceability": handoff.traceability,
                    "ref": handoff.output_ref,
                }
            else:
                current = result
        return {"status": STATUS_ACCEPT, "results": results, "journal": self.journal}

def build_demo_runner() -> Superagent:
    contracts = {
        "M01": Contract("M01", {"SOURCE_PACKAGE"}, "EXTRACTION_RECORDS",
                        {"source_id","batch_id","records","traceability","ref"},
                        {"source_package"}),
        "M02": Contract("M02", {"EXTRACTION_RECORDS","SOURCE_PACKAGE"}, "DISTINCTION_RECORDS",
                        {"source_id","batch_id","records","traceability","ref"}),
        "M03": Contract("M03", {"DISTINCTION_RECORDS","SOURCE_PACKAGE"}, "FORMULATION_RECORDS",
                        {"source_id","batch_id","records","traceability","ref"}),
        "M04": Contract("M04", {"FORMULATION_RECORDS"}, "NOMENCLATURE_CANDIDATES",
                        {"source_id","batch_id","records","traceability","ref"}),
    }

    def m01(inp: dict, b: Batch) -> dict:
        records = inp["records"]
        return {"status": STATUS_ACCEPT, "type":"EXTRACTION_RECORDS",
                "source_id":b.source_id, "batch_id":b.batch_id, "records":records,
                "traceability":{"source_id":b.source_id,"batch_id":b.batch_id,
                                 "locations":[r["location"] for r in records]},
                "ref":f"{b.batch_id}:OUTPUT"}

    def m02(inp: dict, b: Batch) -> dict:
        records=[{"id":f"DIS-{i+1:03d}","source_record":r["id"],
                  "distinction":r["distinction"]} for i,r in enumerate(inp["records"])]
        return {"status":STATUS_ACCEPT, "type":"DISTINCTION_RECORDS",
                "source_id":b.source_id, "batch_id":b.batch_id, "records":records,
                "traceability":{"source_id":b.source_id,"batch_id":b.batch_id,
                                 "from":inp["traceability"]},
                "ref":f"{b.batch_id}:OUTPUT"}

    def m03(inp: dict, b: Batch) -> dict:
        records=[]
        for r in inp["records"]:
            for level in ("INTUITIVE","ENGINEERING","CANONICAL_FORMULATION"):
                records.append({"id":f"FORM-{len(records)+1:03d}",
                                "source_record":r["id"],"level":level,
                                "formulation":f"{level}: {r['distinction']}"})
        return {"status":STATUS_ACCEPT, "type":"FORMULATION_RECORDS",
                "source_id":b.source_id, "batch_id":b.batch_id, "records":records,
                "traceability":{"source_id":b.source_id,"batch_id":b.batch_id,
                                 "from":inp["traceability"]},
                "ref":f"{b.batch_id}:OUTPUT"}

    return Superagent(contracts, {"M01":m01,"M02":m02,"M03":m03}, {"M01":"M01-DEMO","M02":"M02-DEMO","M03":"M03-DEMO"})

def main() -> int:
    payload = json.load(sys.stdin)
    runner = build_demo_runner()
    source = payload["source"]
    initial = payload["input"]
    tasks = payload.get("tasks", ["M01","M02","M03"])
    result = runner.run_chain(payload.get("run_id","RUN-LOCAL-001"), source, initial, tasks)
    json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
    return 0 if result["status"] == STATUS_ACCEPT else 1

if __name__ == "__main__":
    raise SystemExit(main())

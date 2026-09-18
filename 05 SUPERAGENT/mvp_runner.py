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

@dataclass
class Batch:
    batch_id: str
    source_id: str
    task: str
    input_ref: str
    output: Optional[dict] = None

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

class Superagent:
    def __init__(self, contracts: Dict[str, Contract], handlers: Dict[str, Callable[[dict, Batch], dict]]):
        self.contracts = contracts
        self.handlers = handlers
        self.journal: List[JournalEntry] = []
        self._batch_seq: Dict[str, int] = {}

    def new_batch(self, source_id: str, task: str, input_ref: str) -> Batch:
        key = f"{source_id}-{task}"
        self._batch_seq[key] = self._batch_seq.get(key, 0) + 1
        return Batch(f"BATCH-{source_id}-{task}-{self._batch_seq[key]:03d}", source_id, task, input_ref)

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

    def execute(self, run_id: str, source: dict, task: str, inp: dict) -> dict:
        ok, reason = self.check_input(task, inp)
        if not ok:
            self.journal.append(JournalEntry(run_id, source["source_id"], task, None,
                                             inp.get("ref","UNKNOWN"), None, STATUS_REJECT,
                                             "NOT_RUN", "NOT_CREATED", reason))
            return {"status": STATUS_REJECT, "reason": reason, "task": task, "batch_id": None}

        batch = self.new_batch(source["source_id"], task, inp.get("ref","INPUT"))
        handler = self.handlers.get(task)
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
                                             "FAIL", "STOP", reason))
            return {"status": STATUS_REJECT, "reason": reason, "task": task, "batch_id": batch.batch_id}

        batch.output = out
        out["batch_id"] = batch.batch_id
        self.journal.append(JournalEntry(run_id, source["source_id"], task, batch.batch_id,
                                         inp.get("ref","INPUT"), out.get("ref"),
                                         STATUS_ACCEPT, "PASS", "READY", ""))
        return out

    def run_chain(self, run_id: str, source: dict, initial: dict, tasks: List[str]) -> dict:
        current = initial
        results = []
        for task in tasks:
            result = self.execute(run_id, source, task, current)
            results.append(result)
            if result.get("status") != STATUS_ACCEPT:
                return {"status": result.get("status"), "results": results, "journal": self.journal}
            current = {
                **result,
                "type": result["type"],
                "source_id": source["source_id"],
                "traceability": result["traceability"],
                "ref": result["ref"],
            }
        return {"status": STATUS_ACCEPT, "results": results, "journal": self.journal}

def build_demo_runner() -> Superagent:
    contracts = {
        "M01": Contract("M01", {"SOURCE_PACKAGE"}, "EXTRACTION_RECORDS",
                        {"source_id","batch_id","records","traceability","ref"}),
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

    return Superagent(contracts, {"M01":m01,"M02":m02,"M03":m03})

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

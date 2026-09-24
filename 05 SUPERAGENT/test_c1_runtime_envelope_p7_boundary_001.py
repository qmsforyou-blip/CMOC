import copy
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from admission import admit_new, execute_c1_from_admission
from c1_canonization import canonize
from production_cmoc_writer import ProductionCmocWriter


def approved_candidate():
    candidate = {
        "record_id": "REC-C1-P7-001",
        "canonical_name": "C1 P7 Integration Test",
        "object_type": "TERM",
        "value": "integration",
    }
    raw = json.dumps(candidate, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    candidate_hash = hashlib.sha256(raw.encode("utf-8")).hexdigest()

    return {
        "decision_result": "NEW_APPROVED",
        "candidate_id": "CAND-C1-P7-001",
        "source_id": "SRC-C1-P7-001",
        "candidate": candidate,
        "provenance": {
            "source_id": "SRC-C1-P7-001",
            "discovery_run": "RUN-C1-P7-001",
        },
        "traceability": {
            "decision_id": "DEC-C1-P7-001",
            "match_id": "MAT-C1-P7-001",
            "source_id": "SRC-C1-P7-001",
        },
        "approved_candidate_hash": candidate_hash,
        "new_evidence_ref": "EVID-C1-P7-001",
    }


def build_runtime_envelope(canonical, admission):
    body = admission["admission"]
    return {
        **copy.deepcopy(canonical),
        "run_id": "RUN-C1-P7-001",
        "source_id": body["source_id"],
        "batch_id": "BATCH-C1-P7-001",
        "stage_id": "C2_CMOC_WRITE",
        "attempt_id": "ATT-C1-P7-001",
        "result_id": "CANON-C1-P7-001",
    }


class TestC1RuntimeEnvelopeP7Boundary001(unittest.TestCase):
    def setUp(self):
        self.decision = {
            "type": "DECISION",
            "decision": {
                "decision_id": "DEC-C1-P7-001",
                "decision_result": "ADMIT_NEW",
                "match_id": "MAT-C1-P7-001",
                "source_id": "SRC-C1-P7-001",
                "basis": "NEW_APPROVED_BY_HUMAN",
                "decided_at": "2026-09-24T16:00:00+05:00",
                "traceability": {
                    "decision_id": "DEC-C1-P7-001",
                    "match_id": "MAT-C1-P7-001",
                    "source_id": "SRC-C1-P7-001",
                },
            },
        }

    def test_admission_c1_runtime_envelope_p7(self):
        admission = admit_new(self.decision)
        candidate = approved_candidate()
        candidate_before = copy.deepcopy(candidate)

        c1_input = execute_c1_from_admission(admission, candidate)
        canonical = canonize(c1_input)

        self.assertEqual(canonical["status"], "CANONICALIZATION_READY")
        self.assertEqual(
            canonical["traceability"],
            candidate["traceability"],
        )
        self.assertEqual(
            canonical["approved_candidate_hash"],
            candidate["approved_candidate_hash"],
        )

        envelope = build_runtime_envelope(canonical, admission)
        canonical_before = copy.deepcopy(canonical)

        with tempfile.TemporaryDirectory(prefix="cmoc-c1-p7-") as tmp:
            writer = ProductionCmocWriter(Path(tmp))
            result = writer.write(envelope)

            self.assertEqual(result.status, "CMOC_WRITE_ACCEPTED")
            target = Path(tmp) / f"{canonical['object_id']}.md"
            self.assertTrue(target.exists())

            persisted = writer._decode(target.read_text(encoding="utf-8"))

            for field in (
                "object_id",
                "object_type",
                "canonical_name",
                "canonical_representation",
                "provenance",
                "traceability",
                "approved_candidate_hash",
            ):
                self.assertEqual(
                    persisted[field],
                    canonical[field],
                    msg=f"canonical field changed: {field}",
                )

            for field in (
                "run_id",
                "source_id",
                "batch_id",
                "stage_id",
                "attempt_id",
                "result_id",
            ):
                self.assertTrue(persisted.get(field), field)

        self.assertEqual(candidate, candidate_before)
        self.assertEqual(canonical, canonical_before)

    def test_runtime_envelope_does_not_replace_canonical_identity(self):
        admission = admit_new(self.decision)
        canonical = canonize(execute_c1_from_admission(admission, approved_candidate()))
        envelope = build_runtime_envelope(canonical, admission)

        self.assertEqual(envelope["object_id"], canonical["object_id"])
        self.assertEqual(
            envelope["canonical_representation"],
            canonical["canonical_representation"],
        )
        self.assertNotEqual(envelope["run_id"], envelope["object_id"])

    def test_p7_duplicate_is_idempotent_after_c1_envelope(self):
        admission = admit_new(self.decision)
        canonical = canonize(execute_c1_from_admission(admission, approved_candidate()))
        envelope = build_runtime_envelope(canonical, admission)

        with tempfile.TemporaryDirectory(prefix="cmoc-c1-p7-idem-") as tmp:
            writer = ProductionCmocWriter(Path(tmp))
            first = writer.write(envelope)
            second = writer.write(envelope)

            self.assertEqual(first.status, "CMOC_WRITE_ACCEPTED")
            self.assertEqual(second.status, "ALREADY_PERSISTED")

    def test_p7_never_receives_unapproved_c1_state(self):
        admission = admit_new(self.decision)
        candidate = approved_candidate()
        candidate["decision_result"] = "ADMIT_NEW"

        with self.assertRaises(Exception):
            execute_c1_from_admission(admission, candidate)


if __name__ == "__main__":
    unittest.main()

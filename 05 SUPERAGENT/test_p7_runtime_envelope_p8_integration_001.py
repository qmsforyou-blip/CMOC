import copy
import tempfile
import unittest
from pathlib import Path

from production_cmoc_writer import ProductionCmocWriter
from production_object_index_synchronizer import ProductionObjectIndexSynchronizer


ROOT = Path(__file__).resolve().parents[1]
TEST_OBJECT_ID = "OC-0001"


def canonical_payload():
    return {
        "status": "CANONICALIZATION_READY",
        "run_id": "RUN-P7-P8-001",
        "source_id": "SRC-P7-P8-001",
        "batch_id": "BATCH-P7-P8-001",
        "stage_id": "C2_CMOC_WRITE",
        "attempt_id": "ATT-P7-P8-001",
        "result_id": "CANON-P7-P8-001",
        "object_id": TEST_OBJECT_ID,
        "object_type": "ORGANIZATIONAL_CONSTRUCTION",
        "canonical_name": "P7 P8 integration fixture",
        "canonical_representation": {
            "kind": "INTEGRATION_FIXTURE",
            "value": "P7_TO_P8_RUNTIME_ENVELOPE",
        },
        "provenance": {
            "source_id": "SRC-P7-P8-001",
            "basis": "P7-P8-INTEGRATION",
        },
        "traceability": {
            "source_id": "SRC-P7-P8-001",
            "decision_id": "DEC-P7-P8-001",
            "admission_id": "ADM-P7-P8-001",
        },
        "new_evidence_ref": "EVID-P7-P8-001",
        "approved_candidate_hash": "HASH-P7-P8-001",
    }


def build_p8_envelope(canonical, p7_result):
    if p7_result.status != "CMOC_WRITE_ACCEPTED":
        raise ValueError(
            "P8 envelope may be constructed only from CMOC_WRITE_ACCEPTED"
        )
    if not p7_result.object_id:
        raise ValueError("accepted P7 result must contain object_id")

    return {
        "status": p7_result.status,
        "run_id": canonical["run_id"],
        "source_id": canonical["source_id"],
        "batch_id": canonical["batch_id"],
        "stage_id": canonical["stage_id"],
        "attempt_id": canonical["attempt_id"],
        "result_id": p7_result.object_id + "/WRITE",
        "cmoc_write_id": "CMOC-WRITE-" + p7_result.object_id,
        "object_id": p7_result.object_id,
        "provenance": canonical["provenance"],
        "traceability": canonical["traceability"],
        "write_verification": True,
    }


class TestP7RuntimeEnvelopeP8Integration001(unittest.TestCase):
    def test_p7_to_runtime_envelope_to_p8(self):
        canonical = canonical_payload()
        canonical_before = copy.deepcopy(canonical)

        with tempfile.TemporaryDirectory(prefix="cmoc-p7-p8-") as tmp:
            writer = ProductionCmocWriter(Path(tmp))
            p7 = writer.write(canonical)

            self.assertEqual(p7.status, "CMOC_WRITE_ACCEPTED")
            self.assertEqual(p7.object_id, TEST_OBJECT_ID)

            envelope = build_p8_envelope(canonical, p7)
            envelope_before = copy.deepcopy(envelope)

            sync = ProductionObjectIndexSynchronizer(ROOT)
            p8 = sync.synchronize(envelope)

            self.assertEqual(p8.status, "ALREADY_SYNCHRONIZED")
            self.assertEqual(p8.object_id, TEST_OBJECT_ID)
            self.assertTrue(p8.verification["object_id_match"])
            self.assertEqual(
                p8.verification["builder_check"]["check"],
                "PASS",
            )
            self.assertTrue(p8.verification["index_bytes_unchanged"])

            self.assertEqual(canonical, canonical_before)
            self.assertEqual(envelope, envelope_before)

    def test_p7_failure_cannot_be_promoted_to_p8_success(self):
        canonical = canonical_payload()

        with tempfile.TemporaryDirectory(prefix="cmoc-p7-p8-reject-") as tmp:
            writer = ProductionCmocWriter(Path(tmp))
            invalid = copy.deepcopy(canonical)
            invalid["status"] = "CMOC_WRITE_REJECTED"

            p7 = writer.write(invalid)
            self.assertEqual(p7.status, "CMOC_WRITE_REJECTED")
            self.assertIsNone(p7.object_id)

            with self.assertRaises(ValueError):
                build_p8_envelope(invalid, p7)

    def test_p8_requires_p7_write_verification(self):
        canonical = canonical_payload()

        with tempfile.TemporaryDirectory(prefix="cmoc-p7-p8-verification-") as tmp:
            writer = ProductionCmocWriter(Path(tmp))
            p7 = writer.write(canonical)
            self.assertEqual(p7.status, "CMOC_WRITE_ACCEPTED")

            envelope = build_p8_envelope(canonical, p7)
            envelope["write_verification"] = False

            sync = ProductionObjectIndexSynchronizer(ROOT)
            p8 = sync.synchronize(envelope)

            self.assertEqual(p8.status, "INDEX_REJECTED")

    def test_p8_receives_p7_identity_unchanged(self):
        canonical = canonical_payload()

        with tempfile.TemporaryDirectory(prefix="cmoc-p7-p8-identity-") as tmp:
            writer = ProductionCmocWriter(Path(tmp))
            p7 = writer.write(canonical)
            envelope = build_p8_envelope(canonical, p7)

            self.assertEqual(envelope["object_id"], canonical["object_id"])
            self.assertEqual(envelope["object_id"], p7.object_id)
            self.assertNotEqual(envelope["object_id"], envelope["run_id"])


if __name__ == "__main__":
    unittest.main()

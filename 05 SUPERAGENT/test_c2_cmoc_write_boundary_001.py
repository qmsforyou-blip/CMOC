import copy
import hashlib
import json
import unittest


class SyntheticCMOCWriter:
    """Synthetic persistence stub for C2 boundary acceptance only."""

    def __init__(self):
        self.objects = {}

    def write(self, canonical):
        if not isinstance(canonical, dict):
            return {"status": "CMOC_WRITE_REJECTED", "basis": "NOT_ELIGIBLE"}

        if canonical.get("status") != "CANONICALIZATION_READY":
            return {"status": "CMOC_WRITE_REJECTED", "basis": "NOT_ELIGIBLE"}

        required = (
            "object_id",
            "object_type",
            "canonical_representation",
            "provenance",
            "traceability",
            "approved_candidate_hash",
        )
        if any(not canonical.get(field) for field in required):
            return {"status": "CMOC_WRITE_REJECTED", "basis": "MISSING_REQUIRED_DATA"}

        if canonical.get("existing_object_mutation"):
            return {
                "status": "CMOC_WRITE_REJECTED",
                "basis": "EXISTING_OBJECT_WRITE_CONFLICT",
            }

        if canonical.get("relations"):
            return {
                "status": "CMOC_WRITE_REJECTED",
                "basis": "UNSUPPORTED_RELATION_CREATION",
            }

        object_id = canonical["object_id"]
        payload = copy.deepcopy(canonical["canonical_representation"])
        fingerprint = hashlib.sha256(
            json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
        ).hexdigest()

        if object_id in self.objects:
            existing = self.objects[object_id]
            if existing["fingerprint"] == fingerprint:
                return {
                    "status": "ALREADY_PERSISTED",
                    "object_id": object_id,
                    "boundary": {
                        "new_decision": "NOT_PERFORMED",
                        "semantic_comparison": "NOT_PERFORMED",
                        "object_index_write": "NONE",
                    },
                }
            return {
                "status": "CMOC_WRITE_REJECTED",
                "basis": "EXISTING_OBJECT_WRITE_CONFLICT",
            }

        self.objects[object_id] = {
            "canonical": copy.deepcopy(canonical),
            "fingerprint": fingerprint,
        }

        stored = self.objects[object_id]["canonical"]
        if (
            stored["object_id"] != object_id
            or stored["canonical_representation"] != canonical["canonical_representation"]
            or stored["provenance"] != canonical["provenance"]
            or stored["traceability"] != canonical["traceability"]
            or stored["approved_candidate_hash"] != canonical["approved_candidate_hash"]
        ):
            return {
                "status": "CMOC_WRITE_REJECTED",
                "basis": "POST_WRITE_VERIFICATION_FAILED",
            }

        return {
            "status": "CMOC_WRITE_ACCEPTED",
            "object_id": object_id,
            "boundary": {
                "cmoc_write": "PERFORMED",
                "new_decision": "NOT_PERFORMED",
                "semantic_comparison": "NOT_PERFORMED",
                "object_index_write": "NONE",
                "relations_created": "NONE",
            },
        }


def canonical_record():
    return {
        "status": "CANONICALIZATION_READY",
        "object_id": "OBJ-TEST-C2-001",
        "object_type": "TERM",
        "canonical_name": "Test Object",
        "canonical_representation": {
            "record_id": "REC-C2-001",
            "canonical_name": "Test Object",
            "object_type": "TERM",
            "value": "test",
        },
        "provenance": {
            "source_id": "SRC-C2-001",
            "discovery_run": "RUN-C2-001",
        },
        "traceability": {
            "decision_id": "DEC-C2-001",
            "admission_id": "ADM-C2-001",
            "match_id": "MAT-C2-001",
        },
        "approved_candidate_hash": "HASH-C2-001",
        "new_evidence_ref": "EVID-C2-001",
    }


class TestC2CMOCWriteBoundary001(unittest.TestCase):
    def setUp(self):
        self.writer = SyntheticCMOCWriter()
        self.record = canonical_record()

    def test_canonicalization_ready_is_accepted(self):
        result = self.writer.write(self.record)
        self.assertEqual(result["status"], "CMOC_WRITE_ACCEPTED")
        self.assertEqual(result["object_id"], "OBJ-TEST-C2-001")

    def test_non_ready_state_is_rejected(self):
        record = copy.deepcopy(self.record)
        record["status"] = "NEW_APPROVED"
        result = self.writer.write(record)
        self.assertEqual(result["status"], "CMOC_WRITE_REJECTED")
        self.assertEqual(result["basis"], "NOT_ELIGIBLE")

    def test_missing_provenance_is_rejected(self):
        record = copy.deepcopy(self.record)
        record.pop("provenance")
        result = self.writer.write(record)
        self.assertEqual(result["status"], "CMOC_WRITE_REJECTED")

    def test_missing_traceability_is_rejected(self):
        record = copy.deepcopy(self.record)
        record.pop("traceability")
        result = self.writer.write(record)
        self.assertEqual(result["status"], "CMOC_WRITE_REJECTED")

    def test_missing_object_identity_is_rejected(self):
        record = copy.deepcopy(self.record)
        record.pop("object_id")
        result = self.writer.write(record)
        self.assertEqual(result["status"], "CMOC_WRITE_REJECTED")

    def test_existing_object_mutation_is_rejected(self):
        record = copy.deepcopy(self.record)
        record["existing_object_mutation"] = True
        result = self.writer.write(record)
        self.assertEqual(result["status"], "CMOC_WRITE_REJECTED")
        self.assertEqual(result["basis"], "EXISTING_OBJECT_WRITE_CONFLICT")

    def test_unsupported_relations_are_rejected(self):
        record = copy.deepcopy(self.record)
        record["relations"] = [{"from": "OBJ-1", "to": "OBJ-2"}]
        result = self.writer.write(record)
        self.assertEqual(result["status"], "CMOC_WRITE_REJECTED")
        self.assertEqual(result["basis"], "UNSUPPORTED_RELATION_CREATION")

    def test_same_representation_is_idempotent(self):
        first = self.writer.write(self.record)
        second = self.writer.write(self.record)
        self.assertEqual(first["status"], "CMOC_WRITE_ACCEPTED")
        self.assertEqual(second["status"], "ALREADY_PERSISTED")
        self.assertEqual(len(self.writer.objects), 1)

    def test_different_representation_same_identity_is_rejected(self):
        self.writer.write(self.record)
        record = copy.deepcopy(self.record)
        record["canonical_representation"]["value"] = "different"
        result = self.writer.write(record)
        self.assertEqual(result["status"], "CMOC_WRITE_REJECTED")
        self.assertEqual(result["basis"], "EXISTING_OBJECT_WRITE_CONFLICT")
        self.assertEqual(len(self.writer.objects), 1)

    def test_successful_write_preserves_canonical_representation(self):
        original = copy.deepcopy(self.record)
        result = self.writer.write(self.record)
        self.assertEqual(result["status"], "CMOC_WRITE_ACCEPTED")
        stored = self.writer.objects["OBJ-TEST-C2-001"]["canonical"]
        self.assertEqual(stored, original)

    def test_c2_does_not_make_semantic_or_index_decisions(self):
        result = self.writer.write(self.record)
        self.assertEqual(result["boundary"]["new_decision"], "NOT_PERFORMED")
        self.assertEqual(result["boundary"]["semantic_comparison"], "NOT_PERFORMED")
        self.assertEqual(result["boundary"]["object_index_write"], "NONE")

    def test_input_is_not_mutated(self):
        original = copy.deepcopy(self.record)
        self.writer.write(self.record)
        self.assertEqual(self.record, original)


if __name__ == "__main__":
    unittest.main()

import copy
import unittest

from admission import AdmissionError, admit_existing, admit_new, execute_c1_from_admission


class TestAdmissionContract001(unittest.TestCase):
    def setUp(self):
        self.existing_decision = {
            "type": "DECISION",
            "decision": {
                "decision_id": "DEC-TEST-001",
                "decision_result": "ADMIT_EXISTING",
                "match_id": "MAT-001",
                "source_id": "SRC-TEST",
                "cmoc_object_id": "T-0001",
                "decided_at": "2026-09-24T15:00:00+05:00",
                "traceability": {
                    "source_id": "SRC-TEST",
                    "discovery_run": "RUN-TEST-001",
                    "reconciliation_id": "REC-TEST-001",
                    "match_id": "MAT-001",
                },
            },
        }
        self.new_decision = {
            "type": "DECISION",
            "decision": {
                "decision_id": "DEC-TEST-002",
                "decision_result": "ADMIT_NEW",
                "match_id": "MAT-002",
                "source_id": "SRC-TEST",
                "cmoc_object_id": None,
                "basis": "NEW_APPROVED_BY_HUMAN",
                "decided_at": "2026-09-24T15:05:00+05:00",
                "traceability": {
                    "source_id": "SRC-TEST",
                    "discovery_run": "RUN-TEST-001",
                    "reconciliation_id": "REC-TEST-001",
                    "match_id": "MAT-002",
                },
            },
        }

    def test_admit_existing_creates_admission_for_target(self):
        before = copy.deepcopy(self.existing_decision)
        result = admit_existing(self.existing_decision)

        self.assertEqual(self.existing_decision, before)
        self.assertEqual(result["type"], "ADMISSION")

        admission = result["admission"]
        self.assertEqual(admission["admission_result"], "ADMIT_EXISTING")
        self.assertEqual(admission["target_cmoc_object_id"], "T-0001")
        self.assertEqual(admission["decision_id"], "DEC-TEST-001")
        self.assertEqual(admission["match_id"], "MAT-001")
        self.assertTrue(admission["admission_id"].startswith("ADM-"))

    def test_admit_existing_is_deterministic(self):
        first = admit_existing(self.existing_decision)
        second = admit_existing(self.existing_decision)
        self.assertEqual(first["admission"]["admission_id"],
                         second["admission"]["admission_id"])

    def test_admit_existing_preserves_lineage(self):
        result = admit_existing(self.existing_decision)
        admission = result["admission"]

        self.assertEqual(
            admission["source_lineage"],
            self.existing_decision["decision"]["traceability"],
        )
        self.assertEqual(
            admission["traceability"],
            self.existing_decision["decision"]["traceability"],
        )

    def test_admit_existing_boundary_is_non_mutating(self):
        result = admit_existing(self.existing_decision)
        boundary = result["boundary"]

        self.assertEqual(boundary["decision_mutation"], "NONE")
        self.assertEqual(boundary["reconciliation_mutation"], "NONE")
        self.assertEqual(boundary["cmoc_write"], "NONE")
        self.assertEqual(boundary["object_index_write"], "NONE")

    def test_admit_existing_requires_correct_decision(self):
        with self.assertRaises(AdmissionError):
            admit_existing(self.new_decision)

        wrong = copy.deepcopy(self.existing_decision)
        wrong["decision"]["decision_result"] = "REJECT"
        with self.assertRaises(AdmissionError):
            admit_existing(wrong)

    def test_admit_existing_requires_target(self):
        missing = copy.deepcopy(self.existing_decision)
        missing["decision"]["cmoc_object_id"] = None
        with self.assertRaises(AdmissionError):
            admit_existing(missing)

    def test_admit_existing_rejects_incomplete_decision(self):
        required = (
            "decision_id",
            "decision_result",
            "match_id",
            "source_id",
            "traceability",
        )
        for field in required:
            with self.subTest(field=field):
                decision = copy.deepcopy(self.existing_decision)
                decision["decision"].pop(field)
                with self.assertRaises(AdmissionError):
                    admit_existing(decision)

    def test_admit_new_creates_pending_c1_admission(self):
        before = copy.deepcopy(self.new_decision)
        result = admit_new(self.new_decision)

        self.assertEqual(self.new_decision, before)
        self.assertEqual(result["type"], "ADMISSION")

        admission = result["admission"]
        self.assertEqual(admission["admission_result"], "ADMIT_NEW")
        self.assertIsNone(admission["target_cmoc_object_id"])
        self.assertEqual(admission["pipeline_status"], "PENDING_C1")
        self.assertTrue(admission["admission_id"].startswith("ADM-"))

    def test_admit_new_is_deterministic(self):
        first = admit_new(self.new_decision)
        second = admit_new(self.new_decision)
        self.assertEqual(first["admission"]["admission_id"],
                         second["admission"]["admission_id"])

    def test_admit_new_requires_basis_and_correct_decision(self):
        missing = copy.deepcopy(self.new_decision)
        missing["decision"].pop("basis")
        with self.assertRaises(AdmissionError):
            admit_new(missing)

        with self.assertRaises(AdmissionError):
            admit_new(self.existing_decision)

    def test_execute_c1_crosses_only_explicit_boundary(self):
        admission = admit_new(self.new_decision)
        candidate = {
            "decision_result": "NEW_APPROVED",
            "candidate_id": "CAND-001",
            "source_id": "SRC-TEST",
        }

        before = copy.deepcopy(candidate)
        result = execute_c1_from_admission(admission, candidate)

        self.assertEqual(candidate, before)
        self.assertEqual(result["decision_result"], "NEW_APPROVED")
        self.assertEqual(result["admission_id"], admission["admission"]["admission_id"])
        self.assertEqual(result["decision_id"], "DEC-TEST-002")
        self.assertEqual(result["match_id"], "MAT-002")
        self.assertEqual(result["source_id"], "SRC-TEST")

    def test_execute_c1_does_not_accept_unapproved_candidate(self):
        admission = admit_new(self.new_decision)

        with self.assertRaises(AdmissionError):
            execute_c1_from_admission(
                admission,
                {"decision_result": "NEEDS_REVIEW"},
            )

    def test_execute_c1_requires_pending_admission(self):
        admission = admit_new(self.new_decision)
        admission["admission"]["pipeline_status"] = "COMPLETED"

        with self.assertRaises(AdmissionError):
            execute_c1_from_admission(
                admission,
                {"decision_result": "NEW_APPROVED"},
            )


if __name__ == "__main__":
    unittest.main()

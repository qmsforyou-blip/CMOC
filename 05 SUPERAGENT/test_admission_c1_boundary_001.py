import copy
import unittest

from admission import AdmissionError, admit_new, execute_c1_from_admission


class TestAdmissionC1Boundary001(unittest.TestCase):
    def setUp(self):
        self.decision = {
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

        self.approved_candidate = {
            "decision_result": "NEW_APPROVED",
            "candidate_id": "CAND-001",
            "source_id": "SRC-TEST",
            "canonical_name": "Test Object",
            "object_type": "TERM",
        }

    def test_pending_admission_crosses_to_c1_without_semantic_work(self):
        admission = admit_new(self.decision)
        before = copy.deepcopy(self.approved_candidate)

        result = execute_c1_from_admission(admission, self.approved_candidate)

        self.assertEqual(self.approved_candidate, before)
        self.assertEqual(result["decision_result"], "NEW_APPROVED")
        self.assertEqual(
            result["admission_id"],
            admission["admission"]["admission_id"],
        )
        self.assertEqual(result["decision_id"], "DEC-TEST-002")
        self.assertEqual(result["match_id"], "MAT-002")
        self.assertEqual(result["source_id"], "SRC-TEST")

    def test_existing_admission_cannot_cross_to_c1(self):
        existing_decision = copy.deepcopy(self.decision)
        existing_decision["decision"]["decision_result"] = "ADMIT_EXISTING"
        existing_decision["decision"]["cmoc_object_id"] = "T-0001"

        from admission import admit_existing
        admission = admit_existing(existing_decision)

        with self.assertRaises(AdmissionError):
            execute_c1_from_admission(
                admission,
                self.approved_candidate,
            )

    def test_non_admission_artifact_rejected(self):
        with self.assertRaises(AdmissionError):
            execute_c1_from_admission(
                {"type": "DECISION"},
                self.approved_candidate,
            )

    def test_missing_admission_body_rejected(self):
        with self.assertRaises(AdmissionError):
            execute_c1_from_admission(
                {"type": "ADMISSION"},
                self.approved_candidate,
            )

    def test_non_pending_admission_rejected(self):
        admission = admit_new(self.decision)
        admission["admission"]["pipeline_status"] = "COMPLETED"

        with self.assertRaises(AdmissionError):
            execute_c1_from_admission(
                admission,
                self.approved_candidate,
            )

    def test_unapproved_candidate_rejected(self):
        admission = admit_new(self.decision)

        for value in ("NEEDS_REVIEW", "ADMIT_NEW", "NEW_CANDIDATE", None):
            with self.subTest(decision_result=value):
                candidate = copy.deepcopy(self.approved_candidate)
                candidate["decision_result"] = value

                with self.assertRaises(AdmissionError):
                    execute_c1_from_admission(admission, candidate)

    def test_non_object_candidate_rejected(self):
        admission = admit_new(self.decision)

        for candidate in (None, [], "candidate", 123):
            with self.subTest(candidate=candidate):
                with self.assertRaises(AdmissionError):
                    execute_c1_from_admission(admission, candidate)

    def test_c1_boundary_does_not_execute_canonization_or_writes(self):
        admission = admit_new(self.decision)
        result = execute_c1_from_admission(
            admission,
            self.approved_candidate,
        )

        self.assertNotIn("object_id", result)
        self.assertNotIn("canonical_representation", result)
        self.assertNotIn("status", result)

        self.assertEqual(result["decision_result"], "NEW_APPROVED")
        self.assertEqual(result["admission_id"], admission["admission"]["admission_id"])

    def test_c1_input_is_deep_copy(self):
        admission = admit_new(self.decision)
        result = execute_c1_from_admission(
            admission,
            self.approved_candidate,
        )

        result["canonical_name"] = "MUTATED_AFTER_HANDOFF"
        self.assertEqual(
            self.approved_candidate["canonical_name"],
            "Test Object",
        )


if __name__ == "__main__":
    unittest.main()

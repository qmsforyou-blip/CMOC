import copy
import unittest

from decision import DecisionContractError, build_decision


class TestDecisionContract001(unittest.TestCase):
    def setUp(self):
        self.existing = {
            "match_id": "MAT-NOM-001",
            "source_id": "SRC-TEST",
            "cmoc_object_id": "T-0001",
            "match_result": "EXISTING_EQUIVALENT",
            "traceability": {
                "source_id": "SRC-TEST",
                "discovery_run": "RUN-TEST-001",
                "reconciliation_id": "REC-TEST-001",
                "match_id": "MAT-NOM-001",
                "input_record_id": "NOM-TEST-001",
            },
        }
        self.needs_review = {
            "match_id": "MAT-NOM-002",
            "source_id": "SRC-TEST",
            "cmoc_object_id": None,
            "match_result": "NEEDS_REVIEW",
            "traceability": {
                "source_id": "SRC-TEST",
                "discovery_run": "RUN-TEST-001",
                "reconciliation_id": "REC-TEST-001",
                "match_id": "MAT-NOM-002",
                "input_record_id": "NOM-TEST-002",
            },
        }

    def build(self, result, reconciliation_record, **kwargs):
        return build_decision(
            decision_id="DEC-TEST-001",
            decision_type="HUMAN",
            decision_result=result,
            reconciliation_record=reconciliation_record,
            basis="TEST_BASIS",
            decided_by="TEST_OPERATOR",
            decided_at="2026-09-24T15:00:00+05:00",
            **kwargs,
        )

    def test_admit_existing(self):
        r = self.build("ADMIT_EXISTING", self.existing)
        d = r["decision"]
        self.assertEqual(d["decision_result"], "ADMIT_EXISTING")
        self.assertEqual(d["cmoc_object_id"], "T-0001")
        self.assertEqual(d["match_id"], "MAT-NOM-001")

    def test_admit_new(self):
        r = self.build("ADMIT_NEW", self.needs_review)
        d = r["decision"]
        self.assertEqual(d["decision_result"], "ADMIT_NEW")
        self.assertIsNone(d["cmoc_object_id"])

    def test_reject(self):
        r = self.build("REJECT", self.needs_review)
        self.assertEqual(r["decision"]["decision_result"], "REJECT")

    def test_defer(self):
        r = self.build("DEFER", self.needs_review)
        self.assertEqual(r["decision"]["decision_result"], "DEFER")

    def test_traceability_and_boundary(self):
        before = copy.deepcopy(self.existing)
        r = self.build("ADMIT_EXISTING", self.existing)

        self.assertEqual(self.existing, before)
        self.assertEqual(
            r["decision"]["traceability"]["discovery_run"],
            "RUN-TEST-001",
        )
        self.assertEqual(
            r["decision"]["traceability"]["reconciliation_id"],
            "REC-TEST-001",
        )
        self.assertEqual(r["decision"]["traceability"]["match_id"], "MAT-NOM-001")

        self.assertEqual(r["boundary"]["reconciliation_mutation"], "NONE")
        self.assertEqual(r["boundary"]["cmoc_write"], "NONE")
        self.assertEqual(r["boundary"]["object_index_write"], "NONE")
        self.assertEqual(r["boundary"]["admission_execution"], "NOT_PERFORMED")

    def test_missing_required_fields_rejected(self):
        required = [
            "decision_id",
            "match_id",
            "basis",
            "traceability",
        ]

        for field in required:
            with self.subTest(field=field):
                record = copy.deepcopy(self.existing)
                if field == "decision_id":
                    with self.assertRaises(DecisionContractError):
                        build_decision(
                            "",
                            "HUMAN",
                            "REJECT",
                            record,
                            "TEST_BASIS",
                            decided_by="TEST_OPERATOR",
                            decided_at="2026-09-24T15:00:00+05:00",
                        )
                else:
                    record[field] = None
                    if field == "match_id":
                        record["match_id"] = None
                    with self.assertRaises(DecisionContractError):
                        self.build("REJECT", record)

    def test_human_requires_decided_by_and_decided_at(self):
        with self.assertRaises(DecisionContractError):
            build_decision(
                "DEC-TEST-002",
                "HUMAN",
                "REJECT",
                self.needs_review,
                "TEST_BASIS",
                decided_at="2026-09-24T15:00:00+05:00",
            )

        with self.assertRaises(DecisionContractError):
            build_decision(
                "DEC-TEST-003",
                "HUMAN",
                "REJECT",
                self.needs_review,
                "TEST_BASIS",
                decided_by="TEST_OPERATOR",
            )

    def test_rule_requires_rule_id_and_version(self):
        with self.assertRaises(DecisionContractError):
            build_decision(
                "DEC-TEST-004",
                "RULE",
                "REJECT",
                self.needs_review,
                "TEST_BASIS",
                decided_at="2026-09-24T15:00:00+05:00",
                rule_version="1.0",
            )

        with self.assertRaises(DecisionContractError):
            build_decision(
                "DEC-TEST-005",
                "RULE",
                "REJECT",
                self.needs_review,
                "TEST_BASIS",
                decided_at="2026-09-24T15:00:00+05:00",
                rule_id="RULE-001",
            )

    def test_admit_existing_requires_existing_equivalent_and_object_id(self):
        with self.assertRaises(DecisionContractError):
            self.build("ADMIT_EXISTING", self.needs_review)

        record = copy.deepcopy(self.existing)
        record["cmoc_object_id"] = None
        with self.assertRaises(DecisionContractError):
            self.build("ADMIT_EXISTING", record)

    def test_admit_new_requires_needs_review(self):
        with self.assertRaises(DecisionContractError):
            self.build("ADMIT_NEW", self.existing)

    def test_invalid_result_and_upstream_result_rejected(self):
        with self.assertRaises(DecisionContractError):
            self.build("UNKNOWN", self.needs_review)

        record = copy.deepcopy(self.needs_review)
        record["match_result"] = "NO_MATCH"
        with self.assertRaises(DecisionContractError):
            self.build("REJECT", record)

    def test_decision_is_not_admission(self):
        r = self.build("ADMIT_EXISTING", self.existing)
        self.assertEqual(r["type"], "DECISION")
        self.assertEqual(r["boundary"]["admission_execution"], "NOT_PERFORMED")
        self.assertNotIn("admission", r)


if __name__ == "__main__":
    unittest.main()

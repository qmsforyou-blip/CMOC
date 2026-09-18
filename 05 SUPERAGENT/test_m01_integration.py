import unittest

from m01_integration import build_m01_handler


class TestM01Integration(unittest.TestCase):
    def test_real_machine_contract_with_controlled_extractor(self):
        package = {
            "package_id": "SOURCE-002-PACKAGE-001-CONTROLLED-1-6",
            "source_id": "SRC-002",
            "source_name": "GM Quality System Basics Overview — Supplier Audit",
            "source_version": "rev March 2009",
            "fragments": [
                {"location": "p1", "text": "Quality Systems Basics rev March 2009."},
                {"location": "p2", "text": "11 QSB Strategies."},
            ],
        }

        def controlled_extractor(pkg):
            return [
                {
                    "id": "EX-001",
                    "location": "p1",
                    "observation": "The source identifies itself as Quality Systems Basics, rev March 2009.",
                    "source_quote_or_evidence": "Quality Systems Basics rev March 2009.",
                    "uncertainty": "CLEAR",
                    "source_id": pkg["source_id"],
                },
                {
                    "id": "EX-002",
                    "location": "p2",
                    "observation": "The source presents a set of 11 QSB Strategies.",
                    "source_quote_or_evidence": "11 QSB Strategies.",
                    "uncertainty": "CLEAR",
                    "source_id": pkg["source_id"],
                },
            ]

        class Batch:
            source_id = "SRC-002"
            batch_id = "BATCH-SRC-002-M01-REAL-TEST"

        out = build_m01_handler(controlled_extractor)( {"source_package": package}, Batch())
        self.assertEqual(out["status"], "ACCEPT")
        self.assertEqual(out["type"], "EXTRACTION_RECORDS")
        self.assertEqual(out["source_id"], "SRC-002")
        self.assertEqual(len(out["records"]), 2)
        self.assertEqual(out["traceability"]["locations"], ["p1", "p2"])


if __name__ == "__main__":
    unittest.main()

import unittest
from mvp_runner import build_demo_runner

SOURCE = {"source_id":"SRC-002","source_name":"GM Quality System Basics Overview Supplier Audit"}

def initial():
    return {
        "type":"SOURCE_PACKAGE","source_id":"SRC-002",
        "traceability":{"source_id":"SRC-002","pages":[1,2,3,4,5,6]},
        "ref":"SRC-002-PAGES-1-6",
        "records":[
            {"id":"EX-006","location":"p1","distinction":"SOURCE IDENTIFICATION != SOURCE CONTENT"},
            {"id":"EX-007","location":"p2","distinction":"QSB STRATEGY SET != SINGLE STRATEGY"},
            {"id":"EX-008","location":"p3","distinction":"AUDIT RESULT != WORKSHOP DECISION"},
            {"id":"EX-009","location":"p4","distinction":"COMMON PRINCIPLES != COMMON METHODS != COMMON PROCESSES"},
            {"id":"EX-010","location":"p5","distinction":"FAST RESPONSE != PROBLEM SOLVING"},
            {"id":"EX-011","location":"p6","distinction":"PROBLEM IDENTIFICATION != PROBLEM SOLVING"},
        ]
    }

class TestMvpRunner(unittest.TestCase):
    def test_sequential(self):
        r=build_demo_runner()
        result=r.run_chain("MVP-RUN-001",SOURCE,initial(),["M01","M02","M03"])
        self.assertEqual(result["status"],"ACCEPT")
        self.assertEqual([x["type"] for x in result["results"]],
                         ["EXTRACTION_RECORDS","DISTINCTION_RECORDS","FORMULATION_RECORDS"])
        self.assertEqual(len(result["results"][0]["records"]),6)
        self.assertEqual(len(result["results"][1]["records"]),6)
        self.assertEqual(len(result["results"][2]["records"]),18)

    def test_contract_reject_before_execution(self):
        r=build_demo_runner()
        m02=r.execute("MVP-RUN-002",SOURCE,"M02",{**initial(),"type":"SOURCE_PACKAGE","ref":"INPUT"})
        self.assertEqual(m02["status"],"ACCEPT")
        rejected=r.execute("MVP-RUN-002",SOURCE,"M04",
                            {**m02,"type":"DISTINCTION_RECORDS","ref":"M02:OUTPUT"})
        self.assertEqual(rejected["status"],"REJECT")
        self.assertIn("TYPE_MISMATCH",rejected["reason"])
        self.assertIsNone(rejected["batch_id"])
        self.assertFalse(any(e.task=="M04" and e.batch_id for e in r.journal))

    def test_missing_trace_reject(self):
        r=build_demo_runner()
        bad=dict(initial()); bad["traceability"]={}
        result=r.run_chain("MVP-RUN-003",SOURCE,bad,["M01"])
        self.assertEqual(result["status"],"REJECT")
        self.assertEqual(result["results"][0]["reason"],"MISSING_TRACEABILITY")

    def test_trace_survives_chain(self):
        r=build_demo_runner()
        result=r.run_chain("MVP-RUN-005",SOURCE,initial(),["M01","M02","M03"])
        final=result["results"][-1]
        self.assertEqual(final["traceability"]["source_id"],"SRC-002")
        self.assertEqual(final["traceability"]["from"]["source_id"],"SRC-002")
        self.assertTrue(final["batch_id"].startswith("BATCH-SRC-002-M03-"))

    def test_handoff_contract(self):
        r=build_demo_runner()
        m01=r.execute("MVP-RUN-H01",SOURCE,"M01",initial())
        h=r.create_handoff("MVP-RUN-H01",SOURCE,"M01","M02",m01)
        self.assertEqual(h.status,"ACCEPT")
        self.assertEqual(h.from_task,"M01")
        self.assertEqual(h.to_task,"M02")
        self.assertEqual(h.input_type,"EXTRACTION_RECORDS")
        self.assertEqual(h.output_ref,m01["ref"])
        self.assertTrue(h.handoff_id.startswith("HANDOFF-SRC-002-M01-M02-"))
        self.assertEqual(r.handoffs[-1].handoff_id,h.handoff_id)

    def test_handoff_rejects_incompatible_destination(self):
        r=build_demo_runner()
        m01=r.execute("MVP-RUN-H02",SOURCE,"M01",initial())
        h=r.create_handoff("MVP-RUN-H02",SOURCE,"M01","M04",m01)
        self.assertEqual(h.status,"REJECT")
        self.assertIn("TYPE_MISMATCH",h.reason)
        self.assertEqual(r.handoffs[-1].status,"REJECT")
        self.assertEqual(r.journal[-1].handoff_id,h.handoff_id)

    def test_rejected_handoff_creates_no_downstream_batch(self):
        r=build_demo_runner()
        result=r.run_chain("MVP-RUN-H04",SOURCE,initial(),["M01","M04"])
        self.assertEqual(result["status"],"REJECT")
        self.assertEqual(len(r.handoffs),1)
        self.assertEqual(r.handoffs[0].status,"REJECT")
        self.assertIn("TYPE_MISMATCH",r.handoffs[0].reason)
        self.assertEqual(len(r.batches),1)
        self.assertEqual(r.batches[0].task,"M01")
        self.assertEqual(result["results"][0]["batch_id"],r.batches[0].batch_id)
        self.assertEqual(len(result["results"]),1)

    def test_chain_links_handoff_to_downstream_batch(self):
        r=build_demo_runner()
        result=r.run_chain("MVP-RUN-H03",SOURCE,initial(),["M01","M02","M03"])
        self.assertEqual(result["status"],"ACCEPT")
        self.assertEqual(len(r.handoffs),2)
        self.assertEqual(result["results"][1]["batch_id"],"BATCH-SRC-002-M02-001")
        self.assertEqual(r.batches[1].handoff_id,r.handoffs[0].handoff_id)
        self.assertEqual(r.journal[1].handoff_id,r.handoffs[0].handoff_id)
        self.assertEqual(r.batches[2].handoff_id,r.handoffs[1].handoff_id)
        self.assertEqual(r.journal[3].handoff_id,r.handoffs[1].handoff_id)


    def test_handoff_output_becomes_next_input(self):
        r=build_demo_runner()
        result=r.run_chain("MVP-RUN-H05",SOURCE,initial(),["M01","M02","M03"])
        self.assertEqual(result["status"],"ACCEPT")
        self.assertEqual(r.batches[1].input_ref,r.handoffs[0].output_ref)
        self.assertEqual(r.batches[2].input_ref,r.handoffs[1].output_ref)

    def test_next_task_receives_explicit_handoff_input(self):
        r=build_demo_runner()
        received={}
        original_m02=r.handlers["M02"]

        def spy_m02(inp, batch):
            received.update({
                "type":inp["type"],
                "source_id":inp["source_id"],
                "traceability":inp["traceability"],
                "ref":inp["ref"],
            })
            return original_m02(inp, batch)

        r.handlers["M02"]=spy_m02
        result=r.run_chain("MVP-RUN-H06",SOURCE,initial(),["M01","M02","M03"])
        self.assertEqual(result["status"],"ACCEPT")
        h=r.handoffs[0]
        self.assertEqual(received["type"],h.input_type)
        self.assertEqual(received["source_id"],h.source_id)
        self.assertEqual(received["traceability"],h.traceability)
        self.assertEqual(received["ref"],h.output_ref)

    def test_new_batch_per_task(self):
        r=build_demo_runner()
        result=r.run_chain("MVP-RUN-006",SOURCE,initial(),["M01","M02","M03"])
        batches=[x["batch_id"] for x in result["results"]]
        self.assertEqual(len(batches),3)
        self.assertEqual(len(set(batches)),3)

if __name__=="__main__":
    unittest.main()

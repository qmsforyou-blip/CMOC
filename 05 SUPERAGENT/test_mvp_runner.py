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

def test_sequential():
    r=build_demo_runner()
    result=r.run_chain("MVP-RUN-001",SOURCE,initial(),["M01","M02","M03"])
    assert result["status"]=="ACCEPT"
    assert [x["type"] for x in result["results"]]==[
        "EXTRACTION_RECORDS","DISTINCTION_RECORDS","FORMULATION_RECORDS"]
    assert len(result["results"][0]["records"])==6
    assert len(result["results"][1]["records"])==6
    assert len(result["results"][2]["records"])==18

def test_contract_reject_before_execution():
    r=build_demo_runner()
    m02 = r.execute("MVP-RUN-002",SOURCE,"M02",{
        **initial(),"type":"SOURCE_PACKAGE","ref":"INPUT"
    })
    assert m02["status"]=="ACCEPT"
    rejected = r.execute("MVP-RUN-002",SOURCE,"M04",{
        **m02,"type":"DISTINCTION_RECORDS","ref":"M02:OUTPUT"
    })
    assert rejected["status"]=="REJECT"
    assert "TYPE_MISMATCH" in rejected["reason"]
    assert rejected["batch_id"] is None
    assert not any(e.task=="M04" and e.batch_id for e in r.journal)

def test_missing_trace_reject():
    r=build_demo_runner()
    bad=dict(initial()); bad["traceability"]={}
    result=r.run_chain("MVP-RUN-003",SOURCE,bad,["M01"])
    assert result["status"]=="REJECT"
    assert result["results"][0]["reason"]=="MISSING_TRACEABILITY"

def test_trace_survives_chain():
    r=build_demo_runner()
    result=r.run_chain("MVP-RUN-005",SOURCE,initial(),["M01","M02","M03"])
    final=result["results"][-1]
    assert final["traceability"]["source_id"]=="SRC-002"
    assert final["traceability"]["from"]["source_id"]=="SRC-002"
    assert final["batch_id"].startswith("BATCH-SRC-002-M03-")

def test_new_batch_per_task():
    r=build_demo_runner()
    result=r.run_chain("MVP-RUN-006",SOURCE,initial(),["M01","M02","M03"])
    batches=[x["batch_id"] for x in result["results"]]
    assert len(batches)==3
    assert len(set(batches))==3

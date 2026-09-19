#!/usr/bin/env python3
"""SPEC-003 CMOC QUERY v0.2 — read-only query over CMOC-INVENTORY-001."""
from __future__ import annotations
import json, re, sys
from pathlib import Path

CLASS_TO_TYPE = {
    "TERM_FILE":"TERM","DISTINCTION_FILE":"DISTINCTION","GM_FORMULATION_FILE":"GM_FORMULATION",
    "MACHINE":"MACHINE","PATTERN":"PATTERN","CHAIN":"CHAIN","LAW":"LAW","OBSERVATION":"OBSERVATION",
    "ORGANIZATIONAL_CONSTRUCTION":"ORGANIZATIONAL_CONSTRUCTION",
}
TYPE_SCOPE = {
    "TERM":"TERMS","DISTINCTION":"DISTINCTIONS","GM_FORMULATION":"FORMULATIONS","MACHINE":"MACHINES",
    "PATTERN":"PATTERNS","CHAIN":"CHAINS","LAW":"LAW","OBSERVATION":"OBSERVATIONS",
    "ORGANIZATIONAL_CONSTRUCTION":"ORGANIZATIONAL_CONSTRUCTIONS",
}

def norm(v):
    v=v.lower().replace("ё","е")
    return " ".join(re.sub(r"[^0-9a-zа-я]+"," ",v,flags=re.I).split())

def object_from_record(r):
    typ=CLASS_TO_TYPE.get(r["class"])
    if not typ: return None
    stem=Path(r["path"]).stem
    m=re.search(r"(?<![A-Za-z0-9])((?:T|DIS|LAB|MC|MP|CHAIN|LAW|OBS|OC)-[A-Za-z0-9_-]+)",stem)
    if not m: return None
    oid=m.group(1)
    name=stem[m.end():].strip(" -—_.") or stem
    return {"object_id":oid,"object_type":typ,"name":name,"path":r["path"],
            "status":r.get("status","UNKNOWN"),
            "traceability":{"inventory_schema":"CMOC-INVENTORY-001","source_path":r["path"],"git_sha":r["git_sha"]},
            "aliases":[]}

def load_objects(path):
    inv=json.loads(Path(path).read_text(encoding="utf-8"))
    return inv,[o for r in inv["records"] if (o:=object_from_record(r))]

def load_index(path):
    """Backward-compatible loader for RECONCILIATION v0.1 tests/contracts."""
    return load_objects(path)[1]


def query(objects,qid,qtype,target,value,scope):
    scope=set(scope or [])
    if target and TYPE_SCOPE.get(target) not in scope:
        return {"query_id":qid,"match_status":"SCOPE_INSUFFICIENT",
                "match_basis":f"TARGET_OBJECT_TYPE={target} outside QUERY_SCOPE","results":[],"scope_checked":sorted(scope)}
    cand=[o for o in objects if (not target or o["object_type"]==target) and TYPE_SCOPE[o["object_type"]] in scope]
    q=norm(value)
    if qtype=="EXACT":
        hits=[o for o in cand if o["object_id"].upper()==value.strip().upper() or norm(o["name"])==q]
        status="MATCH" if hits else "NO_MATCH"; basis="object id or normalized name"
    elif qtype=="ALIAS":
        hits=[o for o in cand if any(norm(a)==q for a in o["aliases"])]
        status="MATCH" if hits else "NO_MATCH"; basis="registered alias"
    elif qtype in {"TEXT","STRUCTURAL","CANDIDATE"}:
        qt=set(q.split()); scored=[]
        for o in cand:
            overlap=len(qt & set(norm(o["name"]+" "+o["object_id"]).split()))
            if overlap: scored.append((overlap,o))
        scored.sort(key=lambda x:(-x[0],x[1]["object_id"]))
        hits=[o for _,o in scored]; status="CANDIDATE" if hits else "NO_MATCH"; basis="normalized token overlap"
    else: raise ValueError(f"Unsupported QUERY_TYPE: {qtype}")
    return {"query_id":qid,"match_status":status,"results":[{
        "query_id":qid,"object_id":o["object_id"],"object_type":o["object_type"],
        "match_mode":qtype,"match_status":status,"match_basis":basis,
        "object_status":o["status"],"traceability":o["traceability"]} for o in hits],
        "scope_checked":sorted(scope)}

def main():
    p=json.load(sys.stdin)
    ip=p.get("inventory_path",str(Path(__file__).with_name("cmoc_inventory.json")))
    _,objects=load_objects(ip)
    print(json.dumps(query(objects,p["query_id"],p["query_type"],p.get("target_object_type"),
                            p["query_value"],p.get("query_scope")),ensure_ascii=False,indent=2))

if __name__=="__main__": main()

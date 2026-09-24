import json

inv = json.load(open(r"05 SUPERAGENT\cmoc_inventory.json", encoding="utf-8"))
idx = json.load(open(r"05 SUPERAGENT\cmoc_object_index.json", encoding="utf-8"))

inv_paths = {x["path"] for x in inv["records"]}

snap = f"CMOC-INVENTORY-001@{inv['generated_at']}/{inv['source_commit']}"

obj_records = [
    x for x in idx["records"]
    if x.get("count_basis") == "OBJECT_FILE"
]

bad = [
    (x.get("object_id"), x.get("representation", {}).get("container"))
    for x in obj_records
    if x.get("representation", {}).get("container") not in inv_paths
]

provenance_bad = [
    x.get("object_id")
    for x in obj_records
    if x.get("provenance", {}).get("inventory_snapshot") != snap
]

print("--- INVENTORY → OBJECT INDEX ---")
print("Inventory records:", len(inv["records"]))
print("Object Index records:", len(idx["records"]))
print("OBJECT_FILE records:", len(obj_records))
print("Missing Inventory source paths:", len(bad))
print("Provenance mismatches:", len(provenance_bad))
print("Source commit match:", idx.get("source_commit") == inv.get("source_commit"))
print("Branch match:", idx.get("branch") == inv.get("branch"))
print("Repository match:", idx.get("repository") == inv.get("repository"))

result = (
    not bad
    and not provenance_bad
    and idx.get("source_commit") == inv.get("source_commit")
    and idx.get("branch") == inv.get("branch")
    and idx.get("repository") == inv.get("repository")
)

print("RESULT:", "PASS" if result else "FAIL")

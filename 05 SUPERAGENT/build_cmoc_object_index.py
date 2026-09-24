import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "05 SUPERAGENT" / "cmoc_inventory.json"
OUTPUT = ROOT / "05 SUPERAGENT" / "cmoc_object_index.json"


CLASS_TO_TYPE = {
    "TERM_FILE": "TERM",
    "DISTINCTION_FILE": "DISTINCTION",
    "GM_FORMULATION_FILE": "GM_FORMULATION",
    "MACHINE": "MACHINE",
    "CHAIN": "CHAIN",
    "PATTERN": "PATTERN",
    "LAW": "LAW",
    "OBSERVATION": "OBSERVATION",
    "ORGANIZATIONAL_CONSTRUCTION": "ORGANIZATIONAL_CONSTRUCTION",
}

ID_PATTERNS = [
    re.compile(r"\bT-\d{4}\b"),
    re.compile(r"\bDIS-\d+\b"),
    re.compile(r"\bLAB-\d+\b"),
    re.compile(r"\bMC-[A-Z0-9-]+\b"),
    re.compile(r"\bCHAIN-[A-Z0-9-]+\b"),
    re.compile(r"\bMP-[A-Z0-9-]+\b"),
    re.compile(r"\bLAW-\d+\b"),
    re.compile(r"\bOBS-\d+\b"),
    re.compile(r"\bOC-\d+\b"),
]

# Inventory-classified files observed not to be addressable object files.
# They remain in CMOC-INVENTORY-001 but are excluded from OBJECT_FILE indexing.
NON_OBJECT_PATHS = {
    "000 База/01 Термины/01 База Термины.base",
    "000 База/02 Различения/02 база различения.base",
    "000 База/02 Различения/Без названия.md",
    "000 База/03 GM-формулировки/03 GM формулировки.base",
    "03_MACHINE-CATALOG/MACHINES/MACHINE-CANDIDATES.md",
    "07 К/LAW/Реестр LAW.md.md",
}

def read_text(path):
    return path.read_text(encoding="utf-8")

def frontmatter(text):
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    out = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$", line)
        if m:
            out[m.group(1)] = m.group(2).strip().strip('"').strip("'")
    return out

def structure(text):
    fm = frontmatter(text)
    sections = []
    for line in text.splitlines():
        m = re.match(r"^#{1,6}\s+(.+?)\s*$", line)
        if m:
            sections.append(m.group(1).strip())
    return {"fields_present": list(fm.keys()), "sections_present": sections}

def explicit_object_id(text, path):
    fm = frontmatter(text)
    for key in ("id", "machine_id", "chain_id", "pattern_id", "law_id", "observation_id", "construction_id"):
        value = fm.get(key)
        if value and any(p.fullmatch(value) for p in ID_PATTERNS):
            return value
    for part in (Path(path).name, Path(path).stem):
        for p in ID_PATTERNS:
            m = p.search(part)
            if m:
                return m.group(0)
    return None

def object_record(inv, root, repository, inventory_snapshot):
    path = inv["path"]
    text = read_text(root / path)
    fm = frontmatter(text)
    oid = explicit_object_id(text, path)
    otype = CLASS_TO_TYPE[inv["class"]]
    name = fm.get("name")
    return {
        "schema": "CMOC-OBJECT-INDEX-RECORD",
        "version": "0.2",
        "object_id": oid,
        "object_type": otype,
        "object_name": name,
        "representation": {"kind": "OBJECT_FILE", "container": path, "location": "FILE"},
        "indexed_attributes": {},
        "structure": structure(text),
        "provenance": {
            "repository": repository,
            "git_sha": inv["git_sha"],
            "inventory_snapshot": inventory_snapshot,
        },
        "traceability": {
            "source": fm.get("source", "UNKNOWN"),
            "registry": "UNKNOWN",
        },
        "discovery": {"basis": "CMOC-INVENTORY-001 classified object file"},
        "count_basis": "OBJECT_FILE",
    }

def registry_record(oid, otype, container, line, name=None, fields=None, sections=None, source="UNKNOWN", sha=None, repository="UNKNOWN", inventory_snapshot="UNKNOWN"):
    return {
        "schema": "CMOC-OBJECT-INDEX-RECORD",
        "version": "0.2",
        "object_id": oid,
        "object_type": otype,
        "object_name": name,
        "representation": {
            "kind": "REGISTRY_RECORD",
            "container": container,
            "location": {"record_id": oid, "line": line},
        },
        "indexed_attributes": {},
        "structure": {
            "fields_present": fields or ["id"],
            "sections_present": sections or [],
        },
        "provenance": {
            "repository": repository,
            "git_sha": sha,
            "inventory_snapshot": inventory_snapshot,
        },
        "traceability": {"source": source, "registry": container},
        "discovery": {"basis": "mechanical identifier discovery in registry"},
        "count_basis": "REGISTRY_RECORD",
    }

def term_records(text, container, sha, repository="UNKNOWN", inventory_snapshot="UNKNOWN"):
    out = []
    for n, line in enumerate(text.splitlines(), 1):
        m = re.match(r"^\s*(T-\d{4})\s+(.+?)\s*$", line)
        if m:
            out.append(registry_record(m.group(1), "TERM", container, n, m.group(2).strip(), ["id", "name"], sha=sha, repository=repository, inventory_snapshot=inventory_snapshot))
    return out

def distinction_records(text, container, sha, repository="UNKNOWN", inventory_snapshot="UNKNOWN"):
    out = []
    for n, line in enumerate(text.splitlines(), 1):
        m = re.match(r"^\|\s*\*{0,2}(DIS-\d+)\*{0,2}\s*\|", line)
        if m:
            out.append(registry_record(m.group(1), "DISTINCTION", container, n, None, ["id"], sha=sha))
    return out

def invariant_records(text, container, sha, repository="UNKNOWN", inventory_snapshot="UNKNOWN"):
    lines = text.splitlines()
    found = {}
    for n, line in enumerate(lines, 1):
        m = re.match(r"^\s*#{1,6}\s+.*?(INV-\d{4})(?:\s+(.+?))?\s*$", line)
        if m and m.group(1) not in found:
            name = (m.group(2) or "").strip().strip("*") or None
            found[m.group(1)] = (n, name)
    if "INV-0009" not in found:
        for n, line in enumerate(lines, 1):
            if "CMOC INV-0009" in line:
                found["INV-0009"] = (n, None)
                break
    if "INV-0002" not in found:
        for n, line in enumerate(lines, 1):
            if line.strip() == "INV-0002":
                name = lines[n].strip() if n < len(lines) else None
                found["INV-0002"] = (n, name)
                break
    out = []
    for oid, (line, name) in sorted(found.items(), key=lambda x: x[1][0]):
        out.append(registry_record(oid, "INVARIANT", container, line, name, ["id"], sha=sha))
    return out

def organizational_records(text, container, sha, repository="UNKNOWN", inventory_snapshot="UNKNOWN"):
    out = []
    for n, line in enumerate(text.splitlines(), 1):
        m = re.match(r"^\|\s*(C-\d{4})\s*\|\s*([^|]+?)\s*\|", line)
        if m:
            out.append(registry_record(m.group(1), "ORGANIZATIONAL_CONSTRUCTION", container, n, m.group(2).strip(), ["id", "construction"], sha=sha))
    return out

def build(repository_root=None, inventory_path=None):
    root = Path(repository_root) if repository_root is not None else ROOT
    inventory_file = Path(inventory_path) if inventory_path is not None else INVENTORY
    inv = json.loads(read_text(inventory_file))
    required = ("schema", "version", "generated_at", "repository", "branch", "source_commit")
    missing = [key for key in required if key not in inv]
    if missing:
        raise RuntimeError(f"Inventory provenance is incomplete: missing {missing}")
    repository = inv["repository"]
    inventory_snapshot = f'{inv["schema"]}@{inv["generated_at"]}/{inv["source_commit"]}'
    records = []
    for item in inv["records"]:
        if item["class"] in CLASS_TO_TYPE and item["path"] not in NON_OBJECT_PATHS:
            records.append(object_record(item, root, repository, inventory_snapshot))

    containers = {
        "LAB-000": ("08 CMOC Core/LAB-000 Опись терминов ОН.md", "TERM", term_records),
        "LAB-002": ("08 CMOC Core/LAB-002 Реестр различений.md", "DISTINCTION", distinction_records),
        "LAB-004": ("08 CMOC Core/LAB-004 Инварианты.md", "INVARIANT", invariant_records),
        "LAB-005": ("08 CMOC Core/LAB-005 Опись организационных конструкций.md", "ORGANIZATIONAL_CONSTRUCTION", organizational_records),
    }
    by_path = {x["path"]: x["git_sha"] for x in inv["records"]}
    for _, (path, _, parser) in containers.items():
        records.extend(parser(read_text(root / path), path, by_path[path], repository=repository, inventory_snapshot=inventory_snapshot))

    for r in records:
        if r["object_id"] is None:
            raise RuntimeError(
                f"Unresolved object_id in addressable representation: "
                f"{r['representation']['container']}"
            )

    full_keys = [
        (
            r["object_type"],
            r["representation"]["kind"],
            r["representation"]["container"],
            json.dumps(r["representation"]["location"], sort_keys=True),
        )
        for r in records
    ]
    if len(full_keys) != len(set(full_keys)):
        raise RuntimeError("Duplicate addressable representations detected")

    object_types = sorted({r["object_type"] for r in records})
    data = {
        "schema": "CMOC-OBJECT-INDEX-001",
        "version": "0.2",
        "generated_at": inv["generated_at"],
        "repository": repository,
        "branch": inv["branch"],
        "source_inventory": f'{inv["schema"]}@{inv["generated_at"]}',
        "source_commit": inv["source_commit"],
        "purpose": "Read-only structural/addressable index. No semantic reconciliation or CMOC mutation.",
        "record_model": "One record per discovered representation; the same object_id may therefore occur more than once.",
        "representation_record_count": len(records),
        "object_type_counts": {t: sum(r["object_type"] == t for r in records) for t in object_types},
        "representation_kind_counts": {
            "OBJECT_FILE": sum(r["representation"]["kind"] == "OBJECT_FILE" for r in records),
            "REGISTRY_RECORD": sum(r["representation"]["kind"] == "REGISTRY_RECORD" for r in records),
            "OTHER_ADDRESSABLE": sum(r["representation"]["kind"] == "OTHER_ADDRESSABLE" for r in records),
        },
        "count_views": {
            "by_object_type": {
                t: {
                    "representations": sum(r["object_type"] == t for r in records),
                    "object_files": sum(r["object_type"] == t and r["representation"]["kind"] == "OBJECT_FILE" for r in records),
                    "registry_records": sum(r["object_type"] == t and r["representation"]["kind"] == "REGISTRY_RECORD" for r in records),
                    "unique_object_ids": len({r["object_id"] for r in records if r["object_type"] == t}),
                }
                for t in object_types
            },
            "unique_object_ids": len({r["object_id"] for r in records}),
        },
        "records": records,
    }
    return data

if __name__ == "__main__":
    import sys

    data = build()
    generated = json.dumps(data, ensure_ascii=False, indent=2) + "\n"

    if "--check" in sys.argv:
        if not OUTPUT.exists():
            raise SystemExit("OBJECT INDEX file is missing")
        committed = OUTPUT.read_text(encoding="utf-8")
        if committed != generated:
            raise SystemExit("OBJECT INDEX is not reproducible from current repository state")
        print(json.dumps({
            "check": "PASS",
            "representation_record_count": data["representation_record_count"],
            "representation_kind_counts": data["representation_kind_counts"],
            "unique_object_ids": data["count_views"]["unique_object_ids"],
        }, ensure_ascii=False))
    else:
        OUTPUT.write_text(generated, encoding="utf-8")
        print(json.dumps({
            "generated": "OK",
            "representation_record_count": data["representation_record_count"],
            "representation_kind_counts": data["representation_kind_counts"],
            "unique_object_ids": data["count_views"]["unique_object_ids"],
        }, ensure_ascii=False))

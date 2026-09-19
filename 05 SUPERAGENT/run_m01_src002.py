import json
from mvp_runner import Superagent, Contract
from m01_integration import build_m01_handler

with open(r"05 SUPERAGENT/SOURCE-PACKAGE-SRC-002-1-6.example.json", encoding="utf-8") as f:
    package = json.load(f)

source = {
    "source_id": package["source_id"],
    "source_name": package["source_name"],
}

contracts = {
    "M01": Contract(
        "M01",
        {"SOURCE_PACKAGE"},
        "EXTRACTION_RECORDS",
        {"source_id", "batch_id", "records", "traceability", "ref"},
        {"source_package"},
    )
}

runner = Superagent(
    contracts,
    {"M01": build_m01_handler()},
    {"M01": "M01-PRODUCTION"},
)

initial = {
    "type": "SOURCE_PACKAGE",
    "source_id": package["source_id"],
    "source_package": package,
    "traceability": {
        "source_id": package["source_id"],
        "source_package": package["package_id"],
    },
    "ref": package["package_id"],
}

result = runner.execute(
    "RUN-SRC-002-M01-001",
    source,
    "M01",
    initial,
)

print(json.dumps(result, ensure_ascii=False, indent=2))

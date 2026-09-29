from __future__ import annotations

import argparse
import json
from pathlib import Path

from admission import admit_new
from admission_store import AdmissionStore


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--decision", required=True)
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()

    decision_path = Path(args.decision)
    decision = json.loads(decision_path.read_text(encoding="utf-8"))
    admission = admit_new(decision)

    store = AdmissionStore(Path(args.output_dir))
    result = store.write(admission)

    print(json.dumps({
        "status": result,
        "admission_id": admission["admission"]["admission_id"],
        "decision_id": admission["admission"]["decision_id"],
        "match_id": admission["admission"]["match_id"],
        "admission_result": admission["admission"]["admission_result"],
        "pipeline_status": admission["admission"]["pipeline_status"],
        "boundary": admission["boundary"],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
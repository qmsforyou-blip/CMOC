from __future__ import annotations

import argparse
import json
from pathlib import Path

from decision_store import DecisionStore
from human_decision_amendment import amend_human_decision


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--original", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--amendment-id", required=True)
    parser.add_argument("--basis", required=True)
    parser.add_argument("--decided-by", required=True)
    args = parser.parse_args()

    original_path = Path(args.original)
    original = json.loads(original_path.read_text(encoding="utf-8"))

    amended = amend_human_decision(
        original=original,
        amendment_id=args.amendment_id,
        new_result="ADMIT_NEW",
        basis=args.basis,
        decided_by=args.decided_by,
    )

    store = DecisionStore(Path(args.output_dir))
    try:
        result = store.write(amended)
    finally:
        store.close()

    print(json.dumps({
        "status": result,
        "decision_id": amended["decision"]["decision_id"],
        "decision_result": amended["decision"]["decision_result"],
        "supersedes_decision_id": amended["decision"]["amendment"][
            "supersedes_decision_id"
        ],
        "original_preserved": True,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
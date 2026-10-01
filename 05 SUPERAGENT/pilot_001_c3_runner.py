from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


def run_command(command: list[str], cwd: Path) -> dict:
    completed = subprocess.run(
        command,
        cwd=str(cwd),
        capture_output=True,
        text=True,
        encoding="utf-8",
    )

    return {
        "command": command,
        "returncode": completed.returncode,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generic C3 Object Index rebuild/check runner"
    )
    parser.add_argument(
        "--repo",
        default=".",
        help="CMOC repository root",
    )
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    superagent = repo / "05 SUPERAGENT"

    rebuild_script = superagent / "rebuild_inventory_object_index.py"
    check_script = superagent / "build_cmoc_object_index.py"

    if not rebuild_script.exists():
        raise SystemExit(
            f"REBUILD_SCRIPT_NOT_FOUND: {rebuild_script}"
        )

    if not check_script.exists():
        raise SystemExit(
            f"CHECK_SCRIPT_NOT_FOUND: {check_script}"
        )

    rebuild = run_command(
        [sys.executable, str(rebuild_script)],
        repo,
    )

    if rebuild["returncode"] != 0:
        print(json.dumps({
            "status": "C3_REBUILD_FAILED",
            "rebuild": rebuild,
        }, ensure_ascii=False, indent=2))
        raise SystemExit(rebuild["returncode"])

    check = run_command(
        [
            sys.executable,
            str(check_script),
            "--check",
        ],
        repo,
    )

    if check["returncode"] != 0:
        print(json.dumps({
            "status": "C3_CHECK_FAILED",
            "rebuild": rebuild,
            "check": check,
        }, ensure_ascii=False, indent=2))
        raise SystemExit(check["returncode"])

    print(json.dumps({
        "status": "C3_REBUILD_AND_CHECK_COMPLETED",
        "rebuild": rebuild,
        "check": check,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
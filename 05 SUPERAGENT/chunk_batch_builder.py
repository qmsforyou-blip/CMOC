from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


def chunk_number(path: Path) -> int:
    match = re.match(r"GM-(\d+)-", path.name)
    if not match:
        raise ValueError(f"INVALID_GM_CHUNK_NAME: {path.name}")
    return int(match.group(1))


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def build_package(
    patch_root: Path,
    start: int,
    end: int,
    package_id: str,
) -> dict:
    files = sorted(
        (
            path
            for path in patch_root.glob("GM-*.md")
            if re.match(r"GM-\d+-", path.name) and start <= chunk_number(path) <= end
        ),
        key=chunk_number,
    )

    expected = list(range(start, end + 1))
    actual = [chunk_number(path) for path in files]
    missing = [number for number in expected if number not in actual]

    if not files:
        raise ValueError("NO_GM_CHUNKS_SELECTED")

    # Наличие пропусков фиксируется в scope, но не блокирует сборку.

    fragments = []
    candidates = []

    for path in files:
        number = chunk_number(path)
        text = path.read_text(encoding="utf-8")

        fragments.append({
            "fragment_id": f"FRAG-SRC002-GM-{number:03d}",
            "chunk_id": f"GM-{number:03d}",
            "source_file": path.name,
            "title": path.stem,
            "text": text,
            "text_sha256": sha256_text(text),
            "candidate_scope": "source-bound content from one prepared GM chunk",
        })

        candidates.append({
            "candidate_id": f"CAND-SRC002-GM-{number:03d}",
            "chunk_id": f"GM-{number:03d}",
            "title": path.stem,
            "object_type": "SOURCE_BOUND_CANDIDATE",
            "basis": path.name,
            "status": "PROVISIONAL",
        })

    return {
        "type": "SOURCE_PACKAGE",
        "package_id": package_id,
        "source_id": "SRC-002",
        "source_name": "GM Quality System Basics Overview Supplier Audit",
        "source_title": "GM Quality System Basics Overview - Supplier Audit",
        "source_revision": "March 2009",
        "scope": {
            "chunk_start": f"GM-{start:03d}",
            "chunk_end": f"GM-{end:03d}",
            "chunk_count": len(files),
            "missing_chunks": [f"GM-{number:03d}" for number in missing],
            "source_directory": str(patch_root),
        },
        "fragments": fragments,
        "provisional_candidates": candidates,
        "processing_boundary": {
            "semantic_decision": "NOT_PERFORMED",
            "cmoc_write": "NONE",
            "object_index_write": "NONE",
            "human_review_required": True,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build SOURCE_PACKAGE from prepared GM chunks"
    )
    parser.add_argument("--patch-root", default="04 PATCH")
    parser.add_argument("--start", type=int, required=True)
    parser.add_argument("--end", type=int, required=True)
    parser.add_argument("--package-id", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    package = build_package(
        Path(args.patch_root),
        args.start,
        args.end,
        args.package_id,
    )

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(package, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(json.dumps({
        "status": "SOURCE_PACKAGE_WRITTEN",
        "output": str(output),
        "chunk_start": package["scope"]["chunk_start"],
        "chunk_end": package["scope"]["chunk_end"],
        "chunk_count": package["scope"]["chunk_count"],
        "fragment_count": len(package["fragments"]),
        "candidate_count": len(package["provisional_candidates"]),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
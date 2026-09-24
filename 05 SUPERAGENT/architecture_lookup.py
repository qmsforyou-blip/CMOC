#!/usr/bin/env python3
"""Read-only Architecture Lookup resolver."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

ROLE_ORDER = ("contract", "implementation", "test", "evidence")
REALIZATION_MODES = ("DIRECT", "COMPOSITE", "GATE")

STATUS_PATTERNS = (
    "ACCEPTED",
    "IMPLEMENTATION PROVEN",
    "DESIGN / ARCHITECTURE CANDIDATE",
    "TESTED / NOT ACCEPTED",
    "PARTIAL / LIMITED",
    "MISSING",
    "NOT_REQUIRED",
)


@dataclass(frozen=True)
class Artifact:
    path: str
    role: str
    status: tuple[str, ...]
    resolution_basis: str


def _norm(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def _subject_tokens(subject_key: str) -> tuple[str, ...]:
    return tuple(x.lower() for x in re.split(r"[^A-Za-z0-9]+", subject_key) if x)


def _subject_matches(path: Path, subject_key: str, text: str) -> bool:
    tokens = _subject_tokens(subject_key)
    if not tokens:
        return False
    filename_tokens = _norm(path.name).split()
    if all(token in filename_tokens for token in tokens):
        return True
    body = _norm(text[:12000])
    return re.search(
        r"(?<![a-z0-9])" + re.escape(subject_key.lower()) + r"(?![a-z0-9])",
        body,
    ) is not None


def _role(path: Path, text: str) -> str | None:
    name = path.name.lower()
    upper = path.name.upper()
    if "EVIDENCE-" in upper:
        return "evidence"
    if name.startswith("test_") or name.startswith("test-") or name.endswith("_test.py"):
        return "test"
    if (
        "BOUNDARY" in upper
        or "CONTRACT" in upper
        or "STANDARD" in upper
        or "READINESS-GATE" in upper
        or "ARCHITECTURE-REVIEW" in upper
        or "PROFILE" in upper
    ) and path.suffix.lower() in {".md", ".txt"}:
        return "contract"
    if path.suffix.lower() == ".py":
        return "implementation"
    return None


def _statuses(text: str) -> tuple[str, ...]:
    found: list[str] = []
    upper = text.upper()
    for status in STATUS_PATTERNS:
        if status in upper and status not in found:
            found.append(status)
    for observed in (
        "READY_WITH_LIMITATIONS",
        "READY_FOR_NEXT_PRODUCTION_PHASE",
        "NOT_READY",
        "EVIDENCE_INCOMPLETE",
    ):
        if observed in upper and observed not in found:
            found.append(observed)
    return tuple(found)


def _iter_files(root: Path) -> Iterable[Path]:
    ignored = {".git", ".obsidian", "__pycache__"}
    for path in sorted(root.rglob("*"), key=lambda p: str(p).lower()):
        if path.is_file() and not any(part in ignored for part in path.parts):
            yield path


def _infer_realization_mode(subject_key: str, contracts: list[Artifact], contract_texts: list[str]) -> str:
    """Infer only from explicit contract wording; never infer from absence alone."""
    corpus = " ".join(contract_texts).upper()
    if "READINESS GATE" in corpus or "READINESS-GATE" in corpus:
        return "GATE"
    if "INTEGRATION" in corpus or "COMPOSITE" in corpus or "COMPOSITION" in corpus:
        return "COMPOSITE"
    return "DIRECT"


def lookup(subject_key: str, repository_root: str | Path) -> dict:
    root = Path(repository_root).resolve()
    if not root.is_dir():
        raise ValueError(f"repository_root is not a directory: {root}")

    grouped: dict[str, list[Artifact]] = {role: [] for role in ROLE_ORDER}
    contract_texts: list[str] = []

    for path in _iter_files(root):
        if path.suffix.lower() not in {".md", ".txt", ".py", ".json"}:
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        role = _role(path, text)
        if role is None or not _subject_matches(path, subject_key, text):
            continue
        rel = path.relative_to(root).as_posix()
        filename_match = all(
            token in _norm(path.name).split() for token in _subject_tokens(subject_key)
        )
        artifact = Artifact(
            path=rel,
            role=role,
            status=_statuses(text),
            resolution_basis="filename" if filename_match else "explicit-subject-reference",
        )
        grouped[role].append(artifact)
        if role == "contract":
            contract_texts.append(text)

    for role in ROLE_ORDER:
        grouped[role].sort(key=lambda item: item.path.lower())

    realization_mode = _infer_realization_mode(
        subject_key, grouped["contract"], contract_texts
    )

    gaps: list[str] = []
    for role in ("contract", "test", "evidence"):
        if not grouped[role]:
            gaps.append(f"MISSING_{role.upper()}")

    # Implementation absence is a gap only for a DIRECT realization.
    # COMPOSITE and GATE subjects are explicitly realized by existing
    # architectural composition or gate/test infrastructure.
    if realization_mode == "DIRECT" and not grouped["implementation"]:
        gaps.append("MISSING_IMPLEMENTATION")

    return {
        "schema": "ARCHITECTURE-LOOKUP-RESULT-001",
        "version": "0.2",
        "subject_key": subject_key,
        "repository_root": str(root),
        "resolved_at": datetime.now(timezone.utc).isoformat(),
        "artifacts": {
            role: [asdict(item) for item in grouped[role]]
            for role in ROLE_ORDER
        },
        "implementation_realization": {
            "mode": realization_mode,
            "artifacts": [asdict(item) for item in grouped["implementation"]],
            "basis": (
                "explicit contract wording"
                if realization_mode != "DIRECT"
                else "default direct realization rule"
            ),
        },
        "gaps": gaps,
        "summary": {
            "contract_count": len(grouped["contract"]),
            "implementation_count": len(grouped["implementation"]),
            "test_count": len(grouped["test"]),
            "evidence_count": len(grouped["evidence"]),
            "realization_mode": realization_mode,
            "gap_count": len(gaps),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("subject_key")
    parser.add_argument("repository_root")
    args = parser.parse_args()
    print(json.dumps(lookup(args.subject_key, args.repository_root), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

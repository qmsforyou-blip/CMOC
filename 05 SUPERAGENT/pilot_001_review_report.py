"""Generate a human-readable Markdown review sheet from a RUN."""
from __future__ import annotations

import argparse
import json
import sqlite3
from pathlib import Path


def build_report(db_path: Path, run_id: str) -> str:
    with sqlite3.connect(str(db_path)) as db:
        row = db.execute(
            "SELECT payload_json FROM adapter_results "
            "WHERE run_id=? AND stage_id='RECONCILIATION' "
            "ORDER BY rowid DESC LIMIT 1",
            (run_id,),
        ).fetchone()
        state = db.execute(
            "SELECT run_status, current_stage_id FROM run_state WHERE run_id=?",
            (run_id,),
        ).fetchone()
        discovery_row = db.execute(
            "SELECT payload_json FROM adapter_results "
            "WHERE run_id=? AND stage_id='DISCOVERY' ORDER BY rowid DESC LIMIT 1",
            (run_id,),
        ).fetchone()
    if row is None:
        raise ValueError("RECONCILIATION_RESULT_NOT_FOUND")
    if state is None:
        raise ValueError("RUN_NOT_FOUND")

    reconciliation = json.loads(row[0])["reconciliation_result"]
    passport_by_id = {}
    if discovery_row is not None:
        discovery = json.loads(discovery_row[0]).get("discovery", {})
        for result in discovery.get("results", []):
            if result.get("type") == "PASSPORT_RECORDS":
                passport_by_id = {item["id"]: item for item in result.get("records", [])}
    summary = reconciliation["summary"]
    lines = [
        "# PILOT-001 — Human Review",
        "",
        f"- **RUN_ID:** `{run_id}`",
        f"- **Состояние RUN:** `{state[0]}`",
        f"- **Стадия:** `{state[1]}`",
        f"- **Всего записей:** {summary['total']}",
        f"- **EXISTING_EQUIVALENT:** {summary['existing_equivalent']}",
        f"- **NEEDS_REVIEW:** {summary['needs_review']}",
        "",
        "## Записи для решения",
        "",
    ]
    for number, record in enumerate(reconciliation["records"], 1):
        trace = record.get("traceability", {})
        passport = passport_by_id.get(record.get("input_record_id"), {})
        lines.extend([
            f"### {number}. `{record['match_id']}`",
            "",
            f"- **Исходная запись:** `{record.get('input_record_id', '')}`",
            f"- **Название:** {passport.get('term', record.get('term', 'см. исходный паспорт'))}",
            f"- **Кандидат:** `{trace.get('candidate_id', '')}`",
            f"- **Результат сопоставления:** `{record['match_result']}`",
            f"- **Статус:** `{record.get('status', '')}`",
            f"- **CMOC object ID:** `{record.get('cmoc_object_id') or 'не найден'}`",
            f"- **Основание Superagent:** {record.get('basis', '')}",
            "",
            "**Решение СГ:** `ADMIT_EXISTING` / `ADMIT_NEW` / `REJECT` / `DEFER`",
            "",
            "**Основание решения:**",
            "",
            "_Заполнить после рассмотрения._",
            "",
        ])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", required=True)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    report = build_report(Path(args.db), args.run_id)
    Path(args.output).write_text(report, encoding="utf-8")
    print(json.dumps({"status": "REVIEW_REPORT_WRITTEN", "output": args.output}, ensure_ascii=False))


if __name__ == "__main__":
    main()

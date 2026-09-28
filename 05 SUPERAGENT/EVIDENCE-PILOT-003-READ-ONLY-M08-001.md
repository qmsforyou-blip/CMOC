# EVIDENCE — PILOT-003 persisted Discovery → reviewed M07 → read-only M08

**Date:** 28-09-2026  
**RUN:** `RUN-PILOT-003-SRC-005`  
**Source:** Imai, *Gemba Kaizen*, chapter 13, page 6 of the supplied extract  
**Status:** diagnostic production M08 result; no RUN decision or CMOC admission

## Input and controls

- M06 passports PAS-001…004 were read from the persisted DISCOVERY adapter result in `pilot_003.sqlite`.
- `PILOT-003-SRC-005-RELATION-BINDING.json` validated RUN, source package, evidence package, passport IDs, working classes, formulation basis, and evidence endpoint pairs without a new M01–M06 run.
- `PILOT-003-M07-REVIEWED-TRANSCRIPT.json` is a controlled transcription of the earlier read-only M07 output. It includes REL-002 and REL-003. REL-001 is excluded because PAS-001 is `STRUCTURAL_DISTINCTION`, so `ROLE_PARTICIPATES_IN_ACTIVITY` is unresolved.
- `pilot_003_m08_probe.py --validate-only` returned `M08_INPUT_VALIDATED`, with no LLM call or writes.

## Live diagnostic M08 result

`pilot_003_m08_probe.py` returned `READ_ONLY_M08_PROBE`:

| Decision | Target | Result | Basis |
| --- | --- | --- | --- |
| DEC-001 | REL-002: PAS-003 → PAS-002 | PROVISIONAL / ЧЕРНОВИК | EVID-IMA-CH13-P6-MEETING-MEASURES |
| DEC-002 | REL-003: PAS-004 → PAS-002 | PROVISIONAL / ЧЕРНОВИК | EVID-IMA-CH13-P6-MEETING-PROBLEMS |

Both decision records preserved `target_kind: RELATION_CANDIDATE`, `epistemic_status: PROVISIONAL`, their respective basis reference, and `evidence_gap: null`. M08 stated that no separate CMOC canonicalization criterion was supplied.

## Scope and next gate

This demonstrates that a controlled M08 diagnostic can evaluate two reviewed M07 relation candidates against the saved M06 passports without repeating Discovery. It does **not** persist M07/M08 results in the RUN journal or supersede the four human `DEFER` decisions. It does not establish a passport for the whole `Value Stream Performance Review` construction in `PATCH-IMA-013-CEO-KAIZEN-v1.md`, semantic NEW, Admission, C1/C2/C3, or a CMOC/index write.

Before a live admission attempt, identify a stable whole-object boundary and target type, compare it semantically against accumulated CMOC objects, and obtain an explicit human decision. No automatic promotion follows from `PROVISIONAL`.

## Извещение на изменение — `0211+280926`: граница целого кандидата

Проверен `DISCOVERY-RESULT-CONTRACT-001`: готовый source-bound DISCOVERY_RESULT передаётся в Reconciliation, а адаптация Reconciliation не вправе добавлять новый смысл добычи или решение NEW. `pilot_001_record_review.py` допускает ручное решение только для уникального `match_id` из сохранённого RECONCILIATION_RESULT. В RUN-003 имеются PAS-001…004, но нет паспорта и `match_id` для целого Value Stream Performance Review.

Следовательно, аналитический кандидат §013.3 PATCH нельзя задним числом добавить в RUN-003 через M07/M08 или оформить как его human decision. Для формального решения о целом потребуется отдельный контролируемый вход Discovery и собственная цепочка PAS → Reconciliation → human review; подготовка такого входа не изменяет исходный RUN-003. Пока тип и выход целого не доказаны, эта новая добыча не запускается автоматически. Протоколы двух read-only relation diagnostics остаются доказательством только их ограниченного охвата.

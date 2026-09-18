# AUTOMATED-RUN-001 — M04 Nomenclature

**Input:** AUTOMATED-RUN-001-M03-FORMULATIONS-RERUN-001.md only  
**Output:** Nomenclature Candidate Records  
**Purpose:** automated consolidation of formulations into source-bound nomenclature candidates.

## Contract

- Input cardinality: 120 Formulation Records.
- Operation: consolidate the three formulations belonging to each distinction into one nomenclature candidate.
- Output cardinality: 40 candidates.
- Candidate is NOT an Object.
- Candidate is NOT a Classification.
- Candidate is NOT a Passport.
- Candidate is NOT a Relation.
- Candidate is NOT a CMOC Canon.
- No prior Run A/B M04 results are used as input.
- No manual reconstruction after execution.

## NOMENCLATURE CANDIDATES

| ID | Candidate | Source Formulations | Status |
|---|---|---|---|
| NOM-AUTO-001 | Руководство по управлению претензиями | F-AUTO-R1-001-1..3 | CANDIDATE |
| NOM-AUTO-002 | Идентичность источника стандарта | F-AUTO-R1-002-1..3 | CANDIDATE |
| NOM-AUTO-003 | Область применимости процесса жалоб | F-AUTO-R1-003-1..3 | CANDIDATE |
| NOM-AUTO-004 | Информация из жалоб | F-AUTO-R1-004-1..3 | CANDIDATE |
| NOM-AUTO-005 | Функции процесса работы с жалобами | F-AUTO-R1-005-1..3 | CANDIDATE |
| NOM-AUTO-006 | Интеграция процесса в СМК | F-AUTO-R1-006-1..3 | CANDIDATE |
| NOM-AUTO-007 | Жизненный цикл процесса жалоб | F-AUTO-R1-007-1..3 | CANDIDATE |
| NOM-AUTO-008 | Условия эффективности процесса | F-AUTO-R1-008-1..3 | CANDIDATE |
| NOM-AUTO-009 | Терминологическая модель процесса жалоб | F-AUTO-R1-009-1..3 | CANDIDATE |
| NOM-AUTO-010 | Жалоба | F-AUTO-R1-010-1..3 | CANDIDATE |
| NOM-AUTO-011 | Удовлетворённость и обратная связь | F-AUTO-R1-011-1..3 | CANDIDATE |
| NOM-AUTO-012 | Цель, политика и процесс | F-AUTO-R1-012-1..3 | CANDIDATE |
| NOM-AUTO-013 | Доступность процесса жалоб | F-AUTO-R1-013-1..3 | CANDIDATE |
| NOM-AUTO-014 | Принципы процесса жалоб | F-AUTO-R1-014-1..3 | CANDIDATE |
| NOM-AUTO-015 | Ответственность в процессе | F-AUTO-R1-015-1..3 | CANDIDATE |
| NOM-AUTO-016 | Обязательства руководства | F-AUTO-R1-016-1..3 | CANDIDATE |
| NOM-AUTO-017 | Политика и процедуры | F-AUTO-R1-017-1..3 | CANDIDATE |
| NOM-AUTO-018 | Ответственность высшего руководства | F-AUTO-R1-018-1..3 | CANDIDATE |
| NOM-AUTO-019 | Представитель руководства | F-AUTO-R1-019-1..3 | CANDIDATE |
| NOM-AUTO-020 | Ответственность руководителей подразделений | F-AUTO-R1-020-1..3 | CANDIDATE |
| NOM-AUTO-021 | Требования к персоналу процесса | F-AUTO-R1-021-1..3 | CANDIDATE |
| NOM-AUTO-022 | Цели и критерии процесса | F-AUTO-R1-022-1..3 | CANDIDATE |
| NOM-AUTO-023 | Проектирование процесса | F-AUTO-R1-023-1..3 | CANDIDATE |
| NOM-AUTO-024 | Информация о процессе | F-AUTO-R1-024-1..3 | CANDIDATE |
| NOM-AUTO-025 | Регистрация жалобы | F-AUTO-R1-025-1..3 | CANDIDATE |
| NOM-AUTO-026 | Прослеживаемость жалобы | F-AUTO-R1-026-1..3 | CANDIDATE |
| NOM-AUTO-027 | Первоначальная оценка жалобы | F-AUTO-R1-027-1..3 | CANDIDATE |
| NOM-AUTO-028 | Расследование жалобы | F-AUTO-R1-028-1..3 | CANDIDATE |
| NOM-AUTO-029 | Решение и действие по жалобе | F-AUTO-R1-029-1..3 | CANDIDATE |
| NOM-AUTO-030 | Закрытие жалобы | F-AUTO-R1-030-1..3 | CANDIDATE |
| NOM-AUTO-031 | Управление записями | F-AUTO-R1-031-1..3 | CANDIDATE |
| NOM-AUTO-032 | Анализ жалоб | F-AUTO-R1-032-1..3 | CANDIDATE |
| NOM-AUTO-033 | Удовлетворённость процессом жалоб | F-AUTO-R1-033-1..3 | CANDIDATE |
| NOM-AUTO-034 | Мониторинг процесса | F-AUTO-R1-034-1..3 | CANDIDATE |
| NOM-AUTO-035 | Аудит процесса | F-AUTO-R1-035-1..3 | CANDIDATE |
| NOM-AUTO-036 | Входы рассмотрения руководством | F-AUTO-R1-036-1..3 | CANDIDATE |
| NOM-AUTO-037 | Выходы рассмотрения руководством | F-AUTO-R1-037-1..3 | CANDIDATE |
| NOM-AUTO-038 | Постоянное улучшение | F-AUTO-R1-038-1..3 | CANDIDATE |
| NOM-AUTO-039 | Соразмерность процесса ресурсам | F-AUTO-R1-039-1..3 | CANDIDATE |
| NOM-AUTO-040 | Форма жалобы | F-AUTO-R1-040-1..3 | CANDIDATE |

## TRACE

Every candidate traces to its three formulations and therefore to the underlying distinction, extraction record, batch and source:

**NOMENCLATURE → FORMULATION → DISTINCTION → EXTRACTION → BATCH → SOURCE**

## QC

- Input formulations: 120
- Processed formulations: 120
- Unprocessed formulations: 0
- Output candidates: 40
- Cardinality: 120 → 40
- Every candidate has exactly 3 source formulation records: PASS
- Candidate/object boundary: PASS
- Classification fields: 0
- Passport fields: 0
- Relation fields: 0
- Canonization: NONE
- Prior Run A/B M04 outputs used as input: NO
- Manual reconstruction after execution: NO
- Traceability: PASS

## RESULT

**PASS** — M04 automated nomenclature stage completed with 120 → 40 candidates and preserved the stage boundary.

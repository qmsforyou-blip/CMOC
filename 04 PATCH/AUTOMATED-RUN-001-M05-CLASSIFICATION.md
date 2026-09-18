# AUTOMATED-RUN-001 — M05 Classification

**Input:** AUTOMATED-RUN-001-M04-NOMENCLATURE.md only  
**Output:** Classification Records  
**Purpose:** automated typing of nomenclature candidates without advancing them to passports, relations or canon.

## CONTRACT

- Input: 40 Nomenclature Candidates.
- Operation: assign one source-bound classification to each candidate.
- Output: 40 Classification Records.
- Cardinality: 40 → 40.
- Candidate remains a candidate until classification is produced; classification does not make the candidate a CMOC object.
- No prior Run A/B M05 results are used as input.
- No passport, relation or canon fields are introduced.

## CLASSIFICATION RECORDS

| ID | Candidate | Classification |
|---|---|---|
| CLS-AUTO-001 | Руководство по управлению претензиями | GUIDANCE |
| CLS-AUTO-002 | Идентичность источника стандарта | SOURCE_IDENTITY |
| CLS-AUTO-003 | Область применимости процесса жалоб | SCOPE |
| CLS-AUTO-004 | Информация из жалоб | INFORMATION |
| CLS-AUTO-005 | Функции процесса работы с жалобами | PROCESS_FUNCTION |
| CLS-AUTO-006 | Интеграция процесса в СМК | INTEGRATION |
| CLS-AUTO-007 | Жизненный цикл процесса жалоб | PROCESS_LIFECYCLE |
| CLS-AUTO-008 | Условия эффективности процесса | CAPABILITY |
| CLS-AUTO-009 | Терминологическая модель процесса жалоб | CONCEPT_MODEL |
| CLS-AUTO-010 | Жалоба | ENTITY |
| CLS-AUTO-011 | Удовлетворённость и обратная связь | INFORMATION |
| CLS-AUTO-012 | Цель, политика и процесс | MANAGEMENT_CONCEPT |
| CLS-AUTO-013 | Доступность процесса жалоб | PROCESS_PROPERTY |
| CLS-AUTO-014 | Принципы процесса жалоб | PRINCIPLE |
| CLS-AUTO-015 | Ответственность в процессе | RESPONSIBILITY |
| CLS-AUTO-016 | Обязательства руководства | RESPONSIBILITY |
| CLS-AUTO-017 | Политика и процедуры | MANAGEMENT_CONCEPT |
| CLS-AUTO-018 | Ответственность высшего руководства | RESPONSIBILITY |
| CLS-AUTO-019 | Представитель руководства | ROLE |
| CLS-AUTO-020 | Ответственность руководителей подразделений | RESPONSIBILITY |
| CLS-AUTO-021 | Требования к персоналу процесса | REQUIREMENT |
| CLS-AUTO-022 | Цели и критерии процесса | REQUIREMENT |
| CLS-AUTO-023 | Проектирование процесса | ACTIVITY |
| CLS-AUTO-024 | Информация о процессе | INFORMATION |
| CLS-AUTO-025 | Регистрация жалобы | ACTIVITY |
| CLS-AUTO-026 | Прослеживаемость жалобы | CAPABILITY |
| CLS-AUTO-027 | Первоначальная оценка жалобы | ACTIVITY |
| CLS-AUTO-028 | Расследование жалобы | ACTIVITY |
| CLS-AUTO-029 | Решение и действие по жалобе | DECISION_ACTIVITY |
| CLS-AUTO-030 | Закрытие жалобы | STATE_TRANSITION |
| CLS-AUTO-031 | Управление записями | PROCESS |
| CLS-AUTO-032 | Анализ жалоб | ACTIVITY |
| CLS-AUTO-033 | Удовлетворённость процессом жалоб | MEASUREMENT |
| CLS-AUTO-034 | Мониторинг процесса | MEASUREMENT |
| CLS-AUTO-035 | Аудит процесса | ACTIVITY |
| CLS-AUTO-036 | Входы рассмотрения руководством | INPUT |
| CLS-AUTO-037 | Выходы рассмотрения руководством | OUTPUT |
| CLS-AUTO-038 | Постоянное улучшение | PROCESS_FUNCTION |
| CLS-AUTO-039 | Соразмерность процесса ресурсам | CONSTRAINT |
| CLS-AUTO-040 | Форма жалобы | ARTIFACT |

## TRACE

**CLASSIFICATION → NOMENCLATURE → FORMULATION → DISTINCTION → EXTRACTION → BATCH → SOURCE**

## QC

- Input candidates: 40
- Processed candidates: 40
- Unprocessed: 0
- Output classifications: 40
- Cardinality: 40 → 40
- One classification per candidate: PASS
- Classification fields introduced: YES, only at M05
- Passport fields: 0
- Relation fields: 0
- Canonization: NONE
- Prior Run A/B M05 outputs used as input: NO
- Manual reconstruction: NO
- Stage boundary: PASS

## RESULT

**PASS** — M05 automated classification completed with 40 → 40 classifications and did not cross into passport, relation or canonization stages.

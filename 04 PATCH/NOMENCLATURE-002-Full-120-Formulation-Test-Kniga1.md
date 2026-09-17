# NOMENCLATURE-002 — Full 40-Distinction / 120-Formulation Test
# MACHINE-SOURCE-001 / M04 NOMENCLATURE

**Дата:** 17-09-2026  
**Статус:** TEST OUTPUT  
**Источник:** `SRC-AU-KNIGA1-001`  
**Вход:** 120 `FORMULATION RECORDS`  
**Выход:** 36 `NOMENCLATURE CANDIDATES`

## Правило M04
M04 выделяет из формулировок кандидатов номенклатуры. Кандидат — это ещё не канонический CMOC-объект. Повтор термина не означает тождество сущностей.

Ключевое различение: **TERM OCCURRENCE ≠ TERM ENTITY** и **SAME TERM ≠ SAME ENTITY**.

## NOMENCLATURE REGISTER

| ID | TERM | PROVISIONAL TYPE | SOURCE FORMULATIONS |
|---|---|---|---|
| NOM-AU-001 | предмет управления | OBJECT_CANDIDATE | FM-AU-001-02; FM-AU-001-03; FM-AU-035-02 |
| NOM-AU-002 | интерпретация | REPRESENTATION_CANDIDATE | FM-AU-001-02; FM-AU-011-03; FM-AU-015-02; FM-AU-036-02 |
| NOM-AU-003 | управление | CONCEPT_CANDIDATE | FM-AU-002-01; FM-AU-004-02; FM-AU-018-03 |
| NOM-AU-004 | основания управления | FOUNDATION_CANDIDATE | FM-AU-002-02; FM-AU-002-03; FM-AU-010-02 |
| NOM-AU-005 | формальная зрелость | STATE_CANDIDATE | FM-AU-003-02; FM-AU-003-03; FM-AU-010-02 |
| NOM-AU-006 | архитектура управления | ARCHITECTURE_CANDIDATE | FM-AU-003-02; FM-AU-003-03; FM-AU-007-02; FM-AU-040-02 |
| NOM-AU-007 | процесс | PROCESS_CANDIDATE | FM-AU-004-02; FM-AU-019-02; FM-AU-020-02; FM-AU-038-02 |
| NOM-AU-008 | деятельность | ACTIVITY_CANDIDATE | FM-AU-004-02; FM-AU-016-02; FM-AU-019-03; FM-AU-020-03 |
| NOM-AU-009 | контроль | CONTROL_CANDIDATE | FM-AU-002-02; FM-AU-004-02; FM-AU-018-02; FM-AU-018-03 |
| NOM-AU-010 | требование | REQUIREMENT_CANDIDATE | FM-AU-005-02; FM-AU-012-02; FM-AU-012-03; FM-AU-037-02 |
| NOM-AU-011 | фиксация | FIXATION_CANDIDATE | FM-AU-005-02; FM-AU-012-02; FM-AU-013-02; FM-AU-014-02; FM-AU-036-02; FM-AU-037-02 |
| NOM-AU-012 | решение | DECISION_CANDIDATE | FM-AU-005-02; FM-AU-016-02; FM-AU-021-02; FM-AU-022-02; FM-AU-025-02; FM-AU-035-02 |
| NOM-AU-013 | ответственность | RESPONSIBILITY_CANDIDATE | FM-AU-005-02; FM-AU-016-02; FM-AU-022-02; FM-AU-023-02; FM-AU-026-02; FM-AU-030-02 |
| NOM-AU-014 | архитектурный язык | LANGUAGE_CANDIDATE | FM-AU-006-02; FM-AU-006-03 |
| NOM-AU-015 | ИТ | TOOL_CANDIDATE | FM-AU-002-01; FM-AU-007-01; FM-AU-007-02 |
| NOM-AU-016 | ИИ | TOOL_CANDIDATE | FM-AU-002-01; FM-AU-007-01; FM-AU-007-02 |
| NOM-AU-017 | реальность | OBJECT_CANDIDATE | FM-AU-011-02; FM-AU-014-02; FM-AU-035-02 |
| NOM-AU-018 | представление | REPRESENTATION_CANDIDATE | FM-AU-011-02; FM-AU-011-03 |
| NOM-AU-019 | ожидание | EXPECTATION_CANDIDATE | FM-AU-012-02; FM-AU-012-03 |
| NOM-AU-020 | запись | RECORD_CANDIDATE | FM-AU-014-02; FM-AU-037-02 |
| NOM-AU-021 | управленческий факт | FACT_CANDIDATE | FM-AU-015-02; FM-AU-015-03 |
| NOM-AU-022 | героизм | ACTIVITY_PATTERN_CANDIDATE | FM-AU-017-02; FM-AU-017-03; FM-AU-040-02; FM-AU-040-03 |
| NOM-AU-023 | полномочие | AUTHORITY_CANDIDATE | FM-AU-023-02; FM-AU-023-03 |
| NOM-AU-024 | власть | POWER_CANDIDATE | FM-AU-024-02; FM-AU-024-03 |
| NOM-AU-025 | точка решения | DECISION_POINT_CANDIDATE | FM-AU-022-02; FM-AU-022-03; FM-AU-037-02 |
| NOM-AU-026 | коллективное обсуждение | COLLECTIVE_ACTIVITY_CANDIDATE | FM-AU-025-02; FM-AU-025-03; FM-AU-026-02 |
| NOM-AU-027 | выпуск | RELEASE_CANDIDATE | FM-AU-027-02; FM-AU-027-03; FM-AU-028-02; FM-AU-039-02 |
| NOM-AU-028 | результат | RESULT_CANDIDATE | FM-AU-027-02; FM-AU-028-02; FM-AU-029-02; FM-AU-030-02 |
| NOM-AU-029 | необратимость | IRREVERSIBILITY_CANDIDATE | FM-AU-027-02; FM-AU-032-02; FM-AU-039-02 |
| NOM-AU-030 | приёмка | ACCEPTANCE_CANDIDATE | FM-AU-029-02; FM-AU-029-03 |
| NOM-AU-031 | подпись | SIGNATURE_CANDIDATE | FM-AU-030-02; FM-AU-030-03; FM-AU-031-02 |
| NOM-AU-032 | принятие последствий | CONSEQUENCE_ACCEPTANCE_CANDIDATE | FM-AU-030-02; FM-AU-031-02; FM-AU-031-03 |
| NOM-AU-033 | точка невозврата | POINT_OF_NO_RETURN_CANDIDATE | FM-AU-032-02; FM-AU-033-02; FM-AU-033-03; FM-AU-038-02 |
| NOM-AU-034 | предметный указатель | INDEX_CANDIDATE | FM-AU-034-01; FM-AU-034-02; FM-AU-034-03 |
| NOM-AU-035 | комиссия | COMMISSION_CANDIDATE | FM-AU-025-02; FM-AU-031-02; FM-AU-039-02 |
| NOM-AU-036 | каноническая формулировка | REPRESENTATION_CANDIDATE | FM-AU-006-02; FM-AU-034-02 |

## QC

- [x] 120 / 120 Formulation Records приняты M04.
- [x] 36 кандидатов номенклатуры выделены.
- [x] Повторяющиеся употребления одного термина сгруппированы как occurrences, но не объявлены одной сущностью.
- [x] Каждый кандидат имеет обратную трассировку к одному или нескольким Formulation Records.
- [x] M04 не выполняет CLASSIFICATION, PASSPORT, RELATIONS или CANONIZATION.
- [x] Provisional Type используется только как рабочая подсказка и не является каноническим типом CMOC.

## Handoff Contract

```text
FORMULATION REGISTER
        ↓
M04 NOMENCLATURE
        ↓
NOMENCLATURE REGISTER
```

Полная производственная трасса сохраняется:
```text
NOMENCLATURE
→ FORMULATION
→ DISTINCTION
→ EXTRACTION
→ BATCH
→ SOURCE
```

## Результат теста

**M04 FULL 120-FORMULATION TEST — PASSED**

Из 120 Formulation Records выделено 36 кандидатов номенклатуры. Кандидаты не объявлены каноническими объектами; повторные употребления терминов не склеены автоматически в сущности.

Ограничение: тест подтверждает интерфейс M04 на полном тестовом регистре из 120 формулировок, но не является доказательством автоматического прогона M05–M08.

## Следующий интерфейс

`NOMENCLATURE → CLASSIFICATION`

M05 должен типизировать кандидатов, сохраняя различие между рабочим типом и каноническим объектом.

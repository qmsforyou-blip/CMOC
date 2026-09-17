# CLASSIFICATION-002 — Full 36-Nomenclature Test
# MACHINE-SOURCE-001 / M05 CLASSIFICATION

**Дата:** 17-09-2026  
**Статус:** TEST OUTPUT  
**Источник:** `SRC-AU-KNIGA1-001`  
**Вход:** 36 `NOMENCLATURE CANDIDATES`  
**Выход:** 36 `CLASSIFICATION RECORDS`

## Правило M05
M05 присваивает кандидату рабочий тип на основании уже полученной номенклатуры. Рабочий тип не является утверждением о канонической сущности.

Ключевое различение: **TYPE ≠ CANONICAL OBJECT**.

## CLASSIFICATION REGISTER

| ID | NOMENCLATURE_ID | TERM | PROVISIONAL TYPE | BASIS |
|---|---|---|---|---|
| CLS-AU-001 | NOM-AU-001 | предмет управления | OBJECT_CANDIDATE | кандидат обозначает предмет управления |
| CLS-AU-002 | NOM-AU-002 | интерпретация | REPRESENTATION_CANDIDATE | кандидат обозначает интерпретацию |
| CLS-AU-003 | NOM-AU-003 | управление | CONCEPT_CANDIDATE | кандидат обозначает общее понятие управления |
| CLS-AU-004 | NOM-AU-004 | основания управления | FOUNDATION_CANDIDATE | кандидат обозначает основания |
| CLS-AU-005 | NOM-AU-005 | формальная зрелость | STATE_CANDIDATE | кандидат обозначает состояние |
| CLS-AU-006 | NOM-AU-006 | архитектура управления | ARCHITECTURE_CANDIDATE | кандидат обозначает архитектуру |
| CLS-AU-007 | NOM-AU-007 | процесс | PROCESS_CANDIDATE | кандидат обозначает процесс |
| CLS-AU-008 | NOM-AU-008 | деятельность | ACTIVITY_CANDIDATE | кандидат обозначает деятельность |
| CLS-AU-009 | NOM-AU-009 | контроль | CONTROL_CANDIDATE | кандидат обозначает контроль |
| CLS-AU-010 | NOM-AU-010 | требование | REQUIREMENT_CANDIDATE | кандидат обозначает требование |
| CLS-AU-011 | NOM-AU-011 | фиксация | FIXATION_CANDIDATE | кандидат обозначает фиксацию |
| CLS-AU-012 | NOM-AU-012 | решение | DECISION_CANDIDATE | кандидат обозначает решение |
| CLS-AU-013 | NOM-AU-013 | ответственность | RESPONSIBILITY_CANDIDATE | кандидат обозначает ответственность |
| CLS-AU-014 | NOM-AU-014 | архитектурный язык | LANGUAGE_CANDIDATE | кандидат обозначает язык описания |
| CLS-AU-015 | NOM-AU-015 | ИТ | TOOL_CANDIDATE | кандидат обозначает инструмент |
| CLS-AU-016 | NOM-AU-016 | ИИ | TOOL_CANDIDATE | кандидат обозначает инструмент |
| CLS-AU-017 | NOM-AU-017 | реальность | OBJECT_CANDIDATE | кандидат обозначает реальность как объект различения |
| CLS-AU-018 | NOM-AU-018 | представление | REPRESENTATION_CANDIDATE | кандидат обозначает представление |
| CLS-AU-019 | NOM-AU-019 | ожидание | EXPECTATION_CANDIDATE | кандидат обозначает ожидание |
| CLS-AU-020 | NOM-AU-020 | запись | RECORD_CANDIDATE | кандидат обозначает запись как форму фиксации |
| CLS-AU-021 | NOM-AU-021 | управленческий факт | FACT_CANDIDATE | кандидат обозначает управленческий факт |
| CLS-AU-022 | NOM-AU-022 | героизм | ACTIVITY_PATTERN_CANDIDATE | кандидат обозначает паттерн деятельности |
| CLS-AU-023 | NOM-AU-023 | полномочие | AUTHORITY_CANDIDATE | кандидат обозначает полномочие |
| CLS-AU-024 | NOM-AU-024 | власть | POWER_CANDIDATE | кандидат обозначает власть |
| CLS-AU-025 | NOM-AU-025 | точка решения | DECISION_POINT_CANDIDATE | кандидат обозначает точку решения |
| CLS-AU-026 | NOM-AU-026 | коллективное обсуждение | COLLECTIVE_ACTIVITY_CANDIDATE | кандидат обозначает коллективную деятельность |
| CLS-AU-027 | NOM-AU-027 | выпуск | RELEASE_CANDIDATE | кандидат обозначает выпуск |
| CLS-AU-028 | NOM-AU-028 | результат | RESULT_CANDIDATE | кандидат обозначает результат |
| CLS-AU-029 | NOM-AU-029 | необратимость | IRREVERSIBILITY_CANDIDATE | кандидат обозначает необратимость |
| CLS-AU-030 | NOM-AU-030 | приёмка | ACCEPTANCE_CANDIDATE | кандидат обозначает приёмку |
| CLS-AU-031 | NOM-AU-031 | подпись | SIGNATURE_CANDIDATE | кандидат обозначает подпись |
| CLS-AU-032 | NOM-AU-032 | принятие последствий | CONSEQUENCE_ACCEPTANCE_CANDIDATE | кандидат обозначает принятие последствий |
| CLS-AU-033 | NOM-AU-033 | точка невозврата | POINT_OF_NO_RETURN_CANDIDATE | кандидат обозначает точку невозврата |
| CLS-AU-034 | NOM-AU-034 | предметный указатель | INDEX_CANDIDATE | кандидат обозначает указатель |
| CLS-AU-035 | NOM-AU-035 | комиссия | COMMISSION_CANDIDATE | кандидат обозначает комиссию |
| CLS-AU-036 | NOM-AU-036 | каноническая формулировка | REPRESENTATION_CANDIDATE | кандидат обозначает форму представления |

## QC

- [x] 36 / 36 Nomenclature Candidates приняты M05.
- [x] 36 / 36 получили рабочий `PROVISIONAL TYPE`.
- [x] Ни один рабочий тип не объявлен каноническим объектом.
- [x] Идентичность кандидатов не изменена и автоматически не склеена.
- [x] Каждый Classification Record имеет обратную ссылку на `NOMENCLATURE_ID`.
- [x] M05 не выполняет PASSPORT, RELATIONS или CANONIZATION.

## Handoff Contract

```text
NOMENCLATURE REGISTER
        ↓
M05 CLASSIFICATION
        ↓
CLASSIFICATION REGISTER
```

Полная производственная трасса:
```text
CLASSIFICATION
→ NOMENCLATURE
→ FORMULATION
→ DISTINCTION
→ EXTRACTION
→ BATCH
→ SOURCE
```

## Результат теста

**M05 FULL 36-NOMENCLATURE TEST — PASSED**

36 кандидатов номенклатуры типизированы без превращения рабочего типа в утверждение о каноническом объекте.

Ограничение: тест подтверждает интерфейс M05 на полном тестовом регистре из 36 кандидатов; автоматический прогон M06–M08 отдельно не доказан.

## Следующий интерфейс

`CLASSIFICATION → PASSPORT`

M06 должен собрать паспорт кандидата, не добавляя сведений, которых нет в основаниях.

# RELATIONS-002 — Full 36-Passport Test — Книга 1

**Дата:** 17-09-2026  
**Machine:** M07 RELATIONS  
**Input:** 36 Passport Records  
**Output:** Relation Candidates  
**Status:** TEST PASSED

## Цель

Проверить полный прогон M07 на 36 паспортных записях с сохранением происхождения и с жёстким различением:

> RELATION CANDIDATE ≠ ESTABLISHED RELATION

M07 извлекает только отношения, которые имеют основание в уже полученных Passport Records. Обнаруженное отношение не становится автоматически установленной связью CMOC.

## Результат

Из 36 Passport Records сформировано **18 Relation Candidates**.

| ID | FROM | RELATION | TO | STATUS |
|---|---|---|---|---|
| REL-AU-001 | expectation | LEADS_TO | requirement | PROVISIONAL |
| REL-AU-002 | fixation | ENABLES | requirement | PROVISIONAL |
| REL-AU-003 | record | FIXES | reality | PROVISIONAL |
| REL-AU-004 | decision | CARRIES | responsibility | PROVISIONAL |
| REL-AU-005 | authority | ENABLES | decision | PROVISIONAL |
| REL-AU-006 | collective_discussion | DOES_NOT_REPLACE | personal_decision | PROVISIONAL |
| REL-AU-007 | activity | DISTINCT_FROM | management | PROVISIONAL |
| REL-AU-008 | formal_process | DISTINCT_FROM | management_architecture | PROVISIONAL |
| REL-AU-009 | process | PRODUCES | result | PROVISIONAL |
| REL-AU-010 | result | PRECEDES | release | PROVISIONAL |
| REL-AU-011 | release | CREATES | irreversibility | PROVISIONAL |
| REL-AU-012 | acceptance | CONFIRMS | result | PROVISIONAL |
| REL-AU-013 | signature | EXPRESSES | personal_acceptance | PROVISIONAL |
| REL-AU-014 | commission | DOES_NOT_REPLACE | personal_decision | PROVISIONAL |
| REL-AU-015 | power | ENABLES | transition | PROVISIONAL |
| REL-AU-016 | decision_point | LINKS | responsibility | PROVISIONAL |
| REL-AU-017 | heroism | COMPENSATES_FOR | architecture_defect | PROVISIONAL |
| REL-AU-018 | point_of_no_return | FOLLOWS | release | PROVISIONAL |

## Контроль границы M07

M07 не выполняет:

- канонизацию отношений;
- доказательство отношения сверх оснований Passport Records;
- слияние объектов;
- изменение исходных Passport Records;
- создание новых объектов только ради удобства построения графа.

## Трассировка

Каждый Relation Candidate сохраняет происхождение через паспортную запись и далее по производственной цепочке:

`RELATION → PASSPORT → CLASSIFICATION → NOMENCLATURE → FORMULATION → DISTINCTION → EXTRACTION → BATCH → SOURCE`

## Контроль неопределённости

Все отношения имеют статус `PROVISIONAL`. Это означает, что отношение выявлено как кандидат на основании предыдущих производственных результатов, но ещё не прошло M08 CANONIZATION.

## Проверки

- 36/36 Passport Records рассмотрены;
- Relation Candidates сформированы только из имеющейся производственной базы;
- направление и тип отношения указаны явно;
- статус отношения отделён от факта его обнаружения;
- исходные паспорта не изменены;
- кандидаты отношений не объявлены установленными отношениями;
- обратная трассировка предусмотрена.

## Вердикт

**M07 FULL 36-PASSPORT TEST — PASSED**

Следующий тест: **M08 CANONIZATION** — переход от кандидатов объектов и отношений к решению о статусе `CANONICAL / PROVISIONAL / NEEDS_EVIDENCE`.

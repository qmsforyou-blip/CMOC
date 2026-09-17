# REPEATABILITY-RUN-001-GOST-M08-A-B-SEMANTIC-COMPARISON

Дата: 17-09-2026

## Назначение

Сверка результатов M08 CANONIZATION между Run A и Run B для:

`SOURCE_ID: SRC-GOST-ISO-10002-2007-001`

Сравнение выполнено по идентичности паспортных объектов и по решениям канонизации, а не по поверхностным формулировкам.

## Исходные результаты

### Run A
- Objects: 40
- PROVISIONAL: 32
- NEEDS_EVIDENCE: 8
- CANONICAL: 0

В Run A статус `NEEDS_EVIDENCE` был присвоен объектам 001–008.

### Run B
- Objects: 40
- PROVISIONAL: 36
- NEEDS_EVIDENCE: 4
- CANONICAL: 0

В Run B статус `NEEDS_EVIDENCE` был присвоен объектам 002, 009, 012, 019.

Relations Run B:
- 25 PROVISIONAL
- 0 CANONICAL

## Сверка объектов

Общим `NEEDS_EVIDENCE` является только объект 002.

Следовательно:

- PROVISIONAL / PROVISIONAL: **29**
- NEEDS_EVIDENCE / NEEDS_EVIDENCE: **1**
- Run A NEEDS_EVIDENCE → Run B PROVISIONAL: **7**
- Run A PROVISIONAL → Run B NEEDS_EVIDENCE: **3**
- CANONICAL в обоих: **0**

Итого:

**MATCH: 30/40**  
**VARIANT: 10/40**  
**DIVERGENCE: 0/40**

Здесь `VARIANT` означает нестабильность решения степени доказанности, а не потерю объекта или содержательное расхождение самого объекта.

## Матрица нестабильных решений

| Object | Run A | Run B | Тип |
|---|---|---|---|
| 001 | NEEDS_EVIDENCE | PROVISIONAL | variant |
| 003 | NEEDS_EVIDENCE | PROVISIONAL | variant |
| 004 | NEEDS_EVIDENCE | PROVISIONAL | variant |
| 005 | NEEDS_EVIDENCE | PROVISIONAL | variant |
| 006 | NEEDS_EVIDENCE | PROVISIONAL | variant |
| 007 | NEEDS_EVIDENCE | PROVISIONAL | variant |
| 008 | NEEDS_EVIDENCE | PROVISIONAL | variant |
| 009 | PROVISIONAL | NEEDS_EVIDENCE | variant |
| 012 | PROVISIONAL | NEEDS_EVIDENCE | variant |
| 019 | PROVISIONAL | NEEDS_EVIDENCE | variant |

Объект 002 совпадает как `NEEDS_EVIDENCE`.

## Relations

Для Run B получено 25 PROVISIONAL Relations.

По результатам M07 после нормализации endpoint identity:

**25/25 MATCH, 0 VARIANT, 0 DIVERGENCE.**

Поэтому на уровне множества и семантики Relations расхождения между повторными проходами не обнаружено.

## Вывод

M08 **не проходит строгий тест повторяемости решений по epistemic status**.

Однако это не означает, что M08 разрушает трассируемость или меняет объектную модель:

- все 40 объектов сохранены;
- все 40 получили явное решение;
- 0 объектов потеряно;
- 0 объектов получили CANONICAL;
- нестабильность затронула только границу `PROVISIONAL ↔ NEEDS_EVIDENCE`.

Иными словами, проблема находится не в добыче объектов, а в **критерии присвоения степени доказанности на M08**.

## Методологический вывод

M08 требует более жёсткого и воспроизводимого `DECISION_RULE`.

До следующего запуска необходимо отделить:

1. факт наличия достаточного основания для фиксации объекта;
2. наличие конкретного дефицита доказательств;
3. критерий, при котором объект обязан перейти из `PROVISIONAL` в `NEEDS_EVIDENCE`.

Рекомендуемая следующая операция:

**не переписывать Run A или Run B задним числом**, а создать отдельный QC/patch для определения нормативного критерия M08 и затем провести контрольную сверку на тех 10 объектах, где решения расходятся.

## Статус Repeatability Run

| Модуль | Результат |
|---|---|
| M01 | повторяемость по cardinality подтверждена |
| M02 | объектное множество сохранено; требуется учитывать naming variation |
| M03 | 40→120 |
| M04 | 40/40 semantic MATCH |
| M05 | 40/40 semantic MATCH |
| M06 | 40/40 semantic MATCH |
| M07 | 25/25 semantic MATCH после endpoint normalization |
| M08 | **30/40 MATCH; 10 VARIANT** |

### Общий вывод

Повторный прогон подтвердил устойчивость основной производственной цепочки до M07 и выявил конкретную точку, где требуется нормативное уточнение: **M08 decision rule for epistemic status**.

Это результат теста, а не основание для искусственного выравнивания Run A и Run B.

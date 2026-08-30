# GM-083 — S-4: STANDARDIZE / 4.4.1 Standard Operation / SOS — Major Steps & Time

**Дата:** 30-08-2026
**Статус:** SOURCE-SUPPORTED / SINGLE-SOURCE
**Извещение на изменение:** 0192+300826

## 1. SOURCE

Раздел 4.4.1 — STANDARDIZED WORK вводит Standard Operation / Standard Operation Sheet (SOS).

На уровне 4.4.1 SOURCE задаёт: **Major Steps, how long should it take? (SOS)**.

На примере Standard Operation Sheet SOURCE перечисляет обязательное содержание:

- Work Elements — элементы работы;
- Element Times — время элементов;
- Work Flow - Sequence — поток работы / последовательность;
- Standard in-process stock — стандартный запас в процессе;
- Operation Cycle Time — цикл операции;
- Takt Time – Customer and Actual — такт времени по заказчику и фактический.

Форма также содержит поля:
- Step No.;
- Workstation Area Drawn to Scale;
- Operation;
- From / To;
- Quantity per Shift;
- Customer Cycle Time;
- Shift;
- Operator Cycle Time;
- Work Element;
- Element Time;
- Standard In-Process Stock;
- Quality Check;
- Critical Operation;
- Safety;
- Hand Work;
- Machine;
- Walk;
- Total.

## 2. TERMS — ТЕРМИНЫ

| English | Русский |
|---|---|
| Standard Operation | стандартная операция |
| Standard Operation Sheet (SOS) | лист стандартной операции |
| Major Steps | основные шаги |
| Work Element | элемент работы |
| Element Time | время элемента |
| Work Flow | поток работы |
| Sequence | последовательность |
| Standard In-Process Stock | стандартный запас в процессе |
| Operation Cycle Time | время цикла операции |
| Customer Cycle Time | цикл по требованию заказчика |
| Operator Cycle Time | цикл оператора |
| Takt Time | тактовое время |
| Customer Takt Time | тактовое время по заказчику |
| Actual Takt Time | фактическое тактовое время |
| Workstation Area Drawn to Scale | рабочая зона, выполненная в масштабе |
| Step No. | номер шага |
| Quantity per Shift | количество за смену |
| Quality Check | проверка качества |
| Critical Operation | критическая операция |
| Safety | безопасность |
| Hand Work | ручная работа |
| Machine | машинная работа |
| Walk | перемещение / ходьба |
| Total | итог |

## 3. DISTINCTIONS — РАЗЛИЧЕНИЯ

### Major Steps ≠ Work Elements

В 4.4.1 SOURCE на обзорном уровне говорит о Major Steps, а в форме SOS конкретизирует структуру через Work Elements. Не отождествляем эти термины автоматически.

### Element Time ≠ Operation Cycle Time

В форме присутствуют оба поля. Следовательно, время отдельного элемента и время полного цикла операции — разные величины.

### Customer Cycle Time ≠ Operator Cycle Time

Оба поля присутствуют в SOS. SOURCE не разрешает сводить их к одной величине.

### Takt Time ≠ Cycle Time

SOURCE включает Takt Time и Operation Cycle Time как разные элементы Standard Operation Sheet.

### Work Flow ≠ Workstation Location

SOS одновременно описывает последовательность работы и рабочую зону, выполненную в масштабе. Это разные представления.

### Walk ≠ Work Element

В последующем SOURCE отдельно уточняет, что walking is not an element и обычно не включается в element sheets. Поэтому перемещение не следует автоматически считать самостоятельным Work Element.

## 4. EXTRACTION — ИЗВЛЕЧЕНИЕ

```text
STANDARD OPERATION
↓
MAJOR STEPS
↓
WORK ELEMENTS
↓
ELEMENT TIMES
↓
WORK FLOW / SEQUENCE
↓
OPERATION CYCLE TIME
+
TAKT TIME
```

Формальная структура SOS:

```text
WORK ELEMENT
→ ELEMENT TIME
→ SEQUENCE
→ STANDARD IN-PROCESS STOCK
→ QUALITY / CRITICAL / SAFETY
→ HAND WORK / MACHINE / WALK
→ TOTAL
```

**Статус:** первая схема — CMOC-реконструкция; вторая — реконструкция структуры формы SOURCE.

## 5. MECHANISM — МЕХАНИЗМ

### Standard Operation Sheet as Structured Work Representation

**CANDIDATE / SINGLE-SOURCE**

SOS представляет операцию через элементы работы, последовательность и временные характеристики, дополняя их данными о запасе в процессе, качестве, критичности и безопасности.

### Element Time Decomposition

**CANDIDATE / SINGLE-SOURCE**

Операция представляется как набор Work Elements, каждому из которых соответствует Element Time.

## 6. CAPABILITY — СПОСОБНОСТИ

- представлять стандартную операцию как последовательность Work Elements;
- фиксировать время отдельных элементов;
- фиксировать Operation Cycle Time;
- сопоставлять Customer Cycle Time и Operator Cycle Time;
- представлять Work Flow / Sequence;
- фиксировать стандартный запас в процессе;
- визуально связывать работу с рабочей зоной, выполненной в масштабе;
- выделять Quality Check, Critical Operation и Safety.

**Статус:** CANDIDATE / SINGLE-SOURCE.

## 7. MACHINE — МАШИНКА

### Standard Operation Structuring

```text
INPUT
Operation
↓
[ DECOMPOSE ]
Work Elements
↓
[ ORDER ]
Work Flow / Sequence
↓
[ TIME ]
Element Times
↓
[ AGGREGATE / REPRESENT ]
Operation Cycle Time
↓
[ COMPARE / CONTEXTUALIZE ]
Customer Cycle Time + Operator Cycle Time + Takt Time
↓
OUTPUT
Structured Standard Operation Sheet
```

**MACHINE = CANDIDATE / SINGLE-SOURCE**

Важно: SOURCE показывает наличие этих полей и их совместное представление в SOS, но не даёт в этом фрагменте алгоритма расчёта всех временных показателей.

## 8. CHAIN — ЦЕПОЧКИ

SOURCE-SUPPORTED:

```text
Work Element
→ Element Time
```

```text
Work Elements
→ Work Flow / Sequence
```

```text
Operation
→ Operation Cycle Time
```

```text
Customer Demand / Customer Requirement
→ Takt Time
```

Последняя цепочка относится к определению Takt Time в соседующем SOURCE-фрагменте; в этой GM фиксируется только наличие Takt Time в составе SOS.

## 9. CMOC INTERPRETATION

### Work as a Time-Structured Object

**CANDIDATE**

SOS представляет работу не только как перечень действий, но как структуру, в которой последовательность и время связаны с конкретными Work Elements.

### Standard Operation as Spatial + Sequential + Temporal Representation

**CANDIDATE**

Форма одновременно содержит:

```text
SPATIAL
→ Workstation Area Drawn to Scale

SEQUENTIAL
→ Step No. / Work Flow - Sequence

TEMPORAL
→ Element Time / Cycle Time / Takt Time
```

Это CMOC-интерпретация структуры формы, а не терминология SOURCE.

## 10. RELATION TO GM-079 / GM-082

GM-079 показала, что организованное рабочее пространство может визуализировать Standardized Work, включая work flow, operator movement и time.

GM-082 определила Standardized Work как документ рабочих функций в повторяемой последовательности и как repeatable, predictable baseline.

GM-083 показывает один из конкретных носителей этого представления — SOS, где последовательность и время получают структурированную форму.

Пока это **CMOC INTERPRETATION / CANDIDATE**, не CANON.

## 11. STATUS

- Major Steps / SOS — **SOURCE-SUPPORTED**
- Work Elements / Element Times / Work Flow / Cycle Time / Takt Time as SOS contents — **SOURCE-SUPPORTED**
- Element Time ≠ Operation Cycle Time — **SOURCE-SUPPORTED BY FORM STRUCTURE**
- Customer Cycle Time ≠ Operator Cycle Time — **SOURCE-SUPPORTED BY FORM STRUCTURE**
- Work as Spatial + Sequential + Temporal Representation — **CMOC INTERPRETATION / CANDIDATE**
- **CANON — нет**

## 12. BOUNDARY

Не приписывать GM-083 конкретные правила разбиения работы на элементы, формулы Takt Time или правила расчёта Cycle Time, если они не извлечены из соответствующих последующих страниц SOURCE. Эти вопросы будут разбираться отдельными GM.

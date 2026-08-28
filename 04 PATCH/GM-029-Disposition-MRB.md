# GM-029 — Disposition / MRB

**Извещение на изменение:** 0140+280826  
**SOURCE:** GM Quality System Basics rev. March 2009  
**Раздел:** 2.0 — Control of Nonconforming Product; 2.5 — Disposition  
**Статус:** CANDIDATE / SINGLE-SOURCE

---

## SOURCE

GM задаёт общий контур управления несоответствующей продукцией:

- продукция, не соответствующая требованиям, должна быть **prevented from unintended use**;
- должна быть **contained and/or segregated**;
- должна быть **dispositioned by Management**;
- при escape должна быть обеспечена proper communication;
- используется согласованный процесс идентификации и визуального управления.

В разделе 2.5 Disposition раскрываются два основных маршрута: **Reusable / Rework / Repair** и **Scrap**. Для rework GM требует Work Instruction, метод идентификации scrap и обеспечения traceability rework product; Customer Approval may be required. При reintroduction должны выполняться все предусмотренные Control Plan inspections and tests; при невозможности возврата в точке удаления применяется approved Quality Manager documented rework and inspection procedure.

В разделе Segregation GM также требует метод инвентаризации nonconforming material, включающий **Date, P/N, Defect, MRB disposition**.

Критическое ограничение источника: в доступном фрагменте GM **MRB не раскрывается как отдельная Material Review Board / организационная конструкция**. Поэтому мы не приписываем GM наличие или состав MRB. SOURCE подтверждает только термин **MRB disposition** как поле/элемент учёта и одновременно говорит о disposition by Management.

---

## LOCATION

- p. 54 — Purpose / Responsibility
- p. 58 — Segregation; inventory including MRB disposition
- p. 69 — 2.5 Disposition; Reusable / Rework / Reintroduce
- p. 70 — 2.5.3 Scrap
- p. 71 — 2.6 Summary; Shalls

---

## TERMS — ТЕРМИНЫ

| English | Русский |
|---|---|
| **Disposition** | решение о дальнейшей судьбе / способе обращения с продукцией |
| **Dispositioned by Management** | решение о дальнейшей судьбе принимается руководством |
| **Management** | руководство |
| **Material Review Board (MRB)** | комиссия / орган рассмотрения несоответствующей продукции — термин MRB как отдельная конструкция данным фрагментом не раскрыт |
| **MRB disposition** | решение MRB / поле учёта disposition; источник не раскрывает состав MRB |
| **Reusable** | пригодный для повторного использования |
| **Rework** | доработка |
| **Repair** | ремонт |
| **Reintroduce Product** | повторно ввести продукцию в процесс |
| **Scrap** | брак / продукция, исключённая из дальнейшего использования |
| **Defined Process** | определённый процесс |
| **Authority** | полномочие / право принимать или разрешать решение |
| **Customer Approval** | одобрение заказчика |
| **Quality Manager** | менеджер по качеству |
| **Traceability** | прослеживаемость |
| **Control Plan** | план управления / контрольный план |

---

## DISTINCTIONS — РАЗЛИЧЕНИЯ

### DIS-GM-029-01
**Containment / Segregation ≠ Disposition.**

Containment и segregation удерживают несоответствующую продукцию под контролем. Disposition определяет, что с ней делать дальше.

### DIS-GM-029-02
**Disposition ≠ Rework / Repair / Scrap.**

Disposition — решение / маршрут. Rework, repair, reintroduction и scrap — конкретные варианты обращения с продукцией.

### DIS-GM-029-03
**Disposition by Management ≠ MRB как автоматически установленная комиссия.**

SOURCE говорит о disposition by Management и отдельно использует термин MRB disposition в составе inventory information. Он не раскрывает MRB как отдельный орган, его состав, полномочия или порядок заседания.

### DIS-GM-029-04
**Decision / Authority ≠ физическое действие.**

Решение о дальнейшем обращении и выполнение выбранного маршрута — разные элементы.

### DIS-GM-029-05
**MRB disposition ≠ просто запись.**

В SOURCE MRB disposition входит в требуемую информацию inventory nonconforming material. Но из этого нельзя выводить, что запись сама является актом disposition.

### DIS-GM-029-06
**Defined process and authority ≠ неформальное разрешение.**

GM требует defined process and authority для release; в контуре disposition руководство является субъектом disposition.

---

## GM-FORMULATIONS — ФОРМУЛИРОВКИ ИСТОЧНИКА

- **“Dispositioned by Management”** — решение о дальнейшей судьбе продукции принимается руководством.
- **“A method to inventory non-conforming material is required (Including Date, P/N, Defect, MRB disposition).”**
- **“Released using a defined process and authority.”**
- **“All control plan inspections and tests shall be performed.”**

---

## EXTRACTION — ИЗВЛЕЧЕНИЕ

GM показывает конструкцию:

```text
NONCONFORMING PRODUCT
        ↓
CONTROL / CONTAINMENT / SEGREGATION
        ↓
DISPOSITION BY MANAGEMENT
        ↓
   ┌────┴───────────┐
   ↓                ↓
REUSABLE          SCRAP
   ↓
REWORK / REPAIR
   ↓
REINTRODUCE
   ↓
CONTROL PLAN INSPECTIONS + TESTS
```

Параллельно существует информационный след:

```text
NONCONFORMING MATERIAL
        ↓
INVENTORY
        ↓
Date + P/N + Defect + MRB disposition
```

---

## MECHANISM — МЕХАНИЗМ

### CANDIDATE — Management Disposition Mechanism

**Input:** контролируемая несоответствующая продукция.

**Transformation:** руководство определяет дальнейший маршрут продукции в рамках установленного контура disposition.

**Output:** выбранный и зафиксированный маршрут обращения с продукцией.

**Organizational effect:** физический объект получает управляемую дальнейшую судьбу вместо неопределённого состояния.

**STATUS: CANDIDATE / SINGLE-SOURCE**

---

## CAPABILITY — СПОСОБНОСТЬ

**NONE**

Из этого фрагмента отдельно capability не выводим.

---

## CORE CANDIDATE

> **Management Disposition — воспроизводимый механизм принятия руководством решения о дальнейшей судьбе контролируемой несоответствующей продукции с переводом объекта в определённый маршрут обращения.**

**STATUS: CANDIDATE / SINGLE-SOURCE**

---

## MACHINE — МАШИНКА

### CANDIDATE MACHINE — Management Disposition

```text
INPUT
Controlled Nonconforming Product
        ↓
[ MANAGEMENT DISPOSITION ]
        │
        ├── Reusable / Rework / Repair
        ├── Reintroduce
        └── Scrap
        ↓
OUTPUT
Defined Product Route
        ↓
EFFECT
Uncontrolled product state is replaced
by an authorized disposition route
```

Инженерный тест проходит на уровне кандидата:

- **INPUT:** контролируемая несоответствующая продукция;
- **OPERATION:** принятие disposition;
- **OUTPUT:** выбранный маршрут;
- **EFFECT:** определённая дальнейшая судьба объекта.

**STATUS: CANDIDATE / SINGLE-SOURCE**

Не объявляем отдельной машинкой **MRB**, поскольку SOURCE не описывает его как организационную конструкцию.

---

## CHAIN — ЦЕПОЧКА

### SOURCE-SUPPORTED

```text
Nonconforming Product
        ↓
Contain / Segregate
        ↓
Disposition by Management
        ↓
Reusable / Rework / Repair
        OR
Scrap
```

Для reusable/rework ветви:

```text
Rework / Repair
        ↓
Reintroduce
        ↓
Control Plan Inspections + Tests
        ↓
Process Stream
```

Информационный след:

```text
Nonconforming Material
        ↓
Inventory
        ↓
Date + P/N + Defect + MRB disposition
```

---

## STATUS

**CANDIDATE / SINGLE-SOURCE**

**CANON — нет.**

**MRB как отдельная Entity / Machine — не подтверждён.**

---

## CMOC INTERPRETATION — ИНТЕРПРЕТАЦИЯ CMOC

Здесь появляется важная конструкция:

```text
OBJECT
  ↓
NONCONFORMING STATUS
  ↓
CONTAINMENT
  ↓
DISPOSITION DECISION
  ↓
AUTHORIZED ROUTE
```

То есть управление несоответствующим объектом не заканчивается фиксацией его статуса. Система должна обеспечить **переход от статуса к разрешённой дальнейшей судьбе объекта**.

Для CMOC это потенциально важное различение:

> **Статус говорит, в каком состоянии находится объект. Disposition определяет, что разрешено делать с объектом дальше.**

Это именно **CMOC INTERPRETATION**, а не формулировка GM.

Отдельно сохраняем ограничение:

> **MRB нельзя пока превращать в Entity только потому, что SOURCE содержит поле “MRB disposition”.**

Это хороший пример правила v2.1:

**TERM ≠ ENTITY.**

---

## INTER-SOURCE NOTE

Потенциально интересно для последующего сопоставления с ISO/DIS 9001:2025 по темам authority, disposition, documented information и nonconforming outputs.

В этом PATCH межисточникового подтверждения не утверждаем.

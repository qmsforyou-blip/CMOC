# GM-030 — Summary / Shalls: Control of Nonconforming Product

**Извещение на изменение:** 0141+280826  
**SOURCE:** GM Quality System Basics rev. March 2009  
**Раздел:** 2.6 — Summary: Shalls  
**Статус:** CANDIDATE / SINGLE-SOURCE

---

## 1. SOURCE

На странице Summary GM сводит обязательные требования к управлению несоответствующим материалом:

- Nonconforming Material shall be clearly identified using consistent identification (tagging).
- Shall be segregated in properly identified areas and containers.
- Shall be contained through the use of a Containment Worksheet.
- Shall be released using a defined process and authority.
- Shall be reintroduced into the process stream at or prior to the point of removal and include all Control Plan inspections & tests.
- If this is not possible, a rework & inspection plan is provided.
- Organization shall have a nonconformance alert and containment procedure that meets customer requirements.
- Scrap is prevented from use and is tracked with a plan to reduce.
- Product containment issues shall be reviewed by leadership. fileciteturn46file0

Эта страница является **Summary**, поэтому не добавляем в неё новые требования, которых здесь нет. Она подтверждает и сжимает конструкции, добытые в GM-021—029.

---

## 2. LOCATION

**p. 71 — 2.6 Summary: Shalls, Control of Nonconforming Product.**

Общий контекст раздела 2.0 подтверждён оглавлением: Introduction → Identification → Segregation → Containment → Containment Worksheet → Communication → Disposition → Reusable/Rework → Reintroduce → Scrap → Summary/Shalls. fileciteturn46file14turn46file15

---

## 3. TERMS — ТЕРМИНЫ

| English | Русский |
|---|---|
| **Nonconforming Material** | несоответствующий материал / продукция |
| **Clearly Identified** | однозначно идентифицированный |
| **Consistent Identification** | единообразная идентификация |
| **Tagging** | маркировка / биркование |
| **Segregated** | изолированный / отделённый |
| **Properly Identified Areas and Containers** | надлежащим образом идентифицированные зоны и контейнеры |
| **Containment** | локализация / удержание под контролем |
| **Containment Worksheet** | рабочий лист локализации |
| **Released** | выпущенный / разрешённый к выпуску |
| **Defined Process** | определённый процесс |
| **Authority** | полномочие |
| **Reintroduced** | повторно введённый в процесс |
| **Process Stream** | поток процесса |
| **Control Plan** | план управления / контрольный план |
| **Inspection** | контроль / проверка |
| **Test** | испытание / тестирование |
| **Rework & Inspection Plan** | план доработки и контроля |
| **Nonconformance Alert** | уведомление о несоответствии |
| **Customer Requirements** | требования заказчика |
| **Scrap** | брак / продукция, исключённая из дальнейшего использования |
| **Leadership Review** | рассмотрение руководством |

---

## 4. DISTINCTIONS — РАЗЛИЧЕНИЯ

### DIS-GM-030-01
**Identification ≠ Segregation ≠ Containment.**

Summary намеренно сохраняет три отдельные конструкции: сделать материал распознаваемым, физически отделить его и выполнить containment через специальный Worksheet.

### DIS-GM-030-02
**Containment Worksheet ≠ вся система containment.**

Worksheet является конкретным средством выполнения containment; Summary одновременно требует отдельную nonconformance alert / containment procedure.

### DIS-GM-030-03
**Release ≠ Reintroduction.**

Release требует defined process and authority. Reintroduction — отдельное действие по возврату материала в process stream с Control Plan inspections & tests.

### DIS-GM-030-04
**Reintroduction ≠ Rework.**

При невозможности стандартного возврата GM требует rework & inspection plan.

### DIS-GM-030-05
**Scrap ≠ отсутствие управления.**

Даже scrap должен быть предотвращён от использования, tracked и иметь plan to reduce.

### DIS-GM-030-06
**Containment issue ≠ только операционная задача.**

Summary требует review by leadership.

---

## 5. GM-FORMULATIONS — ФОРМУЛИРОВКИ GM

Ключевые формулировки Summary:

- **“Nonconforming Material shall be: Clearly identified…”**
- **“Segregated in properly identified areas and containers.”**
- **“Contained through the use of a Containment Worksheet.”**
- **“Released using a defined process and authority.”**
- **“Reintroduced into the process stream at or prior to the point of removal…”**
- **“…includes all control plan inspections & test.”**
- **“If is not possible, a rework & inspection plan is provided.”**
- **“Organization shall have a nonconformance alert and containment procedure…”**
- **“Scrap is prevented from use & is tracked with a plan to reduce.”**
- **“Product containment issues shall be reviewed by leadership.”** fileciteturn46file0

---

## 6. EXTRACTION

Summary собирает систему в несколько обязательных контрольных состояний и действий:

```text
NONCONFORMING MATERIAL
        ↓
IDENTIFY
        ↓
SEGREGATE
        ↓
CONTAIN
        ↓
DISPOSITION / RELEASE
        ↓
 ┌───────────────┬─────────────────┐
 ↓               ↓
REINTRODUCE     SCRAP
 ↓               ↓
CONTROL PLAN    PREVENT USE
INSPECTIONS     + TRACK
+ TESTS         + PLAN TO REDUCE
```

Над этим контуром:

```text
NONCONFORMANCE ALERT
        +
CONTAINMENT PROCEDURE
        +
LEADERSHIP REVIEW
```

Это именно **Summary-структура SOURCE**, а не наша расширенная модель.

---

## 7. REL — СВЯЗИ

Summary подтверждает следующие связи:

```text
Nonconforming Material
        ↓
Identification
        ↓
Segregation
        ↓
Containment Worksheet
        ↓
Defined Release / Authority
        ↓
Reintroduction OR Scrap
```

Для Reintroduction:

```text
Reintroduction
        ↓
Point of Removal / Prior to It
        ↓
Control Plan Inspections + Tests
```

Если это невозможно:

```text
No Standard Reintroduction
        ↓
Rework & Inspection Plan
```

Для Scrap:

```text
Scrap
 ↓
Prevent Use
 ↓
Track
 ↓
Plan to Reduce
```

И отдельно:

```text
Containment Issues
        ↓
Leadership Review
```

---

## 8. MECHANISM — МЕХАНИЗМ

### CANDIDATE — Integrated Nonconforming Material Control Mechanism

**Input:** nonconforming material.

**Transformation:** последовательное применение идентификации, segregation, containment, defined release/authority и управляемого маршрута reintroduction либо scrap.

**Output:** материал получает контролируемый статус и определённый дальнейший маршрут.

**Организационный эффект:** предотвращается непреднамеренное использование, а дальнейшее обращение с материалом становится управляемым.

**STATUS: CANDIDATE / SINGLE-SOURCE**

Важно: это **не новая отдельная машина поверх GM-021—029**, а кандидат на сборочную конструкцию, которую Summary подтверждает целиком.

---

## 9. CAPABILITY

**NONE**

Summary не даёт отдельного основания создавать новую Capability.

---

## 10. CORE CANDIDATE

> **Integrated Nonconforming Material Control — системная конструкция управления несоответствующим материалом, объединяющая идентификацию, segregation, containment, управляемый release и определённый маршрут reintroduction либо scrap.**

**STATUS: CANDIDATE / SINGLE-SOURCE**

Это кандидат именно как **сборочная конструкция**. Не заменяет отдельные кандидаты GM-021—029.

---

## 11. MACHINE

### CANDIDATE MACHINE — Integrated Nonconforming Material Control

```text
INPUT
Nonconforming Material
        ↓
IDENTIFY
        ↓
SEGREGATE
        ↓
CONTAIN
        ↓
RELEASE / AUTHORITY
        ↓
 ┌──────────────┬─────────────┐
 ↓              ↓
REINTRODUCE    SCRAP
 ↓              ↓
INSPECT/TEST   PREVENT USE
 ↓              ↓
PROCESS        TRACK + REDUCE
STREAM
```

Инженерный тест на уровне **сборки** выполняется: есть вход, набор преобразований, контролируемые выходные состояния и организационный эффект.

Но важно не переоценивать результат: Summary подтверждает **архитектуру системы**, а не описывает одну физическую реализацию всей конструкции.

**STATUS: CANDIDATE / SINGLE-SOURCE**

---

## 12. CHAIN — ЦЕПОЧКА

### SOURCE-SUPPORTED SUMMARY CHAIN

```text
Nonconforming Material
→ Identify
→ Segregate
→ Contain
→ Release / Authority
→ Reintroduce OR Scrap
```

С дополнительными ветвями:

```text
Reintroduce
→ Control Plan Inspections + Tests
```

```text
Scrap
→ Prevent Use + Track + Plan to Reduce
```

И отдельным управленческим контуром:

```text
Containment Issues
→ Leadership Review
```

---

## 13. STATUS

**CANDIDATE / SINGLE-SOURCE**

Никакого CANON.

---

## 14. CMOC INTERPRETATION

GM-030 ценен прежде всего не новой сущностью, а **проверкой целостности добычи**.

Summary показывает, что добытые нами ранее конструкции действительно складываются в одну SOURCE-архитектуру:

```text
IDENTIFICATION
      ↓
SEGREGATION
      ↓
CONTAINMENT
      ↓
DEFINED RELEASE / AUTHORITY
      ↓
REINTRODUCTION
      OR
SCRAP
```

При этом GM удерживает разные типы управленческих действий:

```text
IDENTIFY     → сделать состояние распознаваемым
SEGREGATE    → физически отделить
CONTAIN      → удержать потенциально затронутую продукцию
RELEASE      → разрешить дальнейшее обращение
REINTRODUCE  → вернуть в поток при заданных условиях
SCRAP        → исключить из использования и отслеживать
REVIEW       → вынести containment issue на leadership review
```

Это уже позволяет говорить о **сборке**, но пока не о CANON.

Особенно важно: Summary не подтверждает автоматически наши CMOC-названия машинок. Он подтверждает SOURCE-конструкции и их обязательность.

---

## 15. ИТОГ ВАГОНЕТКИ

GM-030 не дала большого количества новой добычи.

Её ценность — в другом:

> **Summary / Shalls подтверждает, что Control of Nonconforming Product в GM построен не вокруг одной процедуры, а вокруг набора обязательных управляемых переходов объекта между состояниями и маршрутами.**

Именно поэтому GM-030 следует рассматривать как **контрольную вагонетку**, а не как повод создавать множество новых Entities или Machines.

**Новые Machine-кандидаты: 1 — Integrated Nonconforming Material Control.**

**Новые Core-кандидаты: 1 — Integrated Nonconforming Material Control.**

Остальные элементы — подтверждение уже добытого материала GM-021—029.

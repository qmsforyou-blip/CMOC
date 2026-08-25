`MACHINE-CATALOG.md`

Это будет **только индекс**, не место хранения паспортов.

````
# MACHINE-CATALOG

> Рабочий каталог машинок CMOC.
>
> Статус: WORKING / NON-CANON.
>
> Источник машинки всегда указывается в её паспорте.
> Машинка не становится элементом CMOC-Core автоматически.

---

## Machine Patterns

| ID | Pattern | Status |
|---|---|---|
| MP-001 | Visual Control | CANDIDATE |
| MP-002 | Response to Abnormality | CANDIDATE |
| MP-003 | Problem Solving | CANDIDATE |
| MP-004 | Knowledge Transfer | CANDIDATE |
| MP-005 | Assessment against Criterion | CANDIDATE |

---

## Machines

| ID | Machine | Level | Type | Status |
|---|---|---|---|---|
| MC-008-03 | Визуализация производственного потока | MACHINE | FLOW / CONTROL | CANDIDATE |
| MC-008-05 | Стандарт на рабочем месте | MACHINE | STANDARD / CONTROL | CANDIDATE |
| MC-008-06 | Цель–факт | MACHINE | CONTROL | CANDIDATE |
| MC-008-07 | Визуальная карта разработки | MACHINE | FLOW / PROJECT | CANDIDATE |
| MC-009-10 | Andon | MACHINE | RESPONSE | STRONG CANDIDATE |
| MC-009-11 | Gemba Walk | MACHINE | DIAGNOSTIC | STRONG CANDIDATE |
| MC-009-12 | Asaichi | MACHINE | PROBLEM-SOLVING | STRONG CANDIDATE |
| MC-009-15 | Audit | MACHINE | VERIFICATION | STRONG CANDIDATE |
| MC-009-17 | Yokoten | MACHINE | KNOWLEDGE TRANSFER | STRONG CANDIDATE |

---

## System Machines

| ID | Machine | Composes | Status |
|---|---|---|---|
| MC-009-14 | Двойной цикл мастера | несколько машин | CANDIDATE |
| MC-009-16 | Kamishibai | Audit | STRONG CANDIDATE |
| MC-009-13 | Сертификация лучшей линии | Audit + Improvement + Replication | CANDIDATE |

---

## Relations

```text
Machine
  → implements → CMOC mechanism

Machine
  → invokes → Machine

System-Machine
  → composes → Machine

Machine
  → produces → Output

Machine
  → develops → Capability
````

---

## Status Rules

CANDIDATE  
→ STRONG CANDIDATE  
→ MULTI-SOURCE CONFIRMED  
→ CORE-RELEVANT  
→ CANON

> Канонизация выполняется отдельно.
> ++++

+++++
# 11. ==И это меняет наш взгляд на MACHINE-CATALOG

Теперь каталог потенциально состоит из **трёх этажей**:

```
MACHINE-CATALOG
│
├── PATTERNS
│
├── MACHINES
│
└── CHAINS
```

### PATTERN

> общий способ действия.

### MACHINE

> конкретная воспроизводимая конструкция.

### CHAIN

> воспроизводимая последовательность машинок.

И вот **Chain** может оказаться тем, что впоследствии позволит CMOC использовать каталог практически.

Например, заказчик говорит:

> «У нас постоянно повторяются дефекты».

CMOC не просто выдаёт ему:

> «Вот CAP-XXX».

Он может показать:

```
Отклонение
   ↓
Andon
   ↓
Asaichi
   ↓
Standardization
   ↓
Audit
   ↓
Yokoten
```

То есть:

> **готовую архитектуру управленческого действия.**

# 7. И я бы добавил в `MACHINE-CATALOG.md` отдельный индекс
## Machine Chains

| ID | Chain | Source | Status |
|---|---|---|---|
| CHAIN-CANDIDATE-001 | Gemba → Gembutsu → Countermeasure → Root Cause → Standardization | Имаи, гл. 9 | SOURCE-SUPPORTED |
++
## MACHINE-CANDIDATES

| ID             | Name                 | Source       | Status        |
| -------------- | -------------------- | ------------ | ------------- |
| MC-CAND-011-01 | Kanban Replenishment | Имаи, гл. 11 | SINGLE-SOURCE |
23.08.26


| ID             | Machine Candidate         | Mechanism                           | Source       | Status                        |
| -------------- | ------------------------- | ----------------------------------- | ------------ | ----------------------------- |
| MC-CAND-011-01 | Kanban Replenishment Loop | Replenishment by Consumption Signal | Имаи, гл. 11 | MULTI-CONFIRMED WITHIN SOURCE |
++

|ID|Candidate|Mechanism|Status|
|---|---|---|---|
|MC-CAND-011-02|Heijunka Box|Heijunka / Production Leveling|SINGLE-SOURCE|
## Извещение на изменение — `0001+240826`

**Название файла:** `MACHINE-CATALOG.md`

Добавить в индекс:

| ID             | Machine Candidate                 | Mechanism                                        | Physical Realization             | Status           |
| -------------- | --------------------------------- | ------------------------------------------------ | -------------------------------- | ---------------- |
| MC-CAND-011-01 | Kanban Replenishment Loop         | Replenishment by Consumption Signal              | container + Kanban + return loop | MULTI-CONFIRMED  |
| MC-CAND-011-02 | Heijunka Box                      | Production Leveling                              | physical scheduling box          | SINGLE-SOURCE    |
| MC-CAND-011-03 | Process-Sequence Equipment Layout | Process Flow Integration                         | physical equipment line          | STRONG CANDIDATE |
| MC-CAND-011-04 | One-Piece Flow Line               | Single-Piece Transfer                            | U-shaped cell                    | CONFIRM / UPDATE |
| MC-CAND-011-05 | U-Shaped One-Piece Flow Cell      | Process Flow Integration + Single-Piece Transfer | U-shaped equipment arrangement   | SINGLE-SOURCE    |

## Извещение на изменение — `0006-1+240826`
` — `MACHINE-CATALOG.md` 
— добавление 
`Line-Side Supermarket`, 
`Junjō Sequential Supply`;
## Извещение на изменение — `0007+240826`

|ID|Machine|Mechanism|Physical realization|Status|
|---|---|---|---|---|
|MC-CAND-011-08|Mizusumashi Material Delivery Loop|Internal Material Flow|recurring route + supermarkets + delivery points|STRONG CANDIDATE|
|MC-CAND-011-09|Heijunka Scheduling System|Production Leveling|Heijunka Box + Kanban + time slots + rules|STRONG CANDIDATE|
### **Извещение на изменение `0008+240826`**


| ID             | Machine                            | Mechanism                      | Physical realization                              | Status        |
| -------------- | ---------------------------------- | ------------------------------ | ------------------------------------------------- | ------------- |
| MC-CAND-011-08 | Mizusumashi Material Delivery Loop | Internal Material Flow         | route + supermarkets + delivery points            | STRONG        |
| MC-CAND-011-09 | Heijunka Scheduling System         | Production Leveling / Planning | Kanban + Heijunka Box + time slots                | STRONG        |
| MC-CAND-011-10 | VMI Replenishment Control          | Replenishment by Actual Stock  | daily stock/order review + replenishment decision | SINGLE-SOURCE |
### Извещение на изменение `0010+240826`

| ID             | Machine           | Mechanism                               | Physical realization     | Status                 |
| -------------- | ----------------- | --------------------------------------- | ------------------------ | ---------------------- |
| MC-CAND-011-11 | Supplier Milk Run | Scheduled Closed-Loop Supplier Delivery | recurring supplier route | STRONG / SINGLE-SOURCE |
|                |                   |                                         |                          |                        |
Application Context:
- Supply
- Delivery

Do not duplicate Machine identity
for different contexts.
++
Status:
MULTI-CONFIRMED / STRONG CANDIDATE

Application Context:
- Supply
- Delivery

Mechanism:
Closed-Loop Material Flow

Physical realization:
frequent repeated route
+ small batches
+ multiple supply/delivery points

Flow Position:
External Logistics
### Извещение на изменение `0013+240826`

`MC-CAND-011-11 — Supplier Milk Run`обновить
## Извещение на изменение `0015+240826`
Для `MC-CAND-011-11 — Supplier Milk Run` обновить:
## Извещение на изменение `0017+240826`
## TRANSFORMATION-MACHINE-CANDIDATES

### TMC-CAND-011-01
Flow Transformation Cycle

Status:
SINGLE-SOURCE / CANDIDATE

Function:
переход от текущей конфигурации
к целевой через анализ,
проектирование и внедрение.

Source:
Имаи, глава 11.
++++
## Извещение на изменение `0019+240826`
## TRANSFORMATION-MACHINE-CANDIDATES

### TMC-CAND-011-01
Flow Transformation Cycle

Type:
TRANSFORMATION

Mechanism:
transition from Current State
to Future State through analysis,
design and implementation.

Physical realization:
Current State Map
+
Future State Map
+
TFM Design
+
Implementation Programme

Evidence:
Company A, TFM project.

Status:
STRONG CANDIDATE / SINGLE-SOURCE
# **Извещение на изменение — `0022+240826`**

> `IMA-011-FINAL`: консолидация кандидатов главы 11; выявление дублей Heijunka; разделение Machine / Artifact / Physical Variant; уточнение Application Context; выделение трёх типов Chain.

### Извещение на изменение `0026+240826`
**Изменений в основном индексе Machine пока нет.**

Добавляем только ссылку в рабочий блок:

```
M-CANDIDATE:
Setup Time Reduction

Machine:
NOT YET IDENTIFIED
```

---
### Извещение на изменение — `0028+240826`


Изменение только индекса кандидатов:

> `Setup Time Reduction` — уточнить `Application Context = Small-Batch / Flexible Production`; `Capability Enabled = Production Responsiveness`.

# Извещение на изменение — `0030+240826`

**Файл:** `MACHINE-CATALOG.md`

Изменение:

- `Flow Transformation Cycle` → **MULTI-SOURCE / STRONG CANDIDATE**;
- `Production Responsiveness` → **MULTI-SOURCE / STRONG CANDIDATE**;
- новых Machine не добавлять.
**Извещение на изменение — `0036+240826`**  
**Файл:** `MACHINE-CATALOG.md`  
**Изменение:** проведена консолидация кандидатов главы 12; `Upstream Quality Stabilization` добавлена как `MACHINE-CANDIDATE`; дубли и элементы физической реализации не канонизированы.

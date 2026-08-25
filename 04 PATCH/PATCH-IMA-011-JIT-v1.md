---
patch_id: PATCH-IMA-011-JIT-v1
source: Имаи Масааки — «Гемба кайдзен»
section: глава 11
status: WORKING
---

# PATCH-IMA-011-JIT-v1

## Current extraction

### DIS

Push Production ≠ Pull Production

Status:
NEW CANDIDATE

---

### REL

Consumption
→ Signal
→ Replenishment

Status:
CONFIRM / UPDATE

Next Process
→ Kanban
→ Previous Process

Status:
NEW CANDIDATE

Kanban
→ carries demand information

Status:
NEW CANDIDATE

---

### M

Replenishment by Consumption Signal

Status:
SINGLE-SOURCE / CANDIDATE

---

### MACHINE-CANDIDATE

Kanban Replenishment

Status:
SINGLE-SOURCE

Passport:
NOT CREATED

---

## Source boundary

Do not equate:

Pull = Kanban

Pull = One-Piece Flow

JIT = Kanban

These relations require separate confirmation.

---

## Core status

CORE NOT MODIFIED.
+++

23.08.26
## 011.13 — Kanban Replenishment Loop

### DIS

CONFIRM:
Pull ≠ Kanban

Applicability boundary:
Kanban is not a universal production-order mechanism.

---

### REL

Consumption
→ Kanban Return
→ Production Order

Physical Object
↔ Information Carrier

Pull
→ implemented by
Kanban-based replenishment

---

### M

Replenishment by Consumption Signal

UPDATE:
mechanism receives concrete source-supported implementation.

---

### MACHINE-CANDIDATE

Kanban Replenishment Loop

Status:
MULTI-CONFIRMED WITHIN SOURCE

Structure:

Production
↓
Delivery
↓
Consumption
↓
Kanban Return
↓
Production Order
↓
Production

---

### CHAIN-CANDIDATE-002

Kanban Replenishment Loop

Status:
SOURCE-SUPPORTED-CANDIDATE

---

### Boundary

Kanban is not treated as a universal mechanism
for all production orders.

---

CORE NOT MODIFIED.
LAB-002 NOT MODIFIED.
++++
## 011.14 — Heijunka

### DIS-CANDIDATE

Pull ≠ Heijunka

---

### REL-CANDIDATES

Demand
→ Signal
→ Sequencing

Status:
SINGLE-SOURCE / CANDIDATE

Kanban
→ Heijunka

Status:
PARTIAL / NO DIRECT CONFIRMATION

---

### MACHINE-CANDIDATE

Heijunka Box

Status:
SINGLE-SOURCE

Function:
Sequencing / production leveling

---

### MACHINE-CHAIN-CANDIDATE-003

Consumption
↓
Kanban Signal
↓
Heijunka
↓
Production Sequence
↓
Production

Status:
SOURCE-SUPPORTED-CANDIDATE

Boundary:
Do not interpret Kanban → Heijunka
as a direct causal relation until source confirms it.

---

CORE NOT MODIFIED.
LAB-002 NOT MODIFIED.
+++++++++++++
## 011.15 — Heijunka

### DIS-CANDIDATE

Production Leveling
≠
Equal Production Quantity

---

### M-CANDIDATE

Heijunka / Production Leveling

Function:
организация производственной последовательности
для выравнивания производственной нагрузки
относительно потребности.

Status:
SINGLE-SOURCE

---

### MACHINE-CANDIDATE

Heijunka Box

Relation:

Heijunka / Production Leveling
    ↓ implemented by
Heijunka Box

Status:
SINGLE-SOURCE

---

### REL-CANDIDATES

Takt
→ constrains / informs
Heijunka

Kanban
→ demand information

Heijunka
→ production sequencing

---

### CHAIN UPDATE

Previous:

Consumption
↓
Kanban
↓
Heijunka
↓
Production

Updated working model:

PULL / REPLENISHMENT LOOP

+

HEIJUNKA / LEVELING LOOP

Direct Kanban → Heijunka relation:
PARTIAL / NO DIRECT CONFIRMATION

---

CORE NOT MODIFIED.
LAB-002 NOT MODIFIED.

# ++++++
## 011.16 — Setup Reduction

### DIS

Frequency of Setups
≠
Setup Time

Status:
NEW CANDIDATE

---

### REL

Small Batch Production
→ increases
Setup Frequency

Status:
SINGLE-SOURCE / CANDIDATE

Setup Reduction
→ enables
Small Batch Production

Status:
SINGLE-SOURCE / CANDIDATE

---

### M

Setup Reduction

Status:
SOURCE-SUPPORTED M-CANDIDATE

Boundary:
конкретная воспроизводимая реализация
в данном фрагменте не раскрыта.

Therefore:
NO MACHINE CREATED.

---

### MACHINE

No new Machine.

---

### TRANSFERABILITY

Aisin Seiki применяет JIT
в различных производственных контекстах.

Status:
SOURCE-SUPPORTED

Interpretation:
potential transferability property of JIT system,
not proof of universal applicability of every component.

---

CORE NOT MODIFIED.
LAB-002 NOT MODIFIED.
+++++
## Извещение на изменение — `0000+240826`
## 011.17 — Establishing Production Flow

### M

Process Flow Integration

Status:
STRONG CANDIDATE / SINGLE-SOURCE

---

### M-CANDIDATE

Single-Piece Transfer

Status:
SINGLE-SOURCE

---

### MACHINE

Process-Sequence Equipment Layout

Update:
Production Flow Layout

Function:
расположение оборудования в соответствии
с последовательностью производственного процесса.

Status:
STRONG CANDIDATE

---

### MACHINE

One-Piece Flow Line

Status:
CONFIRM / UPDATE

---

### PHYSICAL REALIZATION

U-Shaped One-Piece Flow Cell

Status:
NEW / SINGLE-SOURCE

---

### REL

Process Sequence
→ Equipment Arrangement

One-Piece Flow
→ Cycle Time reduction

One-Piece Flow
→ WIP accumulation reduction

Takt
→ synchronizes
One-Piece Flow

---

### CONSTRAINT

Equipment rearrangement is limited
by size, weight and multifunctionality
of equipment.

---

### CHAIN-CANDIDATE

Process Sequence
↓
Equipment Layout
↓
Connected Workstations
↓
One-Piece Transfer
↓
Cycle Time

Status:
SOURCE-SUPPORTED PROCESS CHAIN

Not yet classified as MACHINE-CHAIN.

---

CORE NOT MODIFIED.
LAB-002 NOT MODIFIED.

**Извещение на изменение — `0004+240826
## 011.19 — Line-Side Supply Architecture

### DIS-CANDIDATES

Supermarket ≠ Kanban

Kanban Replenishment ≠ Junjō Sequential Supply

---

### M-CANDIDATES

Point-of-Use Replenishment

Sequential Supply

---

### MACHINE-CANDIDATES

Line-Side Supermarket

Junjō Sequential Supply

---

### PHYSICAL REALIZATION

Line-Side Supermarket:
racks + controlled stock at line boundary.

Junjō:
physical / organizational supply of parts
in required sequence.

---

### REL

Line-Side Supermarket
→ Pull Replenishment

Junjō
→ Sequential Supply

Junjō
→ requires → Synchronization

Sequence Error
→ Line Stop / Schedule Change

---

### MACHINE INTERFACE CANDIDATE

Line
↔
Supply Machine

Candidate only.
Do not create new ontology class yet.

---

CORE NOT MODIFIED.
LAB-002 NOT MODIFIED.
## Извещение на изменение `0005+240826`

## 011.20 — TFM Integration

### SYSTEM / ARCHITECTURE

TFM — Total Flow Management

Status:
SOURCE-SUPPORTED SYSTEM-LEVEL ARCHITECTURE

Not a Machine.

---

### MACHINE-CANDIDATE

Mizusumashi Material Delivery Loop

Mechanism:
Internal Material Flow / Point-of-Use Delivery

Physical realization:
fixed / recurring route between supermarkets
and production line.

Status:
STRONG CANDIDATE

---

### MACHINE UPDATE

Line-Side Supermarket

Status:
MULTI-CONFIRMED WITHIN SOURCE

Function:
interface between pull signal
and physical material flow.

---

### MACHINE UPDATE

Heijunka Scheduling System

Mechanism:
Production Leveling

Inputs:
Kanban / Production Orders

Physical component:
Heijunka Box

Output:
Daily Production Sequence

Status:
STRONG CANDIDATE

---

### REL

Role
→ executes → Machine

Kanban
→ Heijunka Scheduling
→ Daily Production Sequence

Supermarket
→ Mizusumashi
→ Line

---

### CHAIN-CANDIDATE-004

Production Flow:

Line Layout
↓
Line Boundary
↓
Standardized Work
↓
Setup Reduction
↓
Low-Cost Automation

Internal Logistics:

Supermarket
↓
Mizusumashi
↓
Synchronization
↓
Leveling
↓
Pull
↓
Kanban / Junjō

Status:
SOURCE-SUPPORTED

---

CORE NOT MODIFIED.
LAB-002 NOT MODIFIED.
## Извещение на изменение `0006+240826`

## 011.21 — Planning Architecture

### DIS-CANDIDATE

Demand Forecast
≠
Production Order

Source-supported distinction:

Forecast
→ Capacity Planning

Actual Orders / Consumption
→ Pull Planning

---

### REL

Forecast
→ Capacity Planning

Actual Demand / Orders
→ Pull Planning

Orders
→ Kanban
→ Heijunka
→ Production

---

### M-CANDIDATES

Forecast-Based Capacity Planning

Pull Planning

Status:
SINGLE-SOURCE

No Machine created.

---

### CAP-CANDIDATE

Capacity Preparation from Forecast

Status:
SINGLE-SOURCE

Note:
CMOC interpretation, not source terminology.

---

### MACHINE UPDATE

Heijunka Scheduling System

Status:
MULTI-CONFIRMED / STRONG CANDIDATE

---

### CHAIN

Forecast
↓
Capacity Planning

Status:
SOURCE-SUPPORTED

Actual Orders / Consumption
↓
Pull Planning
↓
Kanban
↓
Heijunka
↓
Production

Status:
SOURCE-SUPPORTED

Do not merge the two chains
without further source confirmation.

---

CORE NOT MODIFIED.
LAB-002 NOT MODIFIED.
## Извещение на изменение `0007+240826`
## 011.22 — Planning Decoupling

### DIS-CANDIDATE

Capacity Planning
≠
Order Planning

Status:
STRONG CANDIDATE

---

### M

Forecast-Based Capacity Planning
Status:
CONFIRM / UPDATE

Replenishment Planning by Actual Stock
Status:
CONFIRM / UPDATE

Planning Decoupling
Status:
NEW / STRONG CANDIDATE

---

### MACHINE-CANDIDATE

VMI Replenishment Control
Status:
SINGLE-SOURCE

Heijunka Scheduling System
Status:
STRONG CANDIDATE

---

### CHAIN-CANDIDATE-005

Stock / Customer Orders
↓
Replenishment Need
↓
Production Order List
↓
Kanban
↓
Heijunka Box
↓
Daily Production Plan

Status:
SOURCE-SUPPORTED / STRONG CANDIDATE

---

### ARCHITECTURAL CHANGE

OLD:

Forecast
↓
Monthly Plan
↓
Weekly Plan
↓
Daily Plan

NEW:

Forecast
↓
Capacity Planning

Actual Orders / Stock
↓
Replenishment
↓
Kanban
↓
Heijunka
↓
Daily Plan

---

CORE NOT MODIFIED.
LAB-002 NOT MODIFIED.
### Извещение на изменение `0009+240826`
## 011.23 — Supplier Pull / Milk Run

### DIS-CANDIDATE

Daily Delivery
≠
Closed-Loop Milk Run

---

### M

Threshold-Based Replenishment

Status:
CONFIRM / STRONG CANDIDATE

Scheduled Closed-Loop Supplier Delivery

Status:
NEW / SINGLE-SOURCE

---

### REL

Stock Level
→ Replenishment Decision

Supplier
→ Closed-Loop Route
→ Plant

---

### MACHINE-CANDIDATE

Supplier Milk Run

Mechanism:
Scheduled Closed-Loop Supplier Delivery

Physical realization:
repeated closed-loop route
between suppliers and plant.

Status:
SINGLE-SOURCE / STRONG CANDIDATE

Boundary:
applicability depends on geography,
delivery frequency and supplier capability.

---

### CAP-CANDIDATE

Supplier Capacity Preparation from Forecast

Status:
SINGLE-SOURCE

---

### CHAIN-CANDIDATE-006

Capacity Loop:

Forecast
↓
Supplier Capacity Planning

Replenishment / Logistics Loop:

Actual Stock
↓
Threshold Check
↓
Daily Replenishment Order
↓
Supplier
↓
Milk Run
↓
Plant

Do not treat as one causal chain.

---

### SYSTEM OUTCOMES

Source reports improvements in:
inventory,
defects,
customer service,
schedule adherence,
productivity,
final assembly efficiency.

No causal attribution to individual Machines.

---

CORE NOT MODIFIED.
LAB-002 NOT MODIFIED.
## Извещение на изменение `0011+240826`
## 011.24 — Demand Visibility

### SOURCE CLAIM

Компания A имела два типа потребителей:
внутренние и зарубежные ДЦ.

Внутренний ДЦ ежедневно получал
заказы от магазинов.

Плановики не имели информации
о запасах зарубежных ДЦ.

Производство первоначально
планировалось по месячным прогнозам.

---

### DIS-CANDIDATE

Actual-State Visibility
≠
Forecast-Only Visibility

Status:
SINGLE-SOURCE / CANDIDATE

---

### REL

Forecast
→ Capacity Planning

Status:
CONFIRM / UPDATE

Actual State Visibility
→ Replenishment Decision

Status:
PARTIAL CONFIRMATION

Information Visibility
→ enables → Pull Control

Status:
CANDIDATE

---

### PROPERTY-CANDIDATE

Signal Visibility

Definition:
доступность информации о фактическом состоянии,
необходимой для работы механизма вытягивания.

Status:
SINGLE-SOURCE / CANDIDATE

---

### MACHINE

No new Machine.

---

### CHAIN

Actual State
↓
Visibility
↓
Replenishment Decision

Status:
PARTIAL / SOURCE-SUPPORTED

---

CMOC INTERPRETATION MUST NOT BE PRESENTED
AS DIRECT SOURCE CLAIM.

CORE NOT MODIFIED.
LAB-002 NOT MODIFIED.

### Извещение на изменение `0012+240826`

## 011.25 — Three Pull Domains

### M

Pull Flow

Status:
STRONG CANDIDATE / MULTI-CONFIRMED

Application domains:

1. Production Pull
2. Delivery Pull
3. Supply Pull

---

### DIS-CANDIDATE

Machine
≠
Application Context

Status:
SINGLE-SOURCE / CANDIDATE

---

### REL

Pull
→ Production

Pull
→ Delivery

Pull
→ Supply

---

### MACHINE UPDATE

Supplier Milk Run

New Application Contexts:

- Supply
- Delivery

Machine identity is not duplicated.

---

### CHAIN-CANDIDATE-007

Production Pull
↓
Delivery Pull
↓
Supply Pull

Status:
SOURCE-SUPPORTED STRATEGIC EXPANSION

Not yet classified as operational Machine-Chain.

---

### MACHINE-PASSPORT FIELD CANDIDATE

Application Context

Definition:
контекст, в котором конкретная Machine
применяется для реализации механизма.

CORE NOT MODIFIED.
LAB-002 NOT MODIFIED.
+++++++++++
## Извещение на изменение `0014+240826`

## 011.26 — External Logistics Architecture

### ARCHITECTURE

External Logistics
├── Supply Flow
└── Delivery Flow

Each flow includes:
- Receive
- Ship
- Closed Loop
- Pull

Status:
SOURCE-SUPPORTED

---

### M

Closed-Loop Logistics

Status:
NEW / STRONG CANDIDATE

---

### MACHINE UPDATE

Supplier Milk Run

Status:
MULTI-CONFIRMED / STRONG CANDIDATE

Application Context:
- Supply
- Delivery

---

### REL

External Logistics
→ Supply Flow

External Logistics
→ Delivery Flow

Supply Flow
→ Closed Loop

Delivery Flow
→ Closed Loop

---

### CHAIN-CANDIDATE-008

Supply:

External Logistics
↓
Supply Flow
↓
Closed Loop
↓
Milk Run

Delivery:

External Logistics
↓
Delivery Flow
↓
Closed Loop
↓
Milk Run

Status:
SOURCE-SUPPORTED ARCHITECTURAL CHAIN

---

### MACHINE-CATALOG NOTE

Do not duplicate Milk Run
for Supply and Delivery contexts.

Machine identity remains singular.
Application Context is separate.

CORE NOT MODIFIED.
LAB-002 NOT MODIFIED.
## Извещение на изменение `0016+240826`
## 011.27 — From Tools to System

### SOURCE CLAIM

Компания A применяла множество
кайдзен-инструментов.

При этом отсутствовали:
- единая стратегия;
- система показателей движения вперёд.

В 2005 году начался проект
улучшения потока на основе вытягивания.

Проект включал:
- анализ текущего состояния;
- определение будущего состояния;
- организацию внедрения потока
  на базе модели TFM.

---

### DIS-CANDIDATE

Tools
≠
System / Strategy

Status:
STRONG CANDIDATE

---

### M-CANDIDATE

Flow Transformation Cycle

Current State
↓
Analysis
↓
Future State
↓
Implementation
↓
New State

Status:
SINGLE-SOURCE / CANDIDATE

---

### M-CANDIDATE

Continuous Improvement Management

Status:
SINGLE-SOURCE / CANDIDATE

---

### TOOL CLASSIFICATION

Value Stream Mapping

Role in source:
analysis of current state
and design of future state.

Do not classify as Machine.

---

### TRANSFORMATION-MACHINE-CANDIDATE

Flow Transformation Cycle

Status:
SINGLE-SOURCE

Note:
candidate for a distinct class of
system-transformation Machines.

---

### CHAIN-CANDIDATE

Current State
↓
Analysis
↓
Future State
↓
Implementation
↓
New State

Status:
SOURCE-SUPPORTED / SINGLE-SOURCE

---

CORE NOT MODIFIED.
LAB-002 NOT MODIFIED.
## Извещение на изменение `0018+240826`

## 011.28 — Future State Implementation

### ARCHITECTURE

Future State
≠
Machine

Future State is a target configuration
composed of multiple mechanisms,
Machines, flows and rules.

---

### M

Flow Transformation Cycle

Status:
STRONG CANDIDATE

---

### TRANSFORMATION-MACHINE-CANDIDATE

Flow Transformation Cycle

Type:
TRANSFORMATION

Physical realization:
- Current State Map
- Future State Map
- TFM Design
- Implementation Programme

Status:
STRONG CANDIDATE / SINGLE-SOURCE

---

### REL-CANDIDATE

Transformation Machine
→ requires / uses
Transformation Team

Status:
CANDIDATE

---

### CHAIN-CANDIDATE-009

Current State
↓
Value Stream Analysis
↓
Future State
↓
TFM Design
↓
Implementation
↓
New State
↓
Measured Result

Status:
SOURCE-SUPPORTED / STRONG CANDIDATE

---

### EVIDENCE

Future State implemented during first year.
Production line performance reached
target improvement of 27% after first month
of training.

No attribution to individual Machines.

CORE NOT MODIFIED.
LAB-002 NOT MODIFIED.
## Извещение на изменение `0020+240826`
## 011.29 — Post-Implementation Feedback

### SOURCE CLAIM

После внедрения Future State:
- производительность достигла целевого роста;
- ежедневно проводились кайдзен-собрания;
- собрания проходили в информационном уголке
  рядом со сборочной линией;
- показатели производительности,
  эффективности, качества
  и соблюдения графика были видимы;
- показатели улучшались изо дня в день.

---

### M-CANDIDATE

Daily Performance Feedback Loop

Mechanism:
видимая регулярная информация
о результатах используется
для дальнейшего улучшения.

Status:
SINGLE-SOURCE / CANDIDATE

---

### PHYSICAL REALIZATION-CANDIDATE

Line-Side Information Corner
+
Visible Performance Indicators
+
Daily Meeting

Not classified as Machine.

---

### TRANSFORMATION-MACHINE UPDATE

Flow Transformation Cycle

Post-Implementation Loop:

New State
↓
Measurement
↓
Visible Performance
↓
Daily Review
↓
Kaizen
↓
Further Improvement

Status:
SOURCE-SUPPORTED / CANDIDATE

Do not merge automatically
with Transformation Machine.

---

### CHAIN-CANDIDATE-010

Implemented State
↓
Measurement
↓
Visible Performance
↓
Daily Review
↓
Kaizen
↓
Further Improvement

Status:
SOURCE-SUPPORTED / SINGLE-SOURCE

CORE NOT MODIFIED.
LAB-002 NOT MODIFIED.
# **Извещение на изменение — `0023+240826`**


> Закрытие главы 11. Все результаты сохранены как рабочие кандидаты; CORE не изменён; LAB-002 не изменён.






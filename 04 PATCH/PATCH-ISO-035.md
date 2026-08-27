# PATCH-ISO-035 — 8.7 Control of nonconforming outputs

**Источник:** ISO/DIS 9001:2025(E)-6th-Ed  
**Вагонетка:** ISO-035  
**Дата:** 27-08-2026  
**Извещение на изменение:** 0104+270826  
**Статус:** CANDIDATE / SINGLE-SOURCE

## SOURCE CLAIM

8.7.1 requires outputs that do not conform to requirements to be identified and controlled to prevent unintended use or delivery. Appropriate action is taken based on the nature of the nonconformity and its effect on conformity. This applies also to nonconforming products/services detected after delivery or during/after service provision.

The source gives four possible ways of dealing with nonconforming outputs:
- correction;
- segregation, containment, return or suspension of provision;
- informing the customer;
- obtaining authorization for acceptance under concession.

When a nonconforming output is corrected, conformity to requirements shall be verified.

8.7.2 requires documented information as evidence to:
- describe the nonconformity;
- describe actions taken;
- describe concessions obtained;
- identify the authority deciding the action.

Annex A.8.7 states that nonconformity can occur despite rigorous application of the QMS, at final or intermediate stages, and can be detected through planned controls, accidentally, or after delivery. When correction involves rework/repair/re-performance, controls are repeated to ensure conformity has been restored.

## TERMS

- nonconforming output
- nonconformity
- correction
- segregation
- containment
- return
- suspension
- concession
- unintended use or delivery
- conformity restored

## DISTINCTIONS

### DIS-001 — NONCONFORMING OUTPUT ≠ NONCONFORMITY

The output is the object found not to fulfil requirements; nonconformity is the non-fulfilment of a requirement.

**CANDIDATE / SINGLE-SOURCE**

### DIS-002 — IDENTIFICATION ≠ CONTROL

First the nonconforming output is identified; then it is controlled to prevent unintended use or delivery.

**NEW / SINGLE-SOURCE**

### DIS-003 — CONTROL ≠ CORRECTION

Control prevents unintended use/delivery; correction is one possible action for dealing with the nonconforming output.

**NEW / SINGLE-SOURCE**

### DIS-004 — CORRECTION ≠ CORRECTIVE ACTION

8.7 concerns action on the nonconforming output. Corrective action, as defined separately in Clause 3, addresses cause and recurrence.

**CANDIDATE / SINGLE-SOURCE**

### DIS-005 — CONTAINMENT ≠ CORRECTION

Containment limits the output; correction addresses the nonconforming output itself. The source lists them separately.

**NEW / SINGLE-SOURCE**

### DIS-006 — CONCESSION ≠ CONFORMITY

Acceptance under concession is an authorized way of dealing with a nonconforming output; it does not itself establish conformity.

**STRONG CANDIDATE / SINGLE-SOURCE**

### DIS-007 — CONCESSION ≠ UNAUTHORIZED ACCEPTANCE

Acceptance under concession requires authorization.

**NEW / SINGLE-SOURCE**

### DIS-008 — CORRECTION ≠ RESTORED CONFORMITY

After correction, conformity shall be verified.

**STRONG CANDIDATE / SINGLE-SOURCE**

### DIS-009 — DETECTION BEFORE DELIVERY ≠ DETECTION AFTER DELIVERY

The same control principle applies in both cases, but post-delivery detection extends the control response beyond the original realization stage.

**CANDIDATE / SINGLE-SOURCE**

### DIS-010 — FINAL OUTPUT ≠ INTERMEDIATE OUTPUT

Nonconformity may occur at intermediate stages as well as in the final product/service.

**NEW / SINGLE-SOURCE**

## GM

### GM-001

> Сначала идентифицируй nonconforming output, затем не допусти его unintended use or delivery.

### GM-002

> Выбирай действие по nature of nonconformity и её effect on conformity.

### GM-003

> Не считай correction завершённой без повторной verification conformity.

### GM-004

> Не ограничивай nonconformity management финальным продуктом: intermediate outputs также являются объектами контроля.

### GM-005

> Concession требует отдельного authorization и traceability decision authority.

## REL

### REL-001

```text
REQUIREMENT
  ↓
OUTPUT
  ↓
NONCONFORMITY
  ↓
IDENTIFICATION
  ↓
CONTROL
```

### REL-002

```text
NONCONFORMING OUTPUT
  ↓
ACTION SELECTION
  ├── CORRECTION
  ├── SEGREGATION / CONTAINMENT
  ├── RETURN / SUSPENSION
  ├── CUSTOMER INFORMATION
  └── CONCESSION
```

### REL-003

```text
CORRECTION
  ↓
VERIFICATION
  ↓
CONFORMITY RESTORED
```

### REL-004

```text
NONCONFORMITY
  ↓
ACTION / CONCESSION
  ↓
DOCUMENTED INFORMATION
  ├── NONCONFORMITY
  ├── ACTION
  ├── CONCESSION
  └── DECIDING AUTHORITY
```

### REL-005

```text
NONCONFORMITY
  ↓
DETECTION
  ├── DURING PROCESS
  ├── AT FINAL OUTPUT
  └── AFTER DELIVERY / SERVICE
```

## MECHANISM

### M-040 — Nonconforming-output control mechanism

```text
NONCONFORMING OUTPUT
        ↓
IDENTIFY
        ↓
CONTROL
        ↓
ASSESS NATURE / EFFECT
        ↓
DECIDE ACTION
   ├── CORRECT
   ├── CONTAIN / SEGREGATE / RETURN / SUSPEND
   ├── INFORM CUSTOMER
   └── AUTHORIZE CONCESSION
        ↓
IF CORRECTED
        ↓
VERIFY CONFORMITY
        ↓
CONFORMITY RESTORED
```

**M-040 — CANDIDATE / SINGLE-SOURCE**

## CAPABILITY

### CAP-035 — Nonconforming-output control capability

Способность идентифицировать и удерживать nonconforming outputs от unintended use/delivery, выбирать и реализовывать appropriate action, а после correction подтверждать восстановление conformity.

**CANDIDATE / SINGLE-SOURCE**

## CORE CANDIDATES

### CORE-CANDIDATE-088 — Control precedes disposition

До выбора способа обращения nonconforming output должен быть идентифицирован и controlled.

**STRONG CANDIDATE / SINGLE-SOURCE**

### CORE-CANDIDATE-089 — Disposition is choice among different action classes

ISO не задаёт единственную реакцию: correction, containment/segregation/return/suspension, customer information и concession являются различными способами обращения.

**STRONG CANDIDATE / SINGLE-SOURCE**

### CORE-CANDIDATE-090 — Correction requires re-verification

```text
CORRECT → VERIFY → CONFORMITY RESTORED
```

**STRONG CANDIDATE / SINGLE-SOURCE**

### CORE-CANDIDATE-091 — Nonconformity control can extend beyond delivery

Контроль распространяется и на nonconforming products/services, обнаруженные после delivery.

**CANDIDATE / SINGLE-SOURCE**

### CORE-CANDIDATE-092 — Decision authority is part of the evidence

Documented information должна идентифицировать authority, принимающую решение по nonconformity.

**STRONG CANDIDATE / SINGLE-SOURCE**

## MACHINE

**MACHINE-CANDIDATE-003 — Nonconforming-output disposition machine**

```text
DETECT
 ↓
IDENTIFY
 ↓
CONTROL
 ↓
ASSESS
 ↓
SELECT DISPOSITION
 ↓
ACTION
 ↓
VERIFY IF CORRECTED
 ↓
RELEASE / CONTINUE / OTHER AUTHORIZED DISPOSITION
```

Пока это **MACHINE-CANDIDATE / STRONG CANDIDATE / SINGLE-SOURCE**. Важное отличие от предыдущих вагонеток: здесь источник задаёт не только общий механизм, но и воспроизводимую ветвящуюся конструкцию действий. Однако физическая/организационная реализация как отдельная Machine непосредственно не задана, поэтому в каталог Machine пока не переносится.

## CHAIN

### CHAIN-CANDIDATE-045 — Nonconformity disposition

```text
NONCONFORMING OUTPUT
 ↓
IDENTIFY
 ↓
CONTROL
 ↓
ASSESS
 ↓
ACTION / DISPOSITION
```

### CHAIN-CANDIDATE-046 — Correction loop

```text
NONCONFORMING OUTPUT
 ↓
CORRECTION
 ↓
VERIFICATION
 ↓
CONFORMITY RESTORED
```

### CHAIN-CANDIDATE-047 — Evidence of disposition

```text
NONCONFORMITY
 ↓
ACTION
 ↓
CONCESSION / DECISION
 ↓
AUTHORITY
 ↓
DOCUMENTED INFORMATION
```

Все — **CANDIDATE / SINGLE-SOURCE**.

## ROLE

**NONE**

Source требует идентифицировать authority deciding the action, но новой устойчивой CMOC Role не задаёт.

## PHYSICAL REALIZATION

**NONE**

## DOCUMENT / DOCUMENTED INFORMATION / RECORD

8.7.2 даёт очень сильное продолжение ISO-028:

```text
NONCONFORMITY
 + ACTION
 + CONCESSION
 + DECISION AUTHORITY
        ↓
DOCUMENTED INFORMATION
        ↓
EVIDENCE
```

Функционально это близко к **record** как evidence of results achieved, но автоматическое равенство `documented information = record` не устанавливаем.

Особенно важна связка:

```text
DECISION
 ↓
AUTHORITY
 ↓
TRACEABLE EVIDENCE
```

## CMOC INTERPRETATION

### 1. Nonconformity — это не конец процесса, а переход в другой режим управления

```text
NORMAL REALIZATION
        ↓
NONCONFORMITY DETECTED
        ↓
CONTROLLED DISPOSITION
        ↓
CONFORMITY RESTORED / AUTHORIZED ALTERNATIVE
```

Это **CMOC interpretation**.

### 2. У nonconforming output появляется управленческое состояние

До решения он не должен свободно продолжать движение к use/delivery:

```text
OUTPUT
 ↓
NONCONFORMING
 ↓
CONTROLLED STATE
 ↓
DECISION
```

Это сильная связь с добытыми в ISO-033 `output status` и в ISO-034 `release`.

### 3. Decision становится обязательным элементом управляемости

ISO не просто требует «исправить». Он допускает несколько способов обращения и требует идентифицировать authority, принимающую решение.

Поэтому предварительно:

```text
NONCONFORMITY
 ↓
DECISION
 ↓
ACTION
 ↓
EVIDENCE
```

— **MULTI-CONFIRMATION CANDIDATE**.

## CROSS-CLAUSE

ISO-033 → ISO-034 → ISO-035 теперь дают особенно чистый контур:

```text
ISO-033
OUTPUT
 ↓
STATE OF CONTROL
 ↓
CONFORMITY

ISO-034
CONFORMITY
 ↓
AUTHORIZATION
 ↓
RELEASE

ISO-035
NONCONFORMITY
 ↓
CONTROL
 ↓
DECISION
 ↓
ACTION
 ↓
VERIFY
 ↓
CONFORMITY RESTORED
```

Предварительная общая конструкция:

```text
OUTPUT
 ↓
STATE
 ├── CONFORMING
 │      ↓
 │   AUTHORIZATION
 │      ↓
 │   RELEASE
 │
 └── NONCONFORMING
        ↓
     CONTROL
        ↓
     DECISION
        ↓
     ACTION
        ↓
     VERIFICATION
        ↓
     CONFORMITY / AUTHORIZED DISPOSITION
```

**MULTI-CONFIRMATION CANDIDATE.**

Это пока не Core и не каноническая Chain.

## FINAL STATUS

| Class | Result |
|---|---|
| TERMS | CANDIDATE |
| DISTINCTIONS | 10 |
| GM | 5 |
| REL | 5 |
| MECHANISM | M-040 NEW |
| CAPABILITY | CAP-035 |
| CORE CANDIDATES | 5 |
| MACHINE | MACHINE-CANDIDATE-003 / STRONG CANDIDATE |
| CHAIN | 3 CANDIDATES |
| ROLE | NONE |
| PHYSICAL REALIZATION | NONE |
| Document / Documented information / Record | evidence structure confirmed |
| CROSS-CLAUSE | Output → State → Conformity / Nonconformity → Decision → Action → Verification |

**STATUS: CANDIDATE / SINGLE-SOURCE**

## PHYSICAL FIXATION

Created directly in GitHub:

`04 PATCH/PATCH-ISO-035.md`

**Извещение на изменение — 0104+270826**

CORE, MACHINE-CATALOG, ROLE-CATALOG и CHAIN-CATALOG не изменялись.

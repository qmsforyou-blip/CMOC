---
chain_id: CHAIN-CANDIDATE-001
name: Gemba → Gembutsu → Temporary Countermeasure → Root Cause → Standardization

level: CHAIN
type: PROBLEM-RESPONSE / STANDARDIZATION

source: Имаи Масааки — Гемба кайдзен
source_location: Глава 9

status: SOURCE-SUPPORTED-CANDIDATE

evidence:
  - Gemba Walk
  - Gembutsu Check
  - Temporary Countermeasure
  - Root Cause Analysis
  - Standardization

machines:
  - "[[MC-009-11 Gemba Walk]]"
  - "[[MC-009-12 Asaichi]]"
  - "[[...]]"

cmoc_links: []

confirmation_sources:
  - Имаи Масааки — Гемба кайдзен

---
# CHAIN-CANDIDATE-001
## Gemba → Gembutsu → Temporary Countermeasure → Root Cause → Standardization

## 1. Что это

Подтверждённая источником последовательность действий
при работе с проблемой в гемба.

## 2. Источник

Имаи Масааки, «Гемба кайдзен», глава 9.

## 3. Последовательность


``text
ПРОБЛЕМА
  ↓
GEMBA WALK
  ↓
GEMBUTSU CHECK
  ↓
TEMPORARY COUNTERMEASURE
  ↓
ROOT CAUSE
  ↓
STANDARDIZATION

elements:
  - id: MC-009-11
    name: Gemba Walk
    type: MACHINE

  - id: Gembutsu-Check
    name: Gembutsu Check
    type: ACTION / M-CANDIDATE

  - id: Temporary-Countermeasure
    name: Temporary Countermeasure
    type: ACTION / M-CANDIDATE

  - id: Root-Cause
    name: Root Cause Analysis
    type: M-CANDIDATE

  - id: Standardization
    name: Standardization
    type: M / ACTION
++++
# 10. Что фиксируем сейчас

### `CHAIN-CANDIDATE-001`

**Статус:** `SOURCE-SUPPORTED-CANDIDATE`

**Источник:** Имаи, гл. 9.

**Состав:**

```
Gemba Walk
→ Gembutsu Check
→ Temporary Countermeasure
→ Root Cause Analysis
→ Standardization
```

**Типы элементов:**

```
MACHINE
ACTION / M-CANDIDATE
ACTION / M-CANDIDATE
M-CANDIDATE
M / ACTION
```


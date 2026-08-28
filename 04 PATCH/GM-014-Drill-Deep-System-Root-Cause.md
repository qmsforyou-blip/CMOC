# GM-014 — Drill Deep / System Root Cause

**Источник:** GM Quality System Basics Overview Supplier Audit.pdf  
**Раздел:** Fast Response → 1.3 Problem Solving → Step 3: Identify the Root Cause  
**Извещение на изменение:** 0125+280826  
**STATUS:** CANDIDATE / SINGLE-SOURCE

## SOURCE

После нахождения technical root cause GM требует определить, **WHY the System failed**. В Drill Deep используется отдельное углубление причинного анализа по трём направлениям:

- **Predict** — почему Planning process не предсказал failure;
- **Prevent** — почему Manufacturing process не предотвратил defect;
- **Protect** — почему Quality process не защитил customer (GM) от defect.

GM показывает это как **System RC; 3x5 Why**.

## DISTINCTIONS

- Technical Root Cause ≠ System Root Cause.
- Cause of Failure Mode ≠ причина, по которой система допустила возникновение/прохождение failure.
- Predict ≠ Prevent ≠ Protect.
- Planning System ≠ Manufacturing System ≠ Quality System.
- Error Proofing / Standardized Work относятся к Prevent; Error Detection & Containment — к Protect; informational content in all documentation — к Predict.

## GM

“After the technical root cause is found, determine WHY the System failed.”

“Predict – Why did the planning process not predict the failure?”

“Prevent – Why did the manufacturing process not prevent the defect?”

“Protect – Why did the Quality process not protect the customer (GM) from the defect?”

## REL

```text
TECHNICAL ROOT CAUSE
        ↓
DRILL DEEP
        ↓
┌──────────────┬───────────────┬───────────────┐
│   PREDICT    │    PREVENT    │    PROTECT    │
│  Planning    │ Manufacturing │    Quality    │
│   System     │    System     │    System     │
└──────────────┴───────────────┴───────────────┘
        ↓
SYSTEM ROOT CAUSE(S)
```

## MECHANISM

### CANDIDATE — System Failure Drill-Down

**Input:** Technical Root Cause.

**Transformation:** последовательное применение Why к трём системным вопросам: Predict / Prevent / Protect.

**Output:** System Root Cause(s).

**Organizational effect:** техническая причина переводится в анализ того, почему соответствующие элементы системы не предсказали, не предотвратили или не защитили.

## CAPABILITY

NONE.

## CORE CANDIDATE

**System Failure Drill-Down** — воспроизводимая конструкция углубления анализа от technical root cause к причинам отказа Planning, Manufacturing и Quality systems по направлениям Predict, Prevent и Protect.

## MACHINE

**CANDIDATE MACHINE — Drill Deep / System Root Cause**

```text
TECHNICAL ROOT CAUSE
        ↓
WHY DID THE SYSTEM FAIL?
        ↓
PREDICT ──→ Planning System
PREVENT ──→ Manufacturing System
PROTECT ──→ Quality System
        ↓
SYSTEM ROOT CAUSE(S)
```

Инженерный тест:
- вход — technical root cause;
- операция — системное причинное углубление по трём направлениям;
- выход — system root cause(s);
- воспроизводимость — задана структурой 3×5 Why.

## CHAIN

```text
Technical Root Cause
→ Drill Deep
→ Predict / Prevent / Protect
→ System Why paths
→ System Root Cause(s)
```

## STATUS

**CANDIDATE / SINGLE-SOURCE**

Не CANON. Не подтверждать тождество этой конструкции с ISO corrective action, management system analysis или иной CMOC-конструкцией без отдельного межисточникового основания.

## CMOC INTERPRETATION

Сильное различение GM: после устранения вопроса **“что технически вызвало failure?”** возникает другой вопрос — **“почему система допустила, чтобы этот failure возник или дошёл до customer?”**.

Таким образом, GM разделяет как минимум два уровня причинности:

```text
FAILURE
  ↓
TECHNICAL ROOT CAUSE
  ↓
SYSTEM FAILURE
  ↓
SYSTEM ROOT CAUSE
```

И системный уровень дополнительно раскладывается на три защитные функции:

```text
PREDICT → Planning
PREVENT → Manufacturing
PROTECT → Quality
```

Это потенциально сильная CMOC-конструкция, но пока остаётся **CANDIDATE / SINGLE-SOURCE**.

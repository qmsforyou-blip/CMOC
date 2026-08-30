# GM-093 — Error Proofing Verification — Failure Response & Management Review

## SOURCE

**Source:** GM Quality System Basics Overview Supplier Audit.pdf  
**Section:** 6.2 — Method of Verification (continued); 6.3 — Management Review  
**Pages:** 218–219  
**Status:** SOURCE-SUPPORTED extraction; CMOC interpretations explicitly separated.

---

## 1. SOURCE EXTRACTION

### 6.2 — Verification results and response to failures

SOURCE states that verification results **shall be recorded** and that failures require **immediate responses**.

The required response structure includes:

- develop a log of error proof verification failures with reaction plans to nonconformities, including containment;
- develop a procedure for notification of nonconformities and escalation of reaction to nonconformities;
- open a corrective action report (Core “6 steps” / Fast response) to prevent the error proofing device from failing again.

SOURCE further specifies that reaction plans shall address the case where an error proofing device fails: product shall be verified back to the **last good check**.

SOURCE refers to **Strategy 2.0 — Control of nonconforming product** for this response.

### 6.3 — Management Review

SOURCE states that verification results shall be reviewed by **site leadership**.

The organization shall define:

- the method for getting information to management;
- how the information is to be displayed.

---

## 2. DISTINCTIONS

### D1 — Verification result vs. unrecorded observation

**Status: SOURCE-SUPPORTED**

A verification result is required to be recorded. Verification without a resulting record does not satisfy the stated requirement.

### D2 — Verification failure vs. ordinary observation

**Status: SOURCE-SUPPORTED**

Failure of an error proofing device requires an immediate defined response, not merely observation or later review.

### D3 — Failure record vs. reaction plan

**Status: SOURCE-SUPPORTED**

The failure log is to be accompanied by reaction plans addressing the resulting nonconformity.

### D4 — Reaction plan vs. containment

**Status: SOURCE-SUPPORTED**

Containment is explicitly included within the reaction plan for error proofing verification failures.

### D5 — Notification vs. escalation

**Status: SOURCE-SUPPORTED**

The response system shall provide both notification of nonconformities and escalation of the reaction to them.

### D6 — Immediate correction vs. corrective action

**Status: SOURCE-SUPPORTED**

Immediate reaction to the failure is distinct from opening a corrective action report intended to prevent recurrence of error proofing device failure.

### D7 — Device failure vs. affected product boundary

**Status: SOURCE-SUPPORTED**

When an error proofing device fails, the product affected by the failure is to be verified back to the last good check.

### D8 — Error-proofing failure response vs. control of nonconforming product

**Status: SOURCE-SUPPORTED**

SOURCE connects the reaction to a failed error proofing device with the established strategy for control of nonconforming product.

### D9 — Verification result vs. management information

**Status: SOURCE-SUPPORTED**

Verification results are not only operational records; they are subject to review by site leadership.

### D10 — Information availability vs. information presentation

**Status: SOURCE-SUPPORTED**

Management review requires both a defined method for delivering information to management and a defined way for displaying that information.

---

## 3. TERMS

**English — Русский**

- Verification Result — Результат проверки
- Verification Failure — Отказ / неудовлетворительный результат проверки
- Error Proofing Device — Устройство защиты от ошибок
- Failure Log — Журнал отказов / неудачных проверок
- Reaction Plan — План реагирования
- Containment — Сдерживание / локализация
- Nonconformity — Несоответствие
- Notification — Уведомление
- Escalation — Эскалация
- Corrective Action Report — Отчёт / документ по корректирующим действиям
- Last Good Check — Последняя успешная проверка
- Control of Nonconforming Product — Управление несоответствующей продукцией
- Site Leadership — Руководство площадки
- Management Review — Анализ руководством

---

## 4. MECHANISM

### SOURCE-SUPPORTED

```text
VERIFICATION
     ↓
RECORD RESULT
     ↓
FAILURE?
   /     \
 NO       YES
           ↓
     REACTION PLAN
           ↓
     CONTAINMENT
           ↓
  NOTIFICATION / ESCALATION
           ↓
 PRODUCT VERIFIED BACK TO
    LAST GOOD CHECK
           ↓
 CORRECTIVE ACTION REPORT
           ↓
 PREVENT RECURRENCE
```

### MANAGEMENT REVIEW

```text
VERIFICATION RESULTS
        ↓
 INFORMATION TO MANAGEMENT
        ↓
 SITE LEADERSHIP REVIEW
        ↓
 DEFINED DISPLAY OF INFORMATION
```

### CMOC INTERPRETATION / CANDIDATE

```text
CHECK
 ↓
RESULT
 ↓
RECORD
 ↓
FAILURE STATUS
 ↓
CONTAINMENT / ESCALATION
 ↓
AFFECTED PRODUCT BOUNDARY
 ↓
CORRECTIVE ACTION
 ↓
MANAGEMENT VISIBILITY
```

This is a **CMOC interpretation**, not SOURCE terminology.

---

## 5. CAPABILITY

**SOURCE-SUPPORTED:** the described system provides the organization with a controlled response to failure of an error proofing device and provides verification information for site leadership review.

**CMOC INTERPRETATION / CANDIDATE:** the mechanism converts a failed verification into a bounded product-control response, a recurrence-prevention action, and management visibility.

This stronger formulation is not Canon.

---

## 6. MACHINE

**Candidate Machine:** Error Proofing Failure Response Machine.

```text
VERIFY
  ↓
RECORD
  ↓
DETECT FAILURE
  ↓
CONTAIN
  ↓
NOTIFY / ESCALATE
  ↓
TRACE TO LAST GOOD CHECK
  ↓
CORRECTIVE ACTION
  ↓
MANAGEMENT REVIEW
```

**Status:** CANDIDATE.

Do not promote to CANON without cross-checking with the related nonconforming-product and corrective-action SOURCE blocks.

---

## 7. CHAIN

### SOURCE-SUPPORTED chain

```text
VERIFICATION RESULT
       ↓
RECORD
       ↓
FAILURE RESPONSE
       ↓
CONTAINMENT
       ↓
NOTIFICATION / ESCALATION
       ↓
LAST GOOD CHECK
       ↓
CORRECTIVE ACTION
       ↓
MANAGEMENT REVIEW
```

### CMOC candidate

```text
MEASUREMENT / CHECK
       ↓
RECORD
       ↓
STATUS
       ↓
DECISION / REACTION
       ↓
CONTAINMENT
       ↓
BOUNDARY OF AFFECTED PRODUCT
       ↓
CORRECTIVE ACTION
       ↓
MANAGEMENT VISIBILITY
```

The CMOC candidate chain is an interpretation of the SOURCE structure and is not Canon.

---

## 8. CMOC INTERPRETATION

The key result of pp. 218–219 is that **verification is not an isolated checking activity**.

SOURCE closes the loop around a failed verification:

```text
CHECK → RECORD → FAILURE → CONTAIN → ESCALATE
                         ↓
                 LAST GOOD CHECK
                         ↓
                 AFFECTED PRODUCT
                         ↓
                CORRECTIVE ACTION
```

It then connects verification results to **site leadership review**.

This gives a strong CMOC distinction:

> **A verification system is not complete when it detects failure; it is complete only when the failure produces a controlled response and the result becomes visible to management.**

The quoted formulation is **CMOC interpretation**, not SOURCE text.

---

## 9. STATUS

| Construction | Status |
|---|---|
| Verification results shall be recorded | SOURCE-SUPPORTED |
| Failures require immediate response | SOURCE-SUPPORTED |
| Failure log with reaction plans | SOURCE-SUPPORTED |
| Containment included in reaction plans | SOURCE-SUPPORTED |
| Notification and escalation procedure | SOURCE-SUPPORTED |
| Corrective action to prevent recurrence | SOURCE-SUPPORTED |
| Product verified back to last good check | SOURCE-SUPPORTED |
| Link to control of nonconforming product | SOURCE-SUPPORTED |
| Site leadership review of verification results | SOURCE-SUPPORTED |
| Defined information flow to management | SOURCE-SUPPORTED |
| Defined information display | SOURCE-SUPPORTED |
| Error Proofing Failure Response Machine | CANDIDATE |
| Verification → Record → Status → Reaction → Management visibility | CMOC INTERPRETATION / CANDIDATE |
| CANON | No |

---

## 10. SOURCE BOUNDARY

Не устанавливаются самостоятельно дополнительные сроки, формы журналов, критерии эскалации или конкретные методы containment. SOURCE требует наличия соответствующих механизмов, но не раскрывает в этом фрагменте их детальную организационную форму.

Также не следует смешивать **корректирующее действие** с непосредственной реакцией на отказ: SOURCE явно разделяет immediate response и corrective action report.

---

## 11. LINK TO NEXT SOURCE BLOCK

Следующий блок следует рассматривать как продолжение логики **6.3 Management Review / 6.4 Summary**.

Ключевой вопрос для продолжения извлечения:

> Как SOURCE формулирует итоговые обязательства по Error Proofing Verification и что именно должно быть обеспечено на уровне системы?

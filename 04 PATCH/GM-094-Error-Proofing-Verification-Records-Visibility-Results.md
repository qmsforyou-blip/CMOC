# GM-094 — Error Proofing Verification — Records, Visibility & Results

## SOURCE

**Source:** GM Quality System Basics Overview Supplier Audit.pdf  
**Section:** Error Proofing Verification  
**Pages:** 220–221  
**Status:** SOURCE-SUPPORTED extraction; CMOC interpretations explicitly separated.

---

## 1. SOURCE EXTRACTION

### p. 220 — Error Proofing Verification Checklist

SOURCE provides an **Error Proofing Verification Checklist** with the explicit statement that the listed items are to be checked **daily**.

The checklist records, among other things:

- shift and date;
- verification items associated with operations;
- code for the verification item;
- YES / NO result;
- problem information;
- supervisor and auditor identification/signature.

The checklist includes a visual rule for shaded items: if any shaded item is not working properly, the supervisor must be notified immediately. Any item out of compliance should be reviewed with the supervisor or a copy of the audit given to the supervisor.

SOURCE then states:

> Completion of the verification shall be documented and easily accessible.

It also states that the device's verification status should be visible to everyone in the area.

### p. 221 — Error Proofing Verification Results

SOURCE provides a results display intended to track verification performance over time.

The results record includes monthly measures for:

- % in compliance;
- number of items on the checklist;
- number of verifications;
- total number of items verified;
- number of items in compliance.

The display also provides a section for **items not in compliance** and the number of such items by month.

---

## 2. DISTINCTIONS

### D1 — Verification checklist vs. undocumented check

**Status: SOURCE-SUPPORTED**

A verification activity is not complete merely because the check was performed. Completion of the verification shall be documented.

### D2 — Verification record vs. inaccessible record

**Status: SOURCE-SUPPORTED**

The verification record is required to be easily accessible; documentation that exists but cannot readily be accessed does not satisfy the stated accessibility expectation.

### D3 — Verification result vs. device verification status visibility

**Status: SOURCE-SUPPORTED**

Recording the verification result and making the device's verification status visible to everyone in the area are distinct requirements.

### D4 — Routine noncompliance vs. immediate supervisor notification

**Status: SOURCE-SUPPORTED**

For shaded checklist items that are not working properly, notification of the supervisor is required immediately. This is stronger than simply recording a NO result.

### D5 — Noncompliance record vs. supervisory review

**Status: SOURCE-SUPPORTED**

An item out of compliance is not only recorded; it is to be reviewed with the supervisor or the audit copy is to be provided to the supervisor.

### D6 — Daily verification vs. results trending

**Status: SOURCE-SUPPORTED**

Daily checking of individual items and longer-term aggregation of verification results are distinct control layers: the checklist supports the daily check, while the results display supports monitoring over time.

### D7 — Verification count vs. verified-item count

**Status: SOURCE-SUPPORTED**

The results record distinguishes the **number of verifications** from the **total number of items verified**. These are not interchangeable measures.

### D8 — Number of checklist items vs. number of items in compliance

**Status: SOURCE-SUPPORTED**

The results record separately tracks the number of items on the checklist and the number of items in compliance, enabling the compliance result to be represented against the defined checklist population.

### D9 — Compliance percentage vs. raw compliance count

**Status: SOURCE-SUPPORTED**

The results display distinguishes the percentage in compliance from the underlying count of items in compliance.

### D10 — Current verification status vs. historical performance

**Status: SOURCE-SUPPORTED**

Visible device verification status addresses the current state at the workplace, while the monthly results display provides a historical view of verification performance and noncompliance.

---

## 3. TERMS

**English — Русский**

- Error Proofing Verification Checklist — Чек-лист проверки устройства защиты от ошибок
- Verification Completion — Завершение проверки
- Verification Record — Запись о проверке
- Verification Status — Статус проверки
- Easily Accessible — Легко доступный
- Visible — Видимый / доступный для визуального контроля
- Compliance — Соответствие
- Noncompliance — Несоответствие
- Supervisor Notification — Уведомление руководителя
- Verification Results — Результаты проверок
- Number of Verifications — Количество проверок
- Total Number of Items Verified — Общее количество проверенных пунктов
- Items on Checklist — Пункты чек-листа
- Items in Compliance — Пункты в соответствии
- Items Not in Compliance — Пункты, не соответствующие требованиям
- Results Display — Представление результатов

---

## 4. MECHANISM

### SOURCE-SUPPORTED

```text
DAILY CHECK
    ↓
YES / NO RESULT
    ↓
DOCUMENT COMPLETION
    ↓
ACCESSIBLE RECORD
    ↓
DEVICE STATUS VISIBLE IN AREA
```

For noncompliance:

```text
CHECKLIST RESULT
      ↓
NONCOMPLIANCE
      ↓
SUPERVISOR REVIEW
      ↓
IMMEDIATE NOTIFICATION
      ↓
REACTION
```

For performance monitoring:

```text
INDIVIDUAL VERIFICATIONS
        ↓
AGGREGATED RESULTS
        ↓
MONTHLY COMPLIANCE DATA
        ↓
ITEMS NOT IN COMPLIANCE
        ↓
RESULTS DISPLAY / TREND VIEW
```

### CMOC INTERPRETATION / CANDIDATE

```text
CHECK
 ↓
RECORD
 ↓
STATUS
 ↓
LOCAL VISIBILITY
 ↓
NONCOMPLIANCE / REACTION
 ↓
AGGREGATION
 ↓
TREND / MANAGEMENT INFORMATION
```

This is a **CMOC interpretation**, not SOURCE terminology.

---

## 5. CAPABILITY

**SOURCE-SUPPORTED:** the described system provides documented, accessible and visible verification status at the workplace and aggregates verification results so that compliance and noncompliance can be tracked over time.

**CMOC INTERPRETATION / CANDIDATE:** the mechanism makes the verification state simultaneously actionable at the point of work and observable as a system-level performance signal.

This stronger formulation is not Canon.

---

## 6. MACHINE

**Candidate Machine:** Error Proofing Verification Control & Visibility Machine.

```text
DAILY VERIFY
     ↓
RECORD RESULT
     ↓
MAKE STATUS VISIBLE
     ↓
REACT TO NONCOMPLIANCE
     ↓
AGGREGATE RESULTS
     ↓
DISPLAY PERFORMANCE
```

**Status:** CANDIDATE.

Do not promote to CANON without cross-checking with related SOURCE blocks on error proofing response, control of nonconforming product and management review.

---

## 7. CHAIN

### SOURCE-SUPPORTED chain

```text
DAILY VERIFICATION
       ↓
DOCUMENTED COMPLETION
       ↓
ACCESSIBLE RECORD
       ↓
VISIBLE VERIFICATION STATUS
       ↓
NONCOMPLIANCE IDENTIFIED
       ↓
SUPERVISOR NOTIFICATION / REVIEW
       ↓
MONTHLY RESULTS
       ↓
COMPLIANCE / NONCOMPLIANCE VIEW
```

### CMOC candidate

```text
CHECK
 ↓
RECORD
 ↓
STATUS
 ↓
VISIBILITY
 ↓
DECISION / REACTION
 ↓
AGGREGATION
 ↓
TREND
 ↓
MANAGEMENT VISIBILITY
```

The CMOC candidate chain is an interpretation of the SOURCE structure and is not Canon.

---

## 8. CMOC INTERPRETATION

The key result of pp. 220–221 is that **verification requires both a local operational record and a visible status, while repeated verification results can be aggregated into a performance picture**.

SOURCE therefore distinguishes three layers:

```text
1. CHECK — individual verification
2. STATUS — accessible and visible verification state
3. RESULTS — aggregated compliance / noncompliance performance
```

This gives a strong CMOC distinction:

> **A verification record controls the fact of checking; visible status controls awareness at the point of work; aggregated results control the view of verification performance over time.**

The quoted formulation is **CMOC interpretation**, not SOURCE text.

---

## 9. STATUS

| Construction | Status |
|---|---|
| Items checked daily | SOURCE-SUPPORTED |
| Verification completion documented | SOURCE-SUPPORTED |
| Verification record easily accessible | SOURCE-SUPPORTED |
| Device verification status visible in the area | SOURCE-SUPPORTED |
| Shaded-item failure requires immediate supervisor notification | SOURCE-SUPPORTED |
| Out-of-compliance item reviewed with supervisor / audit provided | SOURCE-SUPPORTED |
| Monthly % in compliance | SOURCE-SUPPORTED |
| Number of checklist items | SOURCE-SUPPORTED |
| Number of verifications | SOURCE-SUPPORTED |
| Total number of items verified | SOURCE-SUPPORTED |
| Number of items in compliance | SOURCE-SUPPORTED |
| Items not in compliance tracked | SOURCE-SUPPORTED |
| Error Proofing Verification Control & Visibility Machine | CANDIDATE |
| Check → Record → Status → Visibility → Results | CMOC INTERPRETATION / CANDIDATE |
| CANON | No |

---

## 10. SOURCE BOUNDARY

Не устанавливаются самостоятельно дополнительные критерии приемки, конкретные формы визуального управления, пороги эскалации, периодичность агрегирования сверх показанной в SOURCE, либо конкретный метод анализа тренда. SOURCE показывает форму чек-листа и результатов и устанавливает требования к документированию, доступности, видимости и представлению результатов, но не раскрывает в этом фрагменте детальную организационную реализацию.

Не следует также смешивать **локальную видимость текущего статуса устройства** с **историческим представлением результатов**: это разные информационные функции SOURCE.

---

## 11. LINK TO NEXT SOURCE BLOCK

Следующий блок следует рассматривать как продолжение раздела 6 — Error Proofing Verification.

Ключевой вопрос для продолжения извлечения:

> Что SOURCE устанавливает далее как итоговые обязательства организации по Error Proofing Verification и какие элементы должны быть обеспечены как система?

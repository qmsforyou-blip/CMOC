# GM-098 — Layered Process Audits — System Components & Operating Flow

## SOURCE

**Source:** GM Quality System Basics Overview Supplier Audit.pdf  
**Section:** 7.2 Process explanation (continued)  
**Pages:** 228–229  
**Status:** SOURCE-SUPPORTED extraction; CMOC interpretations explicitly separated.

---

## 1. SOURCE EXTRACTION

### p. 228 — Components of the LPA system

SOURCE states that the Layered Process Audit system includes:

1. **Schedule and tracking of audits.**
2. **Identifying high risk items for the LPA.**
3. **A LPA Checklist** that evaluates current processes to established standards.
4. **Identification of corrective action requirements and countermeasures.**
5. **Regular review process by senior management** of the audit results and corrective actions.

This is an explicit system-level decomposition of LPA.

### p. 229 — Operating flow

SOURCE presents the following sequence:

**Choose the Workstation**  
→ pick the station to be audited based on the LPA schedule.

**Conduct the Audit**  
→ follow LPA Check sheet.

**Give feedback & document results**  
→ immediately inform all Team members about audit results;  
→ record all deviations on LPA Check sheet and Countermeasure sheet;  
→ assign target close date & champion;  
→ implement suggested countermeasures as soon as possible.

**Follow-up**  
→ follow up on open items and make sure to close by target close date;  
→ elevate problem to higher level after target close date;  
→ perform Management review.

---

## 2. DISTINCTIONS

### D1 — LPA is a system, not merely an audit event

**SOURCE-SUPPORTED**

The LPA system explicitly includes scheduling/tracking, risk-item identification, checklist evaluation, corrective action/countermeasure identification and senior-management review.

### D2 — Audit selection is schedule-driven

**SOURCE-SUPPORTED**

The workstation to be audited is selected based on the LPA schedule.

### D3 — The LPA Check sheet evaluates current process against established standards

**SOURCE-SUPPORTED**

The checklist is an evaluation mechanism comparing the current process with established standards.

### D4 — Audit results include explicit deviation recording

**SOURCE-SUPPORTED**

All deviations are to be recorded on the LPA Check sheet and Countermeasure sheet.

### D5 — Feedback is immediate and includes the Team

**SOURCE-SUPPORTED**

All Team members are to be informed immediately about audit results.

### D6 — A deviation creates a countermeasure-management requirement

**SOURCE-SUPPORTED**

The flow requires assignment of a target close date and a champion, followed by implementation of suggested countermeasures as soon as possible.

### D7 — Open items are actively followed to closure

**SOURCE-SUPPORTED**

Open items are followed up and are expected to close by the target close date.

### D8 — Overdue items escalate

**SOURCE-SUPPORTED**

A problem is elevated to a higher level after the target close date.

### D9 — Management review is part of the operating loop

**SOURCE-SUPPORTED**

Management review appears as the final step in the presented follow-up flow and senior-management review is explicitly included in the system components.

### D10 — LPA connects process verification with corrective action

**SOURCE-SUPPORTED**

The system directly connects checklist-based verification with deviation recording, corrective action/countermeasures, ownership, due dates, follow-up and escalation.

---

## 3. TERMS

- Schedule and tracking — Планирование и отслеживание
- High risk items — Элементы с высоким риском
- LPA Checklist / Check sheet — Чек-лист / проверочный лист LPA
- Established standards — Установленные стандарты
- Corrective action requirements — Требования к корректирующим действиям
- Countermeasures — Контрмеры
- Workstation — Рабочее место / рабочая станция
- Audit results — Результаты аудита
- Deviations — Отклонения
- Target close date — Целевая дата закрытия
- Champion — Ответственный / champion за выполнение
- Follow-up — Контроль последующих действий
- Higher level — Более высокий уровень
- Management review — Анализ со стороны руководства

**Translation note:** SOURCE uses “champion”; this patch does not normalize the term to a specific CMOC role because the source does not define the role further.

---

## 4. MECHANISM

### SOURCE-SUPPORTED operating loop

```text
LPA SCHEDULE
     ↓
CHOOSE WORKSTATION
     ↓
CONDUCT AUDIT
     ↓
LPA CHECK SHEET
     ↓
CURRENT PROCESS ↔ ESTABLISHED STANDARD
     ↓
DEVIATIONS
     ↓
FEEDBACK + DOCUMENT RESULTS
     ↓
TARGET CLOSE DATE + CHAMPION
     ↓
COUNTERMEASURES
     ↓
FOLLOW-UP TO CLOSURE
     ↓
ESCALATION IF OVERDUE
     ↓
MANAGEMENT REVIEW
```

### System-level architecture from p. 228

```text
SCHEDULE / TRACKING
        +
HIGH-RISK ITEMS
        +
LPA CHECKLIST
        +
CORRECTIVE ACTION / COUNTERMEASURES
        +
SENIOR MANAGEMENT REVIEW
        ↓
       LPA SYSTEM
```

---

## 5. CMOC INTERPRETATION

These pages materially change the abstraction level of the LPA concept.

LPA is no longer adequately represented as “audit against a standard.” SOURCE shows a **closed operating system** in which:

```text
PLAN → SELECT → CHECK → RECORD → ASSIGN → ACT → FOLLOW UP → ESCALATE → REVIEW
```

The important engineering feature is that the observation does not terminate at a finding. The source explicitly connects a deviation to:

**record → target date → champion → countermeasure → follow-up → escalation → management review.**

This is a strong candidate for a CMOC **control-and-reaction machine**. The label “closed loop” is an interpretation; SOURCE itself provides the sequence and required actions.

---

## 6. CAPABILITY

**SOURCE-SUPPORTED:** The LPA system provides organizational capability to repeatedly select process locations, verify actual process execution against established standards, record deviations, assign responsibility and a target close date, implement countermeasures, follow open items, escalate overdue problems and bring results into management review.

**CMOC CANDIDATE:** LPA can be modeled as a recurring organizational control loop that converts a process observation into an owned, time-bounded reaction and management visibility.

---

## 7. MACHINE

### Candidate machine: LPA Control Loop

**Input:** LPA schedule; workstation; established standards; high-risk items.  
**Verification:** perform audit using LPA Check sheet.  
**Detection:** identify and record deviations.  
**Reaction setup:** assign target close date and champion.  
**Action:** implement countermeasures.  
**Control:** follow up open items.  
**Escalation:** elevate overdue problem to higher level.  
**Review:** management review.

### Important boundary

The source does not yet provide the detailed rules for constructing the schedule, selecting high-risk items, evaluating checklist responses, or determining when a specific countermeasure is sufficient. Those rules belong to subsequent pages/sections.

---

## 8. CHAIN

```text
LPA SCHEDULE
  → WORKSTATION
  → AUDIT
  → CHECK SHEET
  → DEVIATION
  → DOCUMENTATION
  → CHAMPION + TARGET CLOSE DATE
  → COUNTERMEASURE
  → FOLLOW-UP
  → ESCALATION (IF OVERDUE)
  → MANAGEMENT REVIEW
```

This is the strongest SOURCE-supported chain on pp. 228–229.

---

## 9. STATUS

| Construction | Status |
|---|---|
| LPA system includes schedule/tracking | SOURCE-SUPPORTED |
| LPA system identifies high-risk items | SOURCE-SUPPORTED |
| Checklist evaluates current process to established standards | SOURCE-SUPPORTED |
| Corrective action/countermeasure requirements identified | SOURCE-SUPPORTED |
| Senior management regularly reviews results/actions | SOURCE-SUPPORTED |
| Workstation selected from LPA schedule | SOURCE-SUPPORTED |
| Audit follows LPA Check sheet | SOURCE-SUPPORTED |
| Immediate team feedback | SOURCE-SUPPORTED |
| Deviations recorded | SOURCE-SUPPORTED |
| Target close date assigned | SOURCE-SUPPORTED |
| Champion assigned | SOURCE-SUPPORTED |
| Countermeasures implemented promptly | SOURCE-SUPPORTED |
| Open items followed to closure | SOURCE-SUPPORTED |
| Overdue problem escalated | SOURCE-SUPPORTED |
| Management review performed | SOURCE-SUPPORTED |
| Detailed scheduling rules | NOT YET DEFINED |
| Detailed high-risk selection rules | NOT YET DEFINED |
| Checklist evaluation scale/rules | NOT YET DEFINED |
| Countermeasure acceptance/closure criteria | NOT YET DEFINED |

---

## 10. SOURCE BOUNDARY

Не добавляем пока собственные правила о:

- частоте каждого уровня аудита;
- критериях high-risk;
- классификации отклонений;
- статусах corrective action;
- критериях достаточности countermeasure;
- правилах закрытия;
- составе management review.

SOURCE на pp. 228–229 устанавливает наличие и последовательность этих механизмов, но не раскрывает их полную спецификацию.

---

## 11. LINK TO NEXT SOURCE BLOCK

Следующий блок должен раскрыть **7.2.1 Schedule and tracking** и **7.2.2 Develop high risk items for auditing** — то есть две ключевые части входа в LPA machine: **как формируется расписание** и **как выбираются объекты/элементы высокого риска**.

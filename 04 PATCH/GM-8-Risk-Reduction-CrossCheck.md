# GM QSB — Risk Reduction / Reverse PFMEA — CMOC Cross-Check

**Notice:** 0142+170926

## Source

GM Quality System Basics Overview Supplier Audit, rev. March 2009, strategy 8 — RPN Risk Reduction (Reverse PFMEA), approximately pp. 257–269.

## Purpose of this patch

Провести первый CMOC Cross-Check стратегии Risk Reduction после полного извлечения материала. Патч фиксирует рабочие гипотезы, а не канонизацию.

---

# 1. Extracted constructions

| ID | GM construction | Working CMOC class | Status | Note |
|---|---|---|---|---|
| RR-01 | PFMEA Review Process | PROCESS / ASSESSMENT ASSEMBLY | HOLD | Пересмотр существующей модели риска по trigger/data/requirements |
| RR-02 | PFMEA Risk Reduction Process | ASSEMBLY / CONTROL LOOP | HOLD | Proactive + reactive reduction contours |
| RR-03 | Reverse PFMEA | MACHINE CANDIDATE | CANDIDATE / SINGLE-SOURCE | Повторяемая on-station процедура с командой, расписанием, checklist, verification и action plan |
| RR-04 | Risk Reduction Opportunity List | ARTIFACT | HOLD | Перечень приоритетных возможностей снижения RPN |
| RR-05 | RPN Reduction Action Plan | ARTIFACT / ASSEMBLY | EXISTING PATTERN | Фиксирует action, owner/champion, date, revised RPN |
| RR-06 | Reverse PFMEA Audit Schedule | ARTIFACT / PLANNING MECHANISM | HOLD | Управляет охватом и сроками station audits |
| RR-07 | Reverse PFMEA Checklist | ARTIFACT | HOLD | Стандартизирует критерии проверки |
| RR-08 | Control Existence Verification | ASSESSMENT / VERIFICATION MECHANISM | HOLD | Есть ли предусмотренный Prevention/Detection Control |
| RR-09 | Control Effectiveness Verification | VERIFICATION MECHANISM | HOLD | Работает ли фактический control |
| RR-10 | New Failure Mode Discovery by Station Experiment | DISCOVERY MECHANISM | HOLD | Намеренное воспроизведение потенциального failure mode |
| RR-11 | RPN Reassessment | ASSESSMENT MECHANISM | HOLD | Повторная оценка Occurrence/Detection и resultant RPN |
| RR-12 | PFMEA Update after Action | UPDATE / RECORD MECHANISM | HOLD | Возврат фактического результата в risk model |
| RR-13 | RPN Tracking Matrix | ARTIFACT / MONITORING MECHANISM | HOLD | Тренд совокупного и индивидуального RPN во времени |

---

# 2. Reverse PFMEA — preliminary machine hypothesis

## Candidate identity

**Reverse PFMEA** рассматривается как кандидат на специализированную Machine.

### Input

- действующая PFMEA;
- известные Failure Modes;
- station/process;
- audit schedule;
- checklist;
- cross-functional team.

### Core action

1. Выбрать станцию по расписанию.
2. Проверить каждый Failure Mode из PFMEA.
3. Проверить наличие Prevention/Detection Controls.
4. Проверить фактическую работоспособность Controls.
5. Перейти к следующему Failure Mode.
6. После покрытия известных Failure Modes попытаться обнаружить новые Failure Modes.
7. Зафиксировать обнаруженные nonconformances / opportunities в Action Plan.

### Output

- подтверждённые controls;
- выявленные недостатки controls;
- новые потенциальные Failure Modes;
- Action Plan;
- основания для PFMEA/RPN reassessment.

## Why it is potentially a Machine

Reverse PFMEA имеет собственную воспроизводимую операционную конструкцию:

`SCHEDULE → TEAM → STATION → CHECK EACH FAILURE MODE → VERIFY CONTROL EXISTENCE → VERIFY CONTROL EFFECTIVENESS → DISCOVER NEW FAILURE MODES → ACTION PLAN`

Это больше, чем отдельный Audit или Assessment: процедура задаёт специфическую последовательность, объект проверки, способ discovery и характер выхода.

## Current boundary

Пока не утверждать, что Reverse PFMEA — самостоятельная фундаментальная Machine.

Предварительная формулировка:

> **Специализированная диагностико-верификационная Machine для проверки соответствия фактических station controls модели Failure Modes PFMEA с целью выявления control gaps, новых Failure Modes и возможностей снижения риска.**

---

# 3. Risk Reduction — architecture hypothesis

Risk Reduction пока рассматривается не как одна Machine, а как Assembly/Loop:

```text
PFMEA / RISK MODEL
        ↓
REVIEW
        ↓
RISK REDUCTION OPPORTUNITY
        ↓
PROACTIVE or REACTIVE ACTION
        ↓
CONTROL / ERROR PROOFING
        ↓
VERIFY EFFECTIVENESS
        ↓
REASSESS OCCURRENCE / DETECTION
        ↓
NEW RPN
        ↓
UPDATE PFMEA
        ↓
TRACK
```

Reverse PFMEA является одной из специализированных реализаций внутри этого контура.

---

# 4. Important distinction: Audit vs Reverse PFMEA

Не дублировать существующий `MC-009-15 Audit`.

Рабочая граница:

**Audit** — общий механизм/машинка проверки соответствия критерию.

**Reverse PFMEA** — специализированная процедура, где:

- объектом проверки является station/process;
- критерий формируется через Failure Modes PFMEA;
- проверяется одновременно наличие и работоспособность controls;
- после покрытия известных FM выполняется поиск новых FM;
- результат непосредственно используется для PFMEA review и RPN reduction.

Следовательно, Reverse PFMEA может **использовать Audit / Assessment / Verification как механизмы**, но не тождественен им.

---

# 5. Important distinction: Risk Reduction vs Problem Solving

Не создавать отдельную Machine только для Risk Reduction.

`Problem Solving` отвечает на вопрос:

> почему возникла проблема и какое corrective action необходимо?

`Risk Reduction` отвечает на вопрос:

> где риск ещё слишком велик и какие изменения должны снизить его до приемлемого/целевого уровня?

В GM они связаны, но не идентичны: reactive RPN reduction использует corrective actions/error proofing уже после quality issue; proactive reduction использует Reverse PFMEA для обнаружения gaps до повторного failure.

---

# 6. Deep architectural distinction

В стратегии обнаруживается цикл обратной связи:

```text
MODEL
  ↓
FIELD
  ↓
OBSERVATION / VERIFICATION
  ↓
GAP / NEW FAILURE MODE
  ↓
ACTION
  ↓
VERIFY
  ↓
REASSESS
  ↓
MODEL UPDATE
```

Рабочая гипотеза:

> Risk Reduction содержит не просто «снижение RPN», а механизм согласования **модели риска с фактическим состоянием процесса**.

Это может оказаться более фундаментальным для CMOC, чем сам термин RPN.

---

# 7. CMOC candidate structures

На этом этапе выделяются следующие потенциальные конструкции для дальнейшей проверки:

### A. Risk Model Feedback Loop

`MODEL → FIELD EVIDENCE → GAP → ACTION → VERIFY → REASSESS → MODEL UPDATE`

**Working status:** PATTERN / ASSEMBLY CANDIDATE — HOLD.

### B. Reverse PFMEA

`SCHEDULE → CROSS-FUNCTIONAL REVIEW → VERIFY CONTROLS → DISCOVER NEW FAILURE MODES → ACTION PLAN`

**Working status:** MACHINE CANDIDATE / SINGLE-SOURCE.

### C. Risk Reduction Opportunity Management

`IDENTIFY HIGH RISK → ASSIGN ACTION → TRACK → REASSESS RPN`

**Working status:** ASSEMBLY / CONTROL LOOP — HOLD.

### D. Station Experiment for Failure Mode Discovery

`HYPOTHESIZED FAILURE MODE → CONTROLLED STRESS / WRONG CONDITION → OBSERVE RESULT → RECORD`

**Working status:** DISCOVERY MECHANISM — HOLD.

---

# 8. No catalog / canon changes yet

На данном этапе:

- новые Machine в `MACHINE-CATALOG.md` **не добавлять**;
- новый Pattern в каталог **не добавлять**;
- REG-001 **не менять**;
- Canon **не менять**.

Причина: это первый cross-check одной стратегии одного источника.

---

# 9. Next verification step

Следующий этап — провести independent cross-check для:

1. **Reverse PFMEA** — проверить, является ли конструкция воспроизводимой специализированной Machine вне данного GM-документа.
2. **Risk Model Feedback Loop** — проверить, существует ли более общий Pattern за пределами PFMEA/RPN.
3. **Failure Mode Discovery by controlled station experiment** — проверить, является ли это самостоятельным механизмом или частью broader Verification/Experiment mechanism.

До этого момента все три конструкции остаются NON-CANON.

---

## Source evidence

GM explicitly defines Reverse PFMEA as an on-station review of PFMEA failure modes by a cross-functional team to verify proper prevention/detection controls and their effectiveness; its purpose includes PFMEA review, RPN reduction, discovery of previously unconsidered Failure Modes, and validation of Occurrence/Detection using real data. The process also specifies teams, audit schedule, common criteria, station experiments for new failure modes, and action plans. The flow diagram operationalizes these steps. fileciteturn90file0L36-L46 fileciteturn90file0L49-L72 fileciteturn90file1L112-L147

GM's RPN reduction example tracks recommended action, completion date, responsible person and revised RPN, while the management section assigns leadership responsibility for resources, monitoring and cross-functional PFMEA review. fileciteturn90file0L10-L29 fileciteturn90file9L912-L918

# GM-096 — Systemic Problem Resolution: CMOC Cross-Check

**Source:** GM Quality Systems Basics rev. March 2009
**Candidate:** Systemic Problem Resolution
**Status:** HOLD / EXISTING GM PROBLEM-SOLVING ARCHITECTURE

## 1. Decision

**Do not create a new Machine for Systemic Problem Resolution at this stage.**

The current GM-derived CMOC material already contains a dedicated Problem Solving architecture in earlier patches. The later GM-096 candidate is therefore treated as a **confirmation / enrichment of an existing architecture**, not as a new machine.

## 2. Existing GM architecture found

The repository already contains:

- `GM-008-Problem-Solving-Description-Fundamentals.md` — Problem Solving fundamentals and the distinction between problem identification, situation grasp and cause analysis;
- `GM-009-Define-the-Problem.md` — Step 1, Definition through Standard, Actual / Gap and Time Period;
- `GM-011-Point-of-Cause.md` — Go-See / Point of Cause and upstream investigation;
- `GM-012-7-Diamonds-Root-Cause.md` — initial root-cause diagnostic branch and Diamonds 1–4;
- `GM-013-5-Why-Root-Cause.md` — causal deepening toward real root cause.

The source-derived chain already established by these patches is:

`Problem → Definition → Containment → Point of Cause → Diagnostic Screening → Cause Analysis → Root Cause`

with further downstream work leading to corrective action and prevention of recurrence.

## 3. Why GM-096 does not justify a new Machine

The GM-096 Supply Chain / quality strategy material identifies systemic problem resolution as an operational expectation, including investigation of why planning, process and controls allowed a problem to occur.

That function is already represented by the existing Problem Solving family. Creating a second Machine called `Systemic Problem Resolution` would duplicate the same causal-investigation architecture at a different level of wording.

The stronger CMOC relationship is:

`GM-096 Systemic Problem Resolution → confirms / enriches → existing CMOC Problem Solving architecture`

rather than:

`GM-096 Systemic Problem Resolution → new Machine`.

## 4. Existing architecture is already decomposed

The existing GM patches preserve useful boundaries:

### Problem Definition

Defines the discrepancy before cause analysis. GM-009 explicitly separates Problem Description from Problem Definition and defines Standard, Actual / Gap and Time Period.

### Point-of-Cause Investigation

GM-011 distinguishes where a problem is found from where it occurs and requires first-hand observation / upstream investigation when indicated.

### Diagnostic Screening

GM-012 uses Diamonds 1–4 before deeper analysis and branches to 5-Why when a NO condition is found.

### Causal Deepening

GM-013 treats 5-Why as a cause-investigation mechanism and explicitly avoids reducing it to a universal “five questions” rule.

These are already independent mechanisms / machine candidates. A broad `Systemic Problem Resolution` Machine would overlap all of them.

## 5. Relation to earlier CMOC material

The user's earlier organizational architecture also contains a distinct **Контур удержания**:

`Несоответствие → Анализ причин → Решение → Изменение системы → Контроль повторяемости`

and assigns system-level decision responsibility to ПДКК. This material is present in the earlier working corpus and should not be replaced by the GM terminology.

The relevant source-derived distinction is therefore:

> **GM's Systemic Problem Resolution is evidence for, and an industrial realization of, an already emerging CMOC удержание / problem-solving architecture.**

It is not evidence that a new top-level Machine must be created.

## 6. What GM-096 adds

GM-096 adds an important emphasis to the existing architecture:

`Observed Problem → Technical Cause → Process Cause → Control-System / Planning Cause`

It reinforces the need to ask why the existing planning and control system permitted the problem, not merely why the immediate defect occurred.

This should be recorded as **additional provenance and strengthening evidence** for the existing Problem Solving / Systemic Cause architecture.

## 7. Machine decision

| Candidate | Decision | Reason |
|---|---|---|
| Systemic Problem Resolution | **HOLD / NO NEW MACHINE** | overlaps existing GM Problem Solving family |
| Problem Definition | existing candidate | GM-009 |
| Point-of-Cause Investigation | existing candidate | GM-011 |
| 7 Diamond Diagnostic Process | existing candidate | GM-012 |
| 5-Why Causal Deepening | existing candidate | GM-013 |
| System-level corrective action / recurrence prevention | **future cross-source analysis** | needs explicit relationship to CMOC удержание / ПДКК |

## 8. Canonization consequence

No new Machine is proposed from the GM-096 `Systemic Problem Resolution` candidate.

Instead, future Canonization should consider an evidence relation:

`GM QSB 2009 → supports → Problem Solving / Systemic Cause / Recurrence Prevention`

The exact target Canon objects are not selected here.

## 9. Status

**HOLD / EXISTING ARCHITECTURE CONFIRMATION**

No REG-001 modification.
No new Machine.
No Canon modification.

**Next candidate in the GM-096 Machine-Candidate sequence:** Workshop / Action-Plan Conversion, after the remaining Tier B candidates are screened as needed.

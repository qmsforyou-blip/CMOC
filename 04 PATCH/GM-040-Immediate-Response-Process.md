# GM-040 — Immediate Response Process

**Извещение на изменение:** 0151+280826  
**Источник:** GM Quality System Basics rev. March 2009  
**Раздел:** 3.3 — Defects Entering the Station / Immediate Response, pp. 92–94  
**Статус:** CANDIDATE / SINGLE-SOURCE

## 1. SOURCE

GM показывает пример **Immediate Response Process** с двумя частями документа.

### VS Operator / Inspector Section

Когда срабатывает Alarm, оператор Verification Station должен:

1. предпринять **immediate action**;
2. **call for help**;
3. заполнить левую часть Immediate Response Document.

Повторные Alarm отмечаются по уровню эскалации; вызывается responder следующего уровня. fileciteturn107file0

### Responder's Section

Responder немедленно начинает Problem Solving и документирует результаты. SOURCE перечисляет:

- Containment;
- Immediate fix — sort, repair, scrap;
- Point of Cause;
- Root Cause;
- Corrective Action;
- определение, связана ли проблема с процессом или с поставщиком. fileciteturn107file10

SOURCE также определяет **Break Point** как точку, после которой все последующие детали известны как good вследствие containment и/или corrective action. Для Break Point должны быть зафиксированы **time and location**, а first good part должна быть идентифицирована, чтобы Verification Station знала, когда Break Point пройден. fileciteturn107file4

## 2. LOCATION

**pp. 92–94 — Immediate Response Process.**

## 3. TERMS — ТЕРМИНЫ

| English | Русский |
|---|---|
| **Immediate Response Process** | процесс непосредственной реакции |
| **VS Operator / Inspector** | оператор / инспектор Verification Station |
| **Immediate Action** | непосредственное действие |
| **Call for Help** | обращение за помощью |
| **Immediate Response Document** | документ непосредственной реакции |
| **Repeat Alarm** | повторный Alarm |
| **Escalation Level** | уровень эскалации |
| **Responder** | реагирующий / ответственный участник реакции |
| **Problem Solving** | решение проблемы |
| **Containment** | локализация / удержание под контролем |
| **Immediate Fix** | немедленное исправление |
| **Sort** | сортировка |
| **Repair** | ремонт |
| **Scrap** | списание / брак |
| **Point of Cause** | точка возникновения причины |
| **Root Cause** | коренная причина |
| **Corrective Action** | корректирующее действие |
| **Process Related** | связанный с процессом |
| **Supplier Issue** | проблема поставщика |
| **Break Point** | точка, после которой последующие детали считаются good |
| **Time and Location** | время и место |
| **First Good Part** | первая годная деталь |

## 4. DISTINCTIONS — РАЗЛИЧЕНИЯ

### 4.1 Alarm ≠ Immediate Action

Alarm — сигнал. Immediate Action — действие оператора после сигнала.

### 4.2 Call for Help ≠ Escalation Level

Call for Help запускает обращение за поддержкой. При повторном Alarm фиксируется escalation level и вызывается responder следующего уровня.

### 4.3 Operator Response ≠ Responder Problem Solving

Оператор выполняет immediate action, вызывает помощь и документирует свою часть. Responder начинает Problem Solving и документирует результаты.

### 4.4 Immediate Fix ≠ Corrective Action

SOURCE перечисляет их раздельно. Immediate fix включает sort, repair, scrap; Corrective Action относится к последующему решению причины.

### 4.5 Containment ≠ Break Point

Containment — действие по локализации. Break Point — установленная точка, после которой последующие детали известны как good вследствие containment и/или corrective action.

### 4.6 Break Point ≠ просто дата/время

Для Break Point SOURCE требует фиксировать time and location и идентифицировать first good part. Поэтому это не просто отметка времени.

## 5. GM-FORMULATIONS — ФОРМУЛИРОВКИ GM

> **When an alarm is triggered, the verification station operator shall take immediate action & call for help, then fills in the left side of the immediate response document.**

> **Repeat alarms are noted by the escalation level. The next level responder is called.**

> **The responder begins the problem solving process immediately and shall document the results.**

> **Containment, Immediate fix (sort, repair, scrap)**

> **Point of Cause, Root Cause, Corrective Action**

> **The Break Point is the point at which all subsequent parts are known to be good due to containment and/or corrective action having taken place.**

## 6. EXTRACTION — ИЗВЛЕЧЕНИЕ

### Operator loop

```text
ALARM TRIGGERED
      ↓
IMMEDIATE ACTION
      ↓
CALL FOR HELP
      ↓
FILL OPERATOR SECTION
      ↓
REPEAT ALARM?
      ↓
NOTE ESCALATION LEVEL
      ↓
CALL NEXT LEVEL RESPONDER
```

### Responder loop

```text
RESPONDER CALLED
      ↓
IMMEDIATE PROBLEM SOLVING
      ↓
CONTAINMENT / IMMEDIATE FIX
      ↓
POINT OF CAUSE / ROOT CAUSE
      ↓
CORRECTIVE ACTION
      ↓
DOCUMENT RESULTS
```

### Break Point

```text
CONTAINMENT / CORRECTIVE ACTION
            ↓
      FIRST GOOD PART
            ↓
       TIME + LOCATION
            ↓
        BREAK POINT
            ↓
SUBSEQUENT PARTS KNOWN GOOD
```

## 7. REL — ОТНОШЕНИЯ

```text
Alarm
→ Immediate Action
→ Call for Help
→ Immediate Response Document
```

```text
Repeat Alarm
→ Escalation Level
→ Next Level Responder
```

```text
Responder
→ Problem Solving
→ Containment / Immediate Fix
→ Root Cause / Corrective Action
→ Document Results
```

```text
Containment / Corrective Action
→ First Good Part
→ Time + Location
→ Break Point
→ Subsequent Parts Known Good
```

## 8. MECHANISM — МЕХАНИЗМ

### CANDIDATE — Immediate Response Mechanism

**Input:** сработавший Alarm.

**Transformation:** immediate action оператора → call for help → фиксация реакции → вызов responder соответствующего уровня; responder запускает Problem Solving и документирует результат.

**Output:** локализованная проблема, выполненная немедленная реакция и документированный результат; при достижении Break Point появляется установленная граница после которой последующие детали известны как good.

**Организационный эффект:** Alarm переводится в конкретную, документируемую и эскалируемую реакцию.

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 9. CAPABILITY — СПОСОБНОСТЬ

### CANDIDATE — Управляемая непосредственная реакция

Способность организации обеспечивать немедленное действие после Alarm, своевременно подключать responder нужного уровня, документировать реакцию и доводить её до локализации / исправления и установленного Break Point.

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 10. CORE CANDIDATE

> **Immediate Response Process — воспроизводимая организационная конструкция, связывающая Alarm с немедленным действием оператора, обращением за помощью, документированием, подключением responder соответствующего уровня и последующим Problem Solving до локализации/исправления и установления Break Point.**

**CANDIDATE / SINGLE-SOURCE**

## 11. MACHINE — МАШИНКА

### CANDIDATE MACHINE — Immediate Response Machine

```text
INPUT
Alarm
  ↓
[ IMMEDIATE ACTION ]
  ↓
[ CALL FOR HELP ]
  ↓
[ DOCUMENT ]
  ↓
RESPONDER
  ↓
[ CONTAIN / IMMEDIATE FIX ]
  ↓
[ PROBLEM SOLVING ]
  ↓
[ CORRECTIVE ACTION ]
  ↓
BREAK POINT
  ↓
SUBSEQUENT PARTS KNOWN GOOD
```

Инженерный тест:

- **INPUT:** Alarm;
- **OPERATION:** immediate response + routing + documented problem solving;
- **OUTPUT:** controlled condition / Break Point;
- **ORGANIZATIONAL EFFECT:** переход от сигнала к локализованному и документированному результату.

**MACHINE = CANDIDATE / SINGLE-SOURCE**

При этом не утверждаем, что весь документ является одной физической машиной: SOURCE описывает составную организационную конструкцию.

## 12. CHAIN — ЦЕПОЧКИ

### Operator response

```text
Alarm
→ Immediate Action
→ Call for Help
→ Document
→ Next Level Responder if repeat
```

### Responder response

```text
Responder
→ Problem Solving
→ Containment / Immediate Fix
→ Point of Cause / Root Cause
→ Corrective Action
→ Document Results
```

### Break Point

```text
Containment / Corrective Action
→ First Good Part
→ Time + Location
→ Break Point
→ Subsequent Parts Known Good
```

## 13. STATUS

**CANDIDATE / SINGLE-SOURCE**

CANON не присваивается.

## 14. CMOC INTERPRETATION

GM-040 делает особенно явным различение:

> **Signal → Response → Evidence → State Change**

Alarm сам по себе ничего не исправляет. Immediate Response Process задаёт маршрут, роли и фиксацию результата.

Особенно сильная конструкция — **Break Point**. Это не просто запись о том, что проблема устранена. SOURCE требует доказуемо определить границу, после которой последующие детали известны как good, с фиксацией времени, места и first good part.

Поэтому потенциальная CMOC-конструкция:

```text
DEVIATION
 ↓
SIGNAL
 ↓
ACTION
 ↓
CONTAINMENT / CORRECTION
 ↓
EVIDENCE
 ↓
BREAK POINT
 ↓
KNOWN GOOD STATE
```

Это CMOC INTERPRETATION, а не утверждение, что GM использует именно такую онтологическую схему.

## 15. ГРАНИЦА С GM-038 / GM-039

**GM-038:** Alarm → Support Function → Escalation → Problem Solving.

**GM-039:** несколько Alarm Levels → изменение уровня реакции.

**GM-040:** конкретизирует, **что именно делает участник реакции после Alarm**, как фиксируется действие и как определяется Break Point.

```text
GM-037
Threshold → Alarm

GM-038
Alarm → Response / Escalation

GM-039
Alarm Level → Response Level

GM-040
Response Level → Action → Evidence → Break Point
```

## 16. FIXATION

PATCH зарегистрирован непосредственно в GitHub.

CORE, каталоги, LAB и предыдущие PATCH не изменялись.

# GM-012 — Step 3: 7 Diamonds / Root Cause

## Извещение на изменение

**0123+280826**

---

## 0. SOURCE

**Источник:** GM Quality System Basics Overview Supplier Audit.pdf  
**Версия:** Quality Systems Basics rev March 2009  
**Раздел:** FAST RESPONSE → 1.3 Problem Solving → Step 3 — Identify the Root Cause  
**Основной фрагмент:** pp. 32–38.

---

## 1. LOCATION

- p. 32 — GM представляет 7 Diamond process как initial root cause step и immediate reaction to internal Quality issues.
- p. 33 — Diamonds 1–4: проверка, работает ли manufacturing process to design intent; initial investigation at defect location; при upstream indication — investigation upstream; Statistical Engineering — если process meets design intent, но problem persists.
- pp. 34–37 — содержание четырёх явно показанных проверок: Correct Process, Correct Tool, Correct Part, Parts Quality.
- p. 38 — для каждого NO response в Diamonds 1–4 выполняется 5-Why analysis; при найденной причине Why продолжается до real root cause.

Источник прямо называет конструкцию **7 diamond process**, но в доступном фрагменте явно раскрывает Diamonds 1–4 и далее правило перехода к 5-Why. Поэтому отсутствующее содержание Diamonds 5–7 не додумывается.

---

## 2. TERMS

- 7 Diamond process
- Diamonds 1–4
- Root Cause
- Initial Root Cause Step
- Immediate Reaction
- Internal Quality Issues
- Design Intent
- Process Stability
- Out of Standard Condition
- Special Cause
- Point of Cause
- Upstream Source
- Statistical Engineering
- Correct Process
- Correct Tool
- Correct Part
- Parts Quality
- 5-Why
- Real Root Cause

---

## 3. DISTINCTIONS

### DIS-GM-012-01

**Initial Root Cause Step ≠ complete root-cause analysis.**

GM calls the 7 Diamond process an initial root cause step. It is an immediate reaction to internal Quality issues.

### DIS-GM-012-02

**Diamonds 1–4 ≠ statistical problem solving.**

Their purpose is to quickly determine whether an out-of-standard condition / special cause exists and thereby prevent excessive use of statistical problem-solving techniques.

### DIS-GM-012-03

**Point of Cause ≠ Root Cause.**

Initial investigation is performed where the defect was found. If the cause appears upstream, investigation moves upstream. This locates the causal area before deeper root-cause analysis.

### DIS-GM-012-04

**Process stability / design intent ≠ root cause.**

Diamonds 1–4 test whether the manufacturing process is running to design intent. A negative finding directs the investigation; it is not itself automatically the final root cause.

### DIS-GM-012-05

**NO in Diamonds 1–4 → 5-Why.**

GM explicitly states that for each NO response in Diamonds 1–4, a 5-Why analysis is performed.

### DIS-GM-012-06

**Cause found ≠ real root cause.**

When a cause is found, GM requires asking Why until the real root cause is found.

### DIS-GM-012-07

**Manufacturing cause paths are separated.**

The four explicitly shown checks address Process, Tool, Part and Parts Quality, with different responsible areas and different verification questions.

---

## 4. GM-FORMULATIONS

> “As an initial root cause step, General Motors uses the 7 diamond process as an immediate reaction to internal Quality issues.”

> “The first 4 steps are used to quickly determine if an out of standard condition (special cause) exists.”

> “Diamonds 1-4 evaluate the stability of the process.”

> “Once a problem has been identified, the automatic response should be to immediately perform diamonds 1-4.”

> “Initial investigation is done where the defect was found.”

> “If investigation determines the cause of the problem is upstream, then investigation should be conducted at the upstream source as well.”

> “Statistical Engineering occurs when the manufacturing process does meet design intent and the problem still exists.”

> “For each NO response in Diamonds 1-4, a 5-Why analysis is performed.”

> “When a cause is found, ask why until you find the real root cause (5 Why’s).”

Все приведённые формулировки — **SOURCE CLAIMS**.

---

## 5. EXTRACTION

GM задаёт ветвящийся диагностический контур:

```text
INTERNAL QUALITY ISSUE
        ↓
   7 DIAMOND PROCESS
        ↓
   DIAMONDS 1–4
        ↓
┌───────────────┬───────────────┬───────────────┬───────────────┐
│ ♦1            │ ♦2            │ ♦3            │ ♦4            │
│ Correct       │ Correct       │ Correct       │ Parts         │
│ Process?      │ Tool?         │ Part?         │ Quality?      │
└───────────────┴───────────────┴───────────────┴───────────────┘
        ↓
     NO response
        ↓
     5-WHY
        ↓
     WHY / WHY / WHY
        ↓
  REAL ROOT CAUSE
```

Отдельная ветвь:

```text
Diamonds 1–4
      ↓
process meets design intent
      +
problem still exists
      ↓
Statistical Engineering
```

---

## 6. CONTENT OF THE FOUR EXPLICIT DIAMONDS

### Diamond 1 — Correct Process?

GM проверяет, в частности:

- correct Standardized Work posted;
- Standardized Work followed;
- build documents adhered to, where applicable;
- gaging requirements / frequencies followed;
- same job performed across shifts;
- operator understands product standards;
- regular operator / turnover;
- proper training;
- current visual aids;
- understanding of quality outcomes;
- ability to communicate a problem.

Источник связывает эту проверку с Manufacturing.

### Diamond 2 — Correct Tool?

GM проверяет:

- correct tools and fixtures;
- specified tool settings;
- calibration;
- same tool across shifts;
- tool wear;
- mutilation protection;
- workstation error proofing;
- bypassing tools / error proofing;
- workstation layout;
- preventive maintenance;
- correct tool functioning.

### Diamond 3 — Correct Part?

GM проверяет:

- current routing;
- correct parts being used;
- correct stocking location;
- agreement between box part numbers and location;
- need for error proofing;
- correct operation of existing error-proofing device.

### Diamond 4 — Parts Quality?

Quality Systems проверяет, изменились ли parts и соответствует ли overall part quality, используя:

- Supplier Data;
- CMM Checks;
- Fixture Checks;
- Visual Part to Part;
- Visual Lot to Lot.

Если part quality (out of specification) определяется как root cause, Quality Systems уведомляет Manufacturing и/или Supplier и работает с ними для validation of corrections.

---

## 7. NOMENCLATURE

Предварительные кандидаты:

- 7 Diamond Process
- Diamond 1 — Correct Process
- Diamond 2 — Correct Tool
- Diamond 3 — Correct Part
- Diamond 4 — Parts Quality
- 5-Why Analysis
- Root Cause
- Real Root Cause
- Design Intent
- Special Cause
- Statistical Engineering

Не превращаем автоматически названия Diamonds в отдельные CMOC Entities.

---

## 8. CLASSIFICATION

```text
PROBLEM SOLVING
└── STEP 3 — IDENTIFY THE ROOT CAUSE
    │
    ├── 7 Diamond Process
    │   ├── ♦1 Correct Process
    │   ├── ♦2 Correct Tool
    │   ├── ♦3 Correct Part
    │   └── ♦4 Parts Quality
    │
    ├── NO response
    │   └── 5-Why Analysis
    │       └── Real Root Cause
    │
    └── Process meets design intent + problem persists
        └── Statistical Engineering
```

Это классификация материала SOURCE, не каноническая CMOC-классификация.

---

## 9. PASSPORT

### Candidate — 7 Diamond Diagnostic Process

**Type:** CANDIDATE / SINGLE-SOURCE  
**Role:** initial root-cause step / immediate reaction to internal Quality issues.  
**Explicitly supported scope:** Diamonds 1–4 + transition to 5-Why / Statistical Engineering.

### Candidate — 5-Why Analysis

**Type:** CANDIDATE / SINGLE-SOURCE  
**Role:** for each NO response in Diamonds 1–4, pursue Why until real root cause.

---

## 10. RELATIONS

SOURCE-supported:

```text
Internal Quality Issue
      ↓
Diamonds 1–4
      ↓
NO
      ↓
5-Why
      ↓
Real Root Cause
```

Alternative branch:

```text
Diamonds 1–4
      ↓
Process meets Design Intent
      +
Problem persists
      ↓
Statistical Engineering
```

Location relation:

```text
Defect found
      ↓
Initial investigation
      ↓
If upstream cause indicated
      ↓
Upstream investigation
```

---

## 11. MECHANISM

### CANDIDATE — Diagnostic Branching Mechanism

**INPUT:** identified internal Quality issue.

**TRANSFORMATION:** execute immediate Diamonds 1–4 checks against process / tool / part / parts quality.

**BRANCH:**

- NO → 5-Why analysis;
- process meets design intent but problem persists → Statistical Engineering.

**OUTPUT:** directed path for further investigation rather than undifferentiated use of problem-solving methods.

**STATUS:** CANDIDATE / SINGLE-SOURCE.

---

## 12. MACHINE

### CANDIDATE MACHINE — 7 Diamond Diagnostic Process

```text
INPUT
Internal Quality Issue
        ↓
DIAGNOSTIC OPERATION
Correct Process?
Correct Tool?
Correct Part?
Parts Quality?
        ↓
DECISION
├── NO
│    ↓
│  5-Why
│    ↓
│  Real Root Cause
│
└── Design Intent confirmed
     + Problem persists
     ↓
  Statistical Engineering
```

Почему это сильный кандидат на Machine:

1. есть определённый вход — internal Quality issue;
2. есть заданная воспроизводимая операция проверки;
3. есть стандартизированные ветви дальнейшего действия;
4. есть различимый выход — выбран следующий способ анализа.

При этом не утверждается, что весь 7 Diamond Process является единственной машиной. Внутри него могут быть отдельные диагностические машины.

### CANDIDATE MACHINE — 5-Why

```text
Suspected Cause
      ↓
WHY?
      ↓
WHY?
      ↓
WHY?
      ↓
...
      ↓
Real Root Cause
```

Источник прямо задаёт повторение Why до real root cause.

**STATUS: CANDIDATE / SINGLE-SOURCE**.

---

## 13. CAPABILITY

**NONE**.

В этом фрагменте GM описывает диагностические действия и пути анализа, но не формулирует самостоятельную организационную Capability.

---

## 14. CORE CANDIDATE

> **7 Diamond Diagnostic Process — воспроизводимая первичная диагностика внутренней Quality issue, которая проверяет соответствие процесса, инструмента, детали и качества детали design intent и направляет дальнейший анализ по результату проверки.**

**STATUS: CANDIDATE / SINGLE-SOURCE**

### Дополнительный кандидат

> **5-Why Analysis — последовательное углубление причинного вопроса Why после отрицательного результата диагностической проверки до выявления real root cause.**

**STATUS: CANDIDATE / SINGLE-SOURCE**

---

## 15. CHAIN

### SOURCE-SUPPORTED

```text
Internal Quality Issue
 → Diamonds 1–4
 → NO response
 → 5-Why
 → Real Root Cause
```

### Alternative SOURCE-supported branch

```text
Internal Quality Issue
 → Diamonds 1–4
 → Process meets Design Intent
 → Problem persists
 → Statistical Engineering
```

### Investigation-location branch

```text
Defect found
 → Initial investigation
 → Upstream indication
 → Upstream investigation
```

---

## 16. STATUS

**CANDIDATE / SINGLE-SOURCE**

### CONFIRM / UPDATE

**UPDATE GM-011:** GM-011 выделил Point of Cause и Go-See как локализацию места возникновения. GM-012 показывает, что после локализации GM запускает стандартизированный набор первичных проверок — Diamonds 1–4 — а затем ветвит дальнейший анализ.

**UPDATE GM-008:** общий принцип Cause / Effect и поиска Root Cause получает конкретную операционную реализацию через Diamonds 1–4 и 5-Why.

Никакого CANON.

---

## 17. CMOC INTERPRETATION

Главная добыча:

> **GM не начинает поиск Root Cause с произвольного выбора инструмента. Сначала выполняется стандартизированная диагностическая развилка, которая проверяет несколько конкретных условий производственной реальности. Только результат этой проверки определяет следующий способ анализа.**

Это даёт важное различение:

```text
PROBLEM
   ↓
DIAGNOSIS
   ↓
PATH SELECTION
   ↓
CAUSE ANALYSIS
```

А не:

```text
PROBLEM
   ↓
«Давайте применим 5 Why»
```

И ещё одно сильное различение для CMOC:

> **5-Why в GM не является универсальной стартовой машиной. В SOURCE она запускается как реакция на NO в Diamonds 1–4.**

Это существенно ограничивает нашу интерпретацию и делает её инженерно полезнее.

---

## 18. SOURCE BOUNDARY NOTE

Название раздела — **7 Diamond Process**, но в доступном SOURCE явно раскрыты только Diamonds 1–4 и последующее правило 5-Why. Содержание Diamonds 5–7 в этой вагонетке **не реконструируется по предположению**.

Это принципиальное правило добычи: отсутствие данных в текущем фрагменте не заменяется моделью из памяти или внешним знанием.

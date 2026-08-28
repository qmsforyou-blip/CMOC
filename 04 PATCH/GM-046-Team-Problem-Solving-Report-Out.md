# GM-046 — Team Problem Solving Report Out

**Извещение на изменение:** 0157+280826  
**Источник:** GM Quality System Basics rev. March 2009  
**Раздел:** 3.5 — Problem Solving / Verification Station  
**Статус:** CANDIDATE / SINGLE-SOURCE

## 1. SOURCE

GM устанавливает еженедельный Team Problem Solving Report Out в рамках Verification Station report out. Команда обучена и использует стандартную внутреннюю форму Problem Solving для еженедельного отчёта. На Report Out участник команды сообщает текущее состояние по выполняемому шагу Problem Solving.

Руководство должно:

- определить, когда проблема требует эскалации на следующий уровень Problem Solving, например с применением statistical techniques;
- поддерживать Problem Solving команды на основе данных VS;
- рассматривать Pareto дефектов;
- назначать проблемы команде под руководством Team Lead / Supervisor;
- обеспечить отслеживание проблем и еженедельный Review их статуса.

На ежедневном/еженедельном Review дополнительно проверяются roadblocks, необходимость дополнительных ресурсов, актуальность Tracking Report и необходимость эскалации Problem Solving Assignment. fileciteturn124file1turn124file3

## 2. LOCATION

**p. 101 — 3.5 Problem Solving / Verification Station.**

Связанный контур Review также показан на p. 95 в структуре Leadership Support. fileciteturn124file3

## 3. TERMS — ТЕРМИНЫ

| English | Русский |
|---|---|
| **Team Problem Solving Report Out** | отчёт команды по решению проблемы |
| **Report Out** | представление текущего состояния / отчёт |
| **Standard Internal Problem Solving Form** | стандартная внутренняя форма Problem Solving |
| **Current Problem Solving Step** | текущий шаг решения проблемы |
| **Problem Solving Team** | команда решения проблемы |
| **Problem Status** | статус проблемы |
| **Tracking Report** | отчёт отслеживания |
| **Weekly Review** | еженедельный обзор |
| **Roadblock** | препятствие / блокирующий фактор |
| **Resource** | ресурс |
| **Pareto of Defects** | Парето дефектов |
| **Top Defects** | наиболее значимые дефекты |
| **Assign a Problem** | назначить проблему для работы |
| **Team Lead / Supervisor** | лидер команды / руководитель |
| **Escalation** | эскалация |
| **Statistical Techniques** | статистические методы |
| **VS Data** | данные Verification Station |
| **Problem Solving Assignment** | назначение по решению проблемы |

## 4. DISTINCTIONS — РАЗЛИЧЕНИЯ

### 4.1 Report Out ≠ Problem Solving

Report Out не является самим процессом решения проблемы. Это регулярная точка представления текущего состояния работы команды.

### 4.2 Report Out ≠ просто отчёт

SOURCE связывает Report Out с текущим Problem Solving Step, Review статуса, Roadblocks, ресурсами и возможной эскалацией.

### 4.3 Problem Status ≠ Problem Solving Result

На Report Out представляется **текущее состояние** работы. Наличие статуса не означает завершения Problem Solving.

### 4.4 Tracking Report ≠ Report Out

Tracking Report удерживает состояние назначения/проблемы; Report Out — регулярное представление этого состояния.

### 4.5 Pareto ≠ Assignment

Pareto используется для обсуждения и выбора проблем, а Assignment определяет, кому проблема назначена для работы.

### 4.6 Escalation ≠ failure

SOURCE предусматривает эскалацию на следующий уровень Problem Solving, например к statistical techniques. Эскалация является предусмотренной частью системы, а не обязательно признаком провала.

## 5. GM-FORMULATIONS — ФОРМУЛИРОВКИ GM

> **The Team is trained and uses the standard internal problem solving form to report out weekly during the Verification Station report out.**

> **Leadership should identify when problems need to be escalated to the next level of problem solving such as statistical techniques.**

> **Leadership shall support problem solving by the Team based on VS data.**

> **The pareto of defects is discussed and problems assigned to the team led by the Team Lead/Supervisor.**

> **Problems shall be tracked and the status reviewed weekly.** fileciteturn124file1

## 6. EXTRACTION — ИЗВЛЕЧЕНИЕ

```text
VS DATA
   ↓
PARETO OF DEFECTS
   ↓
SELECT / ASSIGN PROBLEM
   ↓
TEAM PROBLEM SOLVING
   ↓
CURRENT STEP
   ↓
WEEKLY REPORT OUT
   ↓
STATUS REVIEW
   ↓
ROADBLOCKS / RESOURCES / ESCALATION
   ↓
NEXT PROBLEM SOLVING STEP
```

Отдельно SOURCE задаёт эскалацию:

```text
PROBLEM
  ↓
CURRENT PROBLEM SOLVING LEVEL
  ↓
LEADERSHIP REVIEW
  ↓
NEED FOR HIGHER-LEVEL METHOD?
  ↓
STATISTICAL TECHNIQUES / NEXT LEVEL
```

## 7. REL — ОТНОШЕНИЯ

```text
VS Data
→ Pareto of Defects
→ Problem Selection / Assignment
```

```text
Assigned Problem
→ Team Problem Solving
→ Current Step
→ Weekly Report Out
```

```text
Report Out
→ Status Review
→ Roadblocks / Resources
→ Further Action / Escalation
```

```text
Problem Status
→ Weekly Review
```

## 8. MECHANISM — МЕХАНИЗМ

### CANDIDATE — Team Problem Solving Review Loop

**Input:** VS data + assigned problem + current Problem Solving status.

**Transformation:** регулярный Report Out → Review текущего шага → выявление roadblocks / resource needs → решение о дальнейшей работе или escalation.

**Output:** обновлённый статус и определённое продолжение Problem Solving.

**Организационный эффект:** работа команды над проблемой удерживается в регулярном управленческом цикле, а препятствия и потребность в ресурсах становятся предметом руководящего Review.

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 9. CAPABILITY — СПОСОБНОСТЬ

### CANDIDATE — Удержание командного Problem Solving в цикле Review

Способность организации регулярно предъявлять текущее состояние Problem Solving, выявлять препятствия и ресурсные ограничения и при необходимости эскалировать задачу на следующий уровень методов.

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 10. CORE CANDIDATE

> **Team Problem Solving Review Loop — воспроизводимая организационная конструкция, в которой команда регулярно представляет текущий шаг Problem Solving, статус рассматривается руководством, выявляются roadblocks и потребность в ресурсах, а при необходимости инициируется эскалация на следующий уровень решения проблемы.**

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 11. MACHINE — МАШИНКА

### CANDIDATE MACHINE — Team Problem Solving Review Machine

```text
INPUT
Assigned Problem + Current Status + VS Data
        ↓
[ WEEKLY REPORT OUT ]
        ↓
[ REVIEW CURRENT STEP ]
        ↓
ROADBLOCK / RESOURCE / ESCALATION NEED
        ↓
[ ASSIGN / SUPPORT / ESCALATE ]
        ↓
UPDATED STATUS
        ↓
NEXT REVIEW
```

Инженерный тест:

- **INPUT:** проблема, текущий статус, данные VS;
- **OPERATION:** Report Out + Review;
- **OUTPUT:** обновлённый статус / назначение / поддержка / escalation;
- **ORGANIZATIONAL EFFECT:** непрерывность работы команды над проблемой между циклами Review.

**MACHINE = CANDIDATE / SINGLE-SOURCE**

Важно: **standard internal problem solving form** сам по себе не объявляется машинкой. Он является средством стандартизации и предъявления состояния в данном механизме.

## 12. CHAIN — ЦЕПОЧКИ

### SOURCE-SUPPORTED

```text
VS Data
→ Pareto
→ Problem Assignment
→ Team Problem Solving
→ Weekly Report Out
→ Status Review
```

И:

```text
Report Out
→ Roadblocks / Resources
→ Support / Further Assignment
→ Escalation if Needed
```

## 13. STATUS

**CANDIDATE / SINGLE-SOURCE**

CANON не присваивается.

## 14. CMOC INTERPRETATION

GM-046 добавляет к GM-041/042 важную конструкцию:

```text
PROBLEM SOLVING
      ↓
CURRENT STATE
      ↓
REGULAR REVIEW
      ↓
BLOCKAGE / RESOURCE NEED
      ↓
MANAGEMENT ACTION
      ↓
NEXT STATE
```

То есть **Report Out — это не конечный отчёт**, а точка перехода между состояниями незавершённой работы.

В CMOC-оптике это потенциально можно рассматривать как механизм:

> **состояние работы → предъявление состояния → управленческая реакция → новое состояние работы.**

Это **CMOC INTERPRETATION**, а не терминология GM.

## 15. ГРАНИЦА С GM-041 И GM-042

**GM-041 — Leadership Support:** руководство рассматривает VS и Problem Solving, снимает roadblocks, назначает ресурсы и при необходимости эскалирует.

**GM-042 — Assignment Action Sheet:** назначение фиксируется и возвращается в следующий Review.

**GM-046 — Team Problem Solving Report Out:** команда регулярно предъявляет текущее состояние самой работы над проблемой.

```text
GM-041
REVIEW → SUPPORT / ASSIGN
        ↓
GM-042
CAPTURE → NEXT REVIEW
        ↓
GM-046
TEAM REPORT OUT → STATUS / ROADBLOCKS / ESCALATION
```

Это пока три связанных, но не объединённых в одну каноническую конструкцию механизма.

## 16. FIXATION

PATCH зарегистрирован непосредственно в GitHub.

CORE, каталоги, LAB и предыдущие PATCH не изменялись.

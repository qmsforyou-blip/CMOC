# GM-033 — Verification Station: Description, Roles & Responsibilities

**Извещение на изменение:** 0144+280826  
**SOURCE:** GM Quality System Basics rev. March 2009  
**Раздел SOURCE:** 3.2 — Description, Roles, Responsibility  
**Статус:** CANDIDATE / SINGLE-SOURCE

---

## 1. SOURCE

GM определяет Verification Station (VS) как систему **Building Quality in Station** через обратную связь от процесса.

Источник показывает следующие элементы конструкции:

- оператор VS проверяет каждую деталь по стандартизированному процессу контроля и передаёт обратную связь Team;
- 100% In-Line или End-of-Line testing может быть частью механизма feedback и через audio/visual signals сообщать Team о проблеме;
- используются fault codes и данные по повторяемости дефектов, например «3 in a row» или «5 in an hour», с целью развития alarm limit до «1»;
- применяются variable SPC charts и уведомление о выходе процесса из состояния statistical control;
- результаты и работа VS отслеживаются по внутренним метрикам;
- выявленные discrepancies предназначены для correction;
- данные VS направляют Team в Problem Solving при поддержке Leadership;
- проводится Management Process Verification;
- VS калибруется downstream data;
- VS работает full time и предотвращает прохождение quality discrepancies дальше по потоку посредством немедленного обнаружения и разрешения проблем. fileciteturn52file7

### Роли SOURCE

**Verification Station Operator**
- выполняет quality checks;
- реагирует на nonconformance;
- инициирует escalation при достижении alarm limits.

**Engineer, Supervisor, and Maintenance**
- поддерживают Verification Station Alarms для выявленных discrepancies.

**Plant Manager (Manufacturing Lead Person)**
- владеет Verification Station Process;
- развивает и продвигает Problem Solving и Error Proofing;
- ежедневно участвует в Verification Station Report Out;
- обеспечивает поддержку Team, чтобы процесс работал.

**Quality Manager**
- поддерживает ежедневную Verification Station meeting;
- поддерживает Problem Solving и follow-up. fileciteturn52file0

---

## 2. LOCATION

**pp. 79–81**, раздел **3.2 — Description, Roles, Responsibility**.

---

## 3. TERMS — ТЕРМИНЫ

| English | Русский |
|---|---|
| **Verification Station (VS)** | станция верификации / контрольная станция |
| **Building Quality in Station** | встраивание качества непосредственно в месте выполнения процесса |
| **Feedback** | обратная связь |
| **Standardized Work Inspection Process** | стандартизированный процесс проверки по стандартной работе |
| **100% In-Line Testing** | стопроцентный контроль непосредственно в процессе |
| **End-of-Line Testing** | контроль в конце процесса |
| **Audio/Visual Signals** | звуковые / визуальные сигналы |
| **Fault Code** | код неисправности / отклонения |
| **Alarm Limit** | порог срабатывания сигнала / тревоги |
| **Variable SPC Chart** | карта статистического управления по количественному параметру |
| **Out-of-Control Condition** | состояние статистической неуправляемости |
| **Discrepancy** | несоответствие / отклонение |
| **Correction** | исправление |
| **Problem Solving** | решение проблем |
| **Leadership Support** | поддержка руководства |
| **Management Process Verification** | проверка руководством функционирования процесса |
| **Downstream Data** | данные последующих стадий / downstream-потребителя |
| **Verification Station Operator** | оператор Verification Station |
| **Plant Manager** | руководитель предприятия / Plant Manager |
| **Quality Manager** | менеджер по качеству |
| **Engineer** | инженер |
| **Supervisor** | руководитель / супервайзер |
| **Maintenance** | служба технического обслуживания |
| **Escalation** | эскалация |
| **Error Proofing** | предотвращение ошибки / error proofing |
| **Report Out** | отчётное представление результатов |
| **Follow-up** | последующее сопровождение / контроль выполнения |

---

## 4. DISTINCTIONS — РАЗЛИЧЕНИЯ

### 4.1 Verification Station ≠ просто место контроля

SOURCE описывает VS как **process/system**, а не только физическую точку проверки. В неё входят стандартизированная проверка, feedback, alarm signals, data, response, Problem Solving и Leadership support.

### 4.2 Quality Check ≠ Reaction

Оператор выполняет quality checks и отдельно реагирует на nonconformance.

### 4.3 Reaction ≠ Escalation

Оператор реагирует на nonconformance; при достижении alarm limit инициируется отдельная escalation.

### 4.4 Alarm ≠ Problem Solving

Alarm сообщает о заданном состоянии/пороговом событии. SOURCE отдельно говорит, что данные VS направляют Team в Problem Solving.

### 4.5 Ownership ≠ Support

Plant Manager **owns the Verification Station Process**.
Engineer / Supervisor / Maintenance **support** alarms.
Quality Manager **supports** meeting, Problem Solving и follow-up.

### 4.6 Feedback ≠ Downstream calibration

VS получает feedback от процесса, но SOURCE отдельно указывает, что VS **calibrated by downstream data**. Не объединять эти понятия автоматически.

### 4.7 Management Process Verification ≠ Operator Check

Проверка оператором и проверка руководством — разные уровни контроля.

---

## 5. GM-FORMULATIONS — ФОРМУЛИРОВКИ SOURCE

Ключевые конструкции SOURCE:

- **“A Verification Station operator reviews each part using a standardized work inspection process and gives feedback to the Team.”**
- **“100% In-Line or End of Line testing”** может быть частью feedback mechanism.
- **“The use of variable SPC charts and notification for out-of-control conditions.”**
- **“Data Drives Teams in Problem Solving Process with Leadership Support.”**
- **“VS is calibrated by ‘downstream’ data.”**
- **“Functions Full Time.”**
- **“Prevents the flow of quality discrepancies beyond the VS by detecting and resolving issues immediately.”** fileciteturn52file7

---

## 6. EXTRACTION — ДОБЫЧА

SOURCE позволяет собрать такую конструкцию:

```text
PROCESS / PRODUCT
        ↓
STANDARDIZED INSPECTION
        ↓
CHECK EACH PART
        ↓
FEEDBACK TO TEAM
        ↓
ALARM / DATA / SPC
        ↓
RESPONSE TO DISCREPANCY
        ↓
ESCALATION AT ALARM LIMIT
        ↓
PROBLEM SOLVING
        ↓
LEADERSHIP SUPPORT
```

Параллельно действует организационная конструкция ответственности:

```text
OPERATOR
  → CHECK / REACT / ESCALATE

ENGINEER / SUPERVISOR / MAINTENANCE
  → SUPPORT ALARMS

PLANT MANAGER
  → OWNS PROCESS / SUPPORTS SYSTEM / DAILY REPORT OUT

QUALITY MANAGER
  → SUPPORTS MEETING / PROBLEM SOLVING / FOLLOW-UP
```

---

## 7. MECHANISM — МЕХАНИЗМ

### CANDIDATE — In-Station Verification and Reaction Mechanism

**Input:** деталь / результат процесса.

**Operation:** стандартизированная проверка непосредственно на VS, передача feedback Team, фиксация/сигнализация discrepancy, реакция и, при достижении alarm limit, escalation.

**Output:** выявленное и отреагированное отклонение либо подтверждённый результат процесса.

**Organizational effect:** отклонение обнаруживается и обрабатывается в месте процесса до дальнейшего прохождения по потоку.

**STATUS: CANDIDATE / SINGLE-SOURCE**

---

## 8. CAPABILITY — СПОСОБНОСТЬ

### CANDIDATE — In-Station Detection and Escalation

Способность организации обнаруживать отклонения непосредственно в процессе, обеспечивать немедленную реакцию и запускать escalation по заданному alarm limit.

**STATUS: CANDIDATE / SINGLE-SOURCE**

Это CMOC-интерпретация; SOURCE не формулирует capability как отдельный класс.

---

## 9. CORE CANDIDATE

> **Verification Station — воспроизводимая организационно-производственная конструкция, в которой стандартизированная проверка результата процесса связана с feedback Team, сигнализацией отклонений, реакцией оператора и escalation по заданному порогу, при распределённой поддержке и ownership руководства.**

**STATUS: CANDIDATE / SINGLE-SOURCE**

---

## 10. MACHINE — МАШИНКА

### CANDIDATE MACHINE — Verification Station Operational Loop

```text
INPUT
Деталь / результат процесса
        ↓
[ STANDARDIZED CHECK ]
        ↓
FEEDBACK / ALARM / DATA
        ↓
[ REACT ]
        ↓
DISCREPANCY CONTROLLED
        ↓
ALARM LIMIT REACHED?
      ↙       ↘
    NO         YES
    ↓           ↓
CONTINUE    ESCALATION
                ↓
          SUPPORT / RESPONSE
                ↓
          PROBLEM SOLVING
```

Инженерный тест на уровне кандидата выполняется:

- **Input:** продукт / результат процесса;
- **Operation:** стандартизированная проверка + feedback + reaction + escalation;
- **Output:** выявленное/отреагированное отклонение;
- **Effect:** предотвращение дальнейшего прохождения discrepancy.

**STATUS: CANDIDATE / SINGLE-SOURCE**

Не считать эту схему полностью подтверждённой единой последовательностью: SOURCE раскрывает перечисленные элементы, но более подробная последовательность alarm → immediate response → leadership support будет добываться в следующих вагонетках.

---

## 11. CHAIN — ЦЕПОЧКА

### SOURCE-SUPPORTED

```text
Standardized Inspection
        ↓
Feedback to Team
        ↓
Discrepancy Detection
        ↓
Reaction
        ↓
Escalation at Alarm Limit
```

Отдельная поддерживающая цепочка:

```text
VS Data
   ↓
Team Problem Solving
   ↓
Leadership Support
```

И отдельная цепочка организационного ownership:

```text
Plant Manager
   ↓
Owns VS Process
   ↓
Facilitates Support

Quality Manager
   ↓
Supports Meeting / Problem Solving / Follow-up
```

Не объединяем эти цепочки в одну без дальнейшего SOURCE.

---

## 12. STATUS

**CANDIDATE / SINGLE-SOURCE**

CANON не назначается.

---

## 13. CMOC INTERPRETATION — ИНТЕРПРЕТАЦИЯ

GM-033 добавляет к GM-031 важный слой: **VS становится не просто конструкцией проверки, а распределённой организационной системой ответственности.**

Особенно сильная конструкция:

```text
CHECK
  ↓
REACT
  ↓
ESCALATE
  ↓
SUPPORT
  ↓
PROBLEM SOLVING
```

При этом SOURCE явно распределяет разные действия между ролями:

```text
OPERATOR
→ проверяет и реагирует

SUPPORT FUNCTIONS
→ поддерживают alarm response

PLANT MANAGER
→ владеет процессом VS

QUALITY MANAGER
→ поддерживает meeting / PS / follow-up
```

Это позволяет сделать предварительный вывод CMOC:

> **Распределённая ответственность становится частью механизма только тогда, когда за ролями закреплены конкретные действия в работающем контуре.**

Это именно **CMOC INTERPRETATION**, а не утверждение GM о CMOC.

---

## 14. ВАЖНАЯ ГРАНИЦА ДЛЯ СЛЕДУЮЩЕЙ ВАГОНЕТКИ

На следующей странице SOURCE появляется **Verification Station Information Board**.

Не объявляем её машинкой заранее.

После GM-033 мы знаем только, что Board существует и может интегрировать текущие Team data; её операционную роль необходимо добыть отдельно. Это будет хорошая проверка нашего правила:

**визуальный артефакт ≠ автоматически Machine.**

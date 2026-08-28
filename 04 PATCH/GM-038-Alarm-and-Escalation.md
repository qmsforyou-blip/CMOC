# GM-038 — Alarm and Escalation

**Извещение на изменение:** 0149+280826  
**Источник:** GM Quality System Basics rev. March 2009  
**Раздел:** 3.3 — Defects Entering the Station / Alarm and Escalation, pp. 87–89  
**Статус:** CANDIDATE / SINGLE-SOURCE

## 1. SOURCE

GM задаёт, что при обнаружении дефекта обратная связь соответствующей команде или лицу должна передаваться через communication system. Alarm подаётся аудио/визуальными сигналами, например Andon.

Alarm process направляет support functions к трём действиям:

- **Go and See** the problem;
- применить **containment**, чтобы предотвратить дальнейший поток дефектов;
- инициировать **problem solving**.

GM требует, чтобы alarm & escalation process был документирован и использовался в Verification Stations или на любом manufacturing step. Если проблемы повторяются, последующие alarms должны эскалироваться соответствующим support functions для реакции. По мере срабатывания alarms запускается problem solving для containment, определения root cause, применения effective countermeasures и установления breakpoint для последующих alarms.

SOURCE также показывает уровни Escalation / Response: Team Member → Team Leader → Supervisor (Group Leader) → Superintendent / Shift Manager → Plant Management. Конкретные имена и cell phone numbers должны быть доступны в рабочей конструкции.

## 2. LOCATION

**pp. 87–89 — Alarm and Escalation.**

## 3. TERMS — ТЕРМИНЫ

| English | Русский |
|---|---|
| **Alarm** | сигнал тревоги / сигнал отклонения |
| **Escalation** | эскалация |
| **Communication System** | система коммуникации / передачи сигнала |
| **Audio/Visual Signal** | аудио-визуальный сигнал |
| **Andon** | визуально-звуковая система сигнализации |
| **Support Functions** | обеспечивающие / поддерживающие функции |
| **Go and See** | непосредственно прибыть и увидеть проблему на месте |
| **Containment** | локализация / удержание дальнейшего потока дефектов под контролем |
| **Problem Solving** | решение проблемы |
| **Root Cause** | коренная причина |
| **Effective Countermeasure** | эффективная контрмера |
| **Breakpoint** | точка / условие срабатывания для последующих Alarm |
| **Manufacturing Step** | производственный шаг |
| **Team Member** | член команды |
| **Team Leader** | лидер команды |
| **Supervisor / Group Leader** | руководитель / групп-лидер |
| **Superintendent / Shift Manager** | супервайзер / руководитель смены |
| **Plant Management** | руководство предприятия |
| **Response** | реакция |
| **Repeat Problem** | повторяющаяся проблема |
| **Call for Help** | обращение за помощью |

## 4. DISTINCTIONS — РАЗЛИЧЕНИЯ

### 4.1 Alarm ≠ Escalation

Alarm — сигнал о состоянии. Escalation — передача проблемы на следующий уровень реакции при установленном условии.

### 4.2 Communication System ≠ Alarm

Communication system передаёт feedback соответствующему участнику; Alarm является конкретным сигналом, который может быть аудио/визуальным.

### 4.3 Alarm ≠ Response

Alarm инициирует управленческую реакцию, но сам по себе не является выполненной реакцией.

### 4.4 Escalation ≠ просто информирование

SOURCE связывает escalation с необходимостью ответной реакции соответствующих support functions.

### 4.5 Go and See ≠ Problem Solving

Go and See — непосредственное прибытие к проблеме. Problem Solving — отдельная деятельность по containment, root cause, countermeasures и breakpoint.

### 4.6 Containment ≠ Root Cause

Containment предотвращает дальнейший поток дефектов. Root Cause Analysis направлена на установление причины. SOURCE помещает оба действия внутрь последующего problem solving, но не делает их одним действием.

## 5. GM-FORMULATIONS — ФОРМУЛИРОВКИ GM

> **When a defect is detected, feedback to the appropriate team or individual will be given by using a communication system.**

> **The alarm is raised by using audio/visual signals (e.g. Andon).**

> **The alarm process directs the support functions to: ‘Go and See’ the problem; Apply containment to prevent further flow of defects; Initiate problem solving.**

> **Alarm & escalation process will be documented and used in Verification Stations or any manufacturing step.**

> **If problems repeat, subsequent alarms shall be escalated to the relevant support functions to respond.**

> **As alarms are triggered, the problem solving process is initiated to contain, determine root cause, apply effective countermeasures and establish a breakpoint for subsequent alarms.**

## 6. EXTRACTION — ИЗВЛЕЧЕНИЕ

```text
DEFECT DETECTED
       ↓
FEEDBACK TO APPROPRIATE TEAM / INDIVIDUAL
       ↓
AUDIO / VISUAL ALARM
       ↓
SUPPORT FUNCTIONS
       ↓
┌───────────────┬────────────────┬─────────────────┐
↓               ↓                ↓
GO AND SEE      CONTAIN          PROBLEM SOLVING
                                  ↓
                           ROOT CAUSE
                                  ↓
                         COUNTERMEASURE
                                  ↓
                              BREAKPOINT
```

Отдельная ветвь повторения:

```text
REPEAT PROBLEM
      ↓
SUBSEQUENT ALARM
      ↓
ESCALATION
      ↓
RELEVANT SUPPORT FUNCTION
      ↓
RESPONSE
```

Иерархия Response / Escalation:

```text
Team Member
    ↓
Team Leader
    ↓
Supervisor / Group Leader
    ↓
Superintendent / Shift Manager
    ↓
Plant Management
```

## 7. REL — ОТНОШЕНИЯ

SOURCE поддерживает следующие связи:

```text
Defect Detected
→ Communication System
→ Appropriate Team / Individual
```

```text
Defect Detected
→ Audio / Visual Alarm
→ Support Functions
```

```text
Alarm
→ Go and See
→ Containment
→ Problem Solving
```

```text
Repeat Problem
→ Subsequent Alarm
→ Escalation
→ Relevant Support Function
→ Response
```

```text
Alarm Triggered
→ Problem Solving
→ Containment
→ Root Cause
→ Effective Countermeasure
→ Breakpoint for Subsequent Alarms
```

## 8. MECHANISM — МЕХАНИЗМ

### CANDIDATE — Alarm & Escalation Mechanism

**Input:** обнаруженный дефект / проблема и сработавший Alarm.

**Transformation:** передача сигнала соответствующему участнику, реакция support functions, escalation при повторении и запуск problem solving.

**Output:** организованная реакция на проблему с containment и дальнейшим устранением причины.

**Организационный эффект:** проблема не остаётся на уровне обнаружения; система обеспечивает ответ, эскалацию и переход к problem solving.

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 9. CAPABILITY — СПОСОБНОСТЬ

### CANDIDATE — Управляемая реакция и эскалация

Способность организации переводить обнаруженный дефект через формализованный сигнал в своевременную реакцию, а при повторении — в эскалацию на соответствующий уровень и Problem Solving.

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 10. CORE CANDIDATE

> **Alarm & Escalation — воспроизводимый механизм, переводящий обнаруженный дефект через communication system и audio/visual Alarm в непосредственную реакцию support functions, а при повторении проблемы — в установленную эскалацию и Problem Solving с containment, определением root cause, применением countermeasures и установлением breakpoint.**

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 11. MACHINE — МАШИНКА

### CANDIDATE MACHINE — Alarm & Escalation

```text
INPUT
Defect / Problem
        ↓
[ SIGNAL / ALARM ]
        ↓
[ ASSIGN RESPONSE LEVEL ]
        ↓
GO AND SEE / CONTAIN / PROBLEM SOLVE
        ↓
REPEAT?
   ↙          ↘
 NO            YES
 ↓              ↓
CONTINUE      ESCALATE
                 ↓
          RELEVANT SUPPORT
                 ↓
              RESPONSE
```

Для инженерного теста имеются:

- **INPUT:** defect / problem;
- **OPERATION:** alarm + response routing + escalation;
- **OUTPUT:** направленная реакция и, при повторении, более высокий уровень response;
- **ORGANIZATIONAL EFFECT:** проблема переводится из состояния обнаружения в организованную реакцию и решение.

**MACHINE = CANDIDATE / SINGLE-SOURCE**

## 12. CHAIN — ЦЕПОЧКИ

### SOURCE-SUPPORTED

```text
Defect
→ Feedback
→ Alarm
→ Support Function
→ Go and See / Containment / Problem Solving
```

```text
Repeat Problem
→ Subsequent Alarm
→ Escalation
→ Relevant Support Function
→ Response
```

```text
Alarm
→ Problem Solving
→ Containment
→ Root Cause
→ Countermeasure
→ Breakpoint
```

Не объединяем три цепочки в одну линейную последовательность: SOURCE представляет их как связанные элементы процесса.

## 13. STATUS

**CANDIDATE / SINGLE-SOURCE**

CANON не присваивается.

## 14. CMOC INTERPRETATION

Здесь впервые очень явно проявляется конструкция:

```text
СОСТОЯНИЕ
  ↓
СИГНАЛ
  ↓
НАЗНАЧЕННАЯ РЕАКЦИЯ
  ↓
ЭСКАЛАЦИЯ ПРИ ПОВТОРЕНИИ
  ↓
ИЗМЕНЕНИЕ СОСТОЯНИЯ
```

Особенно важна **эскалация как изменение уровня организационной реакции**, а не просто передача сообщения выше.

И ещё одна потенциально фундаментальная конструкция:

> **Alarm должен иметь заранее определённый маршрут реакции.**

Иначе сигнал существует, но управленческой машинки после сигнала нет.

Это CMOC-интерпретация, не утверждение GM.

## 15. ГРАНИЦА С GM-037

GM-037 определила условие возникновения Alarm через Alarm Limit.

GM-038 показывает, что происходит **после Alarm**:

```text
Alarm Limit
→ Alarm
→ Response
→ Escalation if repeat
→ Problem Solving
```

Таким образом, GM-037 и GM-038 образуют соседние звенья, но не одну вагонетку.

## 16. FIXATION

PATCH зарегистрирован непосредственно в GitHub.

CORE, каталоги, LAB и предыдущие PATCH не изменялись.

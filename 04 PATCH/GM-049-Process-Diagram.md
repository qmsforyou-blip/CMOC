# GM-049 — Process Diagram

**Извещение на изменение:** 0160+280826  
**Источник:** GM Quality System Basics rev. March 2009  
**Раздел:** 3.5 — Problem Solving / Verification Station Process Diagram  
**Статус:** CANDIDATE / SINGLE-SOURCE

## 1. SOURCE

На стр. 102 GM показывает пример производственной последовательности:

```text
OP 10 → OP 20 → VS → OP 30 → OP 40 → VS → OP 50
                         │
                       GP-12
```

На схеме дополнительно показаны каналы:

- Dock Audit;
- Warranty;
- Customer Liaison;
- Feed Back;
- Feed Forward.

Ключевые утверждения SOURCE:

> **Verification Station(s) can be placed anywhere in the process.**

> **Alarm & Escalation should be applied to each step in the process.**

SOURCE помечает схему как **Example**. fileciteturn145file0

## 2. LOCATION

**p. 102 — Process Diagram.**  
Контекст: **3.5 — Problem Solving / Verification Station**.

## 3. TERMS — ТЕРМИНЫ

| English | Русский |
|---|---|
| **Process Diagram** | схема процесса |
| **Operation (OP)** | операция |
| **Verification Station (VS)** | станция верификации / проверки |
| **Alarm** | сигнал тревоги / сигнал отклонения |
| **Escalation** | эскалация |
| **Process Step** | этап процесса |
| **GP-12** | GP-12, контрольная/containment-точка |
| **Dock Audit** | контроль / аудит на отгрузке |
| **Warranty** | гарантийный канал / гарантийные данные |
| **Customer Liaison** | связь с заказчиком |
| **Feedback** | обратная связь |
| **Feed Forward** | передача информации вперёд по цепочке |
| **Process** | процесс |

## 4. DISTINCTIONS — РАЗЛИЧЕНИЯ

### 4.1 Verification Station ≠ отдельный участок процесса

SOURCE говорит, что VS может быть размещена **в любом месте процесса**. Следовательно, VS рассматривается как функция/точка контроля, которую можно встроить в различные места производственного потока.

### 4.2 VS ≠ единственная точка контроля

Пример содержит несколько VS, расположенных между операциями.

### 4.3 Alarm & Escalation ≠ свойство только VS

Это наиболее важное различение GM-049: SOURCE прямо говорит, что Alarm & Escalation should be applied **to each step in the process**.

То есть механизм реакции распространяется шире самой Verification Station.

### 4.4 Process Step ≠ Verification Station

Операция OP10/OP20/OP30 и VS на схеме — разные элементы.

### 4.5 Feedback ≠ Feed Forward

Оба направления присутствуют в схеме, но SOURCE здесь не раскрывает их полный механизм; не объединяем их автоматически в одну причинную цепь.

### 4.6 Process Diagram ≠ Machine

Схема отображает размещение элементов процесса. Сам графический документ не является машинкой.

## 5. GM-FORMULATIONS — ФОРМУЛИРОВКИ GM

> **Verification Station(s) can be placed anywhere in the process.**

> **Alarm & Escalation should be applied to each step in the process.** fileciteturn145file0

## 6. EXTRACTION — ИЗВЛЕЧЕНИЕ

```text
PROCESS
  ↓
OPERATION / PROCESS STEP
  ↓
[ CONTROL / VS WHERE NEEDED ]
  ↓
NEXT PROCESS STEP
  ↓
[ CONTROL / VS WHERE NEEDED ]
```

Сигнальный слой:

```text
EACH PROCESS STEP
        ↓
ALARM & ESCALATION
```

Информационные каналы:

```text
DOWNSTREAM / EXTERNAL INFORMATION
        ↓
FEEDBACK / FEED FORWARD
        ↓
PROCESS
```

## 7. REL — ОТНОШЕНИЯ

SOURCE поддерживает:

```text
Process
→ Process Step
→ Verification Station
```

```text
Each Process Step
→ Alarm & Escalation
```

```text
Dock Audit / Warranty / Customer Liaison
→ Feedback / Feed Forward
→ Process
```

Последнюю связь фиксируем только как наличие соответствующих каналов на схеме; конкретная последовательность передачи SOURCE здесь не раскрывает.

## 8. MECHANISM — МЕХАНИЗМ

### CANDIDATE — Distributed Verification & Escalation

**Input:** производственный процесс, состоящий из последовательных операций/этапов.

**Transformation:** размещение Verification Station(s) в релевантных местах процесса и применение Alarm & Escalation к каждому этапу.

**Output:** процесс получает распределённые точки проверки и механизм реакции на проблемы на каждом этапе.

**Организационный эффект:** контроль и реакция не ограничиваются одной конечной точкой процесса.

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 9. CAPABILITY — СПОСОБНОСТЬ

### CANDIDATE — Распределённая верификация процесса

Способность организации размещать Verification Stations в необходимых местах производственного процесса и обеспечивать Alarm & Escalation на каждом его этапе.

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 10. CORE CANDIDATE

> **Distributed Verification & Escalation — воспроизводимая конструкция распределения Verification Stations по производственному процессу при применении Alarm & Escalation к каждому этапу процесса.**

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 11. MACHINE — МАШИНКА

Здесь важно не переоценить SOURCE.

### CANDIDATE MACHINE — Distributed Process Control

```text
INPUT
Multi-Step Process
        ↓
[ PLACE VERIFICATION POINTS ]
        ↓
VS AT RELEVANT STEPS
        ↓
[ APPLY ALARM & ESCALATION ]
        ↓
OUTPUT
Detected / Escalatable Problems
at Process Steps
        ↓
EFFECT
Control distributed across the process
```

Инженерный тест:

- **INPUT:** многоэтапный процесс;
- **OPERATION:** распределение Verification Stations + применение Alarm & Escalation;
- **OUTPUT:** контрольные/сигнальные точки на этапах;
- **ORGANIZATIONAL EFFECT:** возможность обнаруживать и эскалировать проблемы не только в конце процесса.

**MACHINE = CANDIDATE / SINGLE-SOURCE**

Но сам **Process Diagram** не является машинкой.

## 12. CHAIN — ЦЕПОЧКИ

### SOURCE-SUPPORTED

```text
Process
→ Process Steps
→ VS can be placed at relevant steps
→ Alarm & Escalation at each step
```

Визуальная схема дополнительно показывает:

```text
OP10 → OP20 → VS → OP30 → OP40 → VS → OP50
```

с отдельным GP-12 и каналами Dock Audit / Warranty / Customer Liaison / Feedback / Feed Forward. fileciteturn145file0

## 13. STATUS

**CANDIDATE / SINGLE-SOURCE**

CANON не присваивается.

## 14. CMOC INTERPRETATION

GM-049 делает важный шаг от **локальной точки контроля** к **архитектуре контроля процесса**.

До этого:

```text
PROCESS
 ↓
VS
 ↓
ALARM / RESPONSE
```

Теперь:

```text
PROCESS
 ├→ OPERATION
 ├→ VS
 ├→ OPERATION
 ├→ VS
 └→ OPERATION
```

при этом:

```text
EACH PROCESS STEP
        ↓
ALARM & ESCALATION
```

CMOC-интерпретация:

> **Контроль управляемого процесса может быть распределён по его структуре, а не сосредоточен в одной финальной точке.**

Это не означает, что каждый этап обязательно должен иметь физическую VS: SOURCE говорит, что VS может быть размещена anywhere in the process, а Alarm & Escalation — применяться к each step.

## 15. ГРАНИЦА С GM-043 / GM-044 / GM-045

```text
GM-043
Quality Information Flow
→ стандартизированная передача информации
```

```text
GM-044
Escape
→ Downstream Detection
→ Feedback
```

```text
GM-045
Performance Metrics
→ Effectiveness Check
```

```text
GM-049
Process Structure
→ Distributed Verification
→ Alarm & Escalation
```

Таким образом, GM-049 не заменяет предыдущие механизмы, а показывает, **где в структуре процесса они могут быть расположены**.

## 16. FIXATION

PATCH зарегистрирован непосредственно в GitHub.

CORE, каталоги, LAB и предыдущие PATCH не изменялись.

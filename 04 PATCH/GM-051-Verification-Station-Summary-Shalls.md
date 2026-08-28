# GM-051 — Verification Station Summary / Shalls

**Извещение на изменение:** 0162+280826  
**Источник:** GM Quality System Basics rev. March 2009  
**Раздел:** 3.7 — Summary, Shalls / Verification Station  
**Статус:** CANDIDATE / SINGLE-SOURCE

> **Уточнение нумерации:** пользовательская рабочая метка GM-051 — «C.A.R.E. Summary / Shalls». В самом SOURCE стр. 104 озаглавлена **3.7 — Summary, Shalls** и относится к разделу **VERIFICATION STATION**. C.A.R.E. на стр. 103 является предшествующим подразделом 3.6. Поэтому PATCH фиксирует фактический SOURCE, а не переносит к нему название C.A.R.E.

## 1. SOURCE

На стр. 104 GM сводит обязательные требования для Verification Station:

- Organizations shall implement at least one Verification Station.
- GMPT suppliers shall implement C.A.R.E.
- Organizations shall institute 100% inspection when variable data cannot be used.
- Organizations shall take immediate action when an alarm limit is reached and use escalation for subsequent alarms for the same defect.
- Past Customer defects shall always have an alarm of 1.
- Organizations shall conduct daily Verification Station meetings at the Station.
- Organizations shall document Responses to Calls for Help.
- Organizations shall support problem solving by the Team based on VS data and review weekly. fileciteturn153file5

Это именно **Summary / Shalls**: SOURCE здесь не вводит новую развернутую конструкцию, а собирает ранее описанные требования Verification Station в нормативный список.

## 2. LOCATION

**p. 104 — 3.7 Summary, Shalls / Verification Station.**

Предыдущий фрагмент: p. 103 — 3.6 C.A.R.E.  
Следующий: p. 105 — финальная формула **Do not Build a Defect! / Solve Problems Through Teamwork! / Satisfy Your Customer.** fileciteturn153file10

## 3. TERMS — ТЕРМИНЫ

| English | Русский |
|---|---|
| **Summary, Shalls** | итоговые обязательные требования |
| **Verification Station (VS)** | станция верификации / проверки |
| **C.A.R.E.** | Customer Acceptance Review & Evaluation — обзор и оценка приемлемости для заказчика |
| **100% Inspection** | 100%-ная инспекция / проверка |
| **Variable Data** | переменные данные |
| **Alarm Limit** | порог Alarm |
| **Immediate Action** | немедленное действие |
| **Escalation** | эскалация |
| **Past Customer Defect** | ранее выявленный дефект заказчика |
| **Verification Station Meeting** | совещание на Verification Station |
| **Response to Calls for Help** | реакция на обращения за помощью |
| **VS Data** | данные Verification Station |
| **Problem Solving** | решение проблем |
| **Review Weekly** | еженедельное рассмотрение |
| **Organization** | организация |
| **GMPT Supplier** | поставщик GMPT |

## 4. DISTINCTIONS — РАЗЛИЧЕНИЯ

### 4.1 Summary / Shalls ≠ новая машинка

SOURCE здесь суммирует обязательные требования уже разобранного блока Verification Station. Поэтому не создаём отдельную Machine только из-за формы Summary / Shalls.

### 4.2 Requirement ≠ Mechanism

Каждый Shall задаёт обязательное состояние/действие, но не каждый Shall самостоятельно раскрывает полный механизм.

### 4.3 C.A.R.E. ≠ Verification Station в целом

Для GMPT suppliers C.A.R.E. является отдельным обязательным требованием внутри общего блока Verification Station.

### 4.4 Alarm Limit ≠ Immediate Action

SOURCE задаёт последовательность:

```text
Alarm Limit reached
→ Immediate Action
→ Escalation for subsequent alarms
```

Это не одно и то же действие.

### 4.5 100% Inspection ≠ универсальный режим

100% inspection применяется в указанном SOURCE условии: **when variable data cannot be used**.

### 4.6 VS Data ≠ Problem Solving

VS data является основанием для поддержки Team Problem Solving и weekly review, но данные и сам процесс Problem Solving не смешиваем.

### 4.7 Documented Response ≠ Response

SOURCE требует **document Responses to Calls for Help**. Само действие помощи и его документирование — разные элементы.

## 5. GM-FORMULATIONS — ФОРМУЛИРОВКИ GM

> **Organizations shall: Implement at least one Verification Station.**

> **Institute 100% inspection when variable data cannot be used.**

> **Take immediate action when an alarm limit is reached and use escalation for subsequent alarms for the same defect.**

> **Past Customer defects shall always have an alarm of 1.**

> **Conduct daily Verification Station meetings at the Station.**

> **Document Responses to Calls for Help.**

> **Support problem solving by the Team based on VS data and review weekly.** fileciteturn153file5

## 6. EXTRACTION — ИЗВЛЕЧЕНИЕ

Общая структура требований:

```text
IMPLEMENT VS
      ↓
CONTROL / INSPECTION
      ↓
ALARM
      ↓
IMMEDIATE ACTION
      ↓
ESCALATION
      ↓
DAILY VS MEETING
      ↓
DOCUMENT RESPONSE TO HELP
      ↓
VS DATA
      ↓
TEAM PROBLEM SOLVING
      ↓
WEEKLY REVIEW
```

Но это **сводная архитектурная интерпретация** нескольких Shalls, а не одна дословная последовательность SOURCE. Не выдавать её как SOURCE Chain.

## 7. REL — ОТНОШЕНИЯ

SOURCE непосредственно поддерживает:

```text
Verification Station
→ at least one implemented
```

```text
Alarm Limit reached
→ Immediate Action
→ Escalation for subsequent alarms / same defect
```

```text
Past Customer Defect
→ Alarm Limit = 1
```

```text
VS Data
→ Team Problem Solving
→ Weekly Review
```

```text
Calls for Help
→ Response
→ Documentation
```

## 8. MECHANISM — МЕХАНИЗМЫ

### 8.1 CANDIDATE — Alarm Response & Escalation

**Input:** достижение Alarm Limit.

**Operation:** Immediate Action; при subsequent alarm для того же defect — escalation.

**Output:** непосредственная реакция + последующая эскалация.

**STATUS: CANDIDATE / SINGLE-SOURCE**

Это уже ранее добытый механизм, который здесь получает ещё одно SOURCE-подтверждение.

### 8.2 CANDIDATE — VS Data → Team Problem Solving Review

**Input:** VS data.

**Operation:** поддержка Team Problem Solving + weekly review.

**Output:** регулярное рассмотрение работы команды.

**STATUS: CANDIDATE / SINGLE-SOURCE**

Но это не следует автоматически объединять с GM-046/047 в одну Machine: здесь SOURCE даёт краткое требование.

## 9. CAPABILITY — СПОСОБНОСТИ

### CANDIDATE — Поддержка Problem Solving данными VS

Способность организации использовать данные Verification Station для поддержки Team Problem Solving с регулярным weekly review.

**CANDIDATE / SINGLE-SOURCE**

### CANDIDATE — Эскалация повторного Alarm

Способность организации переходить от immediate action к escalation при subsequent alarm для того же defect.

**CANDIDATE / SINGLE-SOURCE**

## 10. CORE CANDIDATES

### Candidate A — Verification Station Requirement Set

> **Verification Station Requirement Set — совокупность обязательных организационных требований к наличию VS, режимам инспекции, Alarm/Response/Escalation, ежедневному Review, документированию помощи и поддержке Problem Solving.**

**CANDIDATE / SINGLE-SOURCE**

Это именно **набор требований**, а не новая универсальная сущность CMOC.

### Candidate B — Alarm → Action → Escalation

> **Alarm Response & Escalation — воспроизводимая конструкция перехода от достижения Alarm Limit к Immediate Action и, при повторном Alarm для того же дефекта, к Escalation.**

**CANDIDATE / SINGLE-SOURCE**

## 11. MACHINE — МАШИНКИ

### Existing Candidate Machine — Alarm Response & Escalation Machine

```text
INPUT
Alarm Limit Reached
        ↓
[ IMMEDIATE ACTION ]
        ↓
SUBSEQUENT ALARM
FOR SAME DEFECT?
        ↓ YES
[ ESCALATION ]
        ↓
OUTPUT
Escalated Response
```

**MACHINE = CANDIDATE / SINGLE-SOURCE**

Это не новая машинка GM-051; это **повторное подтверждение** ранее добытой конструкции.

### MACHINE — Verification Station Requirement Set

**NONE**.

Список Shalls сам по себе не является машинкой: в нём смешаны implementation requirements, inspection condition, response, meeting, documentation и problem-solving support.

## 12. CHAIN — ЦЕПОЧКИ

### SOURCE-SUPPORTED

```text
Alarm Limit Reached
→ Immediate Action
→ Subsequent Alarm / Same Defect
→ Escalation
```

### SOURCE-SUPPORTED

```text
VS Data
→ Team Problem Solving
→ Weekly Review
```

### SOURCE-SUPPORTED

```text
Calls for Help
→ Response
→ Documentation
```

### NOT SOURCE-SUPPORTED AS ONE CHAIN

```text
Implement VS
→ Alarm
→ Meeting
→ Documentation
→ Problem Solving
```

Это может быть нашей архитектурной сборкой, но стр. 104 не формулирует её как единую последовательность.

## 13. STATUS

**CANDIDATE / SINGLE-SOURCE**

Для ранее добытых механизмов:

- **Alarm Response & Escalation** — CONFIRM / SINGLE-SOURCE, но ещё не MULTI-SOURCE CANON;
- **VS Data → Team Problem Solving Review** — CANDIDATE / SINGLE-SOURCE.

CANON не присваивается.

## 14. CMOC INTERPRETATION

GM-051 особенно ценна не новым термином, а тем, что показывает **связку требований разного типа**:

```text
STRUCTURAL REQUIREMENT
Implement VS

BEHAVIORAL REQUIREMENT
Take Immediate Action

ESCALATION REQUIREMENT
Escalate subsequent alarm

TEMPORAL REQUIREMENT
Daily / Weekly Review

EVIDENCE / RECORD REQUIREMENT
Document Responses

KNOWLEDGE / PROBLEM-SOLVING REQUIREMENT
Use VS Data to support Team Problem Solving
```

Это сильный материал для CMOC, потому что один короткий Summary показывает: **управляемость Verification Station обеспечивается не одним правилом, а совокупностью взаимосвязанных требований к структуре, действию, эскалации, времени, фиксации и использованию данных.**

Это **CMOC INTERPRETATION**, не SOURCE claim.

## 15. СВЯЗЬ С GM-050

GM-050 дала описание C.A.R.E.:

```text
CUSTOMER-RELATED ITEMS
→ C.A.R.E.
→ EFFECTIVENESS OF PROCESS CONTROLS
→ NON-CONFORMING DATA
→ FAST RESPONSE / LPA
```

GM-051 добавляет нормативную рамку:

```text
GMPT SUPPLIER
→ C.A.R.E. SHALL BE IMPLEMENTED
```

Поэтому GM-051 **подтверждает обязательность C.A.R.E. для GMPT suppliers**, но не добавляет нового механизма C.A.R.E.

## 16. ГРАНИЦА С GM-047 / GM-048

```text
GM-047
Tracking → Status → Weekly Review
```

```text
GM-048
Problem Report Out → Status Review → Management Response
```

```text
GM-051
VS Data → Team Problem Solving → Weekly Review
```

Последняя формула является более краткой SOURCE-версией уже добытого weekly review контура.

## 17. FIXATION

PATCH зарегистрирован непосредственно в GitHub.

CORE, каталоги, LAB и предыдущие PATCH не изменялись.

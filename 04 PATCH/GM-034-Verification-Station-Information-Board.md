# GM-034 — Verification Station Information Board

**Извещение на изменение:** 0145+280826  
**SOURCE:** GM Quality System Basics rev. March 2009  
**Раздел:** 3.2 — Verification Station Information Board  
**Статус:** CANDIDATE / SINGLE-SOURCE

---

## 1. SOURCE — ИСТОЧНИК

GM показывает **Verification Station Information Board** на стр. 82 и приводит два примера. При этом источник не требует копировать один фиксированный формат. Напротив, прямо сказано:

> “Integrate current systems and build on it to meet the intent.”

Board может включать или объединять Team data, в том числе:

- productivity — производительность;
- quality alerts — уведомления/сигналы о качестве;
- start-of-shift TPM check sheets — чек-листы TPM начала смены;
- Team safety data — данные по безопасности команды;
- другие действующие стандартные данные Team.

То есть GM задаёт **назначение и содержание**, но допускает интеграцию с уже существующими системами. fileciteturn55file0

Следующая страница даёт более подробный **Verification Station Template**, который показывает, какую информацию Board/Shop Floor Management должен связывать:

- Defects Entering VS — дефекты, входящие на VS;
- Inspection of Product — контроль продукта (Attribute/Variable);
- Prioritizing of Defects — приоритизация дефектов;
- Alarm Escalation Procedure — процедура сигнализации и эскалации;
- Who/When — кто и когда;
- Immediate Responses — немедленные реакции;
- Record of Calls for Help and Escalation — запись обращений за помощью и эскалации;
- Leadership Meeting Every Shift — встреча руководства каждую смену;
- Meeting Assignments — поручения по итогам встречи;
- Pareto Analysis / Defects over Time — анализ Парето / дефекты во времени;
- Problem Solving — решение проблем;
- Team selection of new problems based on Pareto analysis / assignable cause;
- R/Y/G tracking и review roadblocks / problem escalation;
- Defects Leaving VS Station — дефекты, выходящие из VS;
- Feedback: Dock Audit / Containment / Field Rep-Liaison Issues;
- Formal Customer Complaints — официальные жалобы заказчика;
- Team Performance Data, FTQ & SCRAP trend charts, Direct Run, Safety.

Таким образом, SOURCE показывает Board не как декоративную доску, а как **информационный интерфейс управления Verification Station и Shop Floor Management**. fileciteturn55file1

---

## 2. LOCATION — МЕСТО В ИСТОЧНИКЕ

**Стр. 82 — VERIFICATION STATION INFORMATION BOARD.**  
Связанный шаблон — **стр. 83 — VERIFICATION STATION TEMPLATE / Shop Floor Management (Example).** fileciteturn55file0turn55file1

---

## 3. TERMS — ТЕРМИНЫ

| English | Русский |
|---|---|
| **Verification Station Information Board** | информационная доска станции верификации |
| **Information Board** | информационная доска |
| **Shop Floor Management** | управление на производственном участке |
| **Integrate Current Systems** | интегрировать действующие системы |
| **Team Data** | данные команды / участка |
| **Productivity** | производительность |
| **Quality Alerts** | сигналы / уведомления о качестве |
| **Start-of-Shift TPM Check Sheets** | чек-листы TPM начала смены |
| **Team Safety Data** | данные команды по безопасности |
| **Defects Entering VS** | дефекты, входящие на станцию верификации |
| **Inspection of Product** | контроль продукции |
| **Attribute / Variable** | по атрибутивному / количественному признаку |
| **Prioritizing of Defects** | приоритизация дефектов |
| **Alarm Escalation Procedure** | процедура сигнализации и эскалации |
| **Immediate Responses** | немедленные реакции |
| **Record of Calls for Help and Escalation** | запись обращений за помощью и эскалации |
| **Leadership Meeting** | встреча руководства |
| **Meeting Assignments** | поручения по итогам встречи |
| **Pareto Analysis** | анализ Парето |
| **Defects over Time** | динамика дефектов во времени |
| **Problem Solving** | решение проблем |
| **Roadblocks** | препятствия / блокирующие факторы |
| **R/Y/G Tracking** | отслеживание статуса Red / Yellow / Green |
| **Defects Leaving VS Station** | дефекты, выходящие со станции верификации |
| **Feedback** | обратная связь |
| **Dock Audit** | аудит готовой продукции перед отгрузкой |
| **Containment** | локализация / удержание под контролем |
| **Field Rep-Liaison Issues** | вопросы взаимодействия с представителем в поле |
| **Formal Customer Complaints** | официальные жалобы заказчика |
| **FTQ (First Time Quality)** | качество с первого прохода |
| **SCRAP** | брак / продукция на списание |
| **Direct Run** | прямой выпуск / прохождение без повторной обработки |
| **Safety** | безопасность |

---

## 4. DISTINCTIONS — РАЗЛИЧЕНИЯ

### Information Board ≠ Record

Board содержит данные и может включать записи, но SOURCE задаёт ему более широкую функцию: интегрировать данные и поддерживать управление VS.

### Information Board ≠ просто визуализация

SOURCE связывает содержание Board с:

**дефектами → сигналами → реакцией → эскалацией → leadership → problem solving → feedback → metrics.**

Следовательно, Board является частью действующего управленческого контура.

### Board ≠ Verification Station

Board представляет и поддерживает работу VS, но не является всей Verification Station.

### Board ≠ фиксированный шаблон

GM прямо разрешает интегрировать текущие системы и существующие Team data вместо создания отдельной изолированной системы. fileciteturn55file0

### Data ≠ Management

Наличие на Board показателей ещё не доказывает, что ими управляют. Управленческая функция появляется через их включение в review, assignments, escalation и problem solving.

---

## 5. GM-FORMULATIONS — ФОРМУЛИРОВКИ SOURCE

- **“VERIFICATION STATION INFORMATION BOARD”**
- **“Integrate current systems and build on it to meet the intent.”**
- Board may incorporate Team data such as productivity, quality alerts, start-of-shift TPM Check Sheets, Team safety data and other current standard Team data. fileciteturn55file0

---

## 6. EXTRACTION — ДОБЫЧА

SOURCE поддерживает такую конструкцию:

```text
CURRENT SYSTEMS / TEAM DATA
          ↓
       INTEGRATE
          ↓
VERIFICATION STATION INFORMATION BOARD
          ↓
┌─────────┼─────────┬───────────────┐
↓         ↓         ↓               ↓
QUALITY   SAFETY   PRODUCTIVITY   OTHER DATA
          ↓
     SHOP FLOOR MANAGEMENT
          ↓
REVIEW / ASSIGNMENTS / ESCALATION /
PROBLEM SOLVING / FEEDBACK
```

Более детальная схема из Template:

```text
DEFECTS ENTERING VS
        ↓
INSPECTION + PRIORITIZATION
        ↓
ALARM / ESCALATION
        ↓
IMMEDIATE RESPONSE
        ↓
LEADERSHIP MEETING
        ↓
ASSIGNMENTS / PROBLEM SOLVING
        ↓
R/Y/G + ROADBLOCKS
        ↓
DEFECTS LEAVING VS
        ↓
FEEDBACK + CUSTOMER / DOWNSTREAM DATA
        ↓
PERFORMANCE DATA
```

Эта вторая схема является **реконструкцией по содержанию шаблона**, а не буквальной графической схемой SOURCE.

---

## 7. REL — ОТНОШЕНИЯ

SOURCE поддерживает отношения:

```text
Current Systems
      ↓
Integration
      ↓
Information Board
```

```text
Information Board
      ↔
Team Data
```

```text
Information Board
      ↔
Shop Floor Management
```

```text
Board Information
      →
Review / Escalation / Problem Solving
```

```text
Defects Leaving VS
      →
Feedback / Customer / Downstream Information
```

Не утверждаем, что каждый элемент является обязательным физическим разделом одной доски: SOURCE говорит, что системы могут быть **integrated / incorporated**.

---

## 8. MECHANISM — МЕХАНИЗМ

### CANDIDATE — Integrated Shop-Floor Information Mechanism

**Input:** данные действующих систем и Team data.

**Operation:** интеграция и представление данных в Information Board, используемом в управлении VS / Shop Floor Management.

**Output:** общедоступное представление значимой информации о качестве, безопасности, производительности, дефектах, реакциях и улучшениях.

**Организационный эффект:** создаётся общий информационный интерфейс для review, assignments, escalation, problem solving и feedback.

**STATUS: CANDIDATE / SINGLE-SOURCE**

---

## 9. CAPABILITY — СПОСОБНОСТЬ

### CANDIDATE — Shared Operational Visibility

Способность Team и руководства видеть в одном управленческом пространстве данные, необходимые для текущего контроля VS, реакции, эскалации и улучшения.

**STATUS: CANDIDATE / SINGLE-SOURCE**

Это CMOC-интерпретация; GM не использует термин capability в данном фрагменте.

---

## 10. CORE CANDIDATE

> **Verification Station Information Board — интегрированная информационно-визуальная конструкция, объединяющая данные действующих систем и Team data для поддержки управления Verification Station, review, escalation, problem solving, feedback и performance monitoring.**

**STATUS: CANDIDATE / SINGLE-SOURCE**

---

## 11. MACHINE — МАШИНКА

### **CANDIDATE MACHINE — Information Board as Management Interface**

```text
INPUT
Current systems + Team data
        ↓
[ INTEGRATE / PRESENT ]
        ↓
SHARED INFORMATION VIEW
        ↓
Review / Escalation /
Assignments / Problem Solving
        ↓
OUTPUT
Coordinated management information
        ↓
EFFECT
Visible + actionable shop-floor state
```

### Инженерный тест

**INPUT** — данные из нескольких источников.

**OPERATION** — интеграция и визуальное представление.

**OUTPUT** — общее информационное представление.

**EFFECT** — поддержка управленческих действий.

Поэтому:

**MACHINE = CANDIDATE / SINGLE-SOURCE**

Но это принципиально не означает, что **любая информационная доска является машинкой**. Статус кандидата здесь получен из SOURCE благодаря тому, что Board встроена в контур Shop Floor Management и связывается с review, escalation, assignments и problem solving.

---

## 12. CHAIN — ЦЕПОЧКА

SOURCE позволяет осторожно зафиксировать:

```text
Current Systems / Team Data
        ↓
Integration
        ↓
Information Board
        ↓
Shop Floor Management
        ↓
Review / Escalation / Problem Solving
```

А Template добавляет информационную линию:

```text
Defects Entering
        ↓
Inspection / Prioritization
        ↓
Alarm / Escalation
        ↓
Immediate Response
        ↓
Leadership / Problem Solving
        ↓
Defects Leaving
        ↓
Feedback / Downstream Data
```

Не утверждаем, что первая и вторая цепочки физически совпадают один к одному.

---

## 13. STATUS

**CANDIDATE / SINGLE-SOURCE**

Никакого CANON.

---

## 14. CMOC INTERPRETATION — ИНТЕРПРЕТАЦИЯ CMOC

GM-034 даёт очень сильный ответ на наш предыдущий вопрос о Board.

**Board может быть не просто Record.**

В данном случае она потенциально является **интерфейсом управленческого механизма**.

Различие:

```text
RECORD
→ хранит факт

BOARD
→ делает информацию доступной для текущего управления

MANAGEMENT INTERFACE
→ связывает информацию с review,
  решением, действием и последующим контролем
```

Но SOURCE одновременно показывает важное ограничение: Board не обязана иметь единственный физический формат. Она может **интегрировать существующие системы** и Team data. fileciteturn55file0

Поэтому для будущего Атласа правильнее описывать не «доску как предмет», а **конструкцию управленческого информационного интерфейса**, имеющую различные реализации.

И это очень близко к нашему выводу по Fast Response Board — но **не является автоматическим подтверждением тождества двух машинок**. Здесь доказательство должно быть накоплено межисточниково.

---

## 15. INTER-SOURCE NOTE

Потенциально подтверждает уже возникшую в GM-002 линию:

**Board → status / information → review → action**.

Но пока оставляем обе конструкции как **SINGLE-SOURCE CANDIDATES** и не объединяем их в одну CANON Entity или Machine.

---

## 16. PATCH DISCIPLINE

- Новый PATCH: GM-034.
- Старые PATCH не изменяются.
- LAB не изменяется.
- CORE не изменяется.
- Каталоги не изменяются.
- Кандидатная классификация не канонизируется.

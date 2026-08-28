# GM-041 — Leadership Support

**Извещение на изменение:** 0152+280826  
**Источник:** GM Quality System Basics rev. March 2009  
**Раздел:** 3.3 — Defects Entering the Station / Leadership Support, pp. 95–96  
**Статус:** CANDIDATE / SINGLE-SOURCE

## 1. SOURCE

GM устанавливает, что **Management Walk-Through/Meeting shall be held daily on each shift at selected Verification Stations**. Один раз в неделю Team также представляет проблему, над которой работает. Sign-in sheet фиксирует присутствие и поддержку на Management Walk-Through/Daily Meetings.

В примере Leadership Support перечислены Plant Manager, Quality Manager, Engineering Manager, Maintenance Manager, Area Supervisor и Other.

Daily Leadership Review — VS Operator Report Out включает:

1. Review FTQ and Scrap Charts — ухудшается, улучшается или остаётся без изменения;
2. Review Alarms from Previous Shift(s) — какие проблемы, использовался ли Immediate Action Response Sheet, была ли реакция своевременной, определены ли Point of Cause и Root Cause, повторился ли дефект и использовалась ли escalation process;
3. Review Feedback from Downstream Customers — проблемы за последние 24 часа, доведение информации до Team Members, Quality Alert и проверка проблемы на VS.

Weekly Problem Solving Team Report Out включает:

4. Review Control Charts of Top Defects — какие Top Defects и какую следующую проблему следует решать;
5. Problem Solving Team Report Out and Review — текущий шаг Problem Solving, roadblocks, дополнительные ресурсы, актуальность Tracking Report и необходимость эскалации Problem Solving Assignments.

Отдельный **Assignment Action Sheet** фиксирует задания, возникающие на ежедневной VS или еженедельной Problem Solving встрече, и они пересматриваются на следующей встрече. Примеры вопросов включают material presentation, delivery и поддержку, необходимую для выполнения работы лучше, быстрее или точнее.

Источник подтверждает эти элементы как организацию Leadership Support, но не формулирует их как единую CMOC-модель.

## 2. LOCATION

**pp. 95–96 — Leadership Support.**

## 3. TERMS — ТЕРМИНЫ

| English | Русский |
|---|---|
| **Leadership Support** | поддержка руководства |
| **Management Walk-Through / Meeting** | обход / встреча руководства |
| **Verification Station Review** | рассмотрение состояния Verification Station |
| **Daily Leadership Review** | ежедневный обзор руководством |
| **VS Operator Report Out** | отчёт оператора VS |
| **Weekly Problem Solving Team Report Out** | еженедельный отчёт команды Problem Solving |
| **FTQ (First Time Quality)** | качество с первого прохода |
| **Scrap** | брак / списание |
| **Alarm** | сигнал отклонения |
| **Immediate Action Response Sheet** | лист регистрации непосредственной реакции |
| **Point of Cause** | точка возникновения причины |
| **Root Cause** | коренная причина |
| **Downstream Customer** | последующий потребитель процесса |
| **Quality Alert** | предупреждение о качестве |
| **Control Chart** | контрольная карта |
| **Top Defects** | наиболее значимые / частые дефекты |
| **Roadblock** | препятствие / блокирующий фактор |
| **Resource** | ресурс |
| **Tracking Report** | отчёт отслеживания состояния |
| **Problem Solving Assignment** | задание по решению проблемы |
| **Assignment Action Sheet** | лист действий по поручениям |
| **Management Walk-Through** | обход руководства |
| **Sign-in Sheet** | лист регистрации присутствия |

## 4. DISTINCTIONS — РАЗЛИЧЕНИЯ

### 4.1 Leadership Support ≠ присутствие руководителя

GM связывает присутствие с конкретным Review, вопросами, устранением roadblocks, назначением ресурсов и эскалацией Problem Solving Assignments. Простое присутствие не является описанной функцией.

### 4.2 Daily Review ≠ Weekly Problem Solving Review

Daily Review сосредоточен на FTQ/Scrap, предыдущих Alarms и downstream feedback. Weekly Review — на Top Defects, текущем шаге Problem Solving, roadblocks, ресурсах и эскалации.

### 4.3 Review ≠ Problem Solving

Leadership Review проверяет состояние и обеспечивает поддержку; SOURCE не говорит, что руководство само выполняет Problem Solving вместо Team.

### 4.4 Assignment ≠ выполненное действие

Assignment Action Sheet фиксирует задания и обеспечивает их повторный Review на следующей встрече. Сам факт назначения не доказывает выполнение.

### 4.5 Sign-in Sheet ≠ доказательство эффективности

Sign-in Sheet фиксирует присутствие и поддержку; это не равно доказательству улучшения результата.

## 5. GM-FORMULATIONS — ФОРМУЛИРОВКИ GM

> **Management Walk-Through/Meeting shall be held daily on each shift at selected Verification Stations.**

> **Once per week, the Team also reports on a problem they are working to resolve.**

> **Are there any road blocks that need to be removed?**

> **Are there any other resources that need to be assigned?**

> **Do any Problem Solving Assignments need to be escalated?**

## 6. EXTRACTION — ИЗВЛЕЧЕНИЕ

```text
VS / TEAM DATA
      ↓
DAILY LEADERSHIP REVIEW
      ↓
FTQ / SCRAP + ALARMS + DOWNSTREAM FEEDBACK
      ↓
ISSUES / ROADBLOCKS / RESOURCE NEEDS
      ↓
ASSIGNMENT / SUPPORT / ESCALATION
      ↓
NEXT REVIEW
```

Еженедельный контур:

```text
TOP DEFECTS / CONTROL CHARTS
      ↓
PROBLEM SELECTION
      ↓
TEAM REPORT OUT
      ↓
ROADBLOCKS / RESOURCES / ESCALATION
      ↓
ASSIGNMENT ACTION SHEET
      ↓
NEXT MEETING REVIEW
```

## 7. REL — ОТНОШЕНИЯ

```text
VS Data
→ Leadership Review
→ Issue / Roadblock / Resource Need
→ Assignment / Escalation
```

```text
Assignment Action Sheet
→ Review at Next Meeting
```

```text
Top Defects
→ Problem Selection
→ Team Report Out
→ Leadership Support
```

## 8. MECHANISM — МЕХАНИЗМ

### CANDIDATE — Leadership Support Loop

**Input:** данные VS, предыдущие Alarms, downstream feedback, Top Defects и состояние Problem Solving.

**Transformation:** регулярный Leadership Review → выявление проблем/roadblocks/resource needs → назначение поддержки или эскалация → последующий Review.

**Output:** назначенные действия, ресурсы, снятые препятствия или эскалированные задания.

**Организационный эффект:** проблемы Team получают регулярный управленческий Review и поддержку, а незакрытые задания не исчезают после встречи, поскольку возвращаются на следующий Review.

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 9. CAPABILITY — СПОСОБНОСТЬ

### CANDIDATE — Leadership Support for Problem Solving

Способность руководства регулярно видеть состояние VS, распознавать препятствия и потребность в ресурсах, обеспечивать поддержку и при необходимости эскалировать Problem Solving.

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 10. CORE CANDIDATE

> **Leadership Support Loop — воспроизводимая организационная конструкция регулярного Review состояния Verification Station и Problem Solving, в которой руководство выявляет проблемы и препятствия, назначает необходимые ресурсы или эскалацию и возвращает незавершённые задания в следующий цикл Review.**

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 11. MACHINE — МАШИНКА

### CANDIDATE MACHINE — Leadership Support Loop

```text
INPUT
VS Data + Alarms + Feedback + Problem Status
        ↓
[ DAILY / WEEKLY LEADERSHIP REVIEW ]
        ↓
ISSUE / ROADBLOCK / RESOURCE NEED
        ↓
[ ASSIGN / SUPPORT / ESCALATE ]
        ↓
ASSIGNMENT ACTION SHEET
        ↓
NEXT MEETING REVIEW
        ↓
STATUS / FURTHER ACTION
```

Инженерный тест:

- **INPUT:** актуальная информация о состоянии VS и проблемах;
- **OPERATION:** регулярный Review с назначением поддержки/эскалации;
- **OUTPUT:** управленческое действие и зафиксированное задание;
- **ORGANIZATIONAL EFFECT:** проблема получает продолжение до следующего Review вместо исчезновения после встречи.

**MACHINE = CANDIDATE / SINGLE-SOURCE**

Важно: **Management Walk-Through/Meeting сам по себе не объявляется машинкой**. Machine возникает из повторяемого контура Review → Action/Assignment → Next Review.

## 12. CHAIN — ЦЕПОЧКИ

### SOURCE-SUPPORTED

```text
VS Data
→ Daily Leadership Review
→ Issue / Roadblock / Resource Need
→ Assignment / Support / Escalation
→ Next Meeting Review
```

```text
Top Defects
→ Problem Solving Team Report Out
→ Roadblock / Resource Review
→ Assignment / Escalation
→ Next Review
```

## 13. STATUS

**CANDIDATE / SINGLE-SOURCE**

CANON не присваивается.

## 14. CMOC INTERPRETATION

Здесь появляется важное различение:

> **Руководство входит в механизм управления не самим фактом участия, а способностью изменить условия выполнения работы: снять препятствие, выделить ресурс, назначить действие или изменить уровень эскалации.**

И ещё более сильная конструкция:

```text
REVIEW
 ↓
DECISION / ASSIGNMENT
 ↓
RECORD
 ↓
NEXT REVIEW
```

В этом контуре **Assignment Action Sheet** выполняет функцию удержания незавершённого управленческого действия между циклами Review. Это CMOC-интерпретация; GM описывает сам лист и его повторный Review, но не даёт такой онтологической формулировки.

## 15. ГРАНИЦА С GM-040

**GM-040:** непосредственная реакция на конкретный Alarm и восстановление контролируемого состояния.

**GM-041:** регулярный управленческий контур, который рассматривает Alarms, результаты, препятствия и состояние Problem Solving и обеспечивает ресурс/эскалацию.

```text
GM-040
ALARM
 ↓
IMMEDIATE RESPONSE
 ↓
BREAK POINT

GM-041
VS / PROBLEM DATA
 ↓
LEADERSHIP REVIEW
 ↓
SUPPORT / ASSIGNMENT / ESCALATION
 ↓
NEXT REVIEW
```

## 16. FIXATION

PATCH зарегистрирован непосредственно в GitHub.

CORE, каталоги, LAB и предыдущие PATCH не изменялись.

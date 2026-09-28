# GM-042 — Assignment Action Sheet

**Извещение на изменение:** 0153+280826  
**Источник:** GM Quality System Basics rev. March 2009  
**Раздел:** 3.3 — Defects Entering the Station / Leadership Support, p. 96  
**Статус:** CANDIDATE / SINGLE-SOURCE

## 1. SOURCE

GM показывает **ASSIGNMENT ACTION SHEET (Example)**.

Ключевое правило SOURCE:

> As issues come up at the daily VS or weekly Problem Solving report out meeting, any assignments given are captured here and reviewed at next meeting.

В качестве примеров вопросов, по которым могут возникать assignments, GM называет:

- material presentation;
- delivery;
- support needed to do their job better, faster or more accurately.

Следовательно, Sheet используется для удержания выданных поручений между текущим и следующим Review. fileciteturn111file0

## 2. LOCATION

**p. 96 — Assignment Action Sheet (Example), раздел Leadership Support.**

Предыдущая страница описывает Daily Leadership Review и Weekly Problem Solving Team Report Out; среди результатов Review прямо указаны потребность в устранении roadblocks, назначении ресурсов и эскалации Problem Solving Assignments. fileciteturn111file5

## 3. TERMS — ТЕРМИНЫ

| English | Русский |
|---|---|
| **Assignment Action Sheet** | лист поручений и действий |
| **Assignment** | поручение / назначенное действие |
| **Action** | действие |
| **Issue** | проблема / вопрос |
| **Daily VS Report Out Meeting** | ежедневное отчётное совещание VS |
| **Weekly Problem Solving Report Out Meeting** | еженедельное отчётное совещание Problem Solving |
| **Captured** | зафиксирован |
| **Reviewed at Next Meeting** | рассмотрен на следующем совещании |
| **Material Presentation** | представление / подача материала |
| **Delivery** | поставка / доставка |
| **Support Needed** | необходимая поддержка |
| **Roadblock** | препятствие / блокирующий фактор |
| **Resource** | ресурс |
| **Escalation** | эскалация |
| **Status** | состояние / статус |

## 4. DISTINCTIONS — РАЗЛИЧЕНИЯ

### 4.1 Assignment ≠ Action

Assignment — назначенное действие/поручение. SOURCE показывает его как результат Review, который затем удерживается и проверяется.

### 4.2 Assignment Action Sheet ≠ Meeting Record

Sheet не просто фиксирует факт совещания. Его назначение — удерживать **assignments**, данные на совещании, до следующего Review.

### 4.3 Capture ≠ Completion

Фиксация поручения не означает его выполнения. SOURCE специально требует последующего Review.

### 4.4 Next Meeting Review ≠ новое назначение

Следующее совещание выполняет функцию проверки ранее выданных assignments; не следует автоматически считать его только повторным назначением.

### 4.5 Assignment ≠ Problem Solving

Некоторые assignments возникают в Problem Solving Review, но Sheet не является самим Problem Solving.

## 5. GM-FORMULATIONS — ФОРМУЛИРОВКИ GM

> **As issues come up at the daily VS or weekly Problem Solving report out meeting, any assignments given are captured here and reviewed at next meeting.**

> **Issues may include; material presentation, delivery, support needed to do their job better, faster or more accurately.** fileciteturn111file0

## 6. EXTRACTION — ИЗВЛЕЧЕНИЕ

```text
ISSUE
  ↓
DAILY VS / WEEKLY PROBLEM SOLVING REVIEW
  ↓
ASSIGNMENT GIVEN
  ↓
CAPTURE IN ASSIGNMENT ACTION SHEET
  ↓
TIME PASSES / COMPLETION NOT ASSUMED
  ↓
NEXT MEETING
  ↓
REVIEW ASSIGNMENT
  ↓
REVIEWED ASSIGNMENT (OUTCOME NOT SPECIFIED)
```

## 7. REL — ОТНОШЕНИЯ

```text
Issue
→ Review Meeting
→ Assignment
→ Assignment Action Sheet
→ Next Meeting Review
```

```text
Roadblock / Resource Need
→ Assignment
→ Capture
→ Next Meeting Review
```

```text
Assignment
→ Review at Next Meeting

Further Action / Status: not specified by this page
```

## 8. MECHANISM — МЕХАНИЗМ

### CANDIDATE — Assignment Carry-Forward Mechanism

**Input:** проблема/вопрос, выявленный на Daily VS или Weekly Problem Solving Report Out.

**Transformation:** назначение действия и его фиксация в Assignment Action Sheet.

**Output:** задание, удерживаемое до следующего Review.

**Организационный эффект:** поручение не исчезает вместе с завершением совещания; оно переносится в следующий управленческий цикл для проверки.

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 9. CAPABILITY — СПОСОБНОСТЬ

### CANDIDATE — Удержание управленческих поручений

Способность организации фиксировать назначения, возникающие в ходе Review, и возвращать их в следующий цикл Review для проверки состояния и дальнейшего действия.

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 10. CORE CANDIDATE

> **Assignment Carry-Forward — воспроизводимая организационная конструкция, в которой поручение, возникшее при рассмотрении проблемы, фиксируется и переносится в следующий цикл Review, где его состояние повторно рассматривается.**

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 11. MACHINE — МАШИНКА

### CANDIDATE MACHINE — Assignment Carry-Forward Machine

```text
INPUT
Issue / Roadblock / Resource Need
        ↓
[ REVIEW ]
        ↓
[ ASSIGN ACTION ]
        ↓
[ CAPTURE ]
        ↓
ASSIGNMENT ACTION SHEET
        ↓
[ NEXT MEETING REVIEW ]
        ↓
REVIEWED ASSIGNMENT (OUTCOME NOT SPECIFIED)
```

Инженерный тест:

- **INPUT:** Issue / Roadblock / Resource Need;
- **OPERATION:** Review → Assignment → Capture → Carry Forward;
- **OUTPUT:** назначенное и удерживаемое действие;
- **ORGANIZATIONAL EFFECT:** незавершённое поручение сохраняется между циклами управления и возвращается в Review.

**MACHINE = CANDIDATE / SINGLE-SOURCE**

Важно: машинкой является не лист бумаги сам по себе, а **воспроизводимый контур Assignment → Capture → Next Review**. Sheet является его физическим носителем/реализацией в SOURCE.

## 12. CHAIN — ЦЕПОЧКИ

### SOURCE-SUPPORTED

```text
Issue
→ Review
→ Assignment
→ Capture
→ Next Meeting
→ Review
```

Это подтверждённая SOURCE последовательность.

## 13. STATUS

**CANDIDATE / SINGLE-SOURCE**

CANON не присваивается.

## 14. CMOC INTERPRETATION

GM-042 даёт очень чистый пример **удержания незавершённого управленческого действия во времени**.

```text
MEETING
   ↓
DECISION / ASSIGNMENT
   ↓
RECORD
   ↓
TIME
   ↓
NEXT REVIEW
   ↓
STATE CHECK
```

Поэтому потенциальная CMOC-конструкция здесь сильнее, чем просто «Action List»:

> **управленческое поручение становится частью системы только тогда, когда оно не исчезает после назначения, а имеет механизм возврата в следующий цикл управления.**

Это **CMOC INTERPRETATION**, не утверждение GM.

## 15. ГРАНИЦА С GM-041

**GM-041:** Leadership Review выявляет Roadblocks, потребности в ресурсах и вопросы Problem Solving; руководство может назначить поддержку/действие.

**GM-042:** показывает физическую/организационную конструкцию, которая удерживает выданное Assignment до следующего Review.

```text
GM-041
REVIEW
 ↓
IDENTIFY NEED
 ↓
ASSIGN / SUPPORT / ESCALATE

GM-042
ASSIGNMENT
 ↓
CAPTURE
 ↓
NEXT REVIEW
 ↓
REVIEWED ASSIGNMENT (OUTCOME NOT SPECIFIED)
```

## 16. FIXATION

PATCH зарегистрирован непосредственно в GitHub.

CORE, каталоги, LAB и предыдущие PATCH не изменялись.

## 17. Уточнение по графической форме и границе вывода

**Извещение на изменение:** `0226+280926`  
**Название файла:** `04 PATCH/GM-042-Assignment-Action-Sheet.md`

Визуальная проверка исходной страницы 96 показывает в образце формы графы `Shift`, `Assign to`, `Task Name`, `Start Date`, `Expected Completion Date`, `Actual Completion Date`. Поэтому лист фиксирует исполнителя, задачу и плановую дату завершения; он также допускает запись фактической даты завершения. Эти графы отсутствовали в извлечённом тексте PDF и не были отражены в исходной версии PATCH.

Прямое правило GM требует рассмотреть выданное поручение на следующей встрече. Оно не утверждает, что работа обязательно была выполнена между встречами, что к следующему Review заполнена фактическая дата, или что Review непременно породит новое действие. Упоминания `status / further action` в прежних схемах являлись инженерной гипотезой; в схемах разделов 6, 7, 11 и 15 они заменены границей, подтверждённой p. 96. Описание способности и эффекта в разделах 8–14 остаётся CMOC-интерпретацией со статусом кандидата.

Контур в пределах источника: вопрос на встрече → поручение → запись в листе с исполнителем, задачей и сроком → рассмотрение на следующей встрече. Возможность записи фактического завершения не является доказательством исполнения каждого поручения. Канонизация и типизация живого `PAS-001` этим уточнением не выполняются.

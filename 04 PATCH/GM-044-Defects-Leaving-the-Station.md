# GM-044 — Defects Leaving the Station

**Извещение на изменение:** 0155+280826  
**Источник:** GM Quality System Basics rev. March 2009  
**Раздел:** 3.4 — Defects Leaving the Station  
**Статус:** CANDIDATE / SINGLE-SOURCE

## 1. SOURCE

GM ставит контрольный вопрос: **How do we Know that the Verification Station is doing its job and driving Quality back into Station?**

SOURCE перечисляет источники обнаружения дефектов, которые покинули Verification Station:

- defects found at internal audit or containment check points, including GP12;
- issues that escaped to the Customer;
- issues that escaped to the Customer and are caught by the Supplier contact;
- issues that escaped to the customer and are found by the customer.

При этом feedback details должны передаваться от всех downstream customers, включая взаимодействие между departments на manufacturing site. fileciteturn119file3

Таким образом, GM рассматривает Defects Leaving VS не как один канал обнаружения, а как несколько независимых точек обратного обнаружения после прохождения станции.

## 2. LOCATION

**pp. 98–99 — 3.4 Defects Leaving the Station / Quality Feedback–Feed Forward.**

## 3. TERMS — ТЕРМИНЫ

| English | Русский |
|---|---|
| **Defects Leaving the Station** | дефекты, покидающие станцию |
| **Verification Station (VS)** | станция верификации |
| **Internal Audit** | внутренний аудит |
| **Containment Check Point** | контрольная точка проверки containment |
| **GP12** | контроль/containment-процесс GP12 |
| **Escape** | выход дефекта за пределы контролируемой точки |
| **Customer** | заказчик / потребитель |
| **Supplier Contact** | контакт со стороны поставщика |
| **Downstream Customer** | последующий потребитель процесса |
| **Feedback Details** | детали / сведения обратной связи |
| **Manufacturing Site** | производственная площадка |
| **Department** | подразделение |
| **Quality Feedback** | обратная связь по качеству |
| **Feed Forward** | передача информации вперёд по цепочке |

## 4. DISTINCTIONS — РАЗЛИЧЕНИЯ

### 4.1 Defect Leaving VS ≠ место обнаружения

Дефект может покинуть VS, а обнаружиться позднее — на internal audit, containment checkpoint, у Supplier contact или непосредственно у Customer.

### 4.2 Escape ≠ Customer Complaint

SOURCE различает сам факт escape и его обнаружение различными downstream субъектами. Formal Customer Complaints появляются в Template как отдельный информационный элемент, но в этой вагонетке не смешиваем эти конструкции. fileciteturn120file11

### 4.3 Internal Detection ≠ External Detection

Internal audit / containment check points — внутренние точки обнаружения. Supplier contact / Customer — внешние по отношению к исходной VS точки обнаружения.

### 4.4 Feedback ≠ Detection

Detection отвечает на вопрос «где дефект был обнаружен». Feedback обеспечивает передачу информации о результате обратно тем, кому она нужна.

### 4.5 Defect Escape ≠ доказательство неработоспособности VS

SOURCE задаёт вопрос, как узнать, выполняет ли VS свою функцию. Сам факт обнаружения escape ещё не позволяет автоматически заключить, почему он произошёл. Причинный анализ относится к Problem Solving.

## 5. GM-FORMULATIONS — ФОРМУЛИРОВКИ GM

> **How do we Know that the Verification Station is doing its job and driving Quality back into Station?**

SOURCE перечисляет четыре типа источников обнаружения:

> **Defects found at internal audit or containment check points including GP12.**

> **Any issues escaped to the Customer.**

> **Issues that escaped to the Customer and are caught by the Supplier contact.**

> **Issues that escaped to the customer and are found by the customer.** fileciteturn119file3

## 6. EXTRACTION — ИЗВЛЕЧЕНИЕ

```text
DEFECT LEAVES VS
       ↓
┌──────────────┬─────────────────┬──────────────────┬─────────────────┐
↓              ↓                 ↓                  ↓
INTERNAL       CONTAINMENT       SUPPLIER           CUSTOMER
AUDIT          CHECK / GP12      CONTACT            DETECTION
       \           |                |                  /
        \          |                |                 /
         └─────────┴────────────────┴────────────────┘
                           ↓
                     QUALITY FEEDBACK
                           ↓
                 INFORMATION RETURNS TO
                 RELEVANT PROCESS / PEOPLE
```

## 7. REL — ОТНОШЕНИЯ

```text
Verification Station
→ Defect Leaves Station
→ Downstream Detection
→ Feedback
```

```text
Defect Leaving VS
→ Internal Audit / Containment / GP12
```

```text
Defect Leaving VS
→ Supplier Contact Detection
```

```text
Defect Leaving VS
→ Customer Detection
```

```text
Downstream Customer
→ Feedback Details
→ Manufacturing Site / Departments
```

## 8. MECHANISM — МЕХАНИЗМ

### CANDIDATE — Downstream Escape Feedback Loop

**Input:** дефект, покинувший Verification Station и обнаруженный downstream.

**Transformation:** обнаружение в одной из downstream-точек → передача feedback details.

**Output:** информация о downstream escape возвращается в relevant process / departments.

**Организационный эффект:** система получает возможность узнать о дефектах, которые не были обнаружены/удержаны на исходной VS.

**STATUS: CANDIDATE / SINGLE-SOURCE**

Важно: SOURCE в этом фрагменте подтверждает обнаружение и передачу feedback, но не раскрывает здесь полный цикл последующего Problem Solving.

## 9. CAPABILITY — СПОСОБНОСТЬ

### CANDIDATE — Обратное обнаружение escape

Способность организации получать сведения о дефектах, прошедших Verification Station, из нескольких downstream-источников и передавать соответствующую информацию обратно.

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 10. CORE CANDIDATE

> **Downstream Escape Feedback — воспроизводимая конструкция, при которой дефект, покинувший Verification Station, может быть обнаружен на одной из downstream-точек, после чего информация о нём передаётся обратно в relevant process / departments для дальнейшего управления.**

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 11. MACHINE — МАШИНКА

### CANDIDATE MACHINE — Downstream Escape Feedback Machine

```text
INPUT
Defect Escaped from VS
        ↓
[ DOWNSTREAM DETECTION ]
        ↓
Internal Audit / Containment / GP12
        OR
Supplier Contact
        OR
Customer
        ↓
[ CAPTURE / COMMUNICATE FEEDBACK ]
        ↓
OUTPUT
Quality Feedback Details
        ↓
EFFECT
Relevant Process / Departments
receive evidence of escape
```

Инженерный тест проходит на уровне контура:

- **INPUT:** escape;
- **OPERATION:** downstream detection + feedback communication;
- **OUTPUT:** information on escape;
- **ORGANIZATIONAL EFFECT:** исходная система получает информацию о том, что дефект прошёл её контроль.

**MACHINE = CANDIDATE / SINGLE-SOURCE**

Не утверждаем, что каждая отдельная downstream-точка является самостоятельной машинкой.

## 12. CHAIN — ЦЕПОЧКИ

### SOURCE-SUPPORTED

```text
Defect Leaving VS
→ Downstream Detection
→ Feedback Details
→ Relevant Process / Departments
```

Ветви обнаружения:

```text
Defect Leaving VS
→ Internal Audit / Containment / GP12
→ Feedback
```

```text
Defect Leaving VS
→ Supplier Contact
→ Feedback
```

```text
Defect Leaving VS
→ Customer
→ Feedback
```

## 13. STATUS

**CANDIDATE / SINGLE-SOURCE**

CANON не присваивается.

## 14. CMOC INTERPRETATION

GM-044 даёт очень сильное различение:

> **Контур контроля можно проверять не только изнутри, но и по последствиям, обнаруженным downstream.**

Получается:

```text
CONTROL POINT
      ↓
ESCAPE
      ↓
DOWNSTREAM REALITY
      ↓
DETECTION
      ↓
FEEDBACK
      ↓
CONTROL POINT LEARNS
```

То есть downstream становится **источником свидетельства о фактической эффективности upstream-контроля**.

Это особенно интересно для CMOC, потому что связывает:

**контроль → результат → внешнее обнаружение → evidence → feedback.**

Но не делаем следующий шаг автоматически: SOURCE этого фрагмента не говорит, что каждый feedback обязательно приводит к corrective action. Это будет добываться дальше.

## 15. ГРАНИЦА С GM-043

**GM-043** фиксировала общий механизм Quality Feedback / Feed Forward — передачу quality expectations и results по стандартизированным communication pathways.

**GM-044** раскрывает конкретный тип результата, который должен возвращаться в систему: **defect escape, обнаруженный downstream**.

```text
GM-043
QUALITY INFORMATION
→ STANDARDIZED PATHWAY
→ RECIPIENT

GM-044
DEFECT ESCAPE
→ DOWNSTREAM DETECTION
→ FEEDBACK DETAILS
→ RELEVANT PROCESS / DEPARTMENTS
```

## 16. FIXATION

PATCH зарегистрирован непосредственно в GitHub.

CORE, каталоги, LAB и предыдущие PATCH не изменялись.

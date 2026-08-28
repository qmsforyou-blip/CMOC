# GM-027 — Reintroduce Product

**Извещение на изменение:** 0138+280826  
**SOURCE:** GM Quality System Basics rev. March 2009  
**Section:** 2.5.2 — Reintroduce Product  
**Status:** CANDIDATE / SINGLE-SOURCE

---

## 1. SOURCE — ИСТОЧНИК

GM задаёт отдельные правила для продукта, удалённого из утверждённого потока процесса и возвращаемого обратно в процесс.

Ключевые требования SOURCE:

- все **Control Plan inspections and tests** должны быть выполнены;
- продукт, удалённый из approved process flow, следует возвращать в process stream **в точке удаления или до неё**;
- возвращаемый продукт должен быть **identified**;
- GM как best practice рекомендует не прогонять продукт более двух раз;
- если вернуть продукт в точку удаления или до неё невозможно, должна применяться утверждённая Quality Manager документированная процедура rework and inspection, обеспечивающая соответствие всем specification и test requirements.

SOURCE не описывает здесь конкретную технологию повторного прохождения продукта; он задаёт условия управляемого возврата.

---

## 2. LOCATION — РАСПОЛОЖЕНИЕ

**p. 69 — 2.5 DISPOSITION → 2.5.2 Reintroduce Product**

---

## 3. TERMS — ТЕРМИНЫ

- **Reintroduce Product** — повторно ввести продукцию в процесс
- **Approved Process Flow** — утверждённый поток процесса
- **Process Stream** — поток процесса
- **Point of Removal** — точка удаления
- **Control Plan** — план управления / контрольный план
- **Inspection** — контроль / проверка
- **Test** — испытание
- **Identified Product** — идентифицированная продукция
- **Rework and Inspection Procedure** — процедура доработки и контроля
- **Quality Manager** — менеджер по качеству
- **Specification** — спецификация / установленное требование
- **Test Requirements** — требования к испытаниям
- **Best Practice** — рекомендуемая передовая практика

---

## 4. DISTINCTIONS — РАЗЛИЧЕНИЯ

### DIS-GM-027-01
**Rework / Repair ≠ Reintroduction.**

GM-026 описывает контролируемое выполнение rework/repair. GM-027 описывает отдельную операцию возвращения продукта в утверждённый поток процесса.

### DIS-GM-027-02
**Reintroduction ≠ просто физический возврат.**

Возврат сопровождается обязательными Control Plan inspections and tests и идентификацией продукта.

### DIS-GM-027-03
**Point of Removal ≠ произвольная точка возврата.**

GM задаёт предпочтительный маршрут: в точке удаления или до неё.

### DIS-GM-027-04
**Identification ≠ evidence of conformity.**

Идентификация возвращённого продукта необходима, но сама по себе не заменяет требуемые inspections and tests.

### DIS-GM-027-05
**Best Practice ≠ Shall.**

Рекомендация не прогонять продукт более двух раз обозначена GM как best practice, а не как тот же тип обязательного требования, что выполнение inspections/tests.

### DIS-GM-027-06
**Exception path ≠ ordinary reintroduction path.**

Если возврат в точку удаления или до неё невозможен, применяется отдельная утверждённая Quality Manager документированная процедура rework and inspection.

---

## 5. GM-FORMULATIONS — ФОРМУЛИРОВКИ GM

- **“All control plan inspections and tests shall be performed.”** — Все предусмотренные Control Plan проверки и испытания должны быть выполнены.
- **“Product removed from the approved process flow should be reintroduced into the process stream at or prior to the point of removal.”** — Продукция, удалённая из утверждённого потока процесса, должна возвращаться в поток в точке удаления или до неё.
- **“Reintroduced product needs to be identified.”** — Возвращаемая в процесс продукция должна быть идентифицирована.
- **“Best practice would suggest that you do not run product more than twice.”** — Рекомендуемая практика предполагает не прогонять продукцию более двух раз.
- При невозможности возврата в точку удаления или до неё должна применяться утверждённая Quality Manager документированная процедура rework and inspection, обеспечивающая соответствие specification и test requirements.

---

## 6. EXTRACTION — ДОБЫЧА

```text
PRODUCT REMOVED FROM APPROVED PROCESS FLOW
                ↓
        REINTRODUCTION DECISION
                ↓
      CAN RETURN TO POINT OF REMOVAL
             OR PRIOR?
          ↓              ↓
         YES              NO
          ↓               ↓
 REINTRODUCE THERE       APPROVED QM
          ↓              REWORK +
 IDENTIFY PRODUCT        INSPECTION PROCEDURE
          ↓               ↓
 CONTROL PLAN           ASSURE CONFORMANCE
 INSPECTIONS + TESTS    TO SPECIFICATION + TEST
          ↓
 CONTROLLED RETURN
 TO PROCESS STREAM
```

Отдельное SOURCE-условие:

```text
BEST PRACTICE
→ не запускать продукт более двух раз
```

---

## 7. REL — СВЯЗИ

SOURCE поддерживает следующую конструкцию:

```text
Removed Product
      ↓
Point of Removal
      ↓
Reintroduce at / prior to removal point
      ↓
Identify Reintroduced Product
      ↓
Control Plan Inspections + Tests
      ↓
Return to Process Stream
```

И исключительную ветвь:

```text
Cannot reintroduce at / prior to removal
      ↓
Approved Quality Manager Procedure
      ↓
Rework + Inspection
      ↓
Specification + Test Requirements
      ↓
Assured Conformance
```

Не утверждается, что обе ветви выполняются одновременно.

---

## 8. MECHANISM — МЕХАНИЗМ

### CANDIDATE — Controlled Reintroduction Mechanism

**Input:** продукт, удалённый из approved process flow.

**Transformation:** определить допустимую точку возврата, идентифицировать возвращаемый продукт и выполнить требуемые Control Plan inspections/tests; при невозможности стандартного возврата применить утверждённую процедуру rework and inspection.

**Output:** продукт, возвращённый в process stream на контролируемых условиях.

**Организационный эффект:** возврат продукта не обходится без контроля соответствия и не становится неуправляемым повторным прохождением.

**STATUS: CANDIDATE / SINGLE-SOURCE**

---

## 9. CAPABILITY — СПОСОБНОСТЬ

**NONE**

Отдельная capability из этого фрагмента не извлекается.

---

## 10. CORE CANDIDATE — КАНДИДАТ ЯДРА

> **Controlled Reintroduction — воспроизводимый механизм возврата удалённой из утверждённого потока продукции в process stream через заданную точку возврата, с обязательной идентификацией и выполнением предусмотренных Control Plan inspections and tests либо через утверждённую альтернативную процедуру при невозможности стандартного возврата.**

**STATUS: CANDIDATE / SINGLE-SOURCE**

---

## 11. MACHINE — МАШИНКА

### CANDIDATE MACHINE — Controlled Reintroduction

```text
INPUT
Product removed from approved process flow
        ↓
CHECK
Допустима ли точка возврата
в месте удаления или до неё?
        ↓
IDENTIFY
Reintroduced product
        ↓
VERIFY
Control Plan inspections + tests
        ↓
OUTPUT
Product returned to process stream
        ↓
EFFECT
Controlled re-entry into approved process
```

Альтернативный маршрут:

```text
No standard reintroduction point available
        ↓
Approved Quality Manager procedure
        ↓
Rework + Inspection
        ↓
Conformance to specification / test requirements
        ↓
Controlled re-entry
```

Инженерный тест выполнен на уровне кандидата:

- **Input:** удалённый из утверждённого потока продукт;
- **Transformation:** контролируемый возврат с идентификацией и проверками;
- **Output:** продукт в process stream;
- **Effect:** возврат не минует заданный контроль.

**STATUS: CANDIDATE / SINGLE-SOURCE**

---

## 12. CHAIN — ЦЕПОЧКА

### SOURCE-SUPPORTED CANDIDATE

```text
Removed Product
→ Return Point
→ Identification
→ Control Plan Inspections / Tests
→ Process Stream
```

Альтернативная ветвь:

```text
No feasible standard return
→ Approved QM Procedure
→ Rework + Inspection
→ Conformance
→ Process Stream
```

Best Practice:

```text
Do not run product more than twice
```

Не превращаем эту рекомендацию в обязательный переход цепочки.

---

## 13. STATUS

**CANDIDATE / SINGLE-SOURCE**

CANON не присваивается.

---

## 14. CMOC INTERPRETATION — ИНТЕРПРЕТАЦИЯ CMOC

GM-027 показывает, что **возврат объекта в процесс сам является управляемым переходом**, а не просто перемещением назад.

```text
REMOVED FROM FLOW
       ↓
   RETURN POINT
       ↓
 IDENTIFICATION
       ↓
 VERIFICATION
       ↓
 RETURN TO FLOW
```

Особенно важна конструкция:

> **Объект не просто возвращается в процесс; он должен вернуться в контролируемую точку процесса и пройти предусмотренные проверки.**

Для CMOC это потенциально полезная конструкция **управляемого перехода объекта между состояниями/позициями процесса**.

Но не делаем из неё пока универсальную CMOC-модель возврата: SOURCE описывает именно reintroduction продукта после удаления из approved process flow.

---

## 15. INTER-SOURCE NOTE

Конструкция потенциально пригодна для последующего сопоставления с ISO/DIS 9001:2025 в части контроля несоответствующих outputs, проверки соответствия и управления изменённым/повторно введённым output.

В данном PATCH межисточниковое подтверждение не утверждается.

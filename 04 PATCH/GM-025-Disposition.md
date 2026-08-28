# GM-025 — Disposition

**Извещение на изменение:** 0136+280826  
**Источник:** GM Quality System Basics rev. March 2009  
**Раздел:** 2.5 — DISPOSITION (Reusable or scrap)  
**Статус:** CANDIDATE / SINGLE-SOURCE

---

## 1. SOURCE

GM выделяет **Disposition** как самостоятельный элемент управления несоответствующим продуктом после Identification, Segregation и Containment.

Внутри Disposition источник раскрывает, как с продуктом поступать дальше, если он может быть использован повторно: **rework/repair**, **reintroduce product**, либо продукт должен стать **scrap**.

Для rework/repair GM требует:
- рабочую инструкцию на выполнение rework;
- метод идентификации scrap и обеспечения traceability для rework product;
- customer approval may be required.

Для reintroduction GM требует:
- выполнение всех inspections and tests, предусмотренных Control Plan;
- возврат продукта в process stream в точке удаления или ранее;
- идентификацию reintroduced product;
- если вернуть продукт в исходную точку невозможно — утверждённую Quality Manager документированную процедуру rework и inspection, обеспечивающую соответствие всем specification и test requirements.

Источник также указывает, что scrap должен быть предотвращён от использования и отслеживаться с планом его сокращения. fileciteturn34file0turn34file8

---

## 2. LOCATION

**pp. 69–70**, раздел **2.5 — Disposition (Reusable or scrap)** и связанные подпункты:

- 2.5.1 — Reusable; (rework/repair)
- 2.5.2 — Reintroduce product
- Scrap

Оглавление источника подтверждает, что Disposition — отдельный блок после Containment и перед Summary. fileciteturn32file6

---

## 3. TERMS — ТЕРМИНЫ

- **Disposition** — решение о дальнейшей судьбе / способе обращения с продуктом
- **Reusable** — пригодный для повторного использования
- **Rework** — доработка
- **Repair** — ремонт
- **Rework Instruction / Work Instruction** — рабочая инструкция на доработку
- **Scrap** — брак, подлежащий списанию / утилизации
- **Traceability** — прослеживаемость
- **Customer Approval** — одобрение заказчика
- **Reintroduce Product** — повторно ввести продукт в процесс
- **Process Stream** — поток процесса
- **Control Plan** — План управления / контрольный план
- **Inspection** — контроль / проверка
- **Test** — испытание / тестирование
- **Quality Manager** — менеджер по качеству
- **Specification** — спецификация / установленное требование
- **Test Requirements** — требования к испытаниям
- **Scrap Identification** — идентификация брака

---

## 4. DISTINCTIONS

### DIS-GM-025-01
**Containment ≠ Disposition.**

Containment удерживает потенциально затронутый продукт под контролем. Disposition определяет, **что делать с уже контролируемым несоответствующим продуктом дальше**.

### DIS-GM-025-02
**Segregation ≠ Disposition.**

Физически отделить продукт недостаточно. После отделения требуется определить его дальнейшую судьбу.

### DIS-GM-025-03
**Rework/Repair ≠ Reintroduction.**

Rework/repair описывает способ сделать продукт пригодным к дальнейшему использованию; reintroduction описывает, **куда и при каких условиях продукт возвращается в процесс**.

### DIS-GM-025-04
**Reintroduction ≠ автоматический выпуск.**

После reintroduction GM требует выполнения всех соответствующих Control Plan inspections and tests.

### DIS-GM-025-05
**Traceability ≠ Identification.**

GM требует идентифицировать reintroduced product и одновременно обеспечивает traceability rework product. Это связанные, но не тождественные требования.

### DIS-GM-025-06
**Scrap ≠ исчезновение из системы.**

Scrap должен быть предотвращён от использования и отслеживаться; GM также требует план его сокращения. fileciteturn34file8

---

## 5. GM-FORMULATIONS

- “A work instruction to perform rework.”
- “A method to identify scrap and rework product traceability.”
- “Customer approval may be required.”
- “All control plan inspections and tests shall be performed.”
- “Product removed from the approved process flow should be reintroduced into the process stream at or prior to the point of removal.”
- “Reintroduced product needs to be identified.”
- “An approved (Quality Manager) documented rework and inspection procedure shall be used to assure conformance to all specification and test requirements.” fileciteturn34file0

---

## 6. EXTRACTION

```text
NONCONFORMING PRODUCT
        ↓
     DISPOSITION
        ↓
   ┌────┴───────────┐
   ↓                ↓
REUSABLE           SCRAP
   ↓                ↓
REWORK / REPAIR    PREVENT USE
   ↓                ↓
REINTRODUCE?       TRACK + REDUCE
   ↓
CONTROL PLAN
INSPECTIONS / TESTS
   ↓
IDENTIFIED PRODUCT
   ↓
PROCESS STREAM
```

Для случая, когда возврат в исходную точку невозможен:

```text
REINTRODUCTION NOT POSSIBLE
        ↓
APPROVED DOCUMENTED
REWORK + INSPECTION PROCEDURE
        ↓
CONFORMANCE TO SPECIFICATION
AND TEST REQUIREMENTS
```

---

## 7. REL

Источник поддерживает следующую локальную связь:

```text
Controlled Nonconforming Product
        ↓
Disposition
        ↓
Reusable / Scrap
```

Для reusable:

```text
Reusable
   ↓
Rework / Repair
   ↓
Reintroduce Product
   ↓
Control Plan Inspections + Tests
   ↓
Identified Product
   ↓
Process Stream
```

Альтернативный путь:

```text
Product
   ↓
Scrap
   ↓
Prevent Use
   ↓
Track
   ↓
Plan to Reduce Scrap
```

---

## 8. MECHANISM

### CANDIDATE — Disposition Control Mechanism

**Вход:** контролируемый несоответствующий продукт.

**Преобразование:** определить допустимый путь дальнейшего обращения — reusable/rework/repair/reintroduction либо scrap — и задать необходимые условия контроля.

**Выход:** продукт получает определённый и управляемый дальнейший статус/маршрут.

**Организационный эффект:** продукт не остаётся в неопределённом состоянии после containment; его дальнейшее обращение становится контролируемым.

**STATUS: CANDIDATE / SINGLE-SOURCE**

---

## 9. CAPABILITY

**NONE**

Отдельная capability из этой вагонетки не выделяется.

---

## 10. CORE CANDIDATE

> **Disposition Control — воспроизводимый механизм определения и реализации контролируемого дальнейшего пути несоответствующего продукта: повторное использование через rework/repair и установленную проверку, либо controlled scrap с предотвращением использования и прослеживаемостью.**

**STATUS: CANDIDATE / SINGLE-SOURCE**

---

## 11. MACHINE

### CANDIDATE MACHINE — Disposition Control

```text
INPUT
Controlled Nonconforming Product
        ↓
[ DISPOSITION DECISION ]
        ↓
 ┌──────┴─────────┐
 ↓                ↓
REUSABLE         SCRAP
 ↓                ↓
REWORK/REPAIR     PREVENT USE
 ↓                ↓
REINTRODUCE       TRACK + REDUCE
 ↓
CONTROL PLAN
INSPECTIONS / TESTS
 ↓
CONTROLLED RETURN
TO PROCESS
```

Инженерный тест:

- **INPUT:** контролируемый nonconforming product;
- **OPERATION:** выбор и реализация допустимого disposition path;
- **OUTPUT:** продукт получает определённый дальнейший маршрут;
- **ORGANIZATIONAL EFFECT:** исключается неопределённое или несанкционированное обращение с несоответствующим продуктом.

**STATUS: CANDIDATE / SINGLE-SOURCE**

---

## 12. CHAIN

### SOURCE-SUPPORTED CANDIDATE

```text
Containment
   ↓
Disposition
   ↓
Reusable / Scrap
```

Reusable branch:

```text
Rework / Repair
   ↓
Reintroduce Product
   ↓
Control Plan Inspections + Tests
   ↓
Identify
   ↓
Return to Process Stream
```

Scrap branch:

```text
Scrap
   ↓
Prevent Use
   ↓
Track
   ↓
Reduce
```

Не делаем вывод, что GM требует одинаковую процедуру для всех вариантов disposition: источник явно различает reusable/rework/reintroduce и scrap.

---

## 13. STATUS

**CANDIDATE / SINGLE-SOURCE**

CANON не присваивается.

---

## 14. CMOC INTERPRETATION

GM-025 показывает переход от **контроля состояния** к **принятию решения о дальнейшей судьбе объекта**.

```text
IDENTIFY
   ↓
SEGREGATE
   ↓
CONTAIN
   ↓
DISPOSITION
   ↓
┌──────────────┬─────────────┐
↓              ↓
RETURN / USE   REMOVE
```

Особенно важно не смешивать:

> **Containment отвечает за удержание потенциально затронутого продукта под контролем.**
>
> **Disposition отвечает за управляемый выбор дальнейшего маршрута продукта.**

Для CMOC это потенциально важная отдельная конструкция: **решение меняет не только статус объекта, но и его допустимый маршрут в системе**.

При этом SOURCE не даёт нам оснований превращать Quality Manager approval, customer approval или Control Plan в самостоятельные Machines внутри этой вагонетки. Это отдельные условия/механизмы, которые могут быть раскрыты позднее.

Это CMOC-интерпретация, а не утверждение GM о CMOC.

---

## 15. INTER-SOURCE NOTE

Потенциально очень важна для последующего сопоставления с ISO/DIS 9001:2025 в части control of nonconforming outputs, correction, release и authorization. В этом PATCH межисточниковое подтверждение не заявляется.

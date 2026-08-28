# GM-024 — Containment Worksheet

**Извещение на изменение:** `0135+280826`  
**SOURCE:** `GM Quality System Basics Overview Supplier Audit.pdf`  
**Раздел SOURCE:** `2.4.1 — Containment Worksheet`, pp. 61–62  
**STATUS:** `CANDIDATE / SINGLE-SOURCE`

---

## 1. SOURCE

GM требует, чтобы Containment Worksheet использовался и заполнялся для того, чтобы:

- обеспечить **systematic approach** к containment всего suspect product;
- определить потенциальное количество и все области, которые необходимо проверить на nonconforming product;
- сверить ожидаемое количество suspect material с фактически найденным;
- зафиксировать condition дефекта и standard, которому продукт должен соответствовать;
- зафиксировать sort method;
- определить identification method для отсортированного good/bad product;
- отслеживать и документировать результаты containment activity;
- инициировать customer notification, если возможен escape. fileciteturn149file0

SOURCE содержит также крупный заполненный пример Worksheet. В нём зафиксированы Department, Containment Owner, Date, Product Name/Number, Product Nonconformance, Product Containment Scope, потенциальные зоны и количества, ответственные, место segregation, Sort Method, Sort Criteria, идентификация conforming/nonconforming и итог **TOTAL FOUND 2548 / 2548**. fileciteturn30file0

---

## 2. LOCATION

**p. 61:** назначение и структура Containment Worksheet.  
**p. 62:** заполненный пример — `CONTAINMENT WORKSHEET (Example)`.

---

## 3. TERMS

- Containment Worksheet
- systematic approach
- suspect product
- potential quantity
- areas to be checked
- expected quantity
- actual quantity
- defect condition
- standard
- sort method
- sort criteria
- identification method
- conforming product
- nonconforming product
- containment activity
- customer notification
- escape
- containment owner
- responsibility
- verification
- total found

---

# 4. DISTINCTIONS

### DIS-GM-024-01 — Worksheet ≠ Record только

SOURCE не ограничивает Worksheet ролью последующей фиксации результата. GM требует, чтобы Worksheet **использовался и заполнялся для обеспечения systematic approach** к containment.

Следовательно, на уровне SOURCE Worksheet одновременно является **структурирующим инструментом выполнения containment** и его документированным результатом.

---

### DIS-GM-024-02 — Potential Quantity ≠ Actual Found

GM специально требует reconciliation:

```text
EXPECTED / POTENTIAL
        ↕
ACTUAL FOUND
```

В примере это становится видимым числом:

```text
TOTAL FOUND = 2548
VERIFIED = 2548
```

Это не просто запись количества. Это проверка полноты охвата containment. fileciteturn30file0

---

### DIS-GM-024-03 — Area to Check ≠ Area Checked

Worksheet сначала задаёт **где suspect product может находиться**, а затем фиксирует **что там реально проверено и найдено**.

Это различение важно:

```text
POTENTIAL LOCATION
        ↓
VERIFICATION
        ↓
FOUND / NOT FOUND
```

---

### DIS-GM-024-04 — Sort Method ≠ Sort Criteria

GM разделяет:

- **как проверять** — Sort Method;
- **по какому стандарту принимать Pass/Fail** — Sort Criteria.

В примере:

```text
Sort Method   = Visual for burrs
Sort Criteria = Max Burr per standard
```

fileciteturn30file0

---

### DIS-GM-024-05 — Identification of conforming ≠ Identification of nonconforming

GM требует определить отдельно способы маркировки good/bad product.

В примере:

```text
CONFORMING
→ White paint dot near defect area

NONCONFORMING
→ Mark defect with red paint
```

fileciteturn30file0

---

### DIS-GM-024-06 — Containment Scope ≠ Containment Result

Scope определяет **что и где должно быть проверено**.

Result показывает **что реально найдено после выполнения containment**.

---

### DIS-GM-024-07 — Worksheet ≠ Customer Notification

Worksheet может **trigger a customer notification if an escape is possible**, но сам факт наличия Worksheet не означает, что customer notification обязательно произошёл.

---

# 5. GM-FORMULATIONS

> “A Containment worksheet shall be used and completed to provide a systematic approach to containing all suspect product.”

> “Identify a potential quantity and all areas to be checked for nonconforming product.”

> “Reconcile expected quantities of suspect material vs. actual.”

> “Document the defect condition and standard to be met.”

> “Document the sort method.”

> “Specify the identification method for sorted good/bad product.”

> “Track and document results of the containment activity.”

> “Trigger a customer notification if an escape is possible.”

Формулировки приведены как SOURCE claims; CMOC interpretation ниже не является утверждением GM.

---

# 6. EXTRACTION

Worksheet задаёт управляемую конструкцию containment:

```text
PROBLEM / SUSPECT PRODUCT
          ↓
PRODUCT CONTAINMENT SCOPE
          ↓
IDENTIFY ALL POTENTIAL AREAS
          ↓
POTENTIAL QUANTITY
          ↓
VERIFICATION
          ↓
FOUND QUANTITY
          ↓
SORT AGAINST STANDARD
          ↓
IDENTIFY GOOD / BAD
          ↓
RECONCILE EXPECTED ↔ ACTUAL
          ↓
TRACK / DOCUMENT RESULTS
          ↓
ESCAPE POSSIBLE?
       ↓          ↓
      NO         YES
                  ↓
       CUSTOMER NOTIFICATION
```

Заполненный пример делает эту конструкцию операциональной: Laboratory, WIP Storage Areas, Outside Processing, Scrap Bins, Rework Areas и другие потенциальные места имеют quantity / verification / responsibility; затем задаются segregation location, sort method, sort criteria и identification method. fileciteturn30file0

---

# 7. REL

### SOURCE-SUPPORTED

```text
Containment Scope
      ↓
Potential Locations / Quantity
      ↓
Verification
      ↓
Found Quantity
      ↓
Sort Method + Sort Criteria
      ↓
Conforming / Nonconforming Identification
      ↓
Reconciliation
      ↓
Containment Result
```

Отдельная ветвь:

```text
Containment Result
      ↓
Escape Possible?
      ↓
Customer Notification
```

---

# 8. MECHANISM

## CANDIDATE — Containment Planning & Reconciliation Mechanism

**INPUT:** suspect product + известная/предполагаемая область его нахождения.

**TRANSFORMATION:** Worksheet заставляет определить scope, потенциальные locations и quantity, назначить verification/responsibility, задать способ и критерий сортировки, определить маркировку и сопоставить expected с actual.

**OUTPUT:** структурированная и проверенная картина containment activity.

**ORGANIZATIONAL EFFECT:** снижается вероятность пропуска потенциально затронутой продукции и появляется проверяемое основание утверждать, что охват containment выполнен.

**STATUS: CANDIDATE / SINGLE-SOURCE**

---

# 9. CAPABILITY

**NONE**

Отдельную Capability из этой вагонетки не выделяем.

---

# 10. CORE CANDIDATE

> **Containment Worksheet — воспроизводимая структурирующая конструкция, которая переводит containment из общего намерения в заданный scope, перечень потенциальных мест и количества, проверку, сортировку по заданному критерию, идентификацию результатов, reconciliation и документированный результат.**

**STATUS: CANDIDATE / SINGLE-SOURCE**

---

# 11. MACHINE

## CANDIDATE MACHINE — Containment Worksheet

Здесь мы возвращаемся к нашей дискуссии о Fast Response Board.

Worksheet имеет основания рассматриваться не просто как Record:

```text
INPUT
Suspect Product / Containment Issue
        ↓
STRUCTURE
Scope + Locations + Quantity + Responsibility
        ↓
EXECUTION SUPPORT
Verification + Sort Method + Sort Criteria
        ↓
CLASSIFICATION
Conforming / Nonconforming
        ↓
IDENTIFICATION
Good / Bad marking
        ↓
RECONCILIATION
Expected ↔ Actual
        ↓
OUTPUT
Documented Containment Result
        ↓
EFFECT
Controlled / accounted-for suspect population
+ possible customer notification trigger
```

В отличие от простой таблицы, Worksheet **задаёт последовательность операций и необходимые поля, через которые операция должна быть выполнена**.

Но важная оговорка:

> SOURCE не называет Worksheet “machine”. Это **CMOC classification**, поэтому статус остаётся `CANDIDATE / SINGLE-SOURCE`.

---

# 12. CHAIN

### SOURCE-SUPPORTED

```text
SUSPECT PRODUCT
      ↓
DEFINE SCOPE
      ↓
IDENTIFY POTENTIAL LOCATIONS
      ↓
VERIFY
      ↓
SORT
      ↓
IDENTIFY GOOD / BAD
      ↓
RECONCILE
      ↓
DOCUMENT RESULT
```

В примере GM эта цепочка получает количественное подтверждение:

```text
Potential / Verified locations
          ↓
2548 pcs
          ↓
TOTAL FOUND 2548 / 2548
```

fileciteturn30file0

---

# 13. STATUS

**CANDIDATE / SINGLE-SOURCE**

Никакого CANON.

---

# 14. CMOC INTERPRETATION

Здесь появляется важная граница между **Record** и **Machine**.

Обычный Record отвечает:

> **Что произошло?**

А GM Containment Worksheet одновременно задаёт:

> **Что проверить? Где проверить? Сколько ожидать? Кто проверяет? Как проверить? По какому критерию? Как маркировать результат? Что фактически найдено? Совпало ли это с ожиданием?**

Поэтому наиболее сильная интерпретация:

> **Worksheet становится кандидатом на Machine не из-за того, что он является таблицей, а потому что его структура организует и ограничивает выполнение воспроизводимой операции containment.**

Это напрямую поддерживает нашу предыдущую дискуссию о Fast Response Tracking Board:

```text
TABLE / BOARD / FORM
        ≠
MACHINE

но

TABLE / BOARD / FORM
        может быть
REALIZATION OF A MACHINE
```

В GM-024 мы пока имеем основания считать **Containment Worksheet самой реализацией кандидатной машинки**, а не отдельным классом от неё.

При этом заполненный пример особенно важен: он показывает, что конструкция не теоретическая — она содержит реальные locations, quantities, responsibilities, criteria, identification и reconciliation. fileciteturn30file0

---

# 15. INTER-SOURCE NOTE

Потенциально очень сильная точка для последующего сопоставления с ISO/DIS 9001:2025 по темам:

- control of nonconforming outputs;
- documented information;
- evidence;
- identification and traceability;
- actions concerning nonconformity.

Но **межисточниковое подтверждение здесь не выполняется**.

---

## PATCH DISCIPLINE

Новый PATCH относится только к GM-024.

Не изменяются:

- CORE;
- каталоги;
- GM-021;
- GM-022;
- GM-023;
- предыдущие LAB/PATCH.

# GM-096 — Banking Process: Passport → Cross-Check

**Извещение на изменение:** `0133+170926`

## 1. Назначение

Провести PASSPORT → CROSS-CHECK для кандидата **Banking Process**, выделенного
из GM Quality System Basics rev March 2009, Managing Change, pp. 336–339.

Проверка отвечает на вопрос: является ли Banking Process самостоятельной
специализированной Machine или лишь комбинацией механизмов управления
материалом в состоянии extended storage.

---

## 2. Source Basis

GM QSB описывает Banking Process как систему идентификации, защиты и retrieval
parts, находящихся на extended storage.

В рассмотренных страницах явно заданы:

- случаи применения: business transfers, engineering changes, tool refurbishments,
  planned shutdowns;
- роли Material Manager, Operations Manager, Quality Manager;
- approved racks / dunnage;
- clear date / lot tags;
- FIFO;
- защита от rust, contamination, mold, distortion;
- protected material;
- weekly LPA;
- corrective actions;
- quality requirements before shipment.

Источник тем самым описывает не отдельный приём хранения, а связанный набор
управляемых действий вокруг специального состояния материала.

---

## 3. Identity Test

### 3.1 Bounded problem

Да.

Banking возникает при чётко определённом состоянии: материал длительно
находится вне нормального производственного потока.

### 3.2 Bounded trigger

Да.

Триггером является необходимость extended storage в предусмотренных GM
ситуациях.

### 3.3 Reproducible construction

Да.

Последовательность воспроизводима:

`identify → store/protect → tag → FIFO → periodically verify → correct → verify quality → release`

### 3.4 Defined output

Да.

Материал остаётся идентифицированным, защищённым и проверенным до его
использования или shipment.

### 3.5 Defined roles / artifacts

Да.

Источник задаёт ответственные роли и набор управленческих артефактов / следов:
маркировка, LPA, corrective actions, quality verification.

**Вывод:** Identity Test пройден.

---

## 4. Boundary Test

### FIFO

Не отдельная Machine в рамках Banking.

FIFO является одним из механизмов управления запасом внутри Banking.

### Identification / Traceability

Не отдельная Banking Machine.

Идентификация обеспечивает сохранение связи материала с date / lot и его
контролируемым состоянием.

### Preservation / Contamination Control

Сильное пересечение.

Однако рассмотренный Banking включает не только физическую защиту материала,
но также идентификацию, размещение, FIFO, периодическую LPA, corrective action
и проверку качества перед shipment.

Поэтому в текущем cross-check preservation рассматривается как capability /
mechanism внутри Banking, а не как достаточная замена всей конструкции.

### LPA / Audit

LPA — механизм периодической проверки Banking.

Связь с существующим `MC-009-15 Audit` — **NEW PROVENANCE**, а не новая
самостоятельная Audit Machine.

### Corrective Action

Механизм реакции на обнаруженное отклонение.

Не самостоятельная Banking Machine.

### Quarantine

В рассмотренных страницах нет основания отождествлять Banking с quarantine.

Banking — длительное управляемое хранение; quarantine требует отдельного
состояния и отдельной цели блокировки / решения о статусе.

**Вывод:** Banking имеет собственную bounded identity, несмотря на составность.

---

## 5. Machine / Mechanism / Assembly Test

### Machine

**Да, как специализированный кандидат.**

Причина: конструкция имеет собственный trigger, специальное состояние,
последовательность действий, роли, контрольные точки и определённый выход
в виде управляемого материала, готового к дальнейшему решению.

### Mechanism

Отдельные элементы Banking являются механизмами:

- identification;
- FIFO;
- preservation;
- LPA;
- corrective action;
- quality verification.

Но их композиция в Banking образует более широкую воспроизводимую конструкцию.

### Assembly

Banking действительно **composes** несколько механизмов, однако сама
композиция имеет устойчивую предметную границу: extended-storage material.
Поэтому на текущем уровне она не сводится к произвольной Assembly.

---

## 6. Duplicate Test against Current CMOC

### `MC-009-15 Audit`

Нет дубликата.

Audit / LPA проверяет состояние; Banking управляет состоянием материала.

### `MP-002 Response to Abnormality`

Нет дубликата.

Banking не является реакцией на abnormality; extended storage может быть
плановым состоянием.

### `MP-003 Problem Solving`

Нет дубликата.

Corrective action внутри Banking не превращает Banking в Problem Solving Machine.

### Contamination Control architecture

Есть частичное пересечение по physical protection, но Banking шире и имеет
собственную bounded state.

**Вывод:** прямого дубликата среди проверенных текущих конструкций не найдено.

---

## 7. Architectural Position

Banking следует размещать в CMOC как специализированную Machine для
управления материалом в состоянии extended storage.

Упрощённая цепочка:

`Material → Extended Storage → Identification / Protection → Periodic Verification → Correction → Quality Verification → Release`

При этом Banking не следует трактовать как универсальную Machine хранения
или сохранения материальных объектов.

---

## 8. Passport Verdict

**STATUS:** `SPECIALIZED-CANDIDATE / NON-CANON`

**EVIDENCE LEVEL:** `SINGLE-SOURCE`

**BOUNDARY:** extended-storage material

**TYPE:** `MATERIAL STATE CONTROL / PRESERVATION`

**MACHINE TEST:** PASS

**DUPLICATE TEST:** PASS — прямого дубликата не выявлено

**GENERALIZATION:** НЕ ДОПУСКАТЬ до независимой проверки аналогичных конструкций

---

## 9. CMOC Decisions

### NEW SPECIALIZED MACHINE CANDIDATE

- `MC-CAND-096-03 Banking Process`

### EXISTING MACHINE / NEW PROVENANCE

- LPA → `MC-009-15 Audit`

### MECHANISMS / COMPONENTS

- Identification
- FIFO
- Preservation
- Contamination Control
- Periodic Verification / LPA
- Corrective Action
- Quality Verification

### ASSEMBLY ASPECT

Banking composes several mechanisms, but its bounded extended-storage state
supports retaining Machine-candidate identity.

---

## 10. REG-001 / Canon / Catalog Impact

- **REG-001:** NO CHANGE
- **Canon:** NO CHANGE
- **MACHINE-CATALOG:** NO direct catalog promotion
- **Passport:** CREATED
- **Status:** NON-CANON

This patch records the passport and cross-check only.

---

## 11. Next Evidence

Следующий обязательный cross-check — независимые конструкции:

- Material Preservation;
- Controlled Storage;
- Quarantine / Hold;
- Inventory / FIFO control.

Цель — проверить, сохраняется ли отличительная граница Banking как
специализированной Machine или она должна быть понижена до Assembly / Mechanism.

**VERDICT:** Banking Process имеет достаточную bounded identity для статуса
**SPECIALIZED-CANDIDATE**, но остаётся `NON-CANON` до multi-source confirmation.

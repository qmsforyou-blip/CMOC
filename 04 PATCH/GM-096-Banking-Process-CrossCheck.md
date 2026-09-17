# GM-096 — Banking Process — Cross-Check

## Извещение на изменение

**0127+170926**

---

## 1. OBJECT OF CHECK

GM-096, section **11.4 Banking Process**, pp. 336–339.

Вопрос:

> является ли Banking Process самостоятельной Machine, либо набором требований к хранению материала?

**Working verdict:** `SPECIALIZED MACHINE CANDIDATE / NON-CANON`.

---

## 2. SOURCE-DERIVED PURPOSE

GM требует от поставщика процедуру для **identification, protection and retrieval of parts when stored for extended periods of time**.

Источник приводит случаи:

- Business transfers / BTAB Tool moves;
- Engineering changes;
- Tool refurbishments;
- Planned shutdowns.

Ответственность разделена:

- Material Manager — implementation, execution, traceability;
- Operations Manager — protective packaging and storage;
- Quality Manager — quality control process.

fileciteturn557file0L12-L24

---

## 3. SOURCE-DERIVED CONTROL LOGIC

Минимальная логика:

```text
NEED FOR EXTENDED STORAGE
        ↓
IDENTIFY MATERIAL
        ↓
CONTROLLED STORAGE
        ↓
PROTECT MATERIAL
        ↓
MONITOR STORAGE CONDITIONS
        ↓
RETRIEVE / RELEASE
        ↓
QUALITY REQUIREMENTS BEFORE SHIPMENT
```

GM задаёт конкретные controls:

- approved racking / dunnage;
- clear tagging: date, lot etc.;
- FIFO;
- защита от воды, масла, влажности, температуры и других факторов, способных вызвать rust, contamination, mold, distortion;
- protection of banked material;
- weekly LPA;
- documentation of LPA issues and corrective actions;
- quality requirements before shipment.

fileciteturn557file1L172-L183

---

## 4. DISTINCTIONS

### D-01

**Banking ≠ ordinary storage**

Source defines Banking specifically for material held for extended periods and associates it with defined preservation, identification and retrieval controls.

### D-02

**Storage ≠ Preservation**

Наличие места хранения само по себе не обеспечивает защиту материала от факторов деградации.

### D-03

**Identification ≠ Traceability ≠ Protection**

Tagging, traceability и preservation выполняют разные функции внутри одного процесса.

### D-04

**FIFO ≠ Quality Release**

FIFO управляет очередностью использования, но не заменяет проверку quality requirements перед shipment.

### D-05

**LPA ≠ Banking Process**

Weekly LPA является механизмом проверки соблюдения Banking Process, а не самим процессом.

### D-06

**Banking ≠ Change Control**

Change Control управляет изменением процесса; Banking управляет материалом, который необходимо сохранить во время длительного хранения.

---

## 5. MACHINE TEST

| Test | Result |
|---|---|
| Explicit trigger / use condition | YES |
| Defined object | YES — banked material |
| Defined roles | YES |
| Defined controls | YES |
| Identification / traceability | YES |
| Preservation requirements | YES |
| Monitoring / audit | YES |
| Retrieval / release logic | YES |
| Reusable procedure | YES |
| Source explicitly requires procedure | YES |

**Result:** sufficient basis for a specialized Machine candidate.

---

## 6. CMOC CLASSIFICATION

**Banking Process:** `SPECIALIZED MACHINE CANDIDATE`

Не Canon.

Не следует автоматически дробить на отдельные Machines:

- Storage;
- Tagging;
- FIFO;
- LPA;
- Packaging.

В source они образуют составные элементы единого Banking Process.

---

## 7. ARCHITECTURAL VALUE

Banking Process показывает важную связку:

```text
MATERIAL
   ↓
IDENTITY
   ↓
LOCATION / STORAGE STATE
   ↓
PROTECTION
   ↓
MONITORING
   ↓
RETRIEVAL
   ↓
QUALITY RELEASE
```

То есть управляемость здесь возникает не из факта хранения, а из **контролируемого жизненного цикла материала вне обычного производственного потока**.

---

## 8. RELATION TO OTHER MACHINES

```text
Plant Process Change Control
          ↓
      may trigger
          ↓
     Banking Process
          ↓
 preservation / traceability
          ↓
    Quality Release
```

Banking может быть вызвано Engineering Change, Tool Move, Tool Refurbishment или Planned Shutdown, но не является самой машиной изменения.

---

## 9. FINAL WORKING VERDICT

> **Banking Process — самостоятельный специализированный Machine candidate, управляющий идентификацией, сохранностью, контролем и возвратом материала после длительного хранения. Отдельные controls (FIFO, tagging, LPA, packaging) являются компонентами машины, а не самостоятельными Machines.**

**STATUS:** `SPECIALIZED MACHINE CANDIDATE / NON-CANON`

---

## 10. DECISION RECORD

- New Top-Level Machine: NO.
- Specialized Machine candidate: YES — `Banking Process`.
- Existing CMOC duplication found: NO.
- REG-001: unchanged.
- Canon: unchanged.
- Source provenance preserved.

**Next check:** `Production Trial Run (PTR)` — pp. 333–335, если не закрыт отдельным PATCH; затем финальная сверка всего блока Managing Change.

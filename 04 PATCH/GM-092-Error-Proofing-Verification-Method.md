# GM-092 — Error Proofing Verification — Method of Verification

## SOURCE

**Source:** GM Quality System Basics Overview Supplier Audit.pdf  
**Section:** 6.2 — Method of Verification  
**Pages:** 216–217 (визуальные страницы SOURCE; содержание извлечено по предоставленным изображениям)

**Статус:** SOURCE-SUPPORTED extraction; CMOC interpretations explicitly separated.

---

## 1. SOURCE EXTRACTION

SOURCE устанавливает метод проверки error proofing / detection devices.

Все устройства, которые могут отказать, износиться, сместиться или иным образом выйти из регулировки, должны проверяться **как минимум один раз в день**.

При установлении частоты проверки SOURCE предлагает учитывать:

- размер партии изделий, проходящих между проверками;
- историю процесса;
- устойчивость (robustness) процесса;
- простоту локализации/изоляции подозрительной продукции.

Предпочтительный метод — выполнение проверки членом команды / лидером при запуске и в течение смены.

SOURCE отдельно поясняет, что проверка не является mastering gage, например установкой калибра на ноль. Проверка заключается в пропускании через устройство **заведомо годных и заведомо дефектных деталей** для подтверждения корректной работы устройства.

---

## 2. SOURCE DEFINITIONS

### Error Proofing Device

**CAN NOT MAKE** — устройство, которое не допускает изготовление или сборку несоответствующей продукции.

### Error Detection Device

**CAN NOT PASS / CAN NOT ACCEPT** — устройство, которое не допускает передачу несоответствующей продукции дальше по потоку; SOURCE приводит в качестве примера 100% in-line inspection equipment.

SOURCE указывает, что в данном разделе термин **error proofing device** используется как общий термин, включающий как error proofing, так и error detection devices.

---

## 3. DOCUMENTATION REQUIREMENTS FROM SOURCE

SOURCE требует, чтобы устройства были проверены, а их расположение документировано.

Должен существовать master document устройств с:

- идентификационным номером;
- местом расположения.

Также должны быть документированы:

- периодичность проверки;
- используемые masters (Good / Bad);
- дефект, который проверяется;
- требования к сертификации всех masters.

---

## 4. DISTINCTIONS

### D1 — Presence of a device is not verification of the device

**Status: SOURCE-SUPPORTED**

Наличие error proofing / detection device само по себе не подтверждает его работоспособность. Устройство должно регулярно проверяться.

### D2 — Verification frequency is risk/process dependent, but has a minimum

**Status: SOURCE-SUPPORTED**

SOURCE устанавливает минимум — **один раз в день**, одновременно связывая фактическую частоту с размером партии, историей процесса, устойчивостью процесса и возможностью локализации подозрительной продукции.

### D3 — Verification is a process activity, not only a maintenance activity

**Status: SOURCE-SUPPORTED**

Предпочтительно, чтобы проверка выполнялась членом команды / лидером при запуске и в течение смены.

### D4 — Verification is not gage mastering

**Status: SOURCE-SUPPORTED**

SOURCE прямо различает проверку error proofing device и mastering gage. Проверяется способность устройства правильно реагировать на известные хорошие и плохие детали.

### D5 — Verification uses known-good and known-bad masters

**Status: SOURCE-SUPPORTED**

Доказательство корректной работы устройства получают через пропускание заведомо годных и заведомо дефектных деталей.

### D6 — Error proofing and error detection are different mechanisms

**Status: SOURCE-SUPPORTED**

**Error proofing** предотвращает изготовление / сборку несоответствующей продукции (**CAN NOT MAKE**), тогда как **error detection** предотвращает её прохождение / принятие (**CAN NOT PASS / CAN NOT ACCEPT**).

### D7 — Different mechanisms may be managed under one control term

**Status: SOURCE-SUPPORTED**

Несмотря на различие механизмов CAN NOT MAKE и CAN NOT PASS / ACCEPT, данный раздел SOURCE использует общий термин **error proofing device**.

### D8 — Device identity and physical location are controlled information

**Status: SOURCE-SUPPORTED**

Для устройств требуется master document с идентификационным номером и местом расположения.

### D9 — The verification object must be explicit

**Status: SOURCE-SUPPORTED**

Должно быть определено, какие Good / Bad masters используются и какой именно дефект ими проверяется.

### D10 — Masters themselves require defined certification requirements

**Status: SOURCE-SUPPORTED**

SOURCE требует определить требования к сертификации всех masters, используемых при проверке.

---

## 5. MECHANISM

### SOURCE-SUPPORTED

```text
IDENTIFY DEVICE
      ↓
DEFINE VERIFICATION FREQUENCY
      ↓
SELECT GOOD / BAD MASTERS
      ↓
CHECK KNOWN-GOOD / KNOWN-BAD PARTS
      ↓
CONFIRM DEVICE RESPONSE
      ↓
DOCUMENT / CONTROL RESULT
```

Частота выбирается с учётом:

```text
LOT SIZE
PROCESS HISTORY
PROCESS ROBUSTNESS
CONTAINMENT EASE
        ↓
VERIFICATION FREQUENCY
```

### CMOC INTERPRETATION / CANDIDATE

```text
PROTECTION MECHANISM
        ↓
TEST CONDITION
        ↓
OBSERVED RESPONSE
        ↓
VERIFIED / NOT VERIFIED
        ↓
STATUS / RECORD
```

Это **не Canon**. SOURCE поддерживает проверку и документирование, но не формулирует данную последовательность в терминах CMOC.

---

## 6. CAPABILITY

**SOURCE-SUPPORTED:** организация должна быть способна подтвердить, что error proofing / detection devices работают так, как предназначено.

**CMOC INTERPRETATION / CANDIDATE:** verification переводит устройство из состояния «установлено» в состояние «подтверждена способность выполнять защитную функцию».

Эта формулировка пока не Canon.

---

## 7. MACHINE

**Candidate Machine:** Error-Proofing Verification Machine.

```text
DEVICE
  ↓
GOOD / BAD MASTER
  ↓
TEST
  ↓
RESPONSE
  ↓
VERIFICATION STATUS
```

**Status:** CANDIDATE.

Не повышать до CANON до дальнейшего анализа разделов 6.2–6.4 и связанных механизмов управления записями.

---

## 8. CHAIN

### SOURCE-SUPPORTED chain

```text
ERROR PROOFING / DETECTION DEVICE
            ↓
GOOD / BAD MASTER
            ↓
VERIFICATION
            ↓
CONFIRM CORRECT OPERATION
```

### CMOC candidate

```text
REQUIREMENT
    ↓
PROTECTION MECHANISM
    ↓
TEST
    ↓
OBSERVED RESPONSE
    ↓
STATUS
    ↓
RECORD
```

Последняя цепочка является CMOC-интерпретацией.

---

## 9. CMOC INTERPRETATION

Ключевой результат страниц 216–217: **защитный механизм нельзя считать управляемым только потому, что он установлен**.

SOURCE требует воспроизводимой проверки его способности обнаружить или предотвратить дефект через использование известных Good / Bad masters, с определённой частотой и документированными параметрами.

Особенно сильное различение:

```text
DEVICE EXISTS
      ≠
DEVICE VERIFIED
```

и:

```text
GAGE MASTERING
      ≠
ERROR-PROOFING VERIFICATION
```

---

## 10. STATUS

| Construction | Status |
|---|---|
| Minimum verification at least once per day | SOURCE-SUPPORTED |
| Frequency considers lot size | SOURCE-SUPPORTED |
| Frequency considers process history | SOURCE-SUPPORTED |
| Frequency considers process robustness | SOURCE-SUPPORTED |
| Frequency considers containment ease | SOURCE-SUPPORTED |
| Verification at start-up and throughout shift | SOURCE-SUPPORTED |
| Verification uses known-good and known-bad parts | SOURCE-SUPPORTED |
| Error proofing = CAN NOT MAKE | SOURCE-SUPPORTED |
| Error detection = CAN NOT PASS / CAN NOT ACCEPT | SOURCE-SUPPORTED |
| Common umbrella term in this section | SOURCE-SUPPORTED |
| Device ID and location documented | SOURCE-SUPPORTED |
| Verification frequency documented | SOURCE-SUPPORTED |
| Good/Bad masters and defect identified | SOURCE-SUPPORTED |
| Master certification requirements defined | SOURCE-SUPPORTED |
| Verification as proof of protection capability | CMOC INTERPRETATION |
| Error-Proofing Verification Machine | CANDIDATE |
| REQUIREMENT → MECHANISM → TEST → RESPONSE → STATUS → RECORD | CMOC INTERPRETATION |
| CANON | No |

---

## 11. SOURCE BOUNDARY

Не добавляются внешние требования к error proofing, калибровке, MSA, метрологическому обеспечению или управлению записями, которых нет в предоставленных страницах.

В частности, SOURCE здесь задаёт минимум ежедневной проверки и факторы выбора частоты, но не устанавливает единственную универсальную частоту для всех процессов сверх этого минимума.

---

## 12. LINK TO NEXT SOURCE BLOCK

Следующий блок — продолжение **6.2 — Method of Verification**.

Ключевой вопрос для продолжения:

> Какие дополнительные правила SOURCE устанавливает для verification, ownership, records и management review?

# GM-096 — Controlled Deviation / Control Means Verification — Cross-Check

**Извещение на изменение:** 0134+170926

## 1. Цель

Проверить две выделенные конструкции GM-096 на предмет самостоятельности
Machine относительно уже существующих Machine Patterns и механизмов CMOC.

Результат должен отделить bounded Machine от Mechanism / Pattern и не допустить
разрастания каталога из отдельных контрольных приёмов.

## 2. Source Basis

GM Quality System Basics rev March 2009 — Managing Change, pp. 340–343,
связанные с Bypass Process Control.

## 3. Controlled Deviation

### 3.1 Наблюдаемая конструкция

В GM-096 bypass возникает, когда производственный процесс изменяется вне
утверждённого документированного Control Plan. Для такого состояния задаются
ограничения, проверки, ответственность и условия возврата.

### 3.2 Boundary Test

Само `deviation` не образует самостоятельного жизненного цикла Machine.
Оно обозначает отношение текущего состояния к установленному стандарту:

`Approved State → Deviation → Control / Decision → Return or Continued Exception`

Конкретная реализация может быть различной: Bypass Process Control,
Controlled Deviation в другой системе, временное разрешение, concession,
temporary instruction и т.п.

Следовательно, в CMOC `Controlled Deviation` правильнее сохранить как:

**MECHANISM / PATTERN — NON-CANON**

а не создавать `MC-CAND`.

### 3.3 Связи

- Bypass Process Control — специализированная Machine, реализующая этот механизм.
- Decision Gate — механизм принятия решения.
- Response to Abnormality — существующий Pattern.
- Assessment against Criterion — существующий Pattern.

## 4. Control Means Verification

### 4.1 Наблюдаемая конструкция

GM-096 требует проверять параметры, settings и parts перед возвратом из bypass.
Проверка направлена на подтверждение того, что контролируемое средство /
процесс соответствует установленным требованиям перед переходом состояния.

### 4.2 Boundary Test

`Control Means Verification` не имеет в рассмотренном фрагменте GM-096
самостоятельного trigger → input → action → output → responsibility lifecycle.
Она является проверочным механизмом внутри более крупных конструкций.

Типовая форма:

`Requirement → Verification → Evidence → Decision`

Это фундаментальная verification construction, а не отдельная Machine.

Следовательно:

**MECHANISM — NON-CANON**

### 4.3 Связи

- Bypass Process Control использует verification перед возвратом.
- PTR использует evaluation / verification для обработки результата trial.
- Audit / LPA является другим специализированным способом проверки.
- Assessment against Criterion — более общий Pattern.

## 5. Duplicate / Overlap Test

| GM construction | CMOC classification | Existing relation |
|---|---|---|
| Controlled Deviation | Mechanism / Pattern | Bypass Process Control, MP-002, Decision Gate |
| Control Means Verification | Mechanism | MP-005, Audit / LPA, verification mechanisms |
| Bypass Process Control | Specialized Machine Candidate | uses both |

Критерий разделения:

**Machine** замыкает воспроизводимый жизненный цикл управляемого состояния.

**Mechanism** реализует отдельную функцию внутри такого жизненного цикла.

**Pattern** описывает повторяемую форму организации управления, применимую
в разных Machines.

## 6. Архитектурный результат

GM-096 не даёт оснований создавать две новые Machine только потому, что
в тексте присутствуют `Controlled Deviation` и `Control Means Verification`.

Наоборот, они укрепляют внутреннюю архитектуру уже выделенной Bypass Machine:

`Bypass Machine`
→ `Controlled Deviation`
→ `Monitoring / Audit`
→ `Control Means Verification`
→ `Decision / Authorization`
→ `Return`

## 7. Решение CMOC

### Controlled Deviation

**Classification:** `MECHANISM / PATTERN`

**Status:** `NON-CANON`

**Action:** отдельный Machine passport не создавать.

### Control Means Verification

**Classification:** `MECHANISM`

**Status:** `NON-CANON`

**Action:** отдельный Machine passport не создавать.

## 8. REG-001 / Canon / Catalog

- REG-001 — без изменений.
- Canon — без изменений.
- MACHINE-CATALOG — без изменений.
- Новых Machine Candidates не создаём.

## 9. Verdict

GM-096 в данном месте показывает хороший пример принципа CMOC:

> **не каждый устойчиво повторяющийся управленческий приём является Machine.**

`Controlled Deviation` и `Control Means Verification` являются строительными
механизмами / паттернами, которые могут входить в состав разных Machines.

Их выделение как самостоятельных Machine привело бы к искусственному
дроблению каталога.

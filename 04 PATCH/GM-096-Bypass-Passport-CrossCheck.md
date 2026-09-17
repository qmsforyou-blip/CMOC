# GM-096 — Bypass Process Control — Passport Cross-Check

**Извещение на изменение:** 0133+170926

## 1. Цель

Зафиксировать паспорт кандидата `MC-CAND-096-04 Bypass Process Control` и
проверить его границы относительно уже выделенного `Controlled Deviation`,
Fast Response / Andon, LPA / Audit и Verification.

Паспорт не означает канонизацию и не изменяет REG-001 или Canon.

## 2. Основание источника

GM Quality System Basics rev March 2009 — Managing Change, pp. 340–343.

Источник устанавливает Bypass Process Control для случая, когда процесс
изменён вне утверждённого документированного Control Plan. Manufacturing
Process Backup Worksheet фиксирует точки входа / выхода и требования к
оснастке, инспекции и аудиту. Активный bypass рассматривается в Fast Response;
для каждого bypass проводится LPA; операторы обучаются / сертифицируются;
перед возвратом проверяются параметры и settings, parts валидируются,
а возврат утверждается Operations Manager.

## 3. Boundary Test

### 3.1 Bypass Process Control vs Controlled Deviation

`Controlled Deviation` отвечает на более общий вопрос: как управлять
отклонением от установленного состояния.

`Bypass Process Control` содержит более узкую и замкнутую конструкцию:

`entry → defined safeguards → active monitoring → qualification → verification → validation → authorized return`.

Следовательно, Bypass не сводим полностью к самому механизму Controlled
Deviation, хотя явно его реализует.

**Решение:** специализированная Machine-кандидат; Controlled Deviation
сохранить как более общий механизм / паттерн.

### 3.2 Bypass vs Fast Response / Andon

Fast Response обеспечивает реакцию и обзор abnormal state. В GM-096 он
используется для ежедневного review активного bypass, но не исчерпывает
его конструкцию.

**Решение:** существующая архитектура реакции используется внутри Bypass;
нового дубликата Andon не создаём.

### 3.3 Bypass vs LPA / Audit

LPA является одной из проверок внутри активного bypass. Оно не задаёт
жизненный цикл входа, управления и выхода из bypass.

**Решение:** существующий Audit / LPA — встроенный механизм проверки,
новой Audit Machine не создаём.

### 3.4 Bypass vs Verification

Проверка параметров, settings и parts является частью выхода из bypass.
Verification — механизм, а Bypass — более крупная bounded construction,
в которую Verification входит.

**Решение:** Verification сохранить как механизм, не заменять им Bypass.

## 4. Архитектурная роль

Bypass Process Control занимает позицию между общей Change / Abnormality
архитектурой и конкретным возвратом к штатному процессу:

`Normal Process`
→ `Bypass Trigger`
→ `Controlled Bypass State`
→ `Monitoring / Audit`
→ `Verification`
→ `Authorized Return`
→ `Normal Process`

Это специализированная реализация управления состоянием процесса, а не
универсальная Machine для всех отклонений.

## 5. Решение CMOC

**STATUS:** `SPECIALIZED-CANDIDATE / NON-CANON`

**TYPE:** `CHANGE IMPLEMENTATION / BYPASS CONTROL`

**LEVEL:** `MACHINE`

**EVIDENCE:** `SINGLE-SOURCE`

**Classification:**
- Machine Candidate — Bypass Process Control
- Mechanism / Pattern — Controlled Deviation
- Existing Architecture / Provenance — Fast Response / Andon
- Existing Audit Architecture — LPA
- Mechanism — Verification

## 6. Не делать сейчас

- не канонизировать Bypass Process Control;
- не создавать универсальную `Deviation Machine`;
- не создавать отдельную Machine для LPA внутри Bypass;
- не изменять REG-001;
- не изменять Canon;
- не обновлять MACHINE-CATALOG отдельным каталоговым патчем.

## 7. Следующий cross-check

Найти независимые источники с конструкциями:
- contingency / alternate process control;
- temporary process deviation;
- controlled bypass;
- return-to-standard / restoration verification.

Цель — проверить, является ли замкнутый lifecycle Bypass устойчивой
междоменной конструкцией или спецификой GM QSB.

## 8. Verdict

**GM-096 Bypass Process Control сохраняется как специализированная
Machine-кандидат. Его независимость от общего Controlled Deviation пока
не доказана междоменными источниками, поэтому статус остаётся
SPECIALIZED-CANDIDATE / NON-CANON.**

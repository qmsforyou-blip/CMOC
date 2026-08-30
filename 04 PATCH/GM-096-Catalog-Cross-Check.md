# GM-096 — Catalog Cross-Check

## Извещение на изменение — `0060+300826`

**Файл:** `04 PATCH/GM-096-Catalog-Cross-Check.md`

### Назначение

Проведена архитектурная сверка Machine Candidates, извлечённых из GM QSB, с существующим `MACHINE-CATALOG` CMOC.

Правило: **не создавать новую Machine, если механизм уже представлен существующей Machine или если кандидат является Pattern / Mechanism / Physical Variant.**

---

## Результат сверки

| GM Candidate | Решение |
|---|---|
| Decision Gate | NEW CANDIDATE — требует отдельной паспортизации |
| Controlled Change Implementation | NEW CANDIDATE — проверить связь с Decision Gate |
| Production Trial Run | NEW CANDIDATE |
| Bypass Process Control | NEW CANDIDATE |
| Supplier Capability Assessment | NEW CANDIDATE |
| Systemic Problem Resolution | HOLD — сравнить с Problem Solving / Asaichi |
| Nonconforming Product Control | NEW CANDIDATE |
| Workshop / Action-Plan Conversion | HOLD — сравнить с transformation-machines |
| Layered Process Audit | HOLD — сравнить с существующим Audit / Kamishibai |
| Error-Proofing Verification | HOLD — проверить как возможный подтип Verification |
| Measurement-to-Action Loop | PATTERN / MECHANISM — не Machine |
| Control Means Verification | MECHANISM — не Machine на текущем уровне доказательства |
| Fast Response | HOLD — проверить существующую линию Andon / Response |
| Contamination Control | MECHANISM FAMILY — не Machine |
| Supplier Performance Statusing | MECHANISM — не Machine |
| State Representation | ONTOLOGICAL MECHANISM — не Machine |

---

## Архитектурное решение

GM QSB не должен механически расширять каталог CMOC.

Источник поставляет **provenance и evidence** для механизмов. Machine появляется только после проверки того, что механизм имеет самостоятельную воспроизводимую конструкцию и не дублирует уже существующую Machine.

Особенно важные зоны проверки:

1. `Decision Gate` ↔ существующие Audit / Approval mechanisms;
2. `Systemic Problem Resolution` ↔ `Asaichi` / Problem Solving;
3. `Layered Process Audit` ↔ `Audit` / `Kamishibai`;
4. `Workshop / Action-Plan Conversion` ↔ `Day-One Kaizen Launch` / `Transformation Role Installation`.

---

## Статус

**WORKING / NON-CANON**

Новые Machine в основной каталог этим патчем **не канонизируются и не добавляются автоматически**.

Следующий шаг: паспортизация только тех кандидатов, которые после cross-check признаны самостоятельными CMOC Machine.

## Provenance

Source: GM Quality System Basics Overview / GM QSB.

Related working artifact: `GM-096-Machine-Candidates.md`.

Catalog reference: `03_MACHINE-CATALOG/MACHINE-CATALOG.md.md`.

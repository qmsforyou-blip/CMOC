# GM-096 — Managing Change — Final Cross-Check

## Извещение на изменение

**0129+170926**

---

## 1. OBJECT OF CHECK

**Источник:** GM Quality System Basics rev. March 2009, Managing Change, pp. 323–345.

Задача финальной сверки — не создавать новые Machines по каждому названию GM, а проверить границы уже выделенных кандидатов, их отношения и общий контрольный контур.

---

## 2. SOURCE-DERIVED STRUCTURE

В блоке Managing Change GM последовательно рассматривает:

- Plant Process Change Control;
- Production Trial Run (PTR);
- Banking Process;
- Bypass Process Control;
- затем сводит блок в Summary / Shalls и Key Strategies.

В рассмотренных материалах PTR определён как ограниченная, контролируемая и локализованная производственная проба изменения до полной реализации; GM отдельно отделяет PTR от Product Validation. fileciteturn564file0L12-L28

Communication Form фиксирует шаги, approvals и results PTR. fileciteturn563file0L12-L23

Banking требует отдельной процедуры идентификации, защиты и извлечения материала при длительном хранении и содержит собственные controls хранения, защиты, LPA и quality requirements перед shipment. fileciteturn563file3L351-L398

---

## 3. FINAL CANDIDATE MAP

| GM object | CMOC status | Architectural role |
|---|---|---|
| Plant Process Change Control (PPCR) | MACHINE CANDIDATE / NON-CANON | управление авторизацией, реализацией и закрытием изменения |
| Production Trial Run (PTR) | SPECIALIZED MACHINE CANDIDATE / NON-CANON | контролируемая производственная проба изменения |
| Banking Process | SPECIALIZED MACHINE CANDIDATE / NON-CANON | управление материалом вне обычного производственного потока |
| Bypass Process Control | SPECIALIZED MACHINE CANDIDATE / NON-CANON | управляемое временное альтернативное состояние процесса |
| Controlled Deviation | MECHANISM / PATTERN / NON-CANON | общий паттерн управляемого отклонения |
| Control Means Verification | SPECIALIZED MECHANISM / MACHINE-SUBCANDIDATE | проверка самих средств управления |
| Measurement-to-Action | FUNDAMENTAL PATTERN / NON-CANON | общий цикл observation → response → verification |
| LPA | SPECIALIZED AUDIT FAMILY / HOLD | повторяющаяся многоуровневая проверка |
| Workshop / Action-Plan Conversion | ASSEMBLY / PATTERN / NON-CANON | коллективный переход gap → managed action |
| Systemic Problem Resolution | EXISTING ARCHITECTURE / HOLD | подтверждает существующее Problem Solving family |

---

## 4. CORE CHANGE ARCHITECTURE

Финальная CMOC-интерпретация блока:

```text
                    CHANGE / CHANGE NEED
                           │
                           ▼
              PLANT PROCESS CHANGE CONTROL
                           │
              ┌────────────┴────────────┐
              │                         │
              ▼                         ▼
        NORMAL CHANGE              TRIAL REQUIRED
              │                         │
              │                         ▼
              │                PRODUCTION TRIAL RUN
              │                         │
              │                         ▼
              │                QUALITY / EVALUATION
              │                         │
              └────────────┬────────────┘
                           ▼
                    IMPLEMENTED STATE
                           │
             ┌─────────────┼─────────────┐
             │             │             │
             ▼             ▼             ▼
          NORMAL        BANKING       BYPASS
          FLOW          MATERIAL      STATE
             │             │             │
             │             ▼             ▼
             │       PRESERVE /       CONTROL /
             │       RETRIEVE         VERIFY
             │                           │
             └──────────────┬────────────┘
                            ▼
                    VERIFICATION / REVIEW
                            │
                            ▼
                     ACCEPTED / CLOSED
```

Это **архитектурная модель CMOC**, а не утверждение, что GM представляет все эти элементы как один буквальный flow chart.

---

## 5. BOUNDARY TEST

### PPCR ≠ PTR

PPCR управляет самим процессом изменения: инициирование, маршрутизация, approval, implementation, recording и final approval. Его отдельная граница подтверждена предыдущим cross-check. fileciteturn579file0L2-L2

PTR имеет собственную defined procedure, readiness review, controlled tryout и quality review. Поэтому объединять его с PPCR не следует. fileciteturn580file0L1-L2

### PPCR ≠ Banking

Banking не управляет изменением процесса; он управляет сохранностью материала при длительном хранении. fileciteturn585file0L1-L2

### PPCR ≠ Bypass

Bypass является специальным режимом процесса при выходе за пределы утверждённого Control Plan / normal process и имеет собственные entry, monitoring, exit и verification requirements.

### Controlled Deviation ≠ Bypass Process Control

Controlled Deviation остаётся более общим паттерном; Bypass Process Control — специализированной реализацией этого паттерна. fileciteturn588file0L1-L2

### Measurement-to-Action ≠ отдельная Machine

Measurement-to-Action проходит через разные GM-контексты и поэтому остаётся фундаментальным control-loop pattern. fileciteturn586file0L1-L2

---

## 6. THE MAIN ARCHITECTURAL FINDING

GM-096 не столько добавляет четыре независимые Machines, сколько показывает **грамматику управляемого изменения**.

В ней различаются по меньшей мере четыре разных вопроса:

```text
1. МОЖНО ЛИ ИЗМЕНЯТЬ?
   → Plant Process Change Control

2. НУЖНО ЛИ СНАЧАЛА ИСПЫТАТЬ ИЗМЕНЕНИЕ?
   → Production Trial Run

3. ЧТО ДЕЛАТЬ С МАТЕРИАЛОМ ВНЕ ОБЫЧНОГО ПОТОКА?
   → Banking Process

4. ЧТО ДЕЛАТЬ, ЕСЛИ НОРМАЛЬНЫЙ ПРОЦЕСС ВРЕМЕННО НЕДОСТУПЕН?
   → Bypass Process Control
```

И поверх них работают более общие механизмы:

```text
Measurement-to-Action
Control Means Verification
Controlled Deviation
LPA / Verification
```

---

## 7. KEY STRATEGIES — NO AUTOMATIC NEW MACHINES

Страница 345 перечисляет Key Strategies, включая Fast Response, NCP Control, Verification Station, Standardized Operations, Standardized Operator Training, Error Proofing Verification, LPA, Risk Reduction, Contamination Control, SCM и Managing Change.

Факт наличия этих названий на Summary page сам по себе не является основанием создавать по Machine на каждую стратегию.

В частности, уже выполненные cross-check показывают:

- Error-Proofing Verification → specialization of Control Means Verification;
- LPA → Audit family / possible System Machine;
- Systemic Problem Resolution → existing Problem Solving architecture;
- Fast Response и остальные стратегии требуют отдельного cross-check только если понадобится их самостоятельная архитектурная граница.

---

## 8. WHAT IS NOW PROVEN / WHAT IS NOT

### Strongly established within GM-096

- distinct PPCR boundary;
- distinct PTR boundary;
- distinct Banking boundary;
- distinct Bypass boundary;
- Controlled Deviation as a generic abstraction over Bypass;
- Measurement-to-Action as a reusable control pattern;
- Control Means Verification as a specialized mechanism;
- LPA as a specialized verification architecture rather than automatically a new Top-Level Machine.

### Not established yet

- Canon status of any of these objects;
- universal CMOC verification hierarchy;
- universal State Transition relation;
- promotion of any specialized candidate to Top-Level Machine;
- complete relation of all Key Strategies to existing CMOC Machines.

Therefore **no Canon promotion is made by this final cross-check**.

---

## 9. REG-001 / CANON DECISION

**REG-001:** unchanged.

**Canon:** unchanged.

**Existing Machine passports:** unchanged.

Reason: this document consolidates architectural evidence and boundaries but does not yet perform Canonization.

---

## 10. FINAL WORKING VERDICT

> **GM-096 Managing Change establishes a coherent family of distinct control boundaries around organizational process change. Plant Process Change Control, Production Trial Run, Banking Process and Bypass Process Control remain separate Machine candidates at different degrees of specialization. Controlled Deviation, Measurement-to-Action and Control Means Verification operate at more general mechanism/pattern levels. LPA and Workshop remain composite / specialized architectures. No new Top-Level Machine is justified by the final synthesis itself.**

**STATUS:** `FINAL CROSS-CHECK / SOURCE-DERIVED / NON-CANON`

---

## 11. NEXT ARCHITECTURAL STEP

GM-096 can now be considered **closed as a candidate-screening block**.

Следующий этап — не продолжать бесконечно дробить GM-096, а:

1. consolidate GM-derived Machine Candidates;
2. compare them against the existing CMOC Machine Catalog;
3. identify duplicates / specializations / Assemblies;
4. only then begin controlled Canonization.

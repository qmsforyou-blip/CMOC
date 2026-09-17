# GM-096 — Independent Source Cross-Check: Banking / Bypass

**Извещение на изменение:** 0138+170926

## 1. Цель

Проверить два оставшихся специализированных Machine-кандидата GM-096 по независимым и последующим источникам и определить, сохраняется ли их bounded identity за пределами исходного GM QSB 2009.

---

## 2. Banking Process

### Independent evidence

Позднейшие GM BIQS / supplier-audit материалы воспроизводят Banking как отдельную управляемую конструкцию: banking strategy/procedure учитывает capacity, customer need, lead time и safety margin; уровень запаса управляется в ходе изменения; задаются правила длительного хранения и защитной упаковки; применяется FIFO; перед внутренним использованием или отгрузкой выполняется quality review по установленным критериям.

Отдельный GM training material дополнительно фиксирует организационные роли: Material Manager отвечает за выполнение и traceability, Operations Manager — за protective packaging and storage, Quality Manager — за quality control. Требуются FIFO, защита от условий хранения, способных вызвать rust / contamination / mold / distortion, контроль stock level и периодический LPA.

Внешний производственный источник описывает banking как производство деталей для длительного хранения для изоляции заказчика от риска перебоев поставок и указывает на необходимость определённой процедуры, ответственных лиц, protective packaging и критериев разрешения release/shipment banked parts.

### Boundary test

Banking нельзя свести к обычному складу, FIFO или preservation.

Отличительный контур:

`decision to bank → controlled build-up / stock → identification & traceability → protected long-term storage → monitoring / review → release criteria → authorized release / shipment`

Таким образом, объект управления — не просто физическое хранение, а специальное состояние материального потока, введённое для обеспечения continuity during change / transition и сопровождаемое правилами сохранности и выпуска.

При этом внешний источник не является нормативным стандартом и используется только как corroborating evidence. Поэтому подтверждается identity конструкции, но не утверждается универсальность именно GM Banking Process как отдельной отраслевой машины.

### Cross-check result

Banking сохраняет bounded identity, отличную от общего Storage / FIFO / Preservation.

### Status

`MULTI-SOURCE CONFIRMED / SPECIALIZED-CANDIDATE / NON-CANON`

Уровень подтверждения: несколько источников, включая последующие GM материалы и внешний manufacturing source; универсализация за пределы контекста long-term / change-related banking не выполняется.

---

## 3. Bypass Process Control

### Independent evidence

Последующие GM supplier-quality requirements подтверждают отдельный Bypass Management process: организация должна идентифицировать manufacturing processes и error-proofing devices, которые могут быть bypassed; для утверждённых bypass-процессов оценивается риск; существуют Standard Work Instructions; активные bypasses рассматриваются на daily Leadership / Fast Response; выполняется quality-focused audit; restart verification документируется на определённый период.

GM BIQS assessment material дополнительно определяет bypass management как способ контроля out-of-standard manufacturing processes и требует стандартизированного Bypass Process, его review/approval, обучения персонала и включения риска в PFMEA / Control Plan.

Более поздний GM Customer Specific Requirement прямо различает proactive Bypass и reactive deviation: Bypass — заранее установленный и утверждённый процесс на случай потенциального отказа error-proofing, с риском, определённым в PFMEA.

Внешнее профессиональное обсуждение GM Quality System также описывает Bypass как альтернативный manufacturing flow, используемый для сохранения поставок, с документированной процедурой, authorization to enter/exit и work instructions. Это подтверждение терминологии и практической конструкции, но не нормативный источник.

### Boundary test

Bypass не равен:

- обычному Controlled Deviation;
- Audit / LPA;
- Andon / Fast Response;
- простой резервной операции.

Его bounded identity задаётся замкнутым состоянием:

`approved normal process → authorized bypass → controlled execution / monitoring → verification of original process → authorized restart → normal process`

Ключевая граница — управление временно изменённым производственным состоянием и обязательным безопасным возвратом в утверждённый процесс.

Controlled Deviation при этом сохраняется как более общий Mechanism / Pattern, а Bypass — как его специализированная process-state realization.

### Cross-check result

Независимые и последующие источники подтверждают, что Bypass является воспроизводимой специализированной управленческой конструкцией, а не только локальным термином GM-096.

### Status

`MULTI-SOURCE CONFIRMED / SPECIALIZED-CANDIDATE / NON-CANON`

Подтверждение достаточно для усиления Machine-кандидата, но не для его Canonization.

---

## 4. Comparative conclusion

| Candidate | Independent cross-check | CMOC status |
|---|---|---|
| Banking Process | bounded identity подтверждена последующими GM материалами и внешним manufacturing evidence | `MULTI-SOURCE CONFIRMED / SPECIALIZED-CANDIDATE / NON-CANON` |
| Bypass Process Control | bounded identity подтверждена последующими GM requirements / BIQS и внешним corroborating evidence | `MULTI-SOURCE CONFIRMED / SPECIALIZED-CANDIDATE / NON-CANON` |

### Architectural distinction

Banking отвечает на вопрос:

> Что происходит с материалом, который сознательно выводится из обычного потока и должен быть сохранён до последующего управляемого выпуска?

Bypass отвечает на другой вопрос:

> Что происходит, когда утверждённый производственный процесс временно не может выполняться в нормальном виде?

Следовательно, они не являются дубликатами друг друга и не сводятся к общей категории Change Control.

---

## 5. Governance

No Canon promotion is performed by this patch.

REG-001: unchanged.

Main MACHINE-CATALOG: unchanged.

Passport status is strengthened through evidence classification only.

No new Machine ID is introduced.

---

## 6. Final verdict for four GM-096 candidates

After the independent-source cross-check:

1. **PPCR** — `MULTI-SOURCE CONFIRMED / STRONG-CANDIDATE / NON-CANON`.
2. **PTR** — `MULTI-SOURCE CONFIRMED / SPECIALIZED-CANDIDATE / NON-CANON`.
3. **Banking** — `MULTI-SOURCE CONFIRMED / SPECIALIZED-CANDIDATE / NON-CANON`.
4. **Bypass** — `MULTI-SOURCE CONFIRMED / SPECIALIZED-CANDIDATE / NON-CANON`.

The four candidates therefore survive the second evidence layer. This does not promote any of them to Canon and does not yet justify insertion into the main Machine Catalog.

The next appropriate CMOC step is a **comparative cross-source abstraction**: extract the invariant construction shared by these four specialized Machines without collapsing their boundaries into a single generic "Change Management Machine".

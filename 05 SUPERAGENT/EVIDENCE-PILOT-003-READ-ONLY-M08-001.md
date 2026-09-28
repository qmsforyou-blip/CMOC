# EVIDENCE — PILOT-003 persisted Discovery → reviewed M07 → read-only M08

**Date:** 28-09-2026  
**RUN:** `RUN-PILOT-003-SRC-005`  
**Source:** Imai, *Gemba Kaizen*, chapter 13, page 6 of the supplied extract  
**Status:** diagnostic production M08 result; no RUN decision or CMOC admission

## Input and controls

- M06 passports PAS-001…004 were read from the persisted DISCOVERY adapter result in `pilot_003.sqlite`.
- `PILOT-003-SRC-005-RELATION-BINDING.json` validated RUN, source package, evidence package, passport IDs, working classes, formulation basis, and evidence endpoint pairs without a new M01–M06 run.
- `PILOT-003-M07-REVIEWED-TRANSCRIPT.json` is a controlled transcription of the earlier read-only M07 output. It includes REL-002 and REL-003. REL-001 is excluded because PAS-001 is `STRUCTURAL_DISTINCTION`, so `ROLE_PARTICIPATES_IN_ACTIVITY` is unresolved.
- `pilot_003_m08_probe.py --validate-only` returned `M08_INPUT_VALIDATED`, with no LLM call or writes.

## Live diagnostic M08 result

`pilot_003_m08_probe.py` returned `READ_ONLY_M08_PROBE`:

| Decision | Target | Result | Basis |
| --- | --- | --- | --- |
| DEC-001 | REL-002: PAS-003 → PAS-002 | PROVISIONAL / ЧЕРНОВИК | EVID-IMA-CH13-P6-MEETING-MEASURES |
| DEC-002 | REL-003: PAS-004 → PAS-002 | PROVISIONAL / ЧЕРНОВИК | EVID-IMA-CH13-P6-MEETING-PROBLEMS |

Both decision records preserved `target_kind: RELATION_CANDIDATE`, `epistemic_status: PROVISIONAL`, their respective basis reference, and `evidence_gap: null`. M08 stated that no separate CMOC canonicalization criterion was supplied.

## Scope and next gate

This demonstrates that a controlled M08 diagnostic can evaluate two reviewed M07 relation candidates against the saved M06 passports without repeating Discovery. It does **not** persist M07/M08 results in the RUN journal or supersede the four human `DEFER` decisions. It does not establish a passport for the whole `Value Stream Performance Review` construction in `PATCH-IMA-013-CEO-KAIZEN-v1.md`, semantic NEW, Admission, C1/C2/C3, or a CMOC/index write.

Before a live admission attempt, identify a stable whole-object boundary and target type, compare it semantically against accumulated CMOC objects, and obtain an explicit human decision. No automatic promotion follows from `PROVISIONAL`.

## Извещение на изменение — `0211+280926`: граница целого кандидата

Проверен `DISCOVERY-RESULT-CONTRACT-001`: готовый source-bound DISCOVERY_RESULT передаётся в Reconciliation, а адаптация Reconciliation не вправе добавлять новый смысл добычи или решение NEW. `pilot_001_record_review.py` допускает ручное решение только для уникального `match_id` из сохранённого RECONCILIATION_RESULT. В RUN-003 имеются PAS-001…004, но нет паспорта и `match_id` для целого Value Stream Performance Review.

Следовательно, аналитический кандидат §013.3 PATCH нельзя задним числом добавить в RUN-003 через M07/M08 или оформить как его human decision. Для формального решения о целом потребуется отдельный контролируемый вход Discovery и собственная цепочка PAS → Reconciliation → human review; подготовка такого входа не изменяет исходный RUN-003. Пока тип и выход целого не доказаны, эта новая добыча не запускается автоматически. Протоколы двух read-only relation diagnostics остаются доказательством только их ограниченного охвата.

## Извещение на изменение — `0212+280926`: тип целого и контракт M05

Проверка `m05_llm.py` показала разрешённые source-bound `working_class`: `SOURCE_IDENTITY`, `COLLECTION`, `DECISION`, `ACTIVITY`, `CONCEPT_MODEL`, `STRATEGY`, `STRUCTURAL_DISTINCTION`. Класса `ORGANIZATIONAL_CONSTRUCTION` в M05 нет. По `RECONCILIATION-INPUT-CONTRACT-001` рабочий класс паспорта **не отображается автоматически** в целевой тип CMOC; отдельного mapping для этого случая здесь не установлено.

Поэтому предварительное аналитическое описание §013.3 как организационной практики не является готовым M05-классом или паспортом `ORGANIZATIONAL_CONSTRUCTION`. Запуск нового полного RUN ради присвоения этого типа без отдельного решения о границе и mapping дал бы ложное ощущение готовности. Текущий результат — выявленный контрактный пробел для целого; никакого изменения классификатора, RUN или индексируемого объекта.

## Извещение на изменение — `0214+280926`: исход отдельного RUN-005

Пользователь выполнил `RUN-PILOT-005-SRC-005-WHOLE` с контролируемым пакетом `SOURCE-005-PACKAGE-003-CONTROLLED-CH13-P6-7-WHOLE` в отдельной `pilot_005.sqlite`. Runtime вернул `HUMAN_REVIEW_REQUIRED`: пять `NEEDS_REVIEW`, query_scope `TERMS`, CMOC/index write `NONE`, Admission `NOT_PERFORMED`. Пользователь извлёк сохранённые M06 паспорта:

| Паспорт | Рабочий предмет | Класс |
|---|---|---|
| PAS-001 | потоки по семействам с отдельными менеджерами | STRUCTURAL_DISTINCTION |
| PAS-002 | еженедельная встреча команды Бирна с менеджерами | ACTIVITY |
| PAS-003 | отчёт о прогрессе по пяти группам | ACTIVITY |
| PAS-004 | обсуждение текущих задач с ограниченным временем | ACTIVITY |
| PAS-005 | различение целей улучшения и работы по дефектам | STRUCTURAL_DISTINCTION |

**Вывод:** паспорт целого `Value Stream Performance Review` не создан. PAS-001…004 содержательно перекрываются с компонентами RUN-003, но их тождество не оформлено решением. PAS-005 не является целым; его поддержка источником требует отдельной проверки FORM-013…015. Фраза источникового пересказа в пакете 003 об `improvement targets and separate defect-reduction work` могла спровоцировать это различение — причинная связь предполагается, не доказана. Термин PAS-005 сам по себе не доказывает отдельного факта о структуре совещания.

У всех пяти `object_boundary` осталась общей шаблонной формулировкой без описания границы целого. Повторный полный запуск без устранения способа представления композиции не обоснован. Пакет 003 сохраняется неизменным как вход уже выполненного RUN-005; четыре DEFER RUN-003 и RUN-005 не смешиваются. Рекомендация для human review RUN-005 — отложить каждый паспорт до сравнения с RUN-003 и проверки основания PAS-005; это **не записанное** решение человека. Диагностические M07/M08 RUN-003 и статус целого не повышаются.

## Извещение на изменение — `0215+280926`: проверка происхождения PAS-005

Пользователь прочитал сохранённую цепочку RUN-005: `FORM-013…015 → NOM-005 → CLS-005 → PAS-005`. Все три FORM формулируют разделение целей улучшения и работы по снижению дефектов как самостоятельных категорий, с `uncertainty=CLEAR`; M05 дал `STRUCTURAL_DISTINCTION`, M06 — `PROVISIONAL`. Это согласованная передача **внутри** Discovery, но не независимая проверка исходной страницы.

Контроль текста источника (извлечение главы 13, стр. 6–7) подтверждает пять групп показателей, цели улучшения, работу с частыми дефектами и еженедельный обзор потоков. Он не утверждает, что «цели улучшения» и «работа по дефектам» велись как две отдельные категории работы. Слово `separate` присутствует в английском пересказе SOURCE PACKAGE 003. Таким образом, по доступному фрагменту положительное основание именно для DIS-005/PAS-005 не найдено; `CLEAR` отражает согласованность с пересказом, а не истинность пересказа относительно книги.

**Рекомендация human review для MAT-PAS-005 RUN-005:** `REJECT` с основанием «разделение не подтверждено страницами 6–7 источника; возникло из формулировки контролируемого пересказа». Это рекомендация, решение не записано. Пакет 003 нельзя редактировать задним числом после привязки к RUN-005; будущий исправленный пересказ должен получить новый ID и отдельный RUN только при обоснованной цели нового эксперимента. PAS-001…004 требуют отдельной проверки на повтор компонентов RUN-003; целое по-прежнему не выделено. CMOC и OBJECT INDEX без изменений.

## Извещение на изменение — `0216+280926`: решение PAS-005 и сравнение компонентов

Пользователь (СГ) записал `REJECT` для `MAT-PAS-005` RUN-005 с основанием о неподтверждённом разделении и происхождении из пересказа. `pilot_001_record_review.py` вернул `PERSISTED`, `WAITING_HUMAN_REVIEW`, `projection_valid=true`; отдельный JSON решения присутствует в ветке. Решение относится только к PAS-005 и не отменяет остальные четыре `NEEDS_REVIEW`.

| RUN-005 | Ближайший паспорт RUN-003 | Ограничение сравнения |
|---|---|---|
| PAS-001: потоки по семействам, по одному менеджеру | PAS-001: один менеджер на поток семейства | Сходная структура, но разная формулировка фокуса; оба provisional. |
| PAS-002: еженедельные встречи команды Бирна с менеджерами | PAS-002: еженедельные встречи команды с менеджерами | Сходная деятельность в том же источнике; канонического CMOC ID нет. |
| PAS-003: отчёт о прогрессе по пяти группам | PAS-003: отчётность по пяти группам | Сходная деятельность; перечень групп расширен страницей 7 RUN-005. |
| PAS-004: обсуждение текущих задач с ограничением выступления | PAS-004: еженедельное обсуждение текущих проблем и улучшений | Сходная деятельность; акценты на регламенте времени и улучшениях отличаются. |

Это рабочее сопоставление двух RUN, **не** решение `ADMIT_EXISTING`: PAS RUN-003 не являются принятыми объектами CMOC. По каждому из четырёх требуется отдельное human-review решение; `DEFER` обоснован до выяснения границы, возможного дублирования и правила работы с двумя provisional представлениями одного источника. Не подменять эти решения автоматическим слиянием RUN. Admission и запись CMOC/индекса не выполнялись.

## Извещение на изменение — `0217+280926`: комплект human decisions RUN-005

СГ выполнил четыре отдельных решения `DEFER` для `MAT-PAS-001…004` в `RUN-PILOT-005-SRC-005-WHOLE`; каждое выполнение вернуло `PERSISTED`, `WAITING_HUMAN_REVIEW`, `projection_valid=true`. Вместе с ранее записанным `REJECT` для `MAT-PAS-005` все пять JSON решений доступны в `05 SUPERAGENT/human_review_decisions/RUN-PILOT-005-SRC-005-WHOLE/` рабочей ветки и имеют распределение **4 DEFER + 1 REJECT**.

Доказанный итог этого RUN: контролируемый пересказ страниц 6–7 прошёл живую Discovery/Reconciliation и ручную запись решений с корректной проекцией; целая конструкция не была извлечена, а одно неподтверждённое различение отвергнуто человеком. Статус RUN остаётся `WAITING_HUMAN_REVIEW` согласно ответам CLI; агрегированное завершение, Admission, C1/C2/C3, запись в CMOC и OBJECT INDEX не доказаны. Четыре DEFER не превращаются в эквивалентность или NEW. Повторный запуск того же пакета ради целого не требуется.

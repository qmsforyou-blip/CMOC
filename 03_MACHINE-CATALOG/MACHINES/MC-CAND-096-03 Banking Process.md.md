---
machine_id: MC-CAND-096-03
name: Banking Process

source: GM Quality System Basics rev March 2009 — Managing Change
source_location: pp. 336–339

level: MACHINE
type: MATERIAL STATE CONTROL / PRESERVATION

problem: >
  Материал, находящийся вне нормального производственного потока
  в течение длительного периода, может потерять идентификацию,
  пригодность или управляемость и потребовать специального контроля.

purpose: >
  Обеспечить идентификацию, защиту, хранение, периодическую проверку
  и управляемое возвращение материала из состояния extended storage
  до его использования или отгрузки.

trigger_mode: state / controlled storage
trigger: >
  Материал переводится в состояние длительного хранения в связи,
  например, с business transfer, engineering change, tool refurbishment
  или planned shutdown.

input:
  - material requiring extended storage
  - identification data
  - date / lot information
  - approved storage requirements
  - applicable quality requirements

actions:
  - идентификация материала
  - размещение на approved racks / dunnage
  - маркировка с датой и lot
  - обеспечение FIFO
  - защита от rust / contamination / mold / distortion
  - поддержание защищённого состояния материала
  - weekly LPA
  - выполнение corrective actions при выявленных отклонениях
  - проверка выполнения quality requirements перед shipment

output_type: CONTROLLED MATERIAL STATE / RELEASE INPUT
output: >
  Идентифицированный и защищённый материал с контролируемым состоянием
  хранения и подтверждением выполнения требований качества перед использованием
  или отгрузкой.

roles:
  - Material Manager
  - Operations Manager
  - Quality Manager

artifacts:
  - material identification / tags
  - date / lot identification
  - storage controls
  - LPA records
  - corrective action records
  - quality verification before shipment

mechanism: >
  identification → protected storage → periodic verification →
  corrective action when required → quality verification → release

capability: >
  Способность сохранять управляемость материала в состоянии extended storage
  и не допускать его неидентифицированного, повреждённого или непроверенного
  возврата в производственный / отгрузочный поток.

invokes:
  - LPA / audit mechanism
  - corrective action
  - quality verification

feeds:
  - production use
  - shipment decision

checks:
  - identification
  - storage condition
  - FIFO
  - environmental protection
  - LPA findings
  - quality requirements before shipment

improves: []
standardizes:
  - extended-storage controls
replicates: []
composes:
  - identification
  - preservation
  - periodic verification
  - corrective action
  - release verification

conditions:
  - material is subject to extended storage
  - approved storage locations / racks / dunnage are available
  - identification remains legible and traceable
  - periodic LPA is performed
  - quality requirements are verified before shipment

limitations:
  - The reviewed GM pages define Banking specifically for material stored for extended periods; they do not establish a universal material-preservation Machine.
  - FIFO, identification, preservation and LPA are component mechanisms / practices, not by themselves the identity of Banking Process.
  - Banking does not itself constitute product validation or general change approval.

cmoc_links:
  - Material → Extended Storage State
  - Extended Storage → Identification
  - Extended Storage → Preservation
  - Preservation → Verification
  - Verification → Corrective Action
  - Quality Verification → Release
  - Managing Change → Banking Process

source_claim: >
  GM QSB describes a Banking Process for identification, protection and retrieval
  of parts stored for extended periods, including business transfers, engineering
  changes, tool refurbishments and planned shutdowns. It specifies responsible
  roles, approved racks / dunnage, clear date / lot tags, FIFO, protection against
  rust, contamination, mold and distortion, weekly LPA, corrective actions and
  quality requirements before shipment.

cmoc_interpretation: >
  Specialized, bounded Machine candidate for controlling material in an extended-
  storage state. Its identity is the complete reproducible construction that keeps
  material identifiable, protected and periodically verified until quality
  requirements are satisfied for return to the normal flow. The reviewed source
  supports specialization, not a universal preservation Machine.

status: SPECIALIZED-CANDIDATE / NON-CANON
---
# Banking Process

## 1. Что это

Специализированная воспроизводимая конструкция управления материалом,
который выведен из нормального потока и помещён на длительное хранение.

## 2. Проблема

При длительном хранении материал может утратить идентификацию, быть повреждён,
загрязнён или вернуться в поток без подтверждения соответствия требованиям.

## 3. Назначение

Сохранить материал в управляемом состоянии до его использования или отгрузки.

## 4. Триггер

Перевод материала в extended storage, например при business transfer,
engineering change, tool refurbishment или planned shutdown.

## 5. Вход

Материал, подлежащий длительному хранению, его идентификация, date / lot,
требования к хранению и применимые требования качества.

## 6. Действия

1. Идентифицировать материал.
2. Разместить его на approved racks / dunnage.
3. Обеспечить чёткую маркировку date / lot.
4. Соблюдать FIFO.
5. Защитить от rust, contamination, mold и distortion.
6. Проводить weekly LPA.
7. Выполнять corrective actions при необходимости.
8. Перед shipment проверить выполнение quality requirements.

## 7. Выход

Контролируемое состояние материала и основание для его возвращения в поток
или отгрузки.

## 8. Роли

Material Manager, Operations Manager, Quality Manager.

## 9. Артефакты

Маркировка материала, date / lot, записи LPA, corrective actions и подтверждение
выполнения quality requirements.

## 10. Реализуемый механизм

`identification → protection → periodic verification → correction → quality verification → release`

## 11. Развиваемая способность

Удерживать управляемость материала, пока он находится вне нормального потока.

## 12. Граница с другими конструкциями

- **FIFO** — отдельный механизм внутри Banking, а не сама Banking Machine.
- **Identification / traceability** — механизмы обеспечения идентичности материала.
- **Contamination Control** — пересекающаяся специализированная способность,
  но Banking шире: включает также идентификацию, хранение, LPA и возврат.
- **LPA / Audit** — механизм периодической проверки, а не самостоятельная
  сущность Banking.
- **Corrective Action** — реакция на обнаруженное отклонение.

## 13. Условия применения

Наличие extended-storage состояния, контролируемого места хранения,
идентификации, периодической проверки и требований качества перед shipment.

## 14. Ограничения

Источник подтверждает именно специализированную конструкцию для extended
storage. Он не даёт достаточного основания расширять её до универсальной
Machine сохранения любого материального объекта.

## 15. Связи с CMOC

`Material → Storage State → Control → Verification → Correction → Release`

Banking является специализированной Machine управления состоянием материала
внутри более широкой Chain Managing Change.

## 16. Что утверждает источник

GM QSB задаёт Banking Process для идентификации, защиты и извлечения материала,
хранившегося длительное время; задаёт роли, места хранения, маркировку,
FIFO, защиту окружающей среды, weekly LPA, corrective actions и quality
requirements перед shipment.

## 17. Что выделено нами для CMOC

Отличительный признак Banking — не отдельный способ хранения, а замкнутая
конструкция управления специальным состоянием материала: **вне нормального
потока, но не вне управляемости**.

## 18. Статус

**SPECIALIZED-CANDIDATE / NON-CANON**

Следующая проверка: сопоставить Banking с независимыми конструкциями
Material Preservation / Quarantine / Controlled Storage и проверить,
достаточно ли у него собственной идентичности для сохранения статуса Machine.

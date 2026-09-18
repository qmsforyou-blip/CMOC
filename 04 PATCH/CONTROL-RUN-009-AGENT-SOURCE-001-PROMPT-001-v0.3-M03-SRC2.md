# CONTROL-RUN-009 — AGENT-SOURCE-001 + PROMPT-001 v0.3 — M03 — SRC-002

**DATE:** 18-09-2026
**SOURCE_ID:** SRC-002
**BATCH_ID:** BATCH-SRC-002-002
**TASK:** FORMULATIONS
**SOURCE_SCOPE:** PDF pages 1–20
**AGENT:** AGENT-SOURCE-001
**PROMPT:** PROMPT-001 v0.3

## Control objective

Verify structural reproducibility of the fixed machine on a materially different SOURCE than SRC-003, without changing the machine core and without using previous source-processing outputs.

## Input rule

All 20 observations below are taken directly from the source PDF pages 1–20. Previous SRC-002 artifacts are not operational inputs.

## Production result

20 direct source observations → 60 formulations, exactly 3 per observation.

| # | Page | Direct source observation | INTUITIVE | ENGINEERING | CANONICAL_FORM |
|---|---:|---|---|---|---|
|001|1|The presentation is Quality Systems Basics, rev March 2009, developed by GM Global Purchasing and Supply Chain.|QSB is a defined quality-systems reference from GM.|The source has an identified title, revision and originating function.|A source has an identified title, revision and originating organization/function.|
|002|2|QSB lists eleven named strategies.|QSB is a portfolio of distinct strategies.|The system is decomposed into named strategy modules.|A management system can be represented as distinct named strategy modules.|
|003|3|Suppliers are assessed against the latest QSB Audit and Red strategies require a workshop; Red and Yellow questions receive an action plan.|Audit results determine where intervention is required.|Assessment results select interventions and generate action planning.|Assessment status can determine intervention scope and required action planning.|
|004|4|The source emphasizes common principles, common methods and common processes, with one language globally.|The system seeks one common way of talking and working.|Language, methods and processes are standardization elements.|A management system can standardize language, methods and processes across contexts.|
|005|5|Fast Response solves problems faster and earlier upstream through visual management.|Problems should be seen and addressed early.|Fast Response combines early response with visual management.|A response process can use visual management to accelerate upstream problem handling.|
|006|6|Fast Response defines purpose, scope, responsibility, operating elements, exit criteria, statusing, metrics, problem solving and lessons learned.|Fast Response is a structured process, not just a meeting.|The process has defined responsibilities, operations, completion criteria, measures and learning.|A management process can be defined by purpose, scope, responsibility, operations, completion criteria, measures and learning.|
|007|7|Fast Response immediately addresses internal and external quality failures and assigns ownership to the Operations Manager.|Failures need an immediate, visible and owned response.|The process combines response timing, visual status and ownership.|A response process can specify timing, visibility and accountable ownership.|
|008|8|Benefits include systematic problem solving, natural ownership, continuous improvement, lessons learned, prevention and stakeholder engagement.|Problem response connects to learning and improvement.|Fast Response produces ownership, learning and prevention effects.|A management process may generate capabilities for ownership, learning, prevention and stakeholder engagement.|
|009|9|Fast Response standardizes reaction, documentation, communication, visual display and upstream problem identification.|A standard routine makes quality response more consistent.|The process standardizes reaction, evidence, communication, visibility and detection point.|A response mechanism can standardize reaction, evidence, communication, status visibility and detection point.|
|010|10|Quality identifies significant concerns from the previous 24 hours from defined external and internal sources.|The daily process collects recent quality signals.|Problem identification has a defined time window and signal sources.|A monitoring step can define a time window and bounded signal sources.|
|011|11|The meeting is owned by Manufacturing, supported by Quality, Engineering, Maintenance and others; it is a communication meeting, not a problem-solving meeting.|The meeting coordinates status rather than solving the problem.|Ownership, participants, cadence and purpose are differentiated from problem-solving work.|A coordination mechanism can have defined ownership, participants, cadence and purpose distinct from problem-solving execution.|
|012|12|Issue owners update the board before the meeting and carry problem solving and exit criteria through reviews, status updates and reporting.|The owner carries the issue through its required steps.|Ownership includes status, coordination, communication and milestones.|Responsibility for an issue can include status maintenance, coordination, communication and completion of exit criteria.|
|013|13|Plant leadership maintains Fast Response, assigns facilitators and assigns natural owners, support, actions and next report dates.|Leadership makes sure the process works and issues have owners and next actions.|Leadership governs process effectiveness and issue accountability.|Leadership can govern both process effectiveness and issue-level accountability.|
|014|14|A Fast Response tracking board is specified with physical construction elements and status components.|The visual board is a concrete operating object.|Visual management is instantiated as a defined physical information display.|A management mechanism may have a physical realization with specified structural elements.|
|015|15|The board includes ownership, exit criteria, overall status, next report date, target dates and closure-related fields.|The board shows who owns the issue, where it stands and what happens next.|The board represents state, responsibility, milestones, dates and closure controls.|A visual control can represent state, ownership, milestones, dates and closure evidence.|
|016|16|Exit criteria are established for each key step and evidence is reviewed by the owner; validation and prevention elements are documented.|Each important step needs a clear finish condition and evidence.|Completion is controlled through explicit criteria and evidence.|A process step can be governed by explicit completion criteria and required evidence.|
|017|17|Exit criteria have timing; Yellow is the default, Red means timing exceeded, Green means completed, and Red comments explain the next step.|Status changes according to time and completion.|Status is rule-based and linked to timing, completion and next-step information.|A status mechanism can map timing and completion conditions to discrete states and required actions.|
|018|18|Overall status is Red, Yellow or Green and equals the worst condition of any single item; closure timing is also constrained.|Overall status reflects the most serious open condition.|Aggregate status follows an explicit worst-condition rule and closure-time constraints.|An aggregate status can be calculated from component states using an explicit aggregation rule.|
|019|19|A Fast Response report-out format is presented as a defined part of the system.|Reporting has a standard format.|The system includes a defined reporting interface.|A management process can expose a standardized reporting interface.|
|020|20|Leadership ensures Fast Response effectiveness and visible quality status; visual management may show Red/Yellow days, closed issues and average days open.|Leadership checks the process through visible performance information.|Effectiveness monitoring uses defined visual performance measures.|Process effectiveness can be monitored through defined visual performance indicators.|

## Traceability

Each formulation set is traceable to one source page and one direct source observation.

20 observations → 60 formulations. Cardinality: 3 per observation = PASS.

## Prohibitions check

- Previous SRC-002 processing artifacts as operational input: NO.
- External knowledge: NO.
- Downstream nomenclature/classification/passport/relation/canonization: NO.
- CMOC CANONICAL status assigned: NO.

## Structural QC

- AGENT-SOURCE-001 changed: NO.
- PROMPT-001 v0.3 changed: NO.
- SOURCE changed: YES — SRC-002.
- Direct SOURCE_PACKAGE route: PASS.
- 20 direct source observations: PASS.
- 60 formulations: PASS.
- 3 formulations per observation: PASS.
- Traceability: PASS.
- Completion: PASS.

## Control conclusion

**CONTROL-RUN-009: PASS — structural reproducibility confirmed for M03 direct-source route on a second, materially different source (SRC-002), with machine core and prompt unchanged.**

This establishes cross-source structural reproducibility of the M03 route. It does not establish semantic equivalence across sources, universal applicability of M03 to every source, or correctness of CMOC canonization.

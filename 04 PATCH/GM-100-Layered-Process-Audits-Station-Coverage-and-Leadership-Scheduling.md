# GM-100 — Layered Process Audits — Station Coverage and Leadership Scheduling

## Source
GM Quality System Basics Overview Supplier Audit.pdf, pp. 232–233, §7.2.1 Scheduling and tracking.

## SOURCE extraction

### p.232 — station coverage tracking

1. A schedule/chart can be used to ensure that each station within a work area is evaluated at least monthly.
2. The chart is used by all auditors to determine which stations have not yet been audited.
3. The auditor is required to record their name, date, and shift for the stations selected for audit.
4. The stated goal is to audit each workstation where a team member is present one time each month.
5. The slide presents the chart as an **Example**; the specific chart format is therefore not treated as a universal requirement.

### p.233 — leadership audit scheduling

1. Identifying audits to be completed by leadership staff is described as essential to ensure that all areas on the shop floor interact with the management team.
2. The example schedule addresses both the required audit frequency by manager and the status of the management interaction.
3. The slide presents the schedule as an **Example**; the particular visual format and specific management layers are not treated as universal requirements.

## CMOC interpretation candidates

- **CAND-0549 — Audit coverage can be managed as a station-level completeness problem.** The schedule/chart is used to identify stations not yet audited within the required period.
- **CAND-0550 — Audit execution can be made traceable at the station level.** Recording auditor, date, and shift provides a minimum execution trace for the selected station audit.
- **CAND-0551 — Audit scheduling can control both frequency and coverage.** The schedule is not only a calendar; it can expose which required stations have and have not received the audit.
- **CAND-0552 — Leadership interaction with the shop floor can be explicitly scheduled and tracked.** The source connects leadership audit scheduling with ensuring interaction across shop-floor areas.
- **CAND-0553 — Completion status is a control object of the audit schedule.** The p.233 example explicitly represents the status of the required management interaction.

## Architectural significance

The key SOURCE contribution of pp.232–233 is the transition from merely defining audit frequency to **managing coverage and completion**:

**AUDIT FREQUENCY → STATION COVERAGE → EXECUTION RECORD → COMPLETION STATUS**

and, for leadership layers:

**LEADERSHIP AUDIT SCHEDULE → SHOP-FLOOR INTERACTION → COMPLETION STATUS**

The schedule therefore functions as a control mechanism for ensuring that required audit interactions actually occur, rather than merely specifying that audits should occur.

## Boundary

Do not infer from pp.232–233 that every organization must use the illustrated paper charts, exactly monthly station coverage, or the particular leadership-layer configuration shown in the examples. Preserve the distinction between SOURCE requirements and the examples used to demonstrate one implementation method.

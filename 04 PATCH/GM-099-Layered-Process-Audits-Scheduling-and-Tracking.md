# GM-099 — Layered Process Audits — Scheduling and Tracking

## Source
GM Quality System Basics Overview Supplier Audit.pdf, pp. 230–231, §7.2.1 Scheduling and tracking.

## SOURCE extraction

### p.230 — explicit requirements

1. The organization shall define the organizational levels that perform audits.
2. Audit frequency shall be defined for each organizational level.
3. Daily: the manufacturing supervisor shall perform audits.
4. Weekly: the manufacturing area manager shall audit and verify that supervisor verification is being completed.
5. Monthly: site leadership shall conduct Layered Process Audits and review audit results and corrective actions.

### p.231 — example architecture

The example shows four organizational layers and associated minimum frequencies:

| Organizational layer | Example frequency |
|---|---|
| Supervisor / Team Leader | Daily |
| Manager / Engineers | 1 time/week |
| Plant Manager | 1 time/month |
| Executive Managers / Directors | Quarterly / minimum |

The page is explicitly marked **Example**. Therefore these frequencies are not treated as universal SOURCE requirements.

## CMOC interpretation candidates

- **CAND-0546 — Frequency is assigned by organizational layer.** The LPA system is not a single audit cadence; cadence is differentiated by organizational level.
- **CAND-0547 — Layered verification can include verification of lower-layer execution.** The source explicitly states that the weekly manufacturing-area-manager audit verifies that supervisor verification is being completed.
- **CAND-0548 — Higher organizational layers provide progressively less frequent oversight.** Supported by the p.231 example only; do not canonize as a universal rule without additional evidence.

## Architectural significance

The key SOURCE contribution of pp.230–231 is the coupling:

**ORGANIZATIONAL LEVEL → AUDIT FREQUENCY → AUDIT RESPONSIBILITY**

The weekly layer adds a second relation:

**HIGHER LAYER → VERIFIES COMPLETION OF LOWER-LAYER VERIFICATION**

This makes LPA a layered control system rather than merely a collection of independent audits.

## Boundary

Do not infer from p.231 that every organization must use exactly four layers or exactly Daily / Weekly / Monthly / Quarterly frequencies. The slide labels this arrangement as an example. The mandatory SOURCE requirement is to define levels and frequency for each level; the exact configuration is organizationally defined.

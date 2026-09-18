# AUTOMATED-RUN-002-M07-RELATIONS-MULTI-OBJECT-001

## Contract

- SOURCE_ID: SRC-002
- BATCH_ID: BATCH-SRC-002-001
- TASK: RELATIONS
- INPUT: source-supported multi-object context from EX-GM-AUTO-001…100 and DIS-GM-AUTO-001…100
- Rule: create a relation only when both endpoints and the directional relation are explicitly supported by the source context.
- External knowledge: NONE
- Synthesis: NONE

## Relation candidates

| ID | Endpoint A | Relation | Endpoint B | Evidence |
|---|---|---|---|---|
| REL-GM-REL-001 | Fast Response | SUPPORTS | visual management | EX-GM-AUTO-006;EX-GM-AUTO-014 |
| REL-GM-REL-002 | Fast Response | ADDRESSES | quality failures | EX-GM-AUTO-008;EX-GM-AUTO-012 |
| REL-GM-REL-003 | Operations Manager | OWNS | Fast Response | EX-GM-AUTO-010 |
| REL-GM-REL-004 | Quality | IDENTIFIES | significant concerns | EX-GM-AUTO-015 |
| REL-GM-REL-005 | external/internal findings | FEEDS | Fast Response | EX-GM-AUTO-016 |
| REL-GM-REL-006 | Manufacturing | OWNS | Fast Response meeting | EX-GM-AUTO-017 |
| REL-GM-REL-007 | issue owner | OWNS | problem solving | EX-GM-AUTO-020;EX-GM-AUTO-021 |
| REL-GM-REL-008 | tracking board | DISPLAYS | problem-solving status | EX-GM-AUTO-024;EX-GM-AUTO-025 |
| REL-GM-REL-009 | exit criteria | SUPPORTS | closure | EX-GM-AUTO-027;EX-GM-AUTO-028;EX-GM-AUTO-029 |
| REL-GM-REL-010 | overall Fast Response status | DETERMINED_BY | worst individual item | EX-GM-AUTO-030 |
| REL-GM-REL-011 | performance metrics | MEASURE | Fast Response effectiveness | EX-GM-AUTO-031;EX-GM-AUTO-032 |
| REL-GM-REL-012 | problem definition | USES | standard vs actual gap | EX-GM-AUTO-034;EX-GM-AUTO-038 |
| REL-GM-REL-013 | containment | CONTROLS | nonconforming product | EX-GM-AUTO-039;EX-GM-AUTO-047 |
| REL-GM-REL-014 | Verification Station | PROVIDES | prevention/detection/containment | EX-GM-AUTO-048 |
| REL-GM-REL-015 | Verification Station placement | IS_BASED_ON | risk/FTQ/RPN/capability | EX-GM-AUTO-049 |
| REL-GM-REL-016 | Standardized Work | DEFINES | repeatable sequence | EX-GM-AUTO-055 |
| REL-GM-REL-017 | operator training | SUPPORTS | Standardized Work | EX-GM-AUTO-056;EX-GM-AUTO-062 |
| REL-GM-REL-018 | gage control | CONTROLS | calibration/surveillance | EX-GM-AUTO-058;EX-GM-AUTO-060 |
| REL-GM-REL-019 | Error Proof Verification | USES | known-good/known-bad | EX-GM-AUTO-068;EX-GM-AUTO-069 |
| REL-GM-REL-020 | LPA | IMPLEMENTS | standardized layered audit | EX-GM-AUTO-071 |
| REL-GM-REL-021 | LPA | TARGETS | high-risk categories | EX-GM-AUTO-073 |
| REL-GM-REL-022 | PFMEA | SUPPORTS | risk reduction | EX-GM-AUTO-077;EX-GM-AUTO-078 |
| REL-GM-REL-023 | Reverse PFMEA | IMPLEMENTS | risk reduction | EX-GM-AUTO-080 |
| REL-GM-REL-024 | contamination controls | LINKS_TO | PFMEA/Control Plan/LPA/Fast Response | EX-GM-AUTO-087 |
| REL-GM-REL-025 | supplier monitoring | FEEDS | supplier problem resolution | EX-GM-AUTO-091;EX-GM-AUTO-092 |
| REL-GM-REL-026 | Managing Change | INCLUDES | PPCR | EX-GM-AUTO-093;EX-GM-AUTO-094 |
| REL-GM-REL-027 | Managing Change | INCLUDES | PTR | EX-GM-AUTO-096 |
| REL-GM-REL-028 | Managing Change | INCLUDES | Banking | EX-GM-AUTO-097 |
| REL-GM-REL-029 | Managing Change | INCLUDES | Bypass | EX-GM-AUTO-098 |
| REL-GM-REL-030 | eleven strategies | FRAME | workshop deliverables/action plan | EX-GM-AUTO-100 |

## QC

- Multi-object context: PASS
- Relation candidates: 30
- Both endpoints explicit in source context: PASS
- Direction explicit in source context: PASS
- External enrichment: NONE
- Unsupported endpoints: 0
- Canonization: NONE
- Reverse trace available through evidence extraction IDs: PASS

## Conclusion

M07 relation-dependent test is closed: multi-object source context permits creation of explicit directional relation candidates. The prior 100 NO_RELATION result remains historical and unchanged.
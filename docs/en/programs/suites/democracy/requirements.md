# Democracy — Requirements

What `FreeSynergy.Democracy` must and can do, derived from the [frontends](frontends/index.md)
(ADR 0006, 0013). Each capability names its data standard (ADR 0014) and our status.

Status: `implemented` · `planned` · `proposed`

## Required (common to the analysed programs)

| Capability | Seen in | Data / standard | Status |
|------------|---------|-----------------|--------|

## Procedures from the dieBasis effort analysis (2023)

Source: "Aufwandsanalyse für ein Abstimmungsprogramm", AG Vision, dieBasis Hessen, draft 2, 2023-07-14 (CC BY-NC-ND 4.0;
only the procedures are taken up, no text, no figures, no political position). Sent by a friend of the owner
(2026-11-09).

| Capability | Data / standard | Status |
|------------|-----------------|--------|
| **Growing voting radius:** anyone files a motion in their local group; only if it is approved there does it go to the next larger level (town, region, country …), level by level. A natural filter against floods of motions. Same as the owner's rule for passing on surveys (parent sets the rule, child may only be stricter). | groups with several parents (ADR 0056), surveys | planned |
| **Debate and vote strictly apart:** a debate phase with a fixed length (e.g. three weeks), then the vote without further debate. | surveys: phases with dates | planned |
| **Committees for exactly one topic:** advisory and executing committees are separate (conflict of interest); the mandate ends when the topic is solved; each level can recall the members it appointed at any time, only those. | groups with purpose and end, roles | planned |
| **Boards have one vote like everyone,** and act on instructions given by votes. | roles, surveys | planned |
| **Synchronised assemblies:** all local groups vote at the same time on the same announced motions, only per-group totals are published and added up. Secret (no single vote leaves the group) and checkable (everyone can compare their group's total and the sum). Works partly offline. | surveys: entering group totals, public tally | planned |
| **Instructions to mandate holders:** the result is a recorded instruction; proportional or majority voting to be decided per group. | surveys, history | proposed |
| **Mirror external motions** (e.g. from a parliament) and compare the members' result with the official one. | provider for public sources | proposed |
| **Systemic consensing:** each option gets a resistance score 0–10, the option with the least resistance wins; a "keep as is" option is always present. | surveys: method | planned |
| Same modules at every level, only configured; distributed, hard to attack. | P2P (ADR 0059) | planned |
| Political opinion is special-category data (GDPR Art. 9): end-to-end encryption, two factors, data in the EU, independent penetration tests; for elections BSI TR-03169 and BSI-CC-PP-0121 apply. | identity, sharing | planned |

## Optional (notable ideas)

| Capability | Seen in | Data / standard | Status |
|------------|---------|-----------------|--------|
| Opinion groups without replies, consensus becomes visible | Polis | surveys | proposed |
| Decision kinds (consent, dot vote, score) with deadline and recorded outcome | Loomio | surveys | proposed |
| Delegated votes, quorums for proposals | LiquidFeedback | surveys, groups | proposed |
| Participatory budget | Decidim, Consul | resources, surveys | proposed |

## Not planned (deliberately)

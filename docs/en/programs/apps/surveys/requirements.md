# Surveys — Requirements

What `FreeSynergy.Surveys` must and can do.

**Provisional (2026-11-06).** No frontends have been analysed for this category, so nothing here has passed the usual
rule (ADR 0006, 0013). Everything comes from our architecture (*arch.*) or is general knowledge of such programs (⚠️),
and must be checked against analysed programs before the contract is written.

Status: `implemented` · `planned` · `proposed`

## Required

| Capability | Basis | Data / standard | Status |
|------------|-------|-----------------|--------|
| Create and edit a survey (`survey.create`, `survey.edit`) | ⚠️ | AS2 `Collection` + own profile | proposed |
| Add, edit, reorder questions (`question.add`, `question.edit`, `question.move`) | ⚠️ | AS2 `Question`; gap beyond it | proposed |
| Question types: single, multiple, text, number, date, scale (`question.types`) | ⚠️ | `oneOf`, `anyOf`; rest gap | proposed |
| Required questions and validation (`question.validate`) | ⚠️ | gap | proposed |
| Publish, close, reopen (`survey.publish`, `survey.close`) | ⚠️ | AS2 `closed` | proposed |
| Choose the anonymity level and show it to respondents (`survey.anonymity`) | *arch.* ([design](design.md#anonymity)) | gap | proposed |
| Invite people (`survey.invite`) | ⚠️ | contacts, messenger | proposed |
| Open, answer, save and resume, submit (`survey.open`, `response.save`, `response.submit`) | ⚠️ | gap | proposed |
| See results as totals and charts (`result.summary`) | ⚠️ | derived | proposed |
| Export results (`result.export`) | ⚠️ | CSV ⚠️; DDI ⚠️ | proposed |
| Mark sensitive surveys and answers (`survey.classify`) | *arch.* (ADR 0029) | DPV | proposed |
| Embed a poll in another program (`poll.embed`) | *arch.* (ADR 0037) | AS2 `Question` | proposed |
| Notify about changes (`subscribe`) | *arch.* (ADR 0021) | AS2 activities | proposed |

## Optional

| Capability | Basis | Data / standard | Status |
|------------|-------|-----------------|--------|
| Skip logic (`logic.set`) | ⚠️ | gap | proposed |
| Matrix and ranking questions (`question.types`) | ⚠️ | gap | proposed |
| One answer per person with anonymity (`survey.tokens`) | *arch.* | gap | proposed |
| Public link for anyone (`survey.publicLink`) | ⚠️ | gap | proposed |
| Date poll, result goes to the calendar (`poll.date`) | ⚠️ | JSCalendar `Event` | proposed |
| Templates and a question bank (`template.use`) | ⚠️ | wiki templates (ADR 0031) | proposed |
| Filter and cross-tabulate results (`result.filter`) | ⚠️ | derived | proposed |
| Translated surveys (`survey.translate`) | ⚠️ | AS2 `nameMap` | proposed |
| Federated poll to other servers (`poll.federate`) | *arch.* | AS2 `Question`, ActivityPub | proposed |

## Not planned (deliberately)

- Binding elections: they need much stronger guarantees and belong to the democracy suite.
- Tracking respondents (advertising, device fingerprints): contrary to the purpose of the program.
- Automatic analysis of answers by external services: answers must not leave the program.

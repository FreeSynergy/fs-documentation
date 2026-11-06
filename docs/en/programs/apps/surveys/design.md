# Surveys — design

**Status: proposal (2026-11-06).** Back to the [roadmap](../roadmap.md) · [requirements](requirements.md).

## Idea

A survey is a sequence of questions, a set of answers and an evaluation. A quick poll in the messenger is the same thing
with one question, so surveys appear inside other programs as a compact workbench (ADR 0037).

## Data

| Piece | Standard | Evidence | Notes |
|-------|----------|----------|-------|
| One-question poll | AS2 `Question` with `oneOf`, `anyOf`, `closed` | ✅ read 2026-11-06 | Federates directly, but has only single and multiple choice |
| Survey | AS2 `Collection` (ordered) of questions | ✅ type exists | Using it this way is our choice |
| Scales, matrix, ranking, skip logic, validation | ❌ not in AS2 | | **Own profile**, see below |
| Answer | gap | | Must support [anonymity](#anonymity), so it cannot simply carry `actor` |
| Reference vocabulary | DDI, FHIR `Questionnaire` | ⚠️ existence seen, not studied | Candidates for import and export |
| Test and exam formats | QTI | ⚠️ not checked | Tests are outside the first scope |

**Direction from the research:** AS2 `Question` as the outer form, already used for polls by Mastodon. FHIR `Questionnaire`
as a model for typed items and conditions. DDI is metadata for archives and QTI is for graded exams, so neither is a base.
Each was read only in part, so this needs a closer check.

## Anonymity

This is the core of the program. People answer honestly only if they can trust the promise made.

| Level | Promise | How |
|-------|---------|-----|
| **Named** | The organiser sees who answered what | Answer carries the `actor` |
| **Anonymous, open** | Nobody knows who answered; several answers from one person are possible | No identity stored at all |
| **Anonymous, one answer each** | One answer per invited person; answers cannot be traced to them | Hard; see below |
| **Completely open** | Anyone, with no account | See [open surveys](#open-surveys-without-login) |
| **Binding vote** | Verifiable, resistant to coercion | Needs much stronger guarantees; to be handled within the [democracy suite](../../suites/democracy/index.md) |

The third level is the difficult one. A simple token model (one token per invitation, stored apart from the answers)
is easy to build, but the operator could connect the two, and it must say so honestly. Stronger guarantees need
cryptography such as blind signatures, which requires expert review. **We propose to start with the token model and to
state its limit plainly in the interface,** without calling it fully anonymous.

Other risks to handle:

- Timing: storing the time of an answer can identify a person, so times are coarsened or left out.
- Small groups: results with few answers can identify people, so a minimum group size hides them.
- Free text can identify its author, and the interface says so.
- Answers can be sensitive data (ADR 0029): health, politics, faith.

## Open surveys, without login

**A survey can be completely open, with no account.** One party must still not be able to submit a million answers.

From the [research](https://github.com/FreeSynergy/fs-documentation/blob/main/temp/research/surveys-landscape.md): nothing gives
"one person, one answer, no identity, no third party" on a fully open link. Layers can be combined with no third party:
adaptive proof of work, global rate limits, a device marker, quality scoring with a review queue, and showing "all
answers" beside "checked answers". The interface states which protection is in place. Privacy Pass (RFC 9576) is a
standard for private proof of a real device, but only platform vendors issue the tokens today.

## Decision types

Not only majority. Each method is a pluggable strategy, and the same ballots can be shown under several methods: no tool
we found offers this.

Majority, supermajority, approval, score, ranked methods (Schulze, instant runoff, Borda), quadratic voting, consensus,
consent as in sociocracy, systemic consensing (resistance from 0 to 10, with a "carry on as before" option; no open-source
tool found), delegation, and deliberative clustering. Each comes with a fitting [chart](../../../components/charts.md).

## Widening to parent groups

A survey can start small and, if it matters, widen to parent groups in [`fs-groups`](../../platform/groups.md). It stays one
survey, earlier results are carried over, and anonymity can never get weaker on the way. **We found no tool that does this.** Consul comes close in one way: a proposal that gathers enough support moves on to a vote.
Whether it can also move between levels of a hierarchy was not confirmed.

## Patterns

| Pattern | Use |
|---------|-----|
| Strategy | `AnonymityPolicy` per level; one `Evaluation` per question type |
| Registry | Question types, which frontends and plugins can extend |
| State | `draft` → `open` → `closed` → `archived` |
| Interpreter | Skip logic and validation as a small expression model |
| Repository | `SurveyRepository`, `ResponseRepository` |

## Interface sketch

| Interface | Capabilities |
|-----------|--------------|
| `Surveys` (root) | `capabilities()`, hands out the others |
| `Designer` | `survey.create`, `question.add`, `question.edit`, `question.move`, `logic.set`, `survey.publish`, `survey.close` |
| `Respond` | `survey.open`, `response.save`, `response.submit` |
| `Results` | `result.summary`, `result.filter`, `result.export` |
| `subscribe` | New answers, status changes (level-dependent) |

## Components

Mostly existing: `field`, `radio-group`, `checkbox`, `rating`, `slider`, `date-input`, `wizard`, `chart`, `table`. New
are the workbenches `survey-builder` and `survey-form`, plus the widgets `question`, `matrix-question` and `ranking-list`.
See [planned components](../../../components/planned.md).

## Stages

1. Frontend analysis, reading DDI and FHIR, profile draft, contract.
2. Core: question types, named and anonymous-open answering, evaluation; tests.
3. Workbenches, first simple frontend, a poll embedded in the messenger.
4. Tokens (one answer each), skip logic, export.

## Open questions

1. **How strong must anonymity be for the first version?** Recommendation: as in the table above.
2. **Who answers?** Only people with FreeSynergy, or anyone with a link? A public link needs a web form and a server
   that accepts answers. Recommendation: invited people first, then public links.
3. **Date polls (Framadate style):** part of surveys or of the calendar? Recommendation: a question type here, with the
   result handed to `fs-calendar`.
4. **Tests and quizzes with scoring:** in scope? Recommendation: later.

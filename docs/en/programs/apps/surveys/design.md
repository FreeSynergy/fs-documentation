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

**Before writing our own profile,** DDI and FHIR `Questionnaire` must be read properly. FHIR describes structured
questions and comes from healthcare; DDI comes from social research and has a reputation for being costly to adopt.
Reusing a subset would be better than inventing (ADR 0014).

## Anonymity

This is the core of the program. People answer honestly only if they can trust the promise made.

| Level | Promise | How |
|-------|---------|-----|
| **Named** | The organiser sees who answered what | Answer carries the `actor` |
| **Anonymous, open** | Nobody knows who answered; several answers from one person are possible | No identity stored at all |
| **Anonymous, one answer each** | One answer per invited person; answers cannot be traced to them | Hard; see below |
| **Binding vote** | Verifiable, resistant to coercion | Not in this program; belongs to the [democracy suite](../../suites/democracy/index.md) |

The third level is the difficult one. A simple token model (one token per invitation, stored apart from the answers)
is easy to build, but the operator could connect the two, and it must say so honestly. Stronger guarantees need
cryptography such as blind signatures, which requires expert review. **We propose to start with the token model and to
state its limit plainly in the interface,** without calling it fully anonymous.

Other risks to handle:

- Timing: storing the time of an answer can identify a person, so times are coarsened or left out.
- Small groups: results with few answers can identify people, so a minimum group size hides them.
- Free text can identify its author, and the interface says so.
- Answers can be sensitive data (ADR 0029): health, politics, faith.

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

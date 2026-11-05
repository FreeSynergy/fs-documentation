# Rule Editor

| Field | Value |
|-------|-------|
| **Category** | `fields` |
| **Inherits from** | `base` |
| **Variants** | `list`, `simple` |
| **States** | `enabled`, `disabled`, `invalid`, `unsaved` |
| **Gestures** | none – gestures are added by the frontend, not by the component (ADR 0037) |
| **Animations** | `reorder`, `fade-in` |
| **Related** | `repeater`, `select`, `text-input`, `switch`, `tags-input` |
| **Status** | skeleton |

## Description

A rule editor edits rules of the form "if ... then ...": conditions, actions and an on/off switch per rule. Rules are stored as **Sieve**.

## Purpose

- Mail filter rules (sort, label, move, mute)
- Word and user filters in chat
- Automatic handling per conversation

## Variants

| Variant | Description |
|---|---|
| **list** | one row per rule, edited in place |
| **simple** | single rule, e.g. a word filter |

## Features

- Rows built from [repeater](../../data/repeater/), [select](../../../primitives/fields/select/), [text-input](../../../primitives/fields/text-input/) and [switch](../../../primitives/fields/switch/)
- Several conditions (all/any) and several actions
- Reorder, duplicate, test run (`rule.run`)
- Validation before saving

## Data binding

Binds Sieve (RFC 5228; via JMAP Sieve, RFC 9661 for mail). The same rule model is applied to chat conversations (messenger requirement `rule.create`, `rule.run`). Register (ADR 0023): `Rule → rule-editor | text` (Sieve source).

## Distinction

- **Do not confuse with** [repeater](../../data/repeater/): the repeater only repeats a template; the rule editor knows the Sieve vocabulary.
- **Do not confuse with** [code-editor](../../../workbenches/special/code-editor/): that edits raw text; this one edits structured rules. Raw Sieve may be offered as an expert view ⚠️.

## Best Practices

- Show the rule as a sentence ("If sender is ..., move to ...").
- Warn about rules that match everything.
- Save only valid Sieve; show the error at the row.

## Blinc note

No Blinc equivalent (`repeater` is no either). Built in our layer because it binds Sieve. Backlog id: none ⚠️.

## Open points

- ⚠️ Sieve subset supported in the first version
- ⚠️ Round trip of hand-written Sieve scripts that the structured view cannot show

## See also

- [fields – overview](../index.md)
- [Repeater](../../data/repeater/)
- [Select](../../../primitives/fields/select/)
- [Switch](../../../primitives/fields/switch/)
- [Messenger requirements](../../../../programs/apps/messenger/requirements.md)
- [Base component](../../../primitives/basics/base.md)

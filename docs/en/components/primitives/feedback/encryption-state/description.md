# Encryption State

| Field | Value |
|-------|-------|
| **Category** | `feedback` |
| **Inherits from** | `base` |
| **Variants** | `icon`, `icon-text`, `warning` |
| **States** | `encrypted`, `unencrypted`, `unknown`, `focused` |
| **Gestures** | none – gestures are added by the frontend, not by the component (ADR 0037) |
| **Animations** | `pop-in` (state change) |
| **Related** | `badge`, `link`, `message-status`, `key-verification`, `tooltip` |
| **Status** | skeleton |

## Description

An encryption state shows how a message or conversation is protected (MLS, OpenPGP, Megolm, transport only, none). Unencrypted is marked visibly. It is **clickable** and leads to the guide that explains the state.

## Purpose

- Show the encryption of every message and conversation (messenger requirement `message.encryption`)
- Mark unencrypted incoming messages clearly
- Lead to the encryption guide (ADR 0018, ADR 0031)

## Variants

| Variant | Description |
|---|---|
| **icon** | lock glyph only |
| **icon-text** | glyph and kind of encryption |
| **warning** | unencrypted, shown prominently |

## Features

- Five kinds: `mls`, `openpgp`, `megolm`, `transport-only`, `none`
- Click or Enter opens the guide in the library
- Optional hand-over to [key-verification](../../../widgets/overlays/key-verification/) for unverified keys

## Data binding

Binds the encryption field `freesynergy.net:encryption` (`mls`, `openpgp`, `megolm`, `transport-only`, `none`). Register (ADR 0023): `Encryption → encryption-state | text`. Border case decided 2026-11-05: **primitive, not badge**, because it is operable.

## Distinction

- **Do not confuse with** [badge](../badge/): a badge is display only (no interaction); this component is a control that links to the guide.
- **Do not confuse with** [message-status](../message-status/): that one tells delivery progress.
- **Do not confuse with** [key-verification](../../../widgets/overlays/key-verification/): that one is the dialog for confirming trust.

## Best Practices

- State the kind in words in the tooltip, not only by glyph.
- `none` must be more prominent than `mls`, never the other way round.
- Do not suggest security that is not there: `transport-only` is not end-to-end.

## Blinc note

Partly in Blinc (`cn::badge` plus a link), but the data binding makes it our layer. Backlog id: none ⚠️. A generic clickable-marker part could be contributed upstream later ⚠️.

## Open points

- ⚠️ Exact guide target per kind (library page ids)
- ⚠️ Per-message vs. per-conversation display rules

## See also

- [feedback – overview](../index.md)
- [Badge](../badge/)
- [Message Status](../message-status/)
- [Link](../../basics/link/)
- [Key Verification](../../../widgets/overlays/key-verification/)
- [Messenger requirements](../../../../programs/apps/messenger/requirements.md)
- [Base component](../../basics/base.md)

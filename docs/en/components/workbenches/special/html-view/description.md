# HTML View

| Field | Value |
|-------|-------|
| **Category** | `special` |
| **Inherits from** | `base` |
| **Variants** | `sanitised`, `remote-allowed` |
| **States** | `loading`, `blocked-remote`, `ready` |
| **Gestures** | none – gestures are added by the frontend, not by the component (ADR 0037) |
| **Animations** | `fade-in` |
| **Related** | `embed`, `mail-view`, `link`, `image` |
| **Status** | skeleton |

## Description

An HTML view shows foreign HTML (for example a mail body) in cleaned form and without loading anything remote.

## Purpose

- HTML body of a mail
- Rich foreign content in messages
- Safe display without scripts, tracking pixels or remote styles

## Variants

| Variant | Description |
|---|---|
| **sanitised** | default: cleaned HTML, no remote loading |
| **remote-allowed** | remote content allowed for this view |

## Features

- Sanitiser removes scripts, forms, frames, event handlers
- No remote images, fonts or styles; `cid:` parts allowed
- Links are marked and routed through the host
- Hint bar "remote content blocked" with a per-view choice

## Data binding

Binds the `text/html` part of a MIME message. Register (ADR 0023): `Html → html-view`. Band decided 2026-11-05: **workbench**, because the content is only known at run time, like [embed](../embed/).

## Distinction

- **Do not confuse with** [embed](../embed/): embed includes foreign programs or pages; html-view renders inert HTML as content ⚠️ may become a variant of `embed`.
- **Do not confuse with** [mail-view](../../../widgets/data/mail-view/): the mail view is the frame; this renders only the body.

## Best Practices

- Default to blocked remote content.
- Never execute scripts, regardless of variant.
- Fall back to the text part if HTML cannot be cleaned.

## Blinc note

Upstream in Blinc: backlog **a782b47** (`html_view()` phased plan; `embed` has no equivalent). Until it lands, the text fallback is used. The sanitising rules are our layer.

## Open points

- ⚠️ Sanitiser rule set (allow list)
- ⚠️ Dark theme rendering of mail colours

## See also

- [special – overview](../index.md)
- [Embed](../embed/)
- [Mail View](../../../widgets/data/mail-view/)
- [Messenger requirements](../../../../programs/apps/messenger/requirements.md)
- [Base component](../../../primitives/basics/base.md)

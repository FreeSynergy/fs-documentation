# Mail View

| Field | Value |
|-------|-------|
| **Category** | `data` |
| **Inherits from** | `base` |
| **Variants** | `full`, `compact`, `source` |
| **States** | `unread`, `read`, `encrypted`, `signed`, `signature-invalid` |
| **Gestures** | none – gestures are added by the frontend, not by the component (ADR 0037) |
| **Animations** | `fade-in` |
| **Related** | `description-list`, `html-view`, `message-bubble`, `file-upload`, `encryption-state` |
| **Status** | skeleton |

## Description

A mail view shows one e-mail: header (From, To, Cc, Subject, Date), body as text or HTML, attachments, and signature and encryption state.

## Purpose

- Reading pane of a mail program
- Search hits and previews (compact)
- Mail inside a ticket or contact view (ADR 0037)

## Variants

| Variant | Description |
|---|---|
| **full** | header, body and attachments |
| **compact** | header line and excerpt (list preview, search hit) |
| **source** | original MIME ⚠️ |

## Features

- Header fields via [description-list](../description-list/)
- Body as plain text or sanitised HTML through [html-view](../../../workbenches/special/html-view/)
- Attachment list with preview
- Signature and encryption status
- No remote content loaded by default (messenger requirement)

## Data binding

Binds JMAP `Email` plus the original MIME (`message/rfc822`). Register (ADR 0023): `Message → mail`. The HTML body is the `text/html` part and is handed to [html-view](../../../workbenches/special/html-view/).

## Distinction

- **Do not confuse with** [message-bubble](../message-bubble/): chat line versus mail with a header.
- **Do not confuse with** [html-view](../../../workbenches/special/html-view/): that renders only the foreign HTML body; the mail view is the frame around it.
- **Do not confuse with** [description-list](../description-list/): the header is built from it, the mail view adds body and attachments.

## Best Practices

- Show the real sender address, not only the display name.
- Mark unencrypted and unsigned mails visibly.
- Offer "load remote content" only as a conscious, per-mail action.

## Blinc note

No Blinc equivalent (`description-list` is no either). Built in our layer. HTML body depends on the Blinc `html_view()` plan, backlog **a782b47**; until then the text fallback is used.

## Open points

- ⚠️ `source` variant: needed in the first version?
- ⚠️ Inline images with `cid:` parts: allowed, remote URLs blocked; how is the exception shown

## See also

- [data – overview](../index.md)
- [Description List](../description-list/)
- [HTML View](../../../workbenches/special/html-view/)
- [Message Bubble](../message-bubble/)
- [Messenger requirements](../../../../programs/apps/messenger/requirements.md)
- [Base component](../../../primitives/basics/base.md)

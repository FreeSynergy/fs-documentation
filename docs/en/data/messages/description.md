# Messages – description

**What this domain is:** chat, comment and mail-like communications. Canonical payload: **AS2 objects** (`Note`, `Article`) in the ActivityPub envelope (decisions 1+2).

**What it covers:**

- 1:1 and group messages (messenger app)
- Comments attached to resources (wiki page, task, image) — as a `Note` with a reference to the commented object
- Mail-like communications (subject, addressees, threads) as a projection target
- Multilingualism via `contentMap`/`nameMap` (AS2, ✅)
- Disclosure control via `to`/`cc`/`bto`/`bcc` (disclosure, **not** access control — decision 2)

**Differentiation from other domains:**

| Topic | Where it lives | Why |
|-------|----------------|-----|
| Wiki pages, posts with blocks | [../apps/wiki/](../../programs/apps/wiki/index.md) or the planned `documents/` domain | documents are editable works, messages are transient utterances |
| Tag/comment **on a text fragment** | W3C Web Annotation Model (✅) — selector `TextQuoteSelector` | the text is not rewritten |
| iTIP invitation and reply | [events/](../events/index.md) | protocol messages, not chat |
| Notifications | its own domain still open ([index.md → proposed](../index.md)) | a notification points at a message but is not one |

**Not yet carried out (open question 6.2 from the conversation):** what exactly "messages" covers will be derived from the app inventory (messenger, helpdesk tickets, democracy comments, whiteboard comments). The common denominator everywhere is `Note` + reference + audience.

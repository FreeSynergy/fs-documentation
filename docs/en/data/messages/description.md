# Messages – description

**What this domain is:** e-mail, chat, messenger and comments as one domain (ADR 0018), encrypted only. Stored as original + AS2 envelope + activity log (ADR 0020); content standards per kind in [standards.md](standards.md).

**What it covers:**

- 1:1 and group messages (messenger app)
- Comments attached to resources (wiki page, task, image) — as a `Note` with a reference to the commented object
- E-mail as a first-class message kind (original MIME kept, JMAP `Email` fields indexed)
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

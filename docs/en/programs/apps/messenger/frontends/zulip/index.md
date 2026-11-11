# Zulip

> Category: [messenger](../../index.md) · Type: team chat · Vendor: Zulip project · Licence: open source (licence name Open)

## What it is

Zulip is a team chat organised in channels, in which every message belongs to a topic. It can be used by e-mail too: a message can be sent to a channel by e-mail.

## Notable ideas

Why this program is documented here (ADR 0013):

- **A topic on every message**: the sender names a short, specific subject; a reply goes to the topic being read automatically. Conversations stay separate without a second "thread" layer. Relevant for us: it solves the flood in busy group chats and maps onto a conversation context.
- **Topic-based views**: the sidebar shows recent topics per channel; the Inbox shows topics with unread messages; Recent conversations shows activity.
- Topics can be renamed or moved, marked resolved and muted (named in the help index; details not read).
- Keyboard use, for example jumping to the next unread topic.

## Documented versions

| Version | Documented on | Status |
|---------|---------------|--------|
| [latest](latest/description.md) | 2026-11-10 | ⚠️ two help pages |

## Protocols and standards used

Own REST API; bridges to Matrix exist (see Matrix bridge list). See [messages standards](../../../../../data/messages/standards.md).

## Documented versions

<!-- gen:versions (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
| Version | Required files present |
|---------|------------------------|
| [latest](latest/description.md) | 6/7 |

### latest

| File | Contents |
|------|----------|
| [description.md](latest/description.md) | Detailed description, differentiation, who it suits |
| [features.md](latest/features.md) | What the program can do — and what not |
| [layout.md](latest/layout.md) | Window structure, regions, panels |
| [menus.md](latest/menus.md) | Menu structure, context menus, menus by role |
| [shortcuts.md](latest/shortcuts.md) | Keyboard shortcuts |
| [api.md](latest/api.md) | APIs and protocols, authentication, rate limits |

⚠️ Missing required files: `themes/index.md`
<!-- /gen:versions -->

## Sources

| Source | Kind | Retrieved |
|--------|------|-----------|
| https://zulip.com/help/introduction-to-topics ✅ | official help | 2026-11-10 |
| https://zulip.com/help/ ✅ | official help index | 2026-11-10 |
| https://matrix.org/ecosystem/bridges/ ✅ | Matrix bridge list (Zulip appears) | 2026-11-10 |

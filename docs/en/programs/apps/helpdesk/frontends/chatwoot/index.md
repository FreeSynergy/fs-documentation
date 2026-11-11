# Chatwoot

> Category: [helpdesk](../../index.md) · Type: omnichannel customer-support inbox · Vendor: Chatwoot Inc. · Licence: MIT (enterprise edition and paid self-hosted licences exist)

## What it is
Chatwoot is a customer-support platform where conversations from many channels land in one shared inbox. It offers a live-chat widget for websites, e-mail, messengers, SMS, social channels and voice, plus a help centre. It runs as a cloud service or self-hosted.

## Notable ideas
- **All channels in one inbox** — each channel is an inbox; agents, teams and assignment rules work the same for all (ADR 0013). Fits our "every channel is a messenger provider" model in [requirements](../../requirements.md).
- **Website widget** — a snippet embedded in a page; with a pre-chat form and contact data.
- **Voice and video inside the conversation** — calls are logged in the timeline.

## Documented versions
| Version | Documented on | Status |
|---------|---------------|--------|
| [latest](latest/description.md) | 2026-11-10 | ✅ |

## Protocols and standards used
Webhooks, WebSocket, REST; channel protocols are third-party APIs (WhatsApp, Twilio and others). See [data standards](../../../../../data/standards.md).

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
| https://www.chatwoot.com/docs/product | official docs ✅ | 2026-11-10 |
| https://github.com/chatwoot/chatwoot | source README ✅ | 2026-11-10 |

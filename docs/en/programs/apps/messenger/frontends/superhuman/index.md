# Superhuman Mail

> Category: [messenger](../../index.md) · Type: e-mail client (for existing accounts) · Vendor: Superhuman (formerly Grammarly) · Licence: proprietary

## What it is

Superhuman Mail is a paid e-mail client that works on top of existing mail accounts and is built for speed: a command palette, a keyboard-first workflow and a divided inbox. Ownership: the company Grammarly bought Superhuman Mail in 2025 and, in October 2025, renamed itself Superhuman; the mail app is now called Superhuman Mail. The vendor's page lists further products (Go, Docs, Calendar).

## Notable ideas

Why this program is documented here (ADR 0013):

- **Split Inbox**: the inbox is divided into several lists by rules (sender, domain, recipient, subject, label). It divides one person's inbox; it is not a shared inbox of several people.
- **Command palette (Cmd/Ctrl+K)** as the single entry for actions, including creating splits. A two-finger tap opens it on mobile.
- **Keyboard first**: a shortcut for nearly every action.
- Vendor page also lists auto drafts, auto labels, auto archive and availability sharing (AI-based; local-only handling would be required for us, ADR 0029).

## Documented versions

| Version | Documented on | Status |
|---------|---------------|--------|
| [latest](latest/description.md) | 2026-11-10 | ⚠️ vendor page and help-centre search results; help pages returned 403 |

## Protocols and standards used

Works on existing accounts; which protocols is Open. See [messages standards](../../../../data/messages/standards.md).

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
| https://superhuman.com/ ✅ | vendor home page | 2026-11-10 |
| https://www.engadget.com/ai/grammarly-has-rebranded-to-superhuman-151001417.html ⚠️ | press (rebrand; seen in search result) | 2026-11-10 |
| https://help.superhuman.com/article/586-split-inboxes-2-0 ⚠️ | help centre (seen in search result only) | 2026-11-10 |
| https://help.superhuman.com/hc/en-us/articles/46005619081101 ⚠️ | help centre (seen in search result only) | 2026-11-10 |

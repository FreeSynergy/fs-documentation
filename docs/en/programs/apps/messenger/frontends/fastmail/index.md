# Fastmail

> Category: [messenger](../../index.md) · Type: hosted e-mail with web and mobile apps · Vendor: Fastmail · Licence: proprietary ⚠️

## What it is

Fastmail is a paid hosted e-mail service with web and mobile apps; calendar and contacts are part of the offer. Own domains can be used.

## Notable ideas

Why this program is documented here (ADR 0013):

- **Masked Email**: a random address is created per login or sign-up. Companies cannot link two such addresses, a labelled address shows a masked icon on incoming mail, and an address that receives spam can be switched off, which also shows who leaked it. Password managers 1Password and Bitwarden can be connected for creation at sign-up. Custom domains are possible (less anonymous, but portable).
- **Aliases** are separate: chosen addresses for long-lived identities, with their own sender name or signature.

Relevant for us: one address per relationship, revocable without changing the real identity.

## Documented versions

| Version | Documented on | Status |
|---------|---------------|--------|
| [latest](latest/description.md) | 2026-11-10 | ⚠️ one vendor page |

## Protocols and standards used

JMAP is not named on the page read; check the vendor's API documentation (Open). See [messages standards](../../../../../data/messages/standards.md).

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
| https://www.fastmail.com/features/masked-email/ ✅ | vendor feature page | 2026-11-10 |

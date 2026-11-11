# Delta Chat

> Category: [messenger](../../index.md) · Type: chat over e-mail · Vendor: Delta Chat community · Licence: open source (licence name Open)

## What it is

Delta Chat is a chat messenger whose messages travel as encrypted e-mail-style messages through relays ("chatmail"), or through an ordinary e-mail account used only for this. Contacts are added by QR code or invitation link; there is no public directory.

## Notable ideas

Why this program is documented here (ADR 0013):

- **Chat over existing mail infrastructure**: the transport is mail-like, so no new network is needed. Relevant for us: our messenger also joins mail and chat in one program (ADR 0018).
- **Encryption by default** with OpenPGP, key exchange through Autocrypt and Secure-Join; default relays refuse unencrypted messages. Unencrypted mail from a classic account is marked with an e-mail icon.
- **Relays keep no profile data**: names, pictures and group data stay on the devices.
- **Channels** (one-to-many, subscribers cannot reply), **webxdc** in-chat apps (sandboxed, no internet access), several profiles per device, second device by QR code, one-to-one calls.

## Documented versions

| Version | Documented on | Status |
|---------|---------------|--------|
| [latest](latest/description.md) | 2026-11-10 | ⚠️ one help page; no app inspected |

## Protocols and standards used

OpenPGP, Autocrypt, e-mail transport. See [messages standards](../../../../../data/messages/standards.md).

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
| https://delta.chat/en/help ✅ | official help | 2026-11-10 |

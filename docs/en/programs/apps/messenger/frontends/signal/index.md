# Signal

> Category: [messenger](../../index.md) · Type: chat · Vendor: Signal (independent non-profit, 501(c)(3)) · Licence: open source protocol; client licences Open

## What it is

Signal is a private messenger for text, voice messages, photos, videos, files, voice and video calls and group chats. It is funded by grants and donations and carries no ads or trackers, according to the vendor.

## Notable ideas

Why this program is documented here (ADR 0013):

- **Reference for the protocol**: end-to-end encryption on the open Signal Protocol. The documentation lists X3DH, PQXDH (post-quantum key agreement), Double Ratchet, Sesame (sessions across devices), ML-KEM Braid, XEdDSA/VXEdDSA. Relevant for us: the benchmark for what "encrypted by default" means (ADR 0018); our choice of MLS (RFC 9420) differs.
- **Sticker packs** that anyone can create and share, encrypted.
- Funding without ads or tracking, matching ADR 0016.

## Documented versions

| Version | Documented on | Status |
|---------|---------------|--------|
| [latest](latest/description.md) | 2026-11-10 | ⚠️ vendor home page and protocol page; the feature page returned 404 |

## Protocols and standards used

Signal Protocol (own). Bridges from Matrix exist (bridge list). See [messages standards](../../../../../data/messages/standards.md).

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
| https://signal.org/ ✅ | vendor home page | 2026-11-10 |
| https://signal.org/docs/ ✅ | protocol documentation index | 2026-11-10 |
| https://matrix.org/ecosystem/bridges/ ✅ | Matrix bridge list (Signal appears) | 2026-11-10 |

# Everything

> Category: [files](../../index.md) · [frontends](../index.md)

## What it is

Everything (voidtools) is a free search program for Windows that finds files and folders by name while you type ✅. Freeware, not open source ✅ (stated as freeware).

## Notable ideas

- **Instant search by name:** a name index is built in seconds to about a minute, results change with every keystroke ✅. On NTFS volumes it follows the change journal, so changes made while it was closed are caught up at start ✅.
- **Content is not indexed;** content search exists but is slow ✅.
- **Small query language:** space is AND, `|` OR, `!` NOT, wildcards, quotes, path narrowing ✅.
- **Servers and command line:** HTTP and ETP/FTP servers and the `ES` command-line tool in the full version, not in Lite ✅.
- Why here: it is the reference for `file.search` that answers at once (ADR 0013).

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

- https://www.voidtools.com/faq/ ✅ 2026-11-10

# Raycast

> Category: [desktop](../../index.md)

## What it is

Raycast is a keyboard-driven launcher: one search bar that finds applications and files, runs commands and extensions, and offers AI features. The manual covers Mac, Windows and iOS.

## Notable ideas

- **One palette for everything**: apps, files, commands, extensions, clipboard history, snippets, quicklinks and window management are all reached from the same search bar.
- **Action panel**: every result has a second layer of actions, opened from the keyboard.
- **Extensions in a store**, written with React and TypeScript, using shared interface components so they look alike.
- **Script commands** and **aliases/hotkeys** per command.
- Listed here for the idea of a single command palette over many functions (ADR 0013).

## Sources

- ✅ Raycast manual (overview): https://manual.raycast.com/ (fetched 2026-11-10)
- ✅ Raycast developer documentation: https://developers.raycast.com/ (fetched 2026-11-10)
- ⚠️ Individual manual pages (search bar, shortcuts, deeplinks, pricing): not read

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

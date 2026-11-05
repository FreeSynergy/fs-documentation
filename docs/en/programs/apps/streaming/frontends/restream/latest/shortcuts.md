# Restream - Keyboard shortcuts

## Overview

Restream documents **no official shortcuts**. The dashboard and the studio follow the usual web conventions.

## Web UI (dashboard and studio)

| Key | Purpose |
|-----|---------|
| `Tab` / `Shift+Tab` | move between form fields and tiles |
| `Enter` | confirm dialogs, trigger connect/disconnect |
| `Esc` | close modals (channel dialog, event dialog) |
| `Ctrl+Enter` | send chat (chat input field focused) |
| `Ctrl+R` | reload the page |

## Studio (not guaranteed, behaviour similar to other production tools)

| Key | Observed behaviour |
|-----|--------------------|
| `Space` | mute the microphone when the studio has focus |
| `M` | quick camera/microphone control in some studio versions |

These two lines are **observations, not documented promises** — verify them in the current studio before implementing a skin.

## Mac variants

| Windows/Linux | Mac |
|---------------|-----|
| `Ctrl+Enter` | `Cmd+Enter` |
| `Ctrl+R` | `Cmd+R` |
| `Esc` | `Esc` |

## Summary

- In short: **no documented shortcuts**; only standard web operation
- For a FreeSynergy skin implementation the keys have to be defined by yourself (e.g. "go live", "mute", "switch scene") and then documented here
- Automation runs through the API (see `api.md`), not through keys

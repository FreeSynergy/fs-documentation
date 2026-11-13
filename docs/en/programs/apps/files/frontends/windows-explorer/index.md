# Windows Explorer (File Explorer)

> Category: [files](../../index.md) · [frontends](../index.md)

## What it is

The file manager of Windows. Command bar or ribbon, navigation pane, cloud files shown beside local ones.

## Notable ideas

- **Quick access / Home:** pinned folders plus recent items on the start page ✅.
- **Search covers PC and cloud** from Home, after signing in to the cloud account ✅.
- **Cloud files appear as ordinary files** (OneDrive in the pane) ✅.
- **Show more options:** in Windows 11 the short context menu hides the older long one behind a link ✅.
- **Item check boxes** as an option for selection without Ctrl ✅.

## Capabilities seen

| Capability | Seen | Note |
|------------|------|------|
| Cut, copy, paste, rename, share, delete | ✅ | |
| Navigation pane, show or hide | ✅ | |
| View modes: icons, list, details, compact | ✅ | |
| Choose start page; show extensions and hidden items | ✅ | Options |
| Pin and unpin folders | ✅ | |
| Search incl. cloud | ✅ | |
| Preview pane, tabs, undo | ⚠️ | Not on the page read; known from the product |

## Name rules

✅ https://learn.microsoft.com/en-us/windows/win32/fileio/naming-a-file
- Forbidden characters: `< > : " / \ | ? *`, NUL and codes 1 to 31.
- Reserved device names (`CON`, `PRN`, `AUX`, `NUL`, `COM1`..`COM9`, `LPT1`..`LPT9`), also with an extension.
- No trailing space or period in the shell.
- Do not assume case sensitivity; `OSCAR`, `Oscar`, `oscar` count as one name by default.
- Path limit 260 characters, removable by configuration in newer versions.

A folder made on Linux may hold names Windows cannot show. The engine must report which names a backend or client cannot take.

## What we take

Start page of pinned and recent folders. A single search across local and remote. Selection check boxes for touch. The device-name rule list as an example of "what the OS allows" (ADR 0055).

## Documented versions

<!-- gen:versions (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
| Version | Required files present |
|---------|------------------------|
| [latest](latest/description.md) | 7/7 |

### latest

| File | Contents |
|------|----------|
| [description.md](latest/description.md) | Detailed description, differentiation, who it suits |
| [features.md](latest/features.md) | What the program can do — and what not |
| [layout.md](latest/layout.md) | Window structure, regions, panels |
| [menus.md](latest/menus.md) | Menu structure, context menus, menus by role |
| [shortcuts.md](latest/shortcuts.md) | Keyboard shortcuts |
| [api.md](latest/api.md) | APIs and protocols, authentication, rate limits |
| [themes/index.md](latest/themes/index.md) | Themes: colours, typography, spacing — what can be rebuilt |
| [states.md](latest/states.md) | UI states and transitions |
| [dialogs.md](latest/dialogs.md) | Every dialog: purpose, fields, buttons, default, cancel |
| [workflows.md](latest/workflows.md) | Step-by-step workflows: goal, prerequisites, steps, failures, undo |
| [acceptance.md](latest/acceptance.md) | Acceptance checklist: each workflow as a yes/no click test |
| [gaps.md](latest/gaps.md) | What our program cannot do for these workflows, and what it needs |
<!-- /gen:versions -->

## Sources (read 2026-11-06)

- https://support.microsoft.com/en-us/windows/file-explorer-in-windows-ef370130-1cca-9dc5-e0df-2f7416fe1cb1
- https://learn.microsoft.com/en-us/windows/win32/fileio/naming-a-file
- Tried and failed (404): a Microsoft search-help URL; preview pane and tabs not verified.

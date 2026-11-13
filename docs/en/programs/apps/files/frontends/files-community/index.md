# Files (Files App for Windows)

> Category: [files](../../index.md) · [frontends](../index.md)

## What it is

A free, open-source file manager for Windows, built by a community (repository `files-community/Files`, WinUI, C#/.NET) ✅. Dual-licensed MIT and MPL-2.0 ✅. Installed from the Microsoft Store or as a classic installer ✅; a preview version can sit beside the stable one ✅.

## Notable ideas

- **Omnibar:** one control for the breadcrumb path, typed path, folder aliases (`@name`), command palette and search ✅.
- **Command Palette** with more than 150 actions and their shortcuts; shortcuts are editable ✅.
- **Tabs and dual pane in one window;** a tab dragged into the file area becomes the second pane ✅.
- **Tags** on files and folders, stored as NTFS alternate data streams (NTFS only) ✅.
- **Layouts:** details, list, cards, grid, columns, adaptive ✅ (these are views, not frontends).
- **Sidebar** with pinned folders, drives, network, cloud drives, WSL and tags ✅.
- **FTP/FTPS** by typing an address; SFTP not supported ✅.

## Capabilities seen

| Capability | Seen | Note |
|------------|------|------|
| Tabs, dual pane, sidebar, toolbar | ✅ | |
| Copy, cut, paste, rename, delete, permanent delete, undo, redo | ✅ | shortcuts in the Command Palette page |
| Conflict dialog, progress dialog | ⚠️ | not on the pages read |
| Archives: extract, create 7z and zip | ✅ | |
| Git actions | ✅ | |

## What we take

The Omnibar idea (path, aliases and search in one field), tabs plus second pane in the same window, an action list searchable by name with editable shortcuts, tags on files.

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

## Sources (read 2026-11-13)

- https://files.community/docs/ and the feature pages: omnibar, command-palette, tabs, dual-pane, sidebar, toolbar, layout, tags, ftp, cloud-drives
- https://files.community/docs/customize-settings/general , files-and-folders , actions
- https://github.com/files-community/Files
- Not read: appearance, advanced, terminal, git, integrations, troubleshooting, FAQ.

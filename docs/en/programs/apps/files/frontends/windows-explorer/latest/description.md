# Windows Explorer 11 — Description

> [Windows Explorer](../index.md) · version: latest (Windows 11)

The file manager of Windows 11 ("File Explorer"). It browses local drives, removable media, network locations and cloud folders, and does the usual file work: copy, move, rename, delete to the Recycle Bin, search, properties.

**Evidence marks (whole dossier):** ✅ = stated on the official page read on 2026-11-13 (see [Sources](#sources)). `[nicht belegt]` = not stated on that page; the line says what is known from the product or that it is unknown. Only functions and behaviour are described, nothing is copied (ADR 0013).

## Who it suits

Everyone on Windows; it is the reference that people already know. Its weak spots for power users (one pane, shallow batch rename) are what Total Commander and Files fill, see [Total Commander](../../total-commander/index.md) and [Files](../../files-community/index.md).

## Differentiation

- One pane per tab, navigation pane at the side, command bar on top ✅ (ribbon in Windows 10, command bar in 11: command bar `[nicht belegt]` on the page read).
- Short context menu with a "Show more options" link to the full legacy menu ✅.
- Tabs exist in Windows 11 ✅ (shortcuts in [shortcuts.md](shortcuts.md)).
- Cloud files beside local ones ✅.

## Pages of this dossier

[features](features.md) · [layout](layout.md) · [menus](menus.md) · [shortcuts](shortcuts.md) · [api](api.md) · [themes](themes/index.md) · [states](states.md) · [dialogs](dialogs.md) · [workflows](workflows.md) · [acceptance](acceptance.md) · [gaps](gaps.md)

## Sources

- https://support.microsoft.com/en-us/windows/file-explorer-in-windows-ef370130-1cca-9dc5-e0df-2f7416fe1cb1 — retrieved 2026-11-13
- https://support.microsoft.com/en-us/windows/keyboard-shortcuts-in-windows-dcc61a57-8ff0-cffe-9796-cb9706c75eec — retrieved 2026-11-13

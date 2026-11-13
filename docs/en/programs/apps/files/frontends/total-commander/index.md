# Total Commander

> Category: [files](../../index.md) · [frontends](../index.md)

## What it is

A paid (shareware) two-pane file manager for Windows by Christian Ghisler ✅ (home page links to ordering and shareware sites; price not stated there; Wikipedia: shareware on Windows, freeware on Android). Current version on the home page: 11.58.1, 32 and 64 bit, announced 2026-10-29 ✅. A USB version and a mobile version exist ✅.

## Notable ideas

- **Two file windows side by side**, each with tabs, plus a command line ✅. Copy and move default to "the other pane" as target (⚠️ third-party, see shortcuts).
- **Selection by pattern** (`*.txt`, exclusion `|*.exe`, regular expressions with `<`), by extension, inversion, restore of the last selection, save to file ✅.
- **Multi-Rename Tool** with a preview, counters, search and replace, regex and an undo that survives closing ✅.
- **Search** with text-in-file, regex, archives, "Everything" backend ✅; **Synchronize directories** with a per-file direction list ✅; **Directory hotlist** ✅; quick search with optional live filter ✅.
- **Archives** (ZIP, 7Z, RAR, TAR, GZ, CAB, ACE and others, plugins) handled like folders ✅; built-in FTP/FTPS client ✅; file compare ✅; Quick View panel ✅.
- Copy dialog with a choice of overwrite modes (ask, overwrite all, skip all, overwrite older, auto-rename) ✅ via the changelog/forum, not the manual.

## What we take

The idea of an explicit **target pane** for copy and move, selection by pattern, a rename tool with preview and undo, a directory favourites list, and sync with a direction list that shows before it acts.

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

- https://www.ghisler.com/ (home page)
- https://www.ghisler.ch/wiki/index.php?title=Selecting_files , Multi-Rename_Tool , Search , Synchronize_directories , Quick_search , Directory_hotlist , Navigation
- https://www.ghisler.ch/wiki/index.php/List_of_changes and forum threads (via search; overwrite modes)
- https://en.wikipedia.org/wiki/Total_Commander (overview)
- Third-party shortcut lists (hotkeysworld.com, devcrea.com, fvck.in) for F-keys: **not official**.
- Not reachable: the built-in help (F1) and `KEYBOARD.TXT` are offline; wiki pages Copy/Move, Background transfer, Tabbed browsing (empty), Directory history (404).

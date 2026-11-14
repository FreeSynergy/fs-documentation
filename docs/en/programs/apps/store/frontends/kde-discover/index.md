# KDE Discover

> Category: [store](../../index.md) · [frontends](../index.md)

## What it is

KDE Discover is the software centre of the KDE Plasma desktop: it finds, installs, updates and removes applications and add-ons (Plasma add-ons, application add-ons) from several sources through exchangeable backends ✅ (apps.kde.org page, fetched 2026-11-14). It is the store frontend that our own code already stands next to (our store program has a card page, a sources page and a settings page; see [gaps](latest/gaps.md)).

## Notable ideas

- **One window, several sources**: operating-system repository, Flatpak, Snap and AppImages from store.kde.org behind one list ✅ (apps.kde.org). When an app comes from several sources, the person chooses which one is the default ✅ (userbase).
- **Backends as plug-ins** for AppStream preview, Flatpak, PackageKit and Snap ✅ (apps.kde.org).
- **Update area that lights up**: the update entry at the bottom of the left column turns bright yellow when updates are waiting ✅ (userbase); updates can be held back one by one with a check box ✅.
- **Search is scoped to the category** that is open (not global) ✅ (userbase).

## What we take

Honest per-source choice (which source installs this), a visible hint when updates wait, and per-item hold-back in the update list. Only function and behaviour are described, nothing is copied (ADR 0013).

## Evidence marks

✅ stated on an official KDE page read on 2026-11-14; `[nicht belegt]` not found in the allowed sources. **Important limit:** the official Discover handbook on docs.kde.org could not be reached (all tested paths gave 404 or "application not found"); the main source is the KDE Userbase wiki page (revision of 2021-06-07, written for Plasma 5), which is old. Menu bar, hamburger menu and context menus are therefore `[nicht belegt]`.

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

## Sources (all fetched 2026-11-14)

- https://userbase.kde.org/Discover (revision oldid 467904, last edited 2021-06-07) and https://userbase.kde.org/Discover/de
- https://apps.kde.org/discover/ (description, backends, releases 6.8.0 to 6.8.3)
- https://docs.kde.org/stable_kf6/en/khelpcenter/fundamentals/kbd.html (general KDE keys, background only)
- Not reachable (404 or not found): https://docs.kde.org/stable_kf6/en/discover/discover/ , https://docs.kde.org/stable5/en/discover/discover/ , https://docs.kde.org/trunk5/en/discover/discover/index.html , https://docs.kde.org/stable_kf6/en/plasma-desktop/index.html , https://userbase.kde.org/Plasma_Discover

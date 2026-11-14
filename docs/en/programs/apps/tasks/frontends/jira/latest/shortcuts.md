# Jira - Keyboard shortcuts

Sources, official Atlassian help for Jira Cloud, read on 2026-11-14 through a summarising fetch: https://support.atlassian.com/jira-software-cloud/docs/use-keyboard-shortcuts/ (single keys), https://support.atlassian.com/jira-software-cloud/docs/what-is-the-command-palette/ (palette), https://support.atlassian.com/jira-software-cloud/docs/navigate-all-work-with-your-keyboard/ (list view), https://support.atlassian.com/jira-software-cloud/docs/search-issues-projects-and-more-with-the-your-keyboard/ and the "... with your keyboard" articles for status, move, delete, child, parent, assignee, story points, sprint, due date, labels, components (all under the same path). Not read: the articles for fix versions, priority, link/unlink, and the full catalogue in the in-app dialog opened with `?` (the help says it holds the complete list), so this list is **not complete**. `[nicht belegt]` = not found on a page read.

## Documented shortcuts

Platform "web" = the page names no platform; Mac and Windows only where the page separates them.

| Platform | Area | Shortcut | Function | Source |
|----------|------|----------|----------|--------|
| Web | Help | `?` (Shift+/) | Opens the dialog with the shortcuts | use-keyboard-shortcuts |
| Web | Create | `C` | Create a work item | use-keyboard-shortcuts |
| Web | Update work item | `O` | Open the selected work item | use-keyboard-shortcuts |
| Web | Update work item | `A` | Assign the work item to someone | use-keyboard-shortcuts |
| Web | Update work item | `I` | Assign the work item to yourself | use-keyboard-shortcuts |
| Web | Update work item | `M` | Add a comment quickly | use-keyboard-shortcuts |
| Web | Board navigation | `J` | Go down | use-keyboard-shortcuts |
| Web | Board navigation | `K` | Go up | use-keyboard-shortcuts |
| Web | Board navigation | `N` | Go to the next column | use-keyboard-shortcuts |
| Web | Board navigation | `P` | Go to the previous column | use-keyboard-shortcuts |
| Mac | Command palette | `Cmd+K` | Open the command palette | what-is-the-command-palette |
| Windows | Command palette | `Ctrl+K` | Open the command palette | what-is-the-command-palette |
| Web | Command palette | `1` | Jump to the backlog of the space (the page says this also works outside the palette) | what-is-the-command-palette |
| Web | Command palette | `/` | In the palette search work items, spaces, boards and filters | what-is-the-command-palette, search page |
| Web | Command palette | Down arrow | Select the command "Search work items, projects, and more" | search page |
| Web | Palette commands | `Enter` | Confirm the chosen palette command or value (move, delete, parent, assignee, story points, sprint, due date, labels, components) | the "... with your keyboard" articles |
| Web | List view | `Tab` | Move between elements of the view | navigate-all-work-with-your-keyboard |
| Web | List view | Arrow keys | Move between cells | same |
| Web | List view | `Home` / `End` | Start or end of a row | same |
| Web | List view | `Page Up` / `Page Down` | Page through the list | same |
| Web | List cell | `Enter` | Confirm a single value | same |
| Web | List cell | `Tab` | Confirm several values | same |
| Mac | List cell | `Cmd+Return` | Confirm several values | same |
| Windows | List cell | `Ctrl+Enter` | Confirm several values | same |
| Web | List cell | `Delete` | Remove the selection | same |

Changing a status, moving, deleting, adding a child, setting parent, assignee, story points, sprint, due date, labels or components by keyboard goes through the command palette (`Cmd+K` / `Ctrl+K`, then the command by name, for example "Change status", "Move work item", "Delete work item", "Add child", "Assign work item", "Assign to me", "Add Story Points", "Add labels"); these actions have no key of their own on the pages read.

### Modifier for browser access keys (use-keyboard-shortcuts)

| Browser | Windows / Linux | macOS |
|---------|-----------------|-------|
| Chrome | `Alt+Shift` | `Ctrl+Alt` (Option) |
| Firefox | `Alt+Shift` | `Ctrl` |
| Safari | `Ctrl` (Windows) | `Ctrl+Alt` (Option) |
| Internet Explorer | `Alt` (Windows) | n/a |

A shortcut that leads to a link needs `Enter` in addition (same page). Switching shortcuts off: Help > Keyboard shortcuts, no key of its own (same page).

## Not found

- Team-managed space shortcut tables (Essentials, Board and backlog, Navigate spaces, Navigate work items, Work item actions): headings only on the page read, `[nicht belegt]`.
- Keys for fix versions, priority, link/unlink: `[nicht belegt]` (articles not read). The article for the priority was summarised with a wrong sentence about the sprint; unchecked.

## Earlier text (unsourced, kept)

The sections below are the earlier text of this dossier. They carry no source; `m` and `a` agree with the official page, but `x`, `z`, `u`, `/` as quick search, `g` then a letter, `l`, `e` and `d` are **not on the pages read** (the official page names `O` for opening a work item, not `x`), so they are `[nicht belegt]` until re-read.

## Overview

Jira Cloud has documented shortkeys; `?` brings up the overview.

> State: Jira Cloud (2026). Data Center is similar, may differ.

## Global

| Shortcut | Function |
|----------|----------|
| `c` | Create an issue (quick entry) |
| `/` | Focus the quick search |
| `u` | Open your own active issues ("my changes" depending on version) |
| `g` then a letter | Navigation: `g d` dashboards, `g p` projects, `g b` boards |
| `?` | Shortkeys overlay |
| `Esc` | Close panels |

## Issue list/board

| Shortcut | Function |
|----------|----------|
| `j` / `k` | next/previous issue (focused) |
| `x` | Open the issue |
| `z` | Close the issue |

## In the issue

| Shortcut | Function |
|----------|----------|
| `m` | Comment |
| `a` | Assign |
| `l` | Labels |
| `e` | All edit fields (detail) |
| `d` | (in some builds) details panel — not official |

## Explicitly not present

- Freely assignable workflow keys (the transitions remain buttons)

## Mac

`Cmd` replaces `Ctrl` (e.g. `Cmd+K` search in the apps); the single letters as above.

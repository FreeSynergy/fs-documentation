# Tasks — Frontends

Frontends of well-known programs in this category, analysed for their **functions** — nothing is copied (ADR 0013). A program is documented here because it is widely learned or because it has a notable idea. Our own program for this category is `FreeSynergy.Tasks` (ADR 0017); its capabilities and status live in [requirements](../requirements.md).

## Programs

| Program | Versions | What it is |
|---------|----------|------------|
| [Things 3](things-3/index.md) | [latest](things-3/latest/description.md) | Things 3 is a personal to-do app for Apple platforms with fixed day lists (Today, This Evening, Someday) and quick entry. |
| [OmniFocus](omnifocus/index.md) | [latest](omnifocus/latest/description.md) | OmniFocus is a GTD-style task manager for Apple platforms with perspectives, forecast and project review. |
| [Taskwarrior](taskwarrior/index.md) | [latest](taskwarrior/latest/description.md) | Taskwarrior is a command-line task manager that ranks tasks by a configurable computed urgency. |
| [Todoist](todoist/index.md) | [latest](todoist/latest/description.md) | Todoist is a cross-platform task manager known for natural-language dates and a filter query language. |
| [Linear](linear/index.md) | [latest](linear/latest/description.md) | Linear is a fast issue tracker with triage inbox, cycles and a GraphQL API. |

## File set per program (ADR 0012)

```
programs/apps/tasks/frontends/<program>/
├── index.md        what it is, notable ideas, documented versions, sources
├── changelog.md    changes between documented versions (≥ 2 versions)
└── <version>/
    ├── description.md    required · Detailed description, differentiation, who it suits
    ├── features.md       required · What the program can do — and what not
    ├── layout.md         required · Window structure, regions, panels
    ├── menus.md          required · Menu structure, context menus, menus by role
    ├── shortcuts.md      required · Keyboard shortcuts
    ├── api.md            required · APIs and protocols, authentication, rate limits
    ├── themes/index.md   required · Themes: colours, typography, spacing — what can be rebuilt
    ├── interaction.md    if needed · Hover, focus, drag, gestures (finger, mouse, pen)
    ├── states.md         if needed · UI states and transitions
    ├── events.md         if needed · Events to the outside (webhooks, push, streams)
    ├── limits.md         if needed · Known limitations
    ├── i18n.md           if needed · Localisation, writing direction
    └── dependencies.md   if needed · Which of our components a frontend in this style needs
```

Protocols (Matrix, IMAP, CalDAV, …) are not frontends; they are described under [data](../../../../data/standards.md).

# Tasks — Frontends

Frontends of well-known programs in this category, analysed for their **functions** — nothing is copied (ADR 0013). A program is documented here because it is widely learned or because it has a notable idea. Our own program for this category is `FreeSynergy.Tasks` (ADR 0017); its capabilities and status live in [requirements](../requirements.md).

## Programs

| Program | Versions | What it is |
|---------|----------|------------|
| [Linear](linear/index.md) | [latest](linear/latest/description.md) | Linear is a team issue tracker built for speed: keyboard-driven, with cycles (time-boxed iterations), projects, initiatives and a triage inbox. |
| [OmniFocus](omnifocus/index.md) | [latest](omnifocus/latest/description.md) | OmniFocus is a task manager for Mac, iPhone, iPad, Apple Watch and Vision Pro, plus OmniFocus for the Web, aimed at long-term projects and the weekly review. |
| [Taskwarrior](taskwarrior/index.md) | [latest](taskwarrior/latest/description.md) | Taskwarrior is a command-line to-do manager. |
| [Things 3](things-3/index.md) | [latest](things-3/latest/description.md) | Things 3 is a personal to-do app for Mac, iPhone, iPad, Apple Watch and Vision Pro, built around a small set of fixed lists and a calm, fast capture flow. |
| [Todoist](todoist/index.md) | [latest](todoist/latest/description.md) | Todoist is a cross-platform task manager with projects, sections, labels, priorities and natural-language dates. |

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
    ├── dependencies.md   if needed · Which of our components a frontend in this style needs
    ├── dialogs.md        if needed · Every dialog: purpose, fields, buttons, default, cancel
    ├── workflows.md      if needed · Step-by-step workflows: goal, prerequisites, steps, failures, undo
    ├── acceptance.md     if needed · Acceptance checklist: each workflow as a yes/no click test
    └── gaps.md           if needed · What our program cannot do for these workflows, and what it needs
```

Protocols (Matrix, IMAP, CalDAV, …) are not frontends; they are described under [data](../../../../data/standards.md).

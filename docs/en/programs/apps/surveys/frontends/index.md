# Surveys — Frontends

Frontends of well-known programs in this category, analysed for their **functions** — nothing is copied (ADR 0013). A program is documented here because it is widely learned or because it has a notable idea. Our own program for this category is `FreeSynergy.Surveys` (ADR 0017); its capabilities and status live in [requirements](../requirements.md).

## Programs

| Program | Versions | What it is |
|---------|----------|------------|
| [Consul Democracy](consul/index.md) | [latest](consul/latest/description.md) | Consul Democracy is open-source software for citizen participation by governments and organisations: debates, proposals, voting, participatory budgeting, collaborative legislation and polls. |
| [Decidim](decidim/index.md) | [latest](decidim/latest/description.md) | Decidim is a participatory democracy platform, started by Barcelona City Hall. |
| [LiquidFeedback](liquidfeedback/index.md) | [latest](liquidfeedback/latest/description.md) | LiquidFeedback is open-source software for developing proposals and deciding online, published by the Public Software Group (Berlin) under the MIT licence. |
| [Loomio](loomio/index.md) | [latest](loomio/latest/description.md) | Loomio is open-source software for group decision-making: share context, discuss, gather input, vote and keep a record of the outcome. |
| [Polis](polis/index.md) | [latest](polis/latest/description.md) | Polis is an open-source platform for gathering sentiment from large groups on open-ended questions. |

## File set per program (ADR 0012)

```
programs/apps/surveys/frontends/<program>/
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

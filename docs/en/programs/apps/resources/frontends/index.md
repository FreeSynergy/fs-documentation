# Resources — Frontends

Frontends of well-known programs in this category, analysed for their **functions** — nothing is copied (ADR 0013). A program is documented here because it is widely learned or because it has a notable idea. Our own program for this category is `FreeSynergy.Resources` (ADR 0017); its capabilities and status live in [requirements](../requirements.md).

## Programs

| Program | Versions | What it is |
|---------|----------|------------|
| [ERPNext](erpnext/index.md) | [latest](erpnext/latest/description.md) | ERPNext is an open-source business management suite built on the Frappe framework. |
| [Grocy](grocy/index.md) | [latest](grocy/latest/description.md) | Grocy is a self-hosted web app for household groceries and chores: stock, shopping list, recipes, meal plan, chores, tasks, equipment and batteries. |
| [Odoo](odoo/index.md) | [latest](odoo/latest/description.md) | Odoo is a suite of business apps (sales, inventory, accounting and more) on one platform, as open-source community and commercial enterprise editions (edition split: Open). |
| [Snipe-IT](snipe-it/index.md) | [latest](snipe-it/latest/description.md) | Snipe-IT is an open-source IT asset management web app. |

## File set per program (ADR 0012)

```
programs/apps/resources/frontends/<program>/
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

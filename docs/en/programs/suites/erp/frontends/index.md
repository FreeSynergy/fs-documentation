# Erp — Frontends

Frontends of well-known programs in this category, analysed for their **functions** — nothing is copied (ADR 0013). A program is documented here because it is widely learned or because it has a notable idea. Our own program for this category is `FreeSynergy.Erp` (ADR 0017); its capabilities and status live in [requirements](../requirements.md).

## Programs

| Program | Versions | What it is |
|---------|----------|------------|
| [Axelor](axelor/index.md) | [latest](axelor/latest/description.md) | Axelor Open Suite (AGPL, Java) combines ERP (CRM, Sales, Purchasing, Stock, Manufacturing, Account, HR, Project) with **low-code/BPM**: forms, models and workflows are modelled in the "App Builder"… |
| [Dolibarr](dolibarr/index.md) | [latest](dolibarr/latest/description.md) | Dolibarr (GPL, PHP) is the lean SME ERP/CRM: third parties, quotes/orders, invoices, stock, projects, basic accounting — easy to host (LAMP), stable core, extension market. |
| [ERPNext](erpnext/index.md) | [latest](erpnext/latest/description.md) | ERPNext (GPLv3) is the complete open-source ERP built on the **Frappe framework** (Python/MariaDB): accounting, inventory, buying/selling, HR, manufacturing, projects — entirely free of licence fee… |
| [Odoo](odoo/index.md) | [latest](odoo/latest/description.md) | Odoo is the open business suite (LGPL core + commercial Enterprise apps): CRM, sales, purchasing, warehouse, manufacturing, accounting, projects, HR — as integrated modules with a shared ORM layer. |
| [Sage](sage/index.md) | [latest](sage/latest/description.md) | "Sage" is a commercial suite group (Sage Group) for accounting/ERP: **Sage Business Cloud** (SaaS accounting, successor to Sage One, for example), **Sage 100** (mid-market ERP, on-premise), **Sage … |
| [Tryton](tryton/index.md) | [latest](tryton/latest/description.md) | Tryton (GPL, Python) is the calm, modular ERP for technical users: modules for accounting, sales, purchasing, warehouse, projects, time tracking — with strong data integrity, a desktop client (GTK)… |

## File set per program (ADR 0012)

```
programs/suites/erp/frontends/<program>/
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

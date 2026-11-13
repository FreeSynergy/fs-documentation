# Democracy — Frontends

Frontends of well-known programs in this category, analysed for their **functions** — nothing is copied (ADR 0013). A program is documented here because it is widely learned or because it has a notable idea. Our own program for this category is `FreeSynergy.Democracy` (ADR 0017); its capabilities and status live in [requirements](../requirements.md).

## Programs

| Program | Versions | What it is |
|---------|----------|------------|
| [Adhocracy4](adhocracy4/index.md) | [latest](adhocracy4/latest/description.md) | Adhocracy4 (AGPL, Python/Django) is the participation framework behind many municipal portals (including the Berlin portal "mein.berlin.de"): projects with phases (brainstorming, idea review, evalu… |
| [Circo](circo/index.md) | [latest](circo/latest/description.md) | Circo (citizen participation and consultation platform, used in Germany and Austria by associations and for parliamentary consultations) combines **surveys, workshops and online consultations** wit… |
| [Consul](consul/index.md) | [latest](consul/latest/description.md) | Consul ("Decide Madrid" software, Apache-2.0, Ruby on Rails) is the participation platform for municipalities: proposals, participation processes, **citizen budgets**, polls and votes, debates, leg… |
| [Decidim](decidim/index.md) | [latest](decidim/latest/description.md) | Decidim (AGPL, Ruby on Rails) is the platform for **participatory democracy**: processes (citizen budgets, participation, planning), proposals with comments and supports, debates, meetings and even… |
| [LiquidFeedback](liquid-feedback/index.md) | [latest](liquid-feedback/latest/description.md) | LiquidFeedback ("LiQu", PHP, free software) implements **delegative voting (liquid democracy)**: initiatives in topic rooms, delegation chains for votes, arguments for and against, votes with quorums. |
| [Pol.is](polis/index.md) | [latest](polis/latest/description.md) | Pol.is (commercial, with non-profit roots) is the **deliberation scaling platform**: all participants write comments and rate those of others ("agree/disagree/pass") — an algorithm clusters the opi… |

## File set per program (ADR 0012)

```
programs/suites/democracy/frontends/<program>/
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

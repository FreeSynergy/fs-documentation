# Helpdesk — Frontends

Frontends of well-known programs in this category, analysed for their **functions** — nothing is copied (ADR 0013). A program is documented here because it is widely learned or because it has a notable idea. Our own program for this category is `FreeSynergy.Helpdesk` (ADR 0017); its capabilities and status live in [requirements](../requirements.md).

## Programs

| Program | Versions | What it is |
|---------|----------|------------|
| [Chatwoot](chatwoot/index.md) | [latest](chatwoot/latest/description.md) | Chatwoot is a customer-support platform where conversations from many channels land in one shared inbox. |
| [Freshdesk](freshdesk/index.md) | [latest](freshdesk/latest/description.md) | Freshdesk (Freshworks) is a SaaS helpdesk with tickets, knowledge base, SLAs, omnichannel e-mail/phone/chat and Freddy AI. |
| [GLPI](glpi/index.md) | [latest](glpi/latest/description.md) | GLPI is a French-flavoured open-source ITSM: helpdesk tickets plus complete IT asset management (computers, software, contracts, network), reporting that supports projects and budgets. |
| [Helodesk](helodesk/index.md) | [latest](helodesk/latest/description.md) | Helodesk is a French SaaS customer-service suite (contact centre): telephony/softphone, e-mail, chat, SMS and callback in one surface, plus cases (tickets), knowledge base, IVR and reporting. |
| [Help Scout](helpscout/index.md) | [latest](helpscout/latest/description.md) | Help Scout is support as a shared inbox: customers write to an e-mail address ("Conversations"), the team replies as if from a personal mail — without the ticket-number feel. |
| [osTicket](osticket/index.md) | [latest](osticket/latest/description.md) | osTicket is the classic among open-source helpdesks: PHP/MySQL, e-mail ingest, help topics, filter rules and a plain agent and customer portal. |
| [Request Tracker (RT)](request-tracker/index.md) | [latest](request-tracker/latest/description.md) | Request Tracker by Best Practical is the veteran of ticket systems: Perl-based, extremely regexp-/script-driven, with REST 1.0 and JSON-RPC 2.0 APIs. |
| [Zammad](zammad/index.md) | [latest](zammad/latest/description.md) | Zammad is a modern, open-source helpdesk: tickets from e-mail, web form, chat, phone and Telegram converge in one surface, with SLAs, text modules, knowledge base and a fully-fledged REST API. |
| [Zendesk](zendesk/index.md) | [latest](zendesk/latest/description.md) | Zendesk is the commercial support platform (SaaS) with tickets, Help Center, chat/messaging, voice and analytics. |

## File set per program (ADR 0012)

```
programs/apps/helpdesk/frontends/<program>/
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

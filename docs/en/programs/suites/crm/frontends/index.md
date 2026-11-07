# Crm — Frontends

Frontends of well-known programs in this category, analysed for their **functions** — nothing is copied (ADR 0013). A program is documented here because it is widely learned or because it has a notable idea. Our own program for this category is `FreeSynergy.Crm` (ADR 0017); its capabilities and status live in [requirements](../requirements.md).

## Programs

| Program | Versions | What it is |
|---------|----------|------------|
| [CiviCRM](civicrm/index.md) | [latest](civicrm/latest/description.md) | CiviCRM is the open CRM for associations, NGOs and clubs ("Constituent Relationship Management"): contacts, donations, memberships, events, campaigns and cases — embedded in a CMS (Drupal, Joomla o… |
| [EspoCRM](espocrm/index.md) | [latest](espocrm/latest/description.md) | EspoCRM is a lean, fast open-source CRM (PHP + Backbone/JS, SPA): leads, opportunities, accounts, contacts and activities — with a graphical entity manager, workflows and a clean REST API. |
| [HubSpot](hubspot/index.md) | [latest](hubspot/latest/description.md) | HubSpot is the marketing-first CRM suite (SaaS): a free CRM (contacts, companies, deals, tickets) plus paid hubs for marketing (email, campaigns, landing pages), sales (sequences, pipelines) and se… |
| [Pipedrive](pipedrive/index.md) | [latest](pipedrive/latest/description.md) | Pipedrive is a cloud-based sales CRM organized around the sales pipeline: deals move through columns (stages) from qualification to closing, supplemented by leads, contacts, organizations, activiti… |
| [Salesforce](salesforce/index.md) | [latest](salesforce/latest/description.md) | Salesforce is the leading commercial CRM platform (SaaS): leads, accounts, contacts, opportunities and dozens of clouds (Service, Marketing, Commerce, Analytics) on a modelable data core (standard … |
| [SuiteCRM](suitecrm/index.md) | [latest](suitecrm/latest/description.md) | SuiteCRM is an open-source CRM (AGPL-3.0) that emerged in 2013 as a fork of the open SugarCRM suite and is today developed further by the community around SalesAgility. |

## File set per program (ADR 0012)

```
programs/suites/crm/frontends/<program>/
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

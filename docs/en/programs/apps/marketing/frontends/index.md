# Marketing — Frontends

Frontends of well-known programs in this category, analysed for their **functions** — nothing is copied (ADR 0013). A program is documented here because it is widely learned or because it has a notable idea. Our own program for this category is `FreeSynergy.Marketing` (ADR 0017); its capabilities and status live in [requirements](../requirements.md).

## Programs

| Program | Versions | What it is |
|---------|----------|------------|
| [Google Analytics](google-analytics/index.md) | [latest](google-analytics/latest/description.md) | Google Analytics (GA4, commercial) is the standard workhorse of web/app analytics: event-based measurement (events + parameters), audiences, funnels, attribution — linked with Google Ads/Search Con… |
| [Hotjar](hotjar/index.md) | [latest](hotjar/latest/description.md) | Hotjar (commercial) supplements web analytics with the **how**: heatmaps (clicks/scrolls/moves), session replays, surveys (onsite surveys), feedback/rage-click detection and funnel coupling. |
| [Listmonk](listmonk/index.md) | [latest](listmonk/latest/description.md) | Listmonk is a self-hosted newsletter and mailing-list manager as a single binary with PostgreSQL. |
| [Mailchimp](mailchimp/index.md) | [latest](mailchimp/latest/description.md) | Mailchimp (Intuit, commercial) is the newsletter/marketing-automation platform: lists + segments, campaign editor, e-mail automations (journeys), landing pages, CRM-lite and analytics. |
| [Matomo](matomo/index.md) | [latest](matomo/latest/description.md) | Matomo (GPL, formerly Piwik) is the leading **self-hostable web-analytics platform** (PHP/MySQL): visitor analysis capable of running cookieless, cookies with consent integration, heatmaps/session … |
| [Mautic](mautic/index.md) | [latest](mautic/latest/description.md) | Mautic (GPL, PHP/Symfony) is open-source marketing automation: contacts + segments, e-mail campaigns, **campaign tree** (triggers/actions), landing pages/forms, point scoring — self-hosted with ful… |
| [Plausible](plausible/index.md) | [latest](plausible/latest/description.md) | Plausible (MIT/AGPL dual depending on edition) is minimalist web analytics: one script, one numbers view, cookieless and GDPR-friendly, self-hosted or cloud. |
| [Umami](umami/index.md) | [latest](umami/latest/description.md) | Umami is a privacy-focused, cookieless web and product analytics tool with events, funnels, retention and journeys. |

## File set per program (ADR 0012)

```
programs/apps/marketing/frontends/<program>/
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

# Contact — Frontends

Frontends of well-known programs in this category, analysed for their **functions** — nothing is copied (ADR 0013). A program is documented here because it is widely learned or because it has a notable idea. Our own program for this category is `FreeSynergy.Contact` (ADR 0017); its capabilities and status live in [requirements](../requirements.md).

## Programs

| Program | Versions | What it is |
|---------|----------|------------|
| [GNOME Contacts](gnome-contacts/index.md) | [latest](gnome-contacts/latest/description.md) | GNOME Contacts is the lean contact app for GNOME: create contacts, link them, synchronise them with Evolution Data Server sources (local address books, CalDAV/CardDAV accounts, Google, LDAP). |
| [KAddressBook](kaddressbook/index.md) | [latest](kaddressbook/latest/description.md) | KAddressBook is the contact management application of KDE PIM: vCard-based, managed through Akonadi resources (local folders, IMAP-Contacts, CardDAV, LDAP). |
| [Monica](monica/index.md) | [latest](monica/latest/description.md) | Monica is a self-hosted personal CRM: capture people with all their relationships, activities, gifts, tasks and notes — as a web app (Laravel/Vue) with a REST API. |
| [Nextcloud Contacts](nextcloud-contacts/index.md) | [latest](nextcloud-contacts/latest/description.md) | Nextcloud Contacts is the contact app of the Nextcloud suite: address books in the browser, synchronised over CardDAV with all devices, linked to user accounts, circles/groups and the people area o… |

## File set per program (ADR 0012)

```
programs/apps/contact/frontends/<program>/
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

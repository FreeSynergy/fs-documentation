# Wiki — Frontends

Frontends of well-known programs in this category, analysed for their **functions** — nothing is copied (ADR 0013). A program is documented here because it is widely learned or because it has a notable idea. Our own program for this category is `FreeSynergy.Wiki` (ADR 0017); its capabilities and status live in [requirements](../requirements.md).

## Programs

| Program | Versions | What it is |
|---------|----------|------------|
| [Confluence](confluence/index.md) | — | Confluence is an enterprise wiki platform by Atlassian for team collaboration. |
| [MediaWiki](mediawiki/index.md) | — | MediaWiki is the most popular wiki software, used among others by Wikipedia. |
| [Notion](notion/index.md) | — | Notion is an all-in-one platform for notes, documentation and collaboration. |
| [Tango.io](tango.io/index.md) | — | Tango.io is a modern knowledge-management platform that focuses on collaboration. |
| [VSCodium](vscodium/index.md) | — | VSCodium is an open-source version of Microsoft Visual Studio Code. |
| [Wiki.js](wikijs/index.md) | — | Wiki.js is a modern, lightweight wiki system based on Node.js. |
| [XWiki](xwiki/index.md) | — | XWiki is a powerful enterprise wiki platform with advanced features for knowledge management. |

## File set per program (ADR 0012)

```
programs/apps/wiki/frontends/<program>/
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

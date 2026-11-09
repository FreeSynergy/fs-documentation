# Wiki — Frontends

Frontends of well-known programs in this category, analysed for their **functions** — nothing is copied (ADR 0013). A program is documented here because it is widely learned or because it has a notable idea. Our own program for this category is `FreeSynergy.Wiki` (ADR 0017); its capabilities and status live in [requirements](../requirements.md).

## Programs

| Program | Versions | What it is |
|---------|----------|------------|
| [Confluence](confluence/index.md) | [latest](confluence/latest/description.md) | Confluence is a team wiki and collaboration product by Atlassian. |
| [MediaWiki](mediawiki/index.md) | [1.46](mediawiki/1.46/description.md), [latest](mediawiki/latest/description.md) | MediaWiki is the wiki engine behind Wikipedia and the other Wikimedia projects. |
| [Notion](notion/index.md) | [2026-11-07](notion/2026-11-07/description.md), [latest](notion/latest/description.md) | Notion is a hosted all-in-one workspace for notes, documents and databases, built from typed blocks. |
| [Tango](tango/index.md) | [latest](tango/latest/description.md) | Tango turns recorded clicks into step-by-step guides; not a wiki, documented for its capture-to-guide idea. |
| [Tango.io](tango.io/index.md) | [latest](tango.io/latest/description.md) | Tango.io is a modern knowledge management platform focused on collaboration. |
| [VSCodium](vscodium/index.md) | [latest](vscodium/latest/description.md) | VSCodium is an open-source version of Microsoft Visual Studio Code. |
| [Wiki.js](wikijs/index.md) | [3.1.1](wikijs/3.1.1/description.md), [latest](wikijs/latest/description.md) | Wiki.js is an open-source, self-hosted wiki engine. |
| [XWiki](xwiki/index.md) | [latest](xwiki/latest/description.md) | XWiki is a powerful enterprise wiki platform with advanced features for knowledge management. |
| [Logseq](logseq/index.md) | [latest](logseq/latest/description.md) | Logseq is an open-source outliner with block references and a database version with typed tags. |
| [Obsidian](obsidian/index.md) | [latest](obsidian/latest/description.md) | Obsidian is a local-first Markdown notes app with backlinks and a Canvas board. |
| [Tana](tana/index.md) | [latest](tana/latest/description.md) | Tana is an outliner with supertags that turn nodes into typed objects. |

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

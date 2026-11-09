# Store — Frontends

Frontends of well-known programs in this category, analysed for their **functions** — nothing is copied (ADR 0013). A program is documented here because it is widely learned or because it has a notable idea. Our own program for this category is `FreeSynergy.Store` (ADR 0017); its capabilities and status live in [requirements](../requirements.md).

## Programs

| Program | Versions | What it is |
|---------|----------|------------|
| [F-Droid](f-droid/index.md) | [latest](f-droid/latest/description.md) | F-Droid is a community catalogue and installer client for free-software Android apps, with Anti-Feature labels and reproducible-build checks. |
| [Flathub](flathub/index.md) | [latest](flathub/latest/description.md) | Flathub is the main app store for Flatpak on Linux, with verified publishers and client subsets. |
| [Obtainium](obtainium/index.md) | [latest](obtainium/latest/description.md) | Obtainium is an Android app that installs and updates apps straight from their release pages. |

## File set per program (ADR 0012)

```
programs/apps/people/frontends/<program>/
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

# Desktop — Frontends

Frontends of well-known programs in this category, analysed for their **functions** — nothing is copied (ADR 0013). A program is documented here because it is widely learned or because it has a notable idea. Our own program for this category is `FreeSynergy.Desktop` (ADR 0017); its capabilities and status live in [requirements](../requirements.md).

## Programs

| Program | Versions | What it is |
|---------|----------|------------|
| [dashy](dashy/index.md) | [latest](dashy/latest/description.md) |  |
| [gethomepage](gethomepage/index.md) | [latest](gethomepage/latest/description.md) |  |
| [heimdall](heimdall/index.md) | [latest](heimdall/latest/description.md) |  |
| [homarr](homarr/index.md) | [latest](homarr/latest/description.md) |  |
| [homepage](homepage/index.md) | [latest](homepage/latest/description.md) |  |
| [homer](homer/index.md) | [latest](homer/latest/description.md) |  |
| [launchboard](launchboard/index.md) | [latest](launchboard/latest/description.md) |  |
| [opnsense](opnsense/index.md) | [latest](opnsense/latest/description.md) |  |
| [proxmox](proxmox/index.md) | [latest](proxmox/latest/description.md) |  |
| [synology-dsm](synology-dsm/index.md) | [latest](synology-dsm/latest/description.md) |  |
| [truenas](truenas/index.md) | [latest](truenas/latest/description.md) |  |
| [unraid](unraid/index.md) | [latest](unraid/latest/description.md) |  |

## File set per program (ADR 0012)

```
programs/platform/desktop/frontends/<program>/
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

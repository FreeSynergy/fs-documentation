# Whiteboards — Frontends

Frontends of well-known programs in this category, analysed for their **functions** — nothing is copied (ADR 0013). A program is documented here because it is widely learned or because it has a notable idea. Our own program for this category is `FreeSynergy.Whiteboards` (ADR 0017); its capabilities and status live in [requirements](../requirements.md).

## Programs

| Program | Versions | What it is |
|---------|----------|------------|
| [draw.io](drawio/index.md) | — | draw.io (diagrams.net) is a free diagram tool for flowcharts, network plans, UML and BPMN. |
| [Excalidraw](excalidraw/index.md) | — | Excalidraw is a free, open-source collaborative whiteboard in a hand-drawn style. |
| [Miro](miro/index.md) | — | Miro is the commercial online whiteboard (SaaS) for visual collaboration: infinite canvas, shapes/sticky notes, frames, template library (retros, workshops, customer journeys), voting/timer and boa… |
| [Mural](mural/index.md) | — | Mural is the workshop whiteboard suite (SaaS) with strong facilitation: canvas with shapes/notes, "Facilitation Sequence" (moderation flows), participation control and templates. |
| [OpenBoard](openboard/index.md) | — | OpenBoard is a free interactive whiteboard tool (C++, Qt) for teaching and presentations: multi-page "boards", pens/text/images, integrated browser, document and note tools, offline-first with a lo… |
| [tldraw](tldraw/index.md) | — | tldraw is an open-source infinite-canvas whiteboard library and app in TypeScript: ready to use on tldraw.com and as a React SDK (`tldraw`) for your own canvas applications. |

## File set per program (ADR 0012)

```
programs/apps/whiteboards/frontends/<program>/
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

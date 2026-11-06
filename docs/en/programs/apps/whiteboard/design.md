# Whiteboard — design

**Status: proposal (2026-11-06).** Back to the [roadmap](../roadmap.md) · [requirements](requirements.md).

The program is `FreeSynergy.Whiteboard` (`fs-whiteboard`). The docs folder is still called `whiteboards`; renaming it
to match ADR 0017 is pending, since other work is in progress in this folder.

## Idea

An infinite canvas on which people draw, place shapes and write notes, alone or together. Every element is an object
with an id, so elements can be searched, referred to and reused. A board is not just a picture.

## Data

| Piece | Standard | Notes |
|-------|----------|-------|
| Board | AS2 `Collection` | |
| Element: shape, connector, note, image, stroke | ❌ none | **Own specification** ([standards](../../../data/standards.md) records the gap) |
| Text in notes | Same text model as the wiki (ADR 0033, 0042) | |
| Image on a board | Reference to an `fs-files` object | |
| Handwriting | InkML ⚠️ | Weak evidence so far; to be checked before use |
| Export | SVG, PNG, PDF ⚠️ | Export formats, not the data model (ADR 0042) |

The own specification is a real contribution: as far as we found, no open standard describes a whiteboard as a queryable
model. It is a candidate for submission (ADR 0014).

## Live collaboration

Three different kinds of data with different needs:

| Kind | Example | Handling |
|------|---------|----------|
| **Lasting, per object** | Moving a shape | Activity log, last change per property wins |
| **Lasting, growing** | Freehand stroke | Each finished stroke is a new object, so strokes do not conflict |
| **Passing** | Other people's cursors | A live channel only; never stored |

**Recommendation: start with per-object sync, behind an interface,** which matches the object-level sync we already
decided on (ADR 0019). Conflicts are rare because two people seldom change the same property of the same shape.
Notes edited together are the exception: if this proves insufficient, a CRDT (`yrs` 0.28, `automerge` 0.12) can be added
for note text only. The passing channel does not exist yet, and streaming and the messenger could use it too.

**Like in a game (decided 2026-11-06):** you see what others are doing as they do it: cursors, selections, a shape moving
while it is being dragged. That is the live channel, a shared [`Presence` interface](../../../interfaces/index.md). A CRDT is
a separate matter: it merges changes correctly, and we use it only where properties are not enough, for text. Updates to
properties need a logical clock, not wall time, and each property is merged by itself, so that one person's colour change
does not undo another's move.

## Patterns

| Pattern | Use |
|---------|-----|
| Composite | Groups of elements as one element |
| Command | Every change has `apply` and `invert`, for undo (ADR 0042) |
| State | Tools: select, draw, connect, each with its own behaviour |
| Strategy | Export format; connector routing; snapping |
| Observer | Changes and presence |
| Flyweight | Shared style objects when boards hold many elements |

## Rendering

Blinc has a [`canvas`](https://github.com/project-blinc/Blinc) element with direct GPU drawing, which is the basis. The
core has no dependency on Blinc: it computes the scene, and the component draws it.

| Purpose | Crate (2026-11-06) |
|---------|--------------------|
| Find visible elements quickly | `rstar` 0.14 |
| Shapes to triangles, if Blinc does not cover it | `lyon` 1.0 |
| SVG import and export | `usvg`, `resvg` 0.49 |

Stylus pressure and tilt are missing in Blinc and are planned as our contribution upstream.

## Interface sketch

| Interface | Capabilities |
|-----------|--------------|
| `Whiteboard` (root) | `capabilities()`, hands out the others |
| `Boards` | `board.open`, `board.create`, `board.delete` |
| `Board` | `shape.add`, `stroke.draw`, `note.add`, `element.move`, `element.style`, `element.delete`, `element.group`, `element.reorder` |
| `Presence` | Live cursors and selection |
| `Export` | `board.export` |
| `subscribe` | Live changes |

The ids follow the [requirements](requirements.md).

## Components

Workbench `whiteboard` (documented, to be reworked), with a compact read-only or embed variant. New: `infinite-canvas`,
`selection-handles`, `minimap`, `presence-cursors`. See [planned components](../../../components/planned.md).

## Stages

1. Data specification draft, core: elements, groups, undo, spatial index, tests.
2. `infinite-canvas` on Blinc: pan, zoom, shapes, drawing. A measurement of many elements decides whether the approach holds.
3. Workbench, first simple frontend, notes, connectors, images, export.
4. Live collaboration with presence, comments, templates.

## Open questions

1. **Per-object sync or CRDT?** See above; recommendation: per-object first.
2. **Which is first: drawing, or diagrams with connectors?** The frontends split into both camps. We propose freehand and
   simple shapes first, connectors in stage 3.
3. **The stylus:** how important is it for the first version? It requires contributing to Blinc first.
4. **The existing `whiteboard` component** still has German variant names (`zeichnung`, `formen`, `notizen`, `vorlage`)
   and will be reworked.

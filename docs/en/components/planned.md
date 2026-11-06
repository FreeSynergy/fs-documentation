# Planned components

**Status: proposal (2026-11-06), program names partly older than the [overall plan](../programs/apps/roadmap.md): kanban is now part of Tasks, the gallery part of Files.** See also [charts](charts.md). None
is built or documented in detail yet. Layers follow the existing structure: primitives, widgets, workbenches.

As with all components, gestures are not part of them; they come from the frontend (ADR 0037). Names are proposals.

## What exists (`fs-components` v0.2.0, 2026-11-06)

Released: the reader, `text-view`, `avatar-group`, `transfer-list`, `sortable-list`, `lightbox`, `share-dialog`. They have been reviewed, but tested
without a real window; nobody has used them by hand yet. **Not released, although included in this tag:** `charts`, which has open blockers, the five chat components,
which are still being reviewed, and the calendar work.

## Build first: shared by several programs

| Component | Layer | What it does | Used by |
|-----------|-------|--------------|---------|
| `sortable-list` | widgets/data | Reorder items, also between lists; works with keyboard too | Kanban, surveys, files, gallery albums |
| `share-dialog` | widgets/overlays | Choose people and permissions | Files, gallery, kanban, surveys, whiteboard |
| `avatar-group` | widgets/data | Several people in little space | Kanban, whiteboard, messenger |
| `transfer-list` | widgets/data | Running uploads and downloads with progress | Files, gallery, messenger, streaming |
| `lightbox` | widgets/overlays | Show one item full-screen and step through items | Gallery, files, messenger, kanban |

## By program

| Program | New | Reused or changed |
|---------|-----|-------------------|
| **Files** | workbench `file-manager` (compact: `file-picker`); widgets `file-tile`, `file-preview` | `tree-view`, `list-view`, `grid-view`, `breadcrumb`, `context-menu`, `search-field`; **change** `file-upload`: resumable with progress |
| **Tasks (kanban)** | workbench `kanban-board`; widgets `board-column`, `task-card`, `checklist` | `sortable-list`, `card`, `drawer`, `tags-input`, `date-picker`, `badge` (limit reached), `timeline` (activity), `message-list` (comments) |
| **Surveys** | workbenches `survey-builder`, `survey-form`; widgets `question`, `matrix-question`, `ranking-list` | `field`, `radio-group`, `checkbox`, `rating`, `slider`, `date-input`, `wizard`, `progress`, `chart`, `table` |
| **Files (gallery)** | workbench `gallery-browser` | `lightbox`, `carousel`, `image`, `video`, `map-view`, `timeline`, `description-list`; **change** `gallery`: large collections, virtual scrolling, grouping by date |
| **Whiteboard** | widgets `infinite-canvas`, `selection-handles`, `minimap`, `presence-cursors` | `toolbar`, `color-input`, `slider`, `tree-view` (layers), `popover`, `image`; **rework** workbench `whiteboard`: English variant names, compact variant |
| **Assistant** | workbench `llm-chat`; widgets `agent-tree`, `tool-call` | `message-list`, `message-composer`, long-text view on our text core |
| **Streaming** | workbench `stream-studio`; widgets `stream-tile`, `level-meter` | `audio`, `video`, `call-controls`, `grid-view`, `message-list`, `badge` (live); **change** `media-player`: live mode |

## Blinc as the base

| Need | In Blinc 0.6 (`.research-blinc`) | Then |
|------|----------------------------------|------|
| `infinite-canvas` | `canvas` element with direct GPU drawing | Build on it; measure early with many elements |
| `sortable-list` | Drag events exist in `blinc_layout`; no ready-made sortable list seen | Ours, candidate for contribution (`todo/upstream.md`) |
| `tree-view` | `tree` in `blinc_cn` | Adapter |
| `media-player`, `video` | `blinc_media`: player, frames, camera; OpenH264 on the desktop | Live mode to be checked |
| Stylus pressure and tilt | Missing | Contribution already planned |

This table comes from a quick look at the source, not from a test.

## Next step

After the decisions on the roadmap, each component receives the usual documentation skeleton
(`description`, `appearance`, `attributes`, `usage`) and an entry in `conventions/CONVENTIONS.md` §3.

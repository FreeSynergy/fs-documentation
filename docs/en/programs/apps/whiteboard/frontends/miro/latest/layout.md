# Miro - Structure and UI/UX

## Page structure

```
┌──────────────────────────────────────────────────────────────────┐
│ Miro ▾  Title…                Pages (1|2|3)     👥 👤 Share      │
│┌──┐                                                   ┌─────┐    │
││S │     (infinite canvas with frames)                  │Page │    │
││T │     ┌──Frame: Retrospective──┐                     │minia│    │
││O │     │ 🟦 What went well? 🟨… │                     └─────┘    │
││P │     │ [Sticky][Sticky]       │                                │
││↗ │     └────────────────────────┘    Timer 🕐 · Voting ✓         │
│└──┘                                                              │
└──────────────────────────────────────────────────────────────────┘
```

- Left vertical toolbar, right page list with thumbnails, header with participants/share

## UI/UX

- Polished light design, gentle zoom/pan transitions, tooltips for every tool
- Smart layout for mindmaps/organisation charts

## Interactions

- **Multiplayer**: cursors with names, selection locks, live sticky typing
- **Drag & drop**: elements, frames group things, collection "groups"
- **Presenting**: focus on frames, the presenter follows the camera path

## Responsive design

- Web is desktop-centred; iPad with pencil support; mobile app for viewing/quick edits

## Accessibility

- Miro publishes an accessibility roadmap/VPAT (Enterprise); keyboard tools: shortcuts (see [shortcuts.md](shortcuts.md)), stickies fully editable by keyboard

## Performance

- Frames keep large boards (>10k items) workable; older browsers are weak

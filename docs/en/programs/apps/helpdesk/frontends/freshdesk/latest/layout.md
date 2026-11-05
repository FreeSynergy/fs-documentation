# Freshdesk - Structure and UI/UX

## Page structure

```
┌──────────┬───────────────────────────┬──────────────────────────┐
│ 🔍 …                                    Freshworks suite  [👤]   │
├──────────┼───────────────────────────┼──────────────────────────┤
│ Home ▾   │ Ticketlist (filter chips) │ #1024 Invoice incorrect  │
│ Tickets  │ #1024 ●due 2h Beta        │ [↩Reply][Private note]   │
│ Contacts │ #1025 off   Alpha         │ Status: Open ▾ Prio ▾    │
│ KB       │ …                         │ Product ▾ Group ▾ Tags   │
│ Reports  │                           │ ── Conversation ──       │
│ Apps     │                           │ ⏱ Tick · Attachments     │
└──────────┴───────────────────────────┴──────────────────────────┘
```

- Three zones like Zendesk; right-hand attribute column instead of its own app sidebar (apps dock on the right)

## UI/UX

- Freshworks design: friendly blue/white, rounded chips
- Live updates of the lists (polling/WebSocket mix)

## Interactions

- **Drag & drop** attachments; reply templates as snippets; replies via macro buttons
- **Reply editor** with AI suggestions (Freddy, plan-dependent)

## Responsive design

- The web UI is partly responsive; the official **agent app** (iOS/Android) and **customer app** for portals

## Accessibility

- WCAG 2.1-AA efforts documented (Freshworks trust centre); form labels present
- Shortcuts as a mouse substitute (see [shortcuts.md](shortcuts.md))

## Performance

- Lists are virtually scrolled; large instances stay smooth

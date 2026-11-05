# Help Scout - Structure and UI/UX

## Page structure

```
┌──────────────────────────────────────────────────────────────┐
│ [Mailbox ▾] 🔍 …                              Docs Reports ⚙  │
├──────────────┼───────────────────────┼───────────────────────┤
│ Folders      │ Conversation list     │ Conversation          │
│ Needs resp.  │ ✉ Invoice incorrect   │ "Invoice incorrect"   │
│ Active       │ ✉ Printer …           │ [Reply][Forward][Note]│
│ Everyone     │ ✉ API question        │ Status: Active ▾      │
│ Closed       │                       │ Assignee ▾ Tags ▾     │
│              │                       │ ── Thread ──          │
│              │                       ├───────────────────────┤
│              │                       │ Person: Beta GmbH     │
│              │                       │ Fields · History      │
└──────────────┴───────────────────────┴───────────────────────┘
```

## UI/UX

- Calm, white, mail-client aesthetics; no ticket jargon in the customer view
- Person card + snippets on the right

## Interactions

- **Snooze** as a date picker, **assign** by click, **tag** inline
- Collision notice when a colleague is already replying
- No drag & drop (exception: email attachments in a reply)

## Responsive design

- The web is partly responsive; iOS/Android app and desktop app for agents

## Accessibility

- Mail-client standard tabbing; reply field tested with screenreaders
- Shortcuts see [shortcuts.md](shortcuts.md)

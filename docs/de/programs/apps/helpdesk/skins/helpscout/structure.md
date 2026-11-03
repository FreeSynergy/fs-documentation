# Help Scout - Struktur und UI/UX

## Seitenstruktur

```
┌──────────────────────────────────────────────────────────────┐
│ [Mailbox ▾] 🔍 …                              Docs Reports ⚙ │
├──────────────┬───────────────────────┬───────────────────────┤
│ Ordner       │ Konversationsliste    │ Conversation          │
│ Needs resp.  │ ✉ Rechnung falsch    │ „Rechnung falsch“     │
│ Active       │ ✉ Drucker …           │ [Reply][Forward][Note]│
│ Everyone     │ ✉ Frage API           │ Status: Active ▾      │
│ Closed       │                       │ Assignee ▾ Tags ▾     │
│              │                       │ ── Thread ──          │
│              │                       ├───────────────────────┤
│              │                       │ Person: Beta GmbH     │
│              │                       │ Fields · Historie     │
└──────────────┴───────────────────────┴───────────────────────┘
```

## UI/UX

- ruhig, weiß, Mailclient-Ästhetik; kein Ticket-Jargon in der Kundenansicht
- Rechts Person-Karte + Snippets

## Interaktionen

- **Snooze** als Datumspicker, **Assign** per Klick, **Tag** inline
- Kollisionshinweis, wenn ein Kollege bereits antwortet
- Kein Drag & Drop (Ausnahme: E-Mail-Dateianhänge in Reply)

## Responsive Design

- Web teilweise responsiv; iOS-/Android-App und Desktop-App für Agenten

## Accessibility

- Mailclient-Standardtabellen; screenreader-getestetes Reply-Feld
- Shortcuts siehe [shortcuts.md](shortcuts.md)

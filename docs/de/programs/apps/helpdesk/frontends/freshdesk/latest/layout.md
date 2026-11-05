# Freshdesk - Struktur und UI/UX

## Seitenstruktur

```
┌─────────────────────────────────────────────────────────────────┐
│ 🔍 …                                  Freshworks-Suite   [👤]   │
├──────────┬───────────────────────────┬──────────────────────────┤
│ Home ▾   │ Ticketliste (Filterchips) │ #1024 Rechnung falsch    │
│ Tickets  │ #1024 ●due 2h Beta        │ [↩Reply][Private note]   │
│ Kontakte │ #1025 off   Alpha         │ Status: Open ▾ Prio ▾    │
│ KB       │ …                         │ Produkt ▾ Group ▾ Tags   │
│ Berichte │                           │ ── Konversation ──       │
│ Apps     │                           │ ⏱ Tick · Anhänge        │
└──────────┴───────────────────────────┴──────────────────────────┘
```

- Drei Zonen wie Zendesk; rechte Attributspalte statt eigener App-Sidebar (Apps docken rechts an)

## UI/UX

- Freshworks-Design: freundliches Blau/Weiß, abgerundete Chips
- Live-Aktualisierung der Listen (Polling/WebSocket-Mix)

## Interaktionen

- **Drag & Drop** Anhänge; Reply-Vorlagen als Snippets; Replies per Macro-Buttons
- **Reply-Editor** mit KI-Vorschlägen (Freddy, planabhängig)

## Responsive Design

- Web-ui teilresponsiv; offizielle **Agent-App** (iOS/Android) und **Customer-App** für Portale

## Accessibility

- WCAG 2.1-AA-Bemühungen dokumentiert (Freshworks Trust-Center); Formularlabels vorhanden
- Shortcuts als Mausersatz (siehe [shortcuts.md](shortcuts.md))

## Performance

- Listen virtuell gescrollt; große Instanzen bleiben flüssig

# Zendesk - Struktur und UI/UX

## Seitenstruktur (Agent-Werkbank)

```
┌──────────────────────────────────────────────────────────────────┐
│ 🔍 Suche…                    Zendesk          [App] [Avatar]     │
├───────────┬──────────────────────────────┬───────────────────────┤
│ Views     │ Ticketliste (View)           │ Ticket #9031          │
│ ▸ Meine…  │ #9031 VPN…  open  ●4h SLA   │ Kunde: Beta GmbH      │
│ ▸ Unassigned                            │ [Solve][Pending][Hold]│
│ Tickets   │ #9032 Drucker new           │ [Public reply ▾]      │
│ Users     │ …                           │ [Internal note]       │
│ Orgs      │                             │ ── Conversation ──    │
│ Reporting │                             │ 📎 Anhänge            │
│           │                             ├───────────────────────┤
│           │                             │ Sidebar: Fields, Apps │
└───────────┴──────────────────────────────┴───────────────────────┘
```

- Drei Zonen: Navigation | Liste | Ticket mit Konversation + rechter Sidebar (Custom Fields, Apps, Context)

## UI/UX

- Zendesk-„Garden“-Design: Weiß/Gelbakzente (Markenblau), hoher Kontrast, viel Whitespace
- Live: WebSocket-Updates (Ticketliste/Status ändern sich ohne Reload)

## Interaktionen

- **Drag & Drop**: Anhänge; Macros per Klick; Batch-Aktionen über Checkboxen
- **Macros**: Ein Klick füllt Antwort + Aktionen
- **App-Panel** rechts (Marketplace-Apps rendern eigene UI)

## Responsive Design

- Web-App teilweise responsiv; für Mobil: **Zendesk mobile Agent App** (iOS/Android), Client-portal responsive

## Accessibility

- WCARM-Aufgaben offiziell dokumentiert (Zendesk Accessibility-Statement); Screenreader-Tests für Support vorhanden
- Shortcuts (siehe [shortcuts.md](shortcuts.md)) als Mausalternative für Kernaktionen

## Performance

- clientseitig SPA-artig; große Views cachen serverseitig, > 1k Treffer paginieren

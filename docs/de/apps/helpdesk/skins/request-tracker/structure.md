# Request Tracker - Struktur und UI/UX

## Seitenstruktur

```
┌────────────────────────────────────────────────────────────────┐
│ RT   Create | New Search | Saved | Logs | Tools | Admin        │
├──────────────┬─────────────────────────────────────────────────┤
│ Saved        │ Query-Ergebnis (Tabelle)                        │
│ Searches     │ ID  | Betreff         | Queue | Status | Owner  │
│ ▸ Mine       │ 4711| VPN bricht ab   | netz  | open   | anna   │
│ ▸ Overdue    │ 4712| Drucker         | hw    | new    |        │
│              ├─────────────────────────────────────────────────┤
│              │ Ticket #4711  Status: open  Queue: netz         │
│              │ [Reply][Correspond][Comment] Status▼ Owner▼     │
│              │ History | Attachments | Links                   │
└──────────────┴─────────────────────────────────────────────────┘
```

- Grundmuster: Query → Ergebnistabelle → Update-Page (Reply/Correspond/Comment nebeneinander)
- Sidebar mit persönlichen Saved Searches

## UI/UX

- funktional-dichte 2000er-Ästhetik; Templates anpassbar (`share/html`)
- Keine Themes im modernen Sinn; RT 5 MUI vorsichtig modernisierend

## Interaktionen

- **Kein Drag & Drop / keine Live-Updates**
- Status/Owner als Inline-Links/Selects auf der Update-Page
- Batch-Updates über Ergebnistabelle (Checkboxen)

## Responsive Design

- Web-UI nur eingeschränkt mobil; typischer Mobilweg = Mail-Clients (Ingest/Antwort per E-Mail)

## Accessibility

- html-Tabellen/Formulare, Access-Keys in manchen Sprachversionen; Screenreader wegen vieler kleiner Tabellen anstrengend, aber grundsätzlich bedienbar

## Performance

- Query-Engine auf SQL-Indexstärke angewiesen; Saved Searches cachen nicht — große Instanzen brauchen DB-Tuning

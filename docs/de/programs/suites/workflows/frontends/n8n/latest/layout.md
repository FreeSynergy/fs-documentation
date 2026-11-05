# n8n - Struktur und UI/UX

## Editorstruktur

```
┌───────────────────────────────────────────────────────────────────┐
│ ‹ Workflows  „Sync Tickets→CRM“   [⋮] [Save] [Execute] [○ Active] │
├────────┬────────────────────────────────────────┬─────────────────┤
│ Nodes  │  Canvas                                │ Node-Panel      │
│ Palette│   (Webhook) → (IF) → (HTTP Request)    │ Resource: Zammad│
│ Suche… │      ↘ (Error)                         │ Operation:      │
│        │      → (Create Ticket)                 │  create ticket  │
│        │                                        │ Fields …        │
│ Executions│  Zoom: -, 100%, +                  │ [Execute node]  │
└────────┴────────────────────────────────────────┴─────────────────┘
```

- Nodes als Kacheln mit Status-Icons; rechts Parameter-Form; unten Tab für Testdaten-Ausgabe

## UI/UX

- dunkles Standard-Theme, große Node-Icons mit Produktlogos
- Sticky-Notes/„Wait“-Badges im Canvas; Undo-Rail

## Interaktionen

- **Tab** öffnet Node-Palette (schnellste Art), Drag erzeugt Verbindungen
- Node-Doppelklick → Panel; Rechtsklick-Kontextmenüs (Test/Pin/Disable)
- „Execute Workflow“ zeigt Datenpfad farbig (Item-Pilze durchlaufen Nodes)

## Responsive Design

- Desktop-Werkzeug; Mobil nur Viewing/Konfig-Notlösungen

## Accessibility

- Formularpanels tastaturbedienbar; Canvas primär Maus (Zoom per `Strg+Rad`)

## Performance

- Queue-Modus entkoppet Ausführung vom Editor; große Items >10 MB spalten (Binary-Handling)

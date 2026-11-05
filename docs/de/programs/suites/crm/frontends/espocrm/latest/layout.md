# EspoCRM - Struktur und UI/UX

## Seitenstruktur

```
┌──────────────────────────────────────────────────────────────────┐
│ 🔍 Suche…                    EspoCRM            [🔔][👤][⚙]     │
├──────────┬──────────────────────────────┬────────────────────────┤
│ Menü     │ Liste (Records)              │ Detailseite            │
│ Dashboard│ ⌲ Leads  [Filter][⋮][+Add]   │ Andrea Berg            │
│ Streams  │ ☐ Berg   +49…   open         │ [⋮][Bearbeiten]       │
│ Calls    │ ☐ Klein  …                   │ Links: Felder         │
│ Leads    │                              │ Rechts: Streams-Tabs  │
│ Opp.     │                              │ Calls|Meetings|Tasks  │
│ Accounts │                              │ E-Mails               │
└──────────┴──────────────────────────────┴────────────────────────┘
```

- SPA mit Tab-Blättern (Liste → Detail → related), Listen mit Filterpresets und Massen-⋮

## UI/UX

- ruhige, klare SPA; Standard-Farbschema, dunkles Theme optional
- Pipeline-Kanban mit Drag & Drop für Opportunity-Stages

## Interaktionen

- **Kanban-Drag** für Pipeline, Listen-Checkboxen für Mass Actions
- Record-Header: Follow-Glocke, Drucken, Telefon-Click-to-Dial (Extension)
- Live-Ergebnislisten (Debounce-Suche), kein Voll-WebSocket (Streams pollend)

## Responsive Design

- Listen/Detail responsive bis Mobil (schlanke Masken); Portlet-Dashboards stapeln

## Accessibility

- Tastaturtabellen, Filter mit Labels; Volltext-Suche prominent
- Drag-Alternativen: Stage auch per Feld änderbar

## Performance

- sehr schnell; große Listen (100k+) mit Indexierung + „Select All“-Guard

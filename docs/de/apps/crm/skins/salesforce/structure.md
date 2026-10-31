# Salesforce - Struktur und UI/UX

## Seitenstruktur (Lightning)

```
┌───────────────────────────────────────────────────────────────────┐
│ ☁ App-Launcher ▾  Tabs: Accounts Contacts Leads Opps …  🔍 👤 ⚙  │
├──────────────────────────────────────┬────────────────────────────┤
│ Listenansicht (List View)            │ Record-Detail              │
│ [Filter ▾][⋯][+ New]                 │ Andrea Berg   [⋯][Edit]   │
│ ☐ Beta GmbH   Owner: Anna            │ Pfad: ▸Qualify▸Present    │
│ ☐ Alpha AG    Owner: Ben             │ Detail-Felder (Sections)  │
│                                      │ Related Lists: Activities, │
│                                      │   Contacts, Opportunities  │
│                                      │ Sidebar: Notes/Wissen/Apps │
└──────────────────────────────────────┴────────────────────────────┘
```

- Record-Seiten aus Page Layouts/Lightning Pages gebaut — je Profil/Record-Type unterschiedlich

## UI/UX

- Lightning-Design (SLDS), Themer nach Mandant; Dichte hoch, aber konsistent
- Kanban-Ansichten für Opportunities; Master-Detail-Listen

## Interaktionen

- **Drag & Drop**: Stage auf Kanban, List-Column-Resize, Dateianhänge
- **Quick Actions** (Buttons im Header), Toast-Benachrichtigungen
- Live: Platform-Events für interne Echtzeit-Widgets (kein generelles Live-Refresh)

## Responsive Design

- Lightning-App (mobil) spiegelt Object-Detail-/Listenseiten; voll responsives Web-ui
- Salesforce Mobile App mit Offline-Fähigkeiten (Sales/Service)

## Accessibility

- Salesforce dokumentiert WCAG 2.1-Unterstützung für Lightning; Screenreader-getestete Kernmasken
- Shortcuts siehe [shortcuts.md](shortcuts.md)

## Performance

- Listen paginieren (25/50/100); Reports > 2k Zeilen brauchen Indizes/berichtsarme Filter — API-Seite: Limits beachten

# HubSpot - Struktur und UI/UX

## Seitenstruktur

```
┌───────────────────────────────────────────────────────────────────┐
│ [CRM|Marketing|Sales|Service|⚙]   🔍 Suche            [🔔][👤]    │
├───────────────────────────────────────────────────────────────────┤
│ Kontakte  [Filter ▾][+ Create contact][Import]                    │
│ ☐ Andrea Berg   Firma: Beta   Lifecycle: Customer  🕐 2 d         │
│ ☐ Ben Klein     …                                                │
├───────────────────────────────────────────────────────────────────┤
│ Kontaktseite: Andrea Berg   [Email][Call][Task][+]                │
│ Links: Eigenschaften · Rechts: Chronik | E-Mail | Engagements     │
└───────────────────────────────────────────────────────────────────┘
```

- Einheitliche Kartenmasken; Hub-Umschalter oben wechselt Arbeitswelten

## UI/UX

- freundliches Orange/Weiß-Design, hohe Konsistenz zwischen Hubs
- Listen mit gespeicherten Ansichten; Kanban-Deals mit Drag

## Interaktionen

- **Drag & Drop**: Deal-Karten in Pipeline, Formulare im Page-Editor
- **Eingebettete Panels**: E-Mail-Vorschau, Kalender, Call-Player inline
- teilweise Live-Aktualisierung (Engagement-Historie)

## Responsive Design

- Web-App gut responsiv; **HubSpot Mobile App** (iOS/Android) als voller Client inkl. Offline-Notizen

## Accessibility

- HubSpot publiziert VPAT/WCAG-Berichte; Standardmasken screenreader-tauglich
- Tastatur: `Cmd/Ctrl+K`-Schnellsuche (in vielen Ansichten), sonst Tab-Navigation

## Performance

- Clientseitig SPA-artig; große Portale (> 1 Mio. Kontakte) mit Segment-Performancehinweisen

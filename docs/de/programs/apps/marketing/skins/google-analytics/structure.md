# Google Analytics - Struktur und UI/UX

## Layout

```
┌─────────────────────────────────────────────────────────────────┐
│ GA   Eigenschaft ▾  Startseite ▾           🔍    👤             │
├──────────┬──────────────────────────────────────────────────────┤
│ Berichte │ KPI-Karten: aktive Nutzer | Sessions | Engagement    │
│ Überblick│ Diagramm-Blöcke (7/28 Tage)                          │
│ Lebens…  │ Explore-Tabs: Free table | Funnel | Path             │
│ Explorer │ Segment-Overlays (Vergleichs-Linien)                 │
│ Admin    │ Zielgruppen-Verwaltung (Ads-Aktivierung)             │
└──────────┴──────────────────────────────────────────────────────┘
```

## UI/UX

- Material-Look, geführte KPI-Karten; Explorer ist das „Power-User“-Pendant
- Datenverzug: Echtzeit-Bericht minutengenau, Standardberichte bis 24 h

## Interaktionen

- Datumsbereich/Segment-Buttons oben; Rechtsklick auf Balken → Drilldown
- Metriken per Drag in „Freie Tabelle“

## Responsive Design

- Desktop-zentriert; Mobile-Ansichten lesend (App „Google Analytics“)

## Accessibility

- Standard-Material-Komponenten; Charts mit Zahlen-Zusammenfassungen

## Performance

- riesige Properties: Sampling-Meldung sichtbar; BigQuery-Export für Ausweichanalysen

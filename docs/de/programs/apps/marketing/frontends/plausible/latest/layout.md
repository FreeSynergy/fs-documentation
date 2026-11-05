# Plausible - Struktur und UI/UX

## Dashboard-Eine-Seite

```
┌──────────────────────────────────────────────────────────────┐
│ Domain ▾   Zeitraum ▾  [Vergleich ⊘]              Einstellungen│
├──────────────────────────────────────────────────────────────┤
│ KPI-Zeile:  Besuche | Views/Besuch | Absprungrate | Zeit      │
│ Zeitreihen-Fläche (Tagesbalken)                              │
│ Quellen-Segmentierer: Search | Social | Direct | Email | Ads  │
├──────────────────────────────┬───────────────────────────────┤
│ Top-Seiten (Liste+%)         │ Länder / Geräte / Browser     │
└──────────────────────────────┴───────────────────────────────┘
```

## UI/UX

- radikal reduziert: eine Seite, keine Drilldown-Ebene unterhalb der Listen
- Prozente statt Rohzahlen-Kolonnen; Balken proportional

## Interaktionen

- Klick auf Quellen-Kategorie filtert die ganze Seite
- Zeitraum-Picker mit Vergleichsperiode (Vorzeitraum/Individual)

## Responsive Design

- voll responsiv (auch mobil schnell)

## Accessibility

- schlichte Listen/Balken, kontraststark

## Performance

- Aggregat-Tabellen statt Besuch-Logs → sehr schnelles Laden

# Matomo - Struktur und UI/UX

## Layout

```
┌─────────────────────────────────────────────────────────────────┐
│ Matomo  Website ▾  Zeitraum ▾                    ⚙ 👤           │
├──────────┬──────────────────────────────────────────────────────┘
│ Besuche  │ Besucher-Protokoll: Zeile je Besuch mit Aktionen-     │
│ Verhalten│   Baum (Seiten→Clicks→Search)                        │
│ Akquise  │ Balken-Charts (Tagesaggregate), Sparklines           │
│ Ziele    │ Segment-Leiste (oben, anwendbar auf alle Berichte)   │
└──────────┴──────────────────────────────────────────────────────┘
Widget-Grid auf Dashboard; Drilldown pro Zeile
```

## UI/UX

- funktional-dicht (klassisches Analytics-Tabellen-UI); Dunkel-Modus vorhanden
- Hover zeigt „Actions“-Unterbaum des Besuchs — das Alleinstellungsmerkmal

## Interaktionen

- Klick auf Zeilen → Drilldown-Spalten; Segmente per Klick-Kombinator erstellen
- Report-Download (CSV/JSON/PNG) pro Bericht

## Responsive Design

- Web responsiv; Reports auf Mobil lesend

## Accessibility

- Tabellen/Links-Grundlagen; Charts mit Daten-Pendants

## Performance

- Visits-Tabelle groß → Archiv-Plugin + Cron; Datenbank-Partitionierung bei >100 Mio. Zeilen

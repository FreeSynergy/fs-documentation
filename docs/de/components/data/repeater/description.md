# Repeater (Wiederholer)

| Feld | Wert |
|------|------|
| **Kategorie** | `data` |
| **Erbt von** | `base` |
| **Varianten** | `liste`, `raster`, `eingabe` |
| **Zustände** | `leer`, `gefiltert`, `wartend` |
| **Gesten** | `tap`, `swipe`, `long-press` |
| **Animationen** | `fade-in`, `stagger`, `progress` |
| **Verwandt** | `list-view`, `grid-view`, `table`, `pagination`, `search-field` |
| **Status** | dokumentiert |

## Beschreibung
Ein Repeater ist ein Wiederholtes Layout für Listen.

## Verwendungszweck

- Produkte
- Kontakte
- Artikel
- Listen

## Features

- Filter
- Sort
- Search
- Pagination

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **liste** | ein Eintrag pro Zeile (Standard) |
| **raster** | Einträge als Karten nebeneinander |
| **eingabe** | wiederholte Formularzeilen, z. B. Positionszeilen mit Hinzufügen/Löschen |

## Abgrenzung

- **Nicht verwechseln mit** [list-view](../list-view/): die Listenansicht zeigt Einträge,
  der Repeater ist die ganze Baugruppe aus Suche, Filter, Sortierung, Seiten und Template.
- **Nicht verwechseln mit** [table](../table/): die Tabelle bringt ihre eigene Spaltenstruktur mit,
  der Repeater wiederholt ein frei definiertes Template.
- Die Variante `eingabe` ersetzt keine einzelnen Felder – sie wiederholt eine Feldgruppe.

## Best Practices

- Reihenfolge der Bedienelemente einheitlich: Suche, Filter, Sortierung, Ergebniszahl.
- Gilt ein Filter, muss er sichtbar und mit einem Knopf zurücknehmbar sein (`gefiltert`).
- Entweder Seitenzahlen oder nachladendes Scrollen, beides zusammen verwirrt.
- Leere Daten und leeres Suchergebnis unterschiedlich beschriften.
- Das Template nur einmal definieren; neue Einträge erben es, statt es zu kopieren.

## Siehe auch

- [data – Übersicht](../index.md)
- [List View](../list-view/) — reine Ansicht ohne Steuerung
- [Pagination](../../navigation/pagination/) — Seitennavigation
- [Basiskomponente](../../basics/base/)

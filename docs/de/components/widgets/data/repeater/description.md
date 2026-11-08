# Repeater

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
Ein Repeater ist ein sich wiederholendes Layout für Listen.

## Verwendungszweck

- Produkte
- Kontakte
- Artikel
- Listen

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **liste** | ein Eintrag pro Zeile (Standard) |
| **raster** | Einträge als Karten nebeneinander |
| **eingabe** | wiederholte Formularzeilen, z. B. Positionen mit Hinzufügen/Löschen |

## Features

- Filter
- Sortierung
- Suche
- Paginierung

## Abgrenzung

- **Nicht verwechseln mit** [list-view](../list-view/): die List View zeigt Einträge, der Repeater ist
  das Gesamtpaket aus Suche, Filter, Sortierung, Seiten und Vorlage.
- **Nicht verwechseln mit** [table](../table/): die Tabelle bringt ihre eigene Spaltenstruktur mit,
  der Repeater wiederholt eine frei definierte Vorlage.
- Die Variante `eingabe` ersetzt keine einzelnen Felder – sie wiederholt eine Gruppe von Feldern.

## Best Practices

- Die Reihenfolge der Bedienelemente einheitlich halten: Suche, Filter, Sortierung, Trefferzahl.
- Ist ein Filter aktiv, muss er sichtbar sein und mit einem Knopf entfernbar (`gefiltert`).
- Entweder Seitenzahlen oder Scrollen mit Nachladen; beides zusammen verwirrt.
- Leere Daten und ein leeres Suchergebnis unterschiedlich beschriften.
- Die Vorlage nur einmal definieren; neue Einträge übernehmen sie, statt sie zu kopieren.

## Siehe auch

- [data – Übersicht](../index.md)
- [List View](../list-view/) — reine Ansicht ohne Bedienelemente
- [Pagination](../../navigation/pagination/) — Seitennavigation
- [Basiskomponente](../../../primitives/basics/base.md)

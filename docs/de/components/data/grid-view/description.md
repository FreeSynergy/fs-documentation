# Grid View (Rasteransicht)

| Feld | Wert |
|------|------|
| **Kategorie** | `data` |
| **Erbt von** | `base` |
| **Varianten** | `Fixed Grid`, `Responsive Grid`, `Masonry Grid` |
| **Zustände** | `selected`, `dragging` |
| **Gesten** | `tap`, `drag`, `long-press`, `swipe` |
| **Animationen** | `stagger`, `fade-in`, `reorder` |
| **Verwandt** | `list-view`, `table`, `gallery`, `carousel` |
| **Status** | dokumentiert |

## Beschreibung
Grid View ist eine Karten/Raster-Darstellung von Elementen.

## Verwendungszweck

- Bildergalerien
- Produktkataloge
- Kartenansichten
- Dateiverzeichnisse

## Varianten

| Variant | Beschreibung |
|---------|--------------|
| **Fixed Grid** | Feste Spaltenanzahl |
| **Responsive Grid** | Anpassbare Spalten |
| **Masonry Grid** | Unregelmäßige Karten |

## Features

- Responsive
- Hover-Effect
- Selection
- Drag-and-Drop

## Abgrenzung

- **Nicht verwechseln mit** [list-view](../list-view/): die Liste zeigt pro Eintrag eine Zeile,
  die Rasteransicht eine Karte mit mehreren Feldern.
- **Nicht verwechseln mit** [table](../table/): eine Tabelle vergleicht Werte über Spalten,
  ein Raster stellt Objekte nebeneinander.
- **Nicht verwechseln mit** [gallery](../../media/gallery/): die Galerie ist ein zusammenhängender
  Medienverband mit Vergrößerung, das Raster ist eine generische Objektansicht.
- **Nicht verwechseln mit** [carousel](../../media/carousel/): das Karussell zeigt nacheinander,
  das Raster gleichzeitig.

## Best Practices

- Karten einheitlich hoch halten; zu lange Titel kürzen, nicht umbrechen lassen.
- Die Karte selbst ist die Hauptaktion; weitere Aktionen erst bei Hover oder langes Drücken.
- Auswahl über Kästchen in der Ecke, nicht über den Kartenklick – sonst verrutscht man beim Markieren.
- Ansichtswechsel (Raster ↔ Liste) und Sortierung merken, nicht zurücksetzen.
- Auf schmalen Bildschirmen zwei Spalten für Bilder, eine Spalte für Textkarten.

## Siehe auch

- [data – Übersicht](../index.md)
- [List View](../list-view/) — Zeilen statt Karten
- [Gallery](../../media/gallery/) — Medien mit Vergrößerung
- [Basiskomponente](../../basics/base/)

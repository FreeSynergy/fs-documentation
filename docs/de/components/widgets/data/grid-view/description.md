# Grid View

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
Eine Grid View ist eine Karten- bzw. Rasteransicht von Elementen.

## Verwendungszweck

- Bildergalerien
- Produktkataloge
- Kartenansichten
- Dateiverzeichnisse

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Fixed Grid** | feste Anzahl an Spalten |
| **Responsive Grid** | anpassbare Spalten |
| **Masonry Grid** | unregelmäßige Karten |

## Funktionen

- Responsiv
- Hover-Effekt
- Auswahl
- Drag and Drop

## Abgrenzung

- **Nicht verwechseln mit** [list-view](../list-view/): die Liste zeigt eine Zeile pro Eintrag,
  die Grid View eine Karte mit mehreren Feldern.
- **Nicht verwechseln mit** [table](../table/): eine Tabelle vergleicht Werte über Spalten hinweg,
  ein Raster stellt Objekte nebeneinander.
- **Nicht verwechseln mit** [gallery](../../media/gallery/): die Galerie ist eine zusammenhängende
  Gruppe von Medien mit Vergrößerung, das Raster ist eine allgemeine Objektansicht.
- **Nicht verwechseln mit** [carousel](../../media/carousel/): das Karussell zeigt eines nach dem
  anderen, das Raster alle gleichzeitig.

## Best Practices

- Halte die Karten gleich hoch; kürze zu lange Titel, statt sie umbrechen zu lassen.
- Die Karte selbst ist die Hauptaktion; weitere Aktionen nur bei Hover oder langem Drücken.
- Wähle über eine Checkbox in der Ecke aus, nicht per Klick auf die Karte — sonst rutscht man
  beim Markieren leicht ab.
- Merke dir den Wechsel der Ansicht (Raster ↔ Liste) und die Sortierung, setze sie nicht zurück.
- Auf schmalen Bildschirmen zwei Spalten für Bilder, eine Spalte für Textkarten.

## Siehe auch

- [data – Übersicht](../index.md)
- [List View](../list-view/) — Zeilen statt Karten
- [Gallery](../../media/gallery/) — Medien mit Vergrößerung
- [Basiskomponente](../../../primitives/basics/base.md)

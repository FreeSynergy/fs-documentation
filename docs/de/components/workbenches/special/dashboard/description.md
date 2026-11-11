# Dashboard

| Feld | Wert |
|-------|-------|
| **Kategorie** | `special` |
| **Erbt von** | `base` |
| **Varianten** | `vorlage`, `anordbar`, `bericht` |
| **Zustände** | `bearbeiten`, `leer` |
| **Gesten** | `drag`, `tap`, `long-press` |
| **Animationen** | `reorder`, `cascade`, `stagger` |
| **Verwandt** | `card`, `chart`, `grid-view`, `split-view`, `scroll-area` |
| **Status** | dokumentiert |

## Beschreibung
Ein Dashboard ist eine Übersichtsseite mit Widgets.

## Verwendungszweck
- Überblick
- Auswertung
- Projekt

## Varianten

| Variante | Beschreibung |
|---------|-------------|
| **vorlage** | feste Anordnung, vom Benutzer nicht veränderbar |
| **anordbar** | Widgets verschieben, Größe ändern, eigene Auswahl treffen |
| **bericht** | nur Anzeige ohne Bearbeitungsmodus, für geteilte Ansichten |

## Funktionen

- Widgets
- Drag & Drop
- Größe ändern
- Anpassen

## Abgrenzung

- **Nicht verwechseln mit** [grid-view](../../../widgets/data/grid-view/): das Raster zeigt gleichartige
  Einträge, das Dashboard verschiedene Widgets in unterschiedlichen Größen.
- **Nicht verwechseln mit** [card](../../../widgets/containers/card/): die Karte ist ein einzelner Baustein,
  das Dashboard ist die Anordnung mehrerer Bausteine samt ihren Einstellungen.
- **Nicht verwechseln mit** [chart](../../../widgets/data/chart/): das Zeichnen passiert im Diagramm,
  hier werden Dinge nur platziert.

## Best Practices

- Mit einer sinnvollen Standardansicht beginnen, Konfiguration ist optional.
- Bearbeiten als eigener Modus (`bearbeiten`) – im Lesemodus verschiebt sich nichts.
- Raster mit Spalten und Zeilen; jedes Widget bringt eine minimale und maximale Größe mit.
- Den Ladezustand jedes Widgets einzeln behandeln, nicht die ganze Seite sperren.
- Die Anordnung pro Person speichern und einen Zurücksetzen-Knopf anbieten.

## Siehe auch

- [special – Übersicht](../index.md)
- [Card](../../../widgets/containers/card/) — der Baustein
- [Chart](../../../widgets/data/chart/) — das Diagramm
- [Basiskomponente](../../../primitives/basics/base.md)

# Dashboard

| Feld | Wert |
|------|------|
| **Category** | `special` |
| **Inherits from** | `base` |
| **Variants** | `vorlage`, `anordbar`, `bericht` |
| **States** | `bearbeiten`, `leer` |
| **Gestures** | `drag`, `tap`, `long-press` |
| **Animations** | `reorder`, `cascade`, `stagger` |
| **Related** | `card`, `chart`, `grid-view`, `split-view`, `scroll-area` |
| **Status** | documented |

## Beschreibung
Ein Dashboard ist eine Übersichtsseite mit Widgets.

## Zweck

- Überblick
- Auswertung
- Projekt

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **vorlage** | feste Anordnung, vom Benutzer nicht veränderbar |
| **anordbar** | Widgets verschieben, in der Größe ändern, eigene Auswahl treffen |
| **bericht** | nur Anzeige ohne Bearbeitungsmodus, für geteilte Ansichten |

## Funktionen

- Widgets
- Drag & Drop
- Größe ändern
- Anpassen

## Abgrenzung

- **Nicht verwechseln mit** [grid-view](../../../widgets/data/grid-view/): Das Raster zeigt gleichartige
  Einträge, das Dashboard verschiedene Widgets in unterschiedlichen Größen.
- **Nicht verwechseln mit** [card](../../../widgets/containers/card/): Die Karte ist ein einzelner
  Baustein, das Dashboard ist die Anordnung mehrerer Bausteine einschließlich ihrer Einstellungen.
- **Nicht verwechseln mit** [chart](../../../widgets/data/chart/): Gezeichnet wird im Diagramm,
  hier werden Elemente nur platziert.

## Best Practices

- Mit einer sinnvollen Standardansicht beginnen; die Konfiguration ist optional.
- Bearbeiten als eigener Modus (`bearbeiten`) – im Lesemodus verschiebt sich nichts.
- Raster mit Spalten und Zeilen; jedes Widget bringt eine minimale und maximale Größe mit.
- Den Ladezustand jedes Widgets einzeln behandeln, nicht die ganze Seite sperren.
- Die Anordnung pro Person speichern und einen Zurücksetzen-Schalter anbieten.

## Siehe auch

- [special – Übersicht](../index.md)
- [Card](../../../widgets/containers/card/) — der Baustein
- [Chart](../../../widgets/data/chart/) — das Diagramm
- [Basiskomponente](../../../primitives/basics/base.md)

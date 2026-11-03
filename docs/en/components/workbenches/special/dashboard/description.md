# Dashboard

| Field | Value |
| ------ | ------ |
| **Category** | `special` |
| **Inherits from** | `base` |
| **Variants** | `vorlage`, `anordbar`, `bericht` |
| **States** | `bearbeiten`, `leer` |
| **Gestures** | `drag`, `tap`, `long-press` |
| **Animations** | `reorder`, `cascade`, `stagger` |
| **Related** | `card`, `chart`, `grid-view`, `split-view`, `scroll-area` |
| **State** | documented |

## Description
Ein Dashboard ist eine Übersichtsseite mit Widgets.

## Purpose

- Übersicht
- Analytics
- Project

## Variants

| Variant | Description |
| ---------- | -------------- |
| **vorlage** | feste Anordnung, vom Anwender nicht veränderbar |
| **anordbar** | Widgets verschieben, Größe ändern, eigene Auswahl |
| **bericht** | reine Anzeige ohne Bearbeiten-Modus, für geteilte Ansichten |

## Features

- Widgets
- Drag & Drop
- Resize
- Customize

## Distinction

- **Nicht verwechseln mit** [grid-view](../../../widgets/data/grid-view/): das Raster zeigt gleichartige
  Einträge, das Dashboard unterschiedliche Widgets in unterschiedlichen Größen.
- **Nicht verwechseln mit** [card](../../../widgets/containers/card/): die Karte ist ein Baustein,
  das Dashboard ist die Anordnung mehrerer Bausteine samt Einstellung.
- **Nicht verwechseln mit** [chart](../../../widgets/data/chart/): gezeichnet wird im Diagramm,
  hier wird nur platziert.

## Best Practices

- Mit einer sinnvollen Standardansicht starten, Konfiguration ist optional.
- Bearbeiten als eigenen Modus (`bearbeiten`) — im Lesemodus verrutscht nichts.
- Raster mit Spalten und Zeilen, jedes Widget bringt Mindest- und Maximalgröße mit.
- Jeder Widget-Ladezustand einzeln behandeln, die Seite nicht komplett sperren.
- Anordnung je Person speichern und ein Zurücksetzen anbieten.

## See also

- [special – overview](../index.md)
- [Card](../../../widgets/containers/card/) — der Baustein
- [Chart](../../../widgets/data/chart/) — das Diagramm
- [Base component](../../../primitives/basics/base.md)

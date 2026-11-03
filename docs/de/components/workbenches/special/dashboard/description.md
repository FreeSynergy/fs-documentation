# Dashboard (Dashboard)

| Feld | Wert |
|------|------|
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

- Übersicht
- Analytics
- Project

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **vorlage** | feste Anordnung, vom Anwender nicht veränderbar |
| **anordbar** | Widgets verschieben, Größe ändern, eigene Auswahl |
| **bericht** | reine Anzeige ohne Bearbeiten-Modus, für geteilte Ansichten |

## Features

- Widgets
- Drag & Drop
- Resize
- Customize

## Abgrenzung

- **Nicht verwechseln mit** [grid-view](../../data/grid-view/): das Raster zeigt gleichartige
  Einträge, das Dashboard unterschiedliche Widgets in unterschiedlichen Größen.
- **Nicht verwechseln mit** [card](../../containers/card/): die Karte ist ein Baustein,
  das Dashboard ist die Anordnung mehrerer Bausteine samt Einstellung.
- **Nicht verwechseln mit** [chart](../../data/chart/): gezeichnet wird im Diagramm,
  hier wird nur platziert.

## Best Practices

- Mit einer sinnvollen Standardansicht starten, Konfiguration ist optional.
- Bearbeiten als eigenen Modus (`bearbeiten`) — im Lesemodus verrutscht nichts.
- Raster mit Spalten und Zeilen, jedes Widget bringt Mindest- und Maximalgröße mit.
- Jeder Widget-Ladezustand einzeln behandeln, die Seite nicht komplett sperren.
- Anordnung je Person speichern und ein Zurücksetzen anbieten.

## Siehe auch

- [special – Übersicht](../index.md)
- [Card](../../containers/card/) — der Baustein
- [Chart](../../data/chart/) — das Diagramm
- [Basiskomponente](../../basics/base/)

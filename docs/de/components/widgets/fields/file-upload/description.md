# File Upload

| Feld | Wert |
|------|------|
| **Kategorie** | `fields` |
| **Erbt von** | `base` |
| **Varianten** | `File Picker`, `Drag & Drop`, `Image Preview` |
| **Zustände** | `dragover`, `uploading`, `error` |
| **Gesten** | `tap`, `drag` |
| **Animationen** | `progress`, `fade-in`, `expand` |
| **Verwandt** | `image`, `progress`, `input-group`, `field` |
| **Status** | dokumentiert |

## Beschreibung
Ein File Upload ist ein Element zum Auswählen und Hochladen von Dateien.

## Verwendungszweck

- Hochladen von Dateien
- Bilder
- Dokumente

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **File Picker** | Auswahl einer Datei |
| **Drag & Drop** | Ziehen und Ablegen |
| **Image Preview** | Vorschau |

## Funktionen

- Fortschritt
- Vorschau
- Validierung

## Abgrenzung

- **Nicht verwechseln mit** [image](../../../primitives/media/image/): das Bild zeigt eine vorhandene Datei,
  der Upload bringt Dateien ins System.
- **Nicht verwechseln mit** [progress](../../../primitives/feedback/progress/): der Fortschrittsbalken ist hier
  nur eingebettet; `progress` ist das, was ihn zeichnet.
- Der Upload nimmt Dateien entgegen, er verwaltet sie nicht — die Liste liegt in
  [list-view](../../data/list-view/).

## Best Practices

- Typ und Größe **vor** dem Hochladen prüfen und den Fehler benennen („max. 5 MB“),
  nicht erst nach der Serverantwort.
- Eigener Fortschritt pro Datei mit einer Abbrechen- und einer Entfernen-Schaltfläche.
- Drag & Drop zusätzlich zum Dateidialog anbieten, nie als einzige Möglichkeit.
- Nach dem Hochladen Dateiname, Größe und Vorschau zeigen; bei Mehrfachauswahl klar zählen
  („3 Dateien, 12 MB“).

## Siehe auch

- [fields – Übersicht](../index.md)
- [Image](../../../primitives/media/image/) — Anzeige hochgeladener Bilder
- [Progress](../../../primitives/feedback/progress/) — Fortschrittsbalken
- [Basiskomponente](../../../primitives/basics/base.md)

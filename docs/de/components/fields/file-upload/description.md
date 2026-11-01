# File Upload (Datei-Upload)

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
Ein File Upload ist ein Element für Dateiauswahl und Upload.

## Verwendungszweck

- Dateien hochladen
- Bilder
- Dokumente

## Varianten

| Variant | Beschreibung |
|---------|--------------|
| **File Picker** | Dateiauswahl |
| **Drag & Drop** | Drag&Drop |
| **Image Preview** | Vorschau |

## Features

- Progress
- Preview
- Validation

## Abgrenzung

- **Nicht verwechseln mit** [image](../../media/image/): das Bild zeigt eine vorhandene Datei,
  der Upload bringt Dateien erst ins System.
- **Nicht verwechseln mit** [progress](../../feedback/progress/): der Fortschrittsbalken ist hier
  nur eingebettet; dargestellt wird er von `progress`.
- Der Upload nimmt Dateien entgegen, er verwaltet sie nicht – die Liste liegt in
  [list-view](../../data/list-view/).

## Best Practices

- Typ und Größe **vor** dem Upload prüfen und den Fehler benennen ("max. 5 MB"),
  nicht erst nach der Serverantwort.
- Pro Datei eigener Fortschritt mit Abbruch- und Entfernen-Knopf.
- Drag & Drop zusätzlich zum Datei-Dialog anbieten, nie als einzigen Weg.
- Nach dem Upload Dateiname, Größe und Vorschau anzeigen; Mehrfachauswahl klar zählen
  ("3 Dateien, 12 MB").

## Siehe auch

- [fields – Übersicht](../index.md)
- [Image](../../media/image/) — Anzeige hochgeladener Bilder
- [Progress](../../feedback/progress/) — Fortschrittsbalken
- [Basiskomponente](../../basics/base/)

# Embed – Aussehen

## Grundlayout

```
┌──────────────────────────────────────────────┐
│  Title                          ⛶  ↗         │  Kopfzeile (optional)
├──────────────────────────────────────────────┤
│                                              │
│                                              │  eingebettete Fläche
│                                              │
└──────────────────────────────────────────────┘
```

Die Kopfzeile entfällt mit `showTitle = false`; die Symbole für Vollbild und Öffnen in neuem Fenster
erscheinen nur bei Hover oder Fokus.

## Varianten

| `source` | Aussehen |
|----------|----------|
| **app** | wie ein eigenes Programmfenster, ohne eigene Navigationsleiste |
| **widget** | kompakte Fläche, begrenzte Füllhöhe, dezenterer Rahmen |
| **iframe** | fremde Seite ohne Rahmen, Kopfzeile nur mit `showTitle = true` |

## Größen

| Größe | Bedeutung |
|-------|-----------|
| `small` | Zeilenhöhe 280 px, z. B. in Listen |
| `medium` | 480 px Höhe, Standard auf Seiten |
| `large` | füllt die verfügbare Höhe, für Dashboards |

Zusätzlich legt `ratio` das Seitenverhältnis fest (`auto`, `16:9`, `4:3`, `1:1`).

## Farben und Zustände

| Zustand | Aussehen |
|---------|----------|
| `default` | Fläche mit einer Grundfarbe, feiner 1-px-Rahmen |
| `hover` | die Symbole der Kopfzeile werden sichtbar |
| `focus` | 2 px breiter Fokusring um die ganze Fläche |
| `loading` | Platzhalter in der Fläche, die Kopfzeile bleibt bedienbar |
| `error` | Fehlerhinweis in der Fläche, Ursache und ein Link nach außen |
| `disabled` | Fläche abgedunkelt, Bedienung gesperrt |

## Effekte bei Hover und Fokus

| Effekt | Beschreibung |
|--------|--------------|
| `reveal` | Werkzeuge der Kopfzeile erscheinen nur bei Hover oder Fokus |
| `ring` | der Fokusring markiert das gesamte Einbettungselement |

## Responsiv

- In einem schmalen Fenster wird die Fläche volle Breite, die Kopfzeile bleibt in einer Zeile.
- Mit `responsive = false` behält die Fläche ihre feste Höhe und bekommt eine Scrollleiste.

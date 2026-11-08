# Embed – Erscheinungsbild

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

Die Kopfzeile wird mit `showTitle = false` ausgeblendet; die Symbole für Vollbild und Öffnen in neuem Fenster
erscheinen nur bei Hover oder Fokus.

## Varianten

| `source` | Erscheinungsbild |
|----------|------------|
| **app** | wie ein eigenes Programmfenster, ohne eigene Navigationsleiste |
| **widget** | kompakte Fläche, begrenzte Füllhöhe, seltener Rahmen |
| **iframe** | fremde Seite ohne Rahmen, Kopfzeile nur mit `showTitle = true` |

## Größen

| Größe | Bedeutung |
|------|---------|
| `small` | Zeilenhöhe 280 px, z. B. in Listen |
| `medium` | 480 px Höhe, Standard auf Seiten |
| `large` | füllt die verfügbare Höhe, für Dashboards |

Zusätzlich legt `ratio` das Seitenverhältnis fest (`auto`, `16:9`, `4:3`, `1:1`).

## Farben und Zustände

| Zustand | Erscheinungsbild |
|-------|------------|
| `default` | Fläche mit Grundfarbe, dezenter 1-px-Rahmen |
| `hover` | die Symbole in der Kopfzeile werden sichtbar |
| `focus` | 2 px breiter Fokusrahmen um die ganze Fläche |
| `loading` | Platzhalter in der Fläche, die Kopfzeile bleibt bedienbar |
| `error` | Fehlerhinweis in der Fläche, Ursache und ein Link nach außen |
| `disabled` | Fläche abgedunkelt, Bedienung gesperrt |

## Hover- und Fokuseffekte

| Effekt | Beschreibung |
|--------|-------------|
| `reveal` | Werkzeuge der Kopfzeile erscheinen nur bei Hover oder Fokus |
| `ring` | der Fokusrahmen markiert die gesamte Einbettung |

## Responsiv

- In einem schmalen Fenster geht die Fläche auf volle Breite, die Kopfzeile bleibt in einer Zeile.
- Mit `responsive = false` behält die Fläche ihre feste Höhe und bekommt eine Scrollleiste.

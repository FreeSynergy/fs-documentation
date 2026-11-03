# Embed (Einbettung) - Aussehen

## Grundlayout

```
┌──────────────────────────────────────────────┐
│  Titel                          ⛶  ↗         │  Kopfzeile (optional)
├──────────────────────────────────────────────┤
│                                              │
│                                              │  eingebettete Fläche
│                                              │
└──────────────────────────────────────────────┘
```

Die Kopfzeile entfällt bei `showTitle = false`; das Vollbild- und das Öffnen-Symbol
erscheinen erst bei Hover oder Fokus.

## Varianten

| `source` | Aussehen |
|----------|----------|
| **app** | wie ein eigenes Programmfenster, ohne eigene Navigationsleiste |
| **widget** | kompakte Fläche, füllhöhenbegrenzt, seltener Rahmen |
| **iframe** | fremde Seite randlos, Kopfzeile nur bei `showTitle = true` |

## Größen

| Größe | Bedeutung |
|-------|-----------|
| `small` | Zeilenhöhe 280 px, z. B. in Listen |
| `medium` | 480 px Höhe, Standard in Seiten |
| `large` | füllt die verfügbare Höhe, für Dashboards |

Zusätzlich bestimmt `ratio` das Seitenverhältnis (`auto`, `16:9`, `4:3`, `1:1`).

## Farben und Zustände

| Zustand | Aussehen |
|---------|----------|
| `default` | Fläche mit Grundfarbe, dezenter 1 px Rahmen |
| `hover` | Kopfzeilen-Symbole werden sichtbar |
| `focus` | 2 px Fokus-Ring um die Gesamtfläche |
| `loading` | Skeleton in der Fläche, Kopfzeile bleibt bedienbar |
| `error` | Fehlerhinweis in der Fläche, Ursache und Verweis nach außen |
| `disabled` | Fläche abgeblendet, Bedienung gesperrt |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `reveal` | Kopfzeilen-Werkzeuge erscheinen erst bei Hover oder Fokus |
| `ring` | Fokus-Ring markiert die gesamte Einbettung |

## Reaktiv

- Bei schmalem Fenster wird die Fläche vollbreit, die Kopfzeile bleibt einzeilig.
- Bei `responsive = false` behält die Fläche ihre feste Höhe und bekommt Seitenlauf.

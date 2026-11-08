# Link – Erscheinungsbild

## Grundlayout

```
standard:      unterstrichen:   external:
Privacy        a wiki link      OpenProject ↗
```

## Varianten

| Variante | Erscheinungsbild |
|---------|------------|
| **standard** | Primärfarbe, nur bei Hover unterstrichen |
| **muted** | Sekundärtext, gleicher Hover wie standard |
| **icon** | Icon links oder rechts mit 4 px Abstand |
| **unterstrichen** | durchgehende Linie, auch im Ruhezustand |

## Größen

Die Schriftgröße richtet sich nach dem umgebenden Text; `size` passt nur das Icon an:

| Größe | Icon |
|------|------|
| `small` | 12 px |
| `medium` | 14 px |
| `large` | 18 px |

## Farben und Zustände

| Zustand | Farbe |
|-------|--------|
| `default` | Primärfarbe |
| `hover` | Primärfarbe abgedunkelt plus Unterstrich |
| `active` | beim Drücken stark abgedunkelt |
| `focus` | 2 px Fokusrahmen |
| `visited` (extern) | behält die Primärfarbe |

## Hover- und Fokuseffekte

| Effekt | Beschreibung |
|--------|-------------|
| `underline` | die Linie erscheint bei Hover (standard) |
| `ring` | Fokusrahmen für die Tastaturnavigation |

## Responsiv

- Link-Ziele bleiben mindestens so hoch wie die Zeilenhöhe als Trefferfläche
  (Touch: 44 px, siehe Basiskomponente).

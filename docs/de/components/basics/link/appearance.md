# Link (Verweis) - Aussehen

## Grundlayout

```
standard:      unterstrichen:     external:
Datenschutz    ein Wiki-Link      OpenProject ↗
```

## Varianten

| Variante | Aussehen |
|----------|----------|
| **standard** | Primärfarbe, Unterstreichung erst bei Hover |
| **muted** | Sekundärtext, gleiche Hover wie standard |
| **icon** | Icon links oder rechts mit 4 px Abstand |
| **unterstrichen** | durchgehende Linie, auch im Ruhezustand |

## Größen

Die Schriftgröße folgt dem umgebenden Text; `size` passt nur das Icon an:

| Größe | Icon |
|-------|------|
| `small` | 12 px |
| `medium` | 14 px |
| `large` | 18 px |

## Farben und Zustände

| Zustand | Farbe |
|---------|-------|
| `default` | Primärfarbe |
| `hover` | Primärfarbe abgedunkelt plus Unterstreichung |
| `active` | beim Drücken stark abgedunkelt |
| `focus` | 2 px Fokus-Ring |
| `visited` (extern) | behält Primärfarbe bei |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `underline` | Linie erscheint bei Hover (standard) |
| `ring` | Fokus-Ring bei Tastaturnavigation |

## Reaktiv

- Linkziele bleiben als Trefferfläche mindestens Zeilenhöhe hoch
  (Touch: 44 px, siehe Basiskomponente).

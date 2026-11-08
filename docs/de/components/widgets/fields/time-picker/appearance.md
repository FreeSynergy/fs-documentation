# Time Picker - Erscheinungsbild

## Grundlayout

```
┌───────────────────┐
│  ⌂  09:00         │
├───────────────────┤
│  08:30            │
│  08:45            │
│ ▶ 09:00           │  aktuelle Auswahl
│  09:15            │
│  …                │
└───────────────────┘
```

## Varianten

| Variante | Erscheinungsbild |
|----------|------------------|
| **liste** | Liste mit 7 sichtbaren Zeilen, dezente Scrollleiste |
| **ziffernblatt** | Kreis mit Stundenzeiger, innerer Kreis für die Minuten |

## Größen

| Größe | Zeilenhöhe | Breite |
|-------|------------|--------|
| `small` | 28 px | 140 px |
| `medium` | 36 px | 180 px |
| `large` | 44 px | 240 px |

## Farben und Zustände

| Zustand | Erscheinungsbild |
|---------|------------------|
| `default` | Uhrzeiten neutral |
| `hover` | Zeile leicht getönt |
| `active` | gewählte Zeile in der Primärfarbe |
| `open` | Overlay mit Schatten, gewählte Zeile in der Mitte |

## Effekte bei Hover und Fokus

| Effekt | Beschreibung |
|--------|--------------|
| `ring` | Fokusrahmen auf der aktiven Zeile |
| `fade-in` | das Overlay blendet ein |

## Responsiv

- Auf mobilen Geräten erscheint die Liste als am unteren Rand verankerte Fläche.
- `ziffernblatt` wird unter 400 px Breite durch die Liste ersetzt.

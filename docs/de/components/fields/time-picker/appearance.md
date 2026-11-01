# Time Picker (Zeitauswahl) - Aussehen

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

| Variante | Aussehen |
|----------|----------|
| **liste** | Liste mit 7 sichtbaren Zeilen, Scrollbalken dezent |
| **ziffernblatt** | Kreis mit Stundenpunkt, innerer Kreis für Minuten |

## Größen

| Größe | Zeilenhöhe | Breite |
|-------|------------|--------|
| `small` | 28 px | 140 px |
| `medium` | 36 px | 180 px |
| `large` | 44 px | 240 px |

## Farben und Zustände

| Zustand | Aussehen |
|---------|----------|
| `default` | Zeiten neutral |
| `hover` | Zeile leicht hinterlegt |
| `active` | gewählte Zeile in Primärfarbe |
| `open` | Overlay mit Schatten, gewählte Zeile mittig |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `ring` | Fokusrahmen auf der aktiven Zeile |
| `fade-in` | Overlay blendet ein |

## Reaktiv

- Auf Mobilgeräten erscheint die Liste als bodenbündige Fläche.
- `ziffernblatt` wird unter 400 px Breite durch die Liste ersetzt.

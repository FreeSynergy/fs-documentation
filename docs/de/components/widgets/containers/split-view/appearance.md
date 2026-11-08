# Split View - Erscheinungsbild

## Grundlayout
Eine Split View ist ein Layout mit zwei nebeneinanderliegenden Bereichen.

```
┌─────────────────┬──────────────────────┐
│                 │                      │
│   Bereich 1     │     Bereich 2        │
│   (Sidebar)     │     (Hauptinhalt)    │
│                 │                      │
└─────────────────┴──────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Fixed Split** | feste Breite |
| **Resizable Split** | Breite lässt sich per Ziehen ändern |
| **Responsive** | passt sich automatisch an |

## Größen

| Bereich | Breite | Verwendung |
|---------|--------|------------|
| **Sidebar** | 250px | Standard |
| **Content** | auto | restlicher Platz |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Sidebar** | hell | Hintergrund der Sidebar |
| **Content** | hell | Hintergrund des Inhalts |
| **Separator** | grau | Trennlinie |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `resize-cursor` | Cursor zum Verändern der Größe |
| `border` | der Rand leuchtet auf |

## Responsiv

| Breakpoint | Verhalten |
|------------|-----------|
| Desktop (>768px) | nebeneinander |
| Tablet (480–768px) | untereinander gestapelt |
| Mobil (<480px) | Akkordeon |

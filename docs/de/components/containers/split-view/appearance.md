# Split View - Aussehen

## Grundlayout

Ein Split View ist ein Layout mit zwei Bereichen side-by-side.

## Layout

```
┌─────────────────┬──────────────────────┐
│                 │                      │
│   Bereich 1     │     Bereich 2        │
│   (Sidebar)     │     (Hauptinhalt)    │
│                 │                      │
└─────────────────┴──────────────────────┘
```

## Varianten

| Variant | Beschreibung |
|---------|--------------|
| **Fixed Split** | Fixe Breite |
| **Resizable Split** | Breite per Drag änderbar |
| **Responsive** | Auto-Adjustierung |

## Größe-Varianten

| Bereich | Breite | Verwendung |
|---------|--------|------------|
| **Sidebar** | 250px | Standard |
| **Content** | Auto | Verbleibender Platz |

## Farb-Varianten

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Sidebar** | Hell | Sidebar-Hintergrund |
| **Content** | Hell | Content-Hintergrund |
| **Separator** | Grau | Trennlinie |

## Hover-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `resize-cursor` | Resize-Cursor |
| `border` | Rand leuchtet auf |

## Responsive Verhalten

| Breakpoint | Verhalten |
|------------|-----------|
| Desktop (>768px) | Side-by-Side |
| Tablet (480-768px) | Vertical Stack |
| Mobile (<480px) | Accordion |

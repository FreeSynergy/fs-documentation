# Split View - Aussehen

## Grundlayout
Ein Split View ist ein Layout mit zwei Bereichen side-by-side.

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

## Größen

| Bereich | Breite | Verwendung |
|---------|--------|------------|
| **Sidebar** | 250px | Standard |
| **Content** | Auto | Verbleibender Platz |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Sidebar** | Hell | Sidebar-Hintergrund |
| **Content** | Hell | Content-Hintergrund |
| **Separator** | Grau | Trennlinie |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `resize-cursor` | Resize-Cursor |
| `border` | Rand leuchtet auf |

## Reaktiv

| Breakpoint | Verhalten |
|------------|-----------|
| Desktop (>768px) | Side-by-Side |
| Tablet (480-768px) | Vertical Stack |
| Mobile (<480px) | Accordion |

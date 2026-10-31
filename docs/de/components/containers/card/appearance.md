# Card - Aussehen

## Grundlayout

Eine Card ist ein Container-Element, das Inhalte in einer strukturierten Box mit Titel, Inhalt und optionalen Aktionen darstellt.

## Layout

```
┌─────────────────────────────┐
│ 🏠 Titel der Karte          │
├─────────────────────────────┤
│                             │
│   Hier ist der Inhalt       │
│   der Card.                 │
│   Mehrzeiliger Text.        │
│                             │
├─────────────────────────────┤
│  [Btn 1]  [Btn 2]  ⋯       │
└─────────────────────────────┘
```

## Größe-Varianten

| Größe | Breite | Verwendung |
|-------|--------|------------|
| Small | 200px | In List-Items |
| Medium | 300px | Standard |
| Large | 400px | Featured |
| Full | 100% | Volle Breite |

## Farb-Varianten

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Default** | Hell | Standard |
| **Primary** | Primärfarbe | Primär |
| **Secondary** | Sekundärfarbe | Sekundär |
| **Danger** | Rot | Gefährlich |

## Varianten

| Variant | Beschreibung |
|---------|--------------|
| **Default** | Standard mit Header |
| **Flat** | Ohne Schatten |
| **Outlined** | Nur Randlinie |
| **Elevated** | Stark erhöht mit Schatten |
| **Media** | Mit Bild/Thumbnail |

## Hover-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `shadow` | Schatten stärker |
| `transform` | Leichte Hebung |
| `border` | Rand leuchtet auf |

## Interaktivität

```css
.card:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
  transform: translateY(-2px);
}
```

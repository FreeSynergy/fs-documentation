# Card - Erscheinungsbild

## Grundlayout
Eine Card ist ein Container-Element. Es zeigt Inhalte in einem strukturierten Kasten
mit Titel, Inhalt und optionalen Aktionen.

```
┌─────────────────────────────┐
│ 🏠 Titel der Card           │
├─────────────────────────────┤
│                             │
│   Hier steht der Inhalt     │
│   der Card.                 │
│   Mehrzeiliger Text.        │
│                             │
├─────────────────────────────┤
│  [Btn 1]  [Btn 2]  ⋯        │
└─────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **default** | Standard mit Kopfzeile |
| **flat** | ohne Schatten |
| **outlined** | nur ein Umriss |
| **elevated** | stark angehoben mit Schatten |
| **media** | mit Bild oder Vorschaubild |

## Größen

| Größe | Breite | Verwendung |
|-------|--------|------------|
| small | 200px | in Listenelementen |
| medium | 300px | Standard |
| large | 400px | hervorgehoben |
| full | 100% | volle Breite |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **default** | hell | Standard |
| **primary** | Primärfarbe | primär |
| **secondary** | Sekundärfarbe | sekundär |
| **danger** | rot | gefährlich |

## Hover- und Fokuseffekte

| Effekt | Beschreibung |
|--------|--------------|
| `shadow` | der Schatten wird stärker |
| `transform` | leichtes Anheben |
| `border` | der Rahmen leuchtet auf |

## Responsiv

```css
.card:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
  transform: translateY(-2px);
}
```

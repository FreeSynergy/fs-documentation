# Radio Group - Aussehen

## Grundlayout
Eine Radio Group ist eine Gruppe von Optionsfeldern (einzelfach).

```
┌─────────────────────────────────────────┐
│ Option 1  (•)                           │
│ Option 2  ( )                           │
│ Option 3  ( )                           │
└─────────────────────────────────────────┘
```

## Varianten

| Variante | Aussehen |
|----------|----------|
| **einzeln** | Kreis mit Punkt, Label rechts daneben |
| **toggle** | Knopfreihe, aktive Option flächig gefüllt |
| **karte** | Karte mit Radius, aktiver Rand in Primärfarbe |

## Größen

| Größe | Breite | Verwendung |
|-------|--------|------------|
| Small | 20px | Inline |
| Medium | 24px | Standard |
| Large | 28px | Featured |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Selected** | Primärfarbe | Ausgewählt |
| **Unselected** | Grau | Nicht ausgewählt |
| **Disabled** | Grau | Deaktiviert |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `scale` | Vergrößerung |
| `shadow` | Schatten stärker |
| `border` | Rand leuchtet auf |

## With Icons

```
┌─────────────────────────────────────────┐
│ (•) Option 1   [Icon]                   │
│ ( ) Option 2   [Icon]                   │
│ ( ) Option 3   [Icon]                   │
└─────────────────────────────────────────┘
```

## Reaktiv

- Unter `small` Bildschirmbreite werden die Optionen einspaltig und Zeile für Zeile
  mindestens 44 px hoch.
- Die segmentierte Variante wechselt bei schmalem Raum untereinander; die Trennlinien
  bleiben erhalten, damit die Gruppe als zusammengehörig erkennbar bleibt.
- Kartenvarianten stapeln einspaltig, Icon und Beschreibung bleiben linksbündig.

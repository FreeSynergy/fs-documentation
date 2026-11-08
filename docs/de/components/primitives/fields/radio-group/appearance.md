# Radio Group - Erscheinungsbild

## Grundlayout
Eine Radio Group ist eine Gruppe von Optionsfeldern (Einfachauswahl).

```
┌─────────────────────────────────────────┐
│ Option 1  (•)                           │
│ Option 2  ( )                           │
│ Option 3  ( )                           │
└─────────────────────────────────────────┘
```

## Varianten

| Variante | Erscheinungsbild |
|----------|------------------|
| **einzeln** | Kreis mit Punkt, Beschriftung rechts davon |
| **toggle** | Reihe von Buttons, die aktive Option als Fläche gefüllt |
| **karte** | Card mit Radius, aktiver Rahmen in der Primärfarbe |

## Größen

| Größe | Breite | Verwendung |
|-------|--------|------------|
| small | 20px | inline |
| medium | 24px | Standard |
| large | 28px | hervorgehoben |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **selected** | Primärfarbe | ausgewählt |
| **unselected** | grau | nicht ausgewählt |
| **disabled** | grau | deaktiviert |

## Hover- und Fokuseffekte

| Effekt | Beschreibung |
|--------|--------------|
| `scale` | Vergrößerung |
| `shadow` | der Schatten wird stärker |
| `border` | der Rahmen leuchtet auf |

## Responsiv

- Unterhalb der Breite `small` stehen die Optionen in einer Spalte. Jede Zeile ist
  mindestens 44 px hoch.
- Die segmentierte Variante stapelt sich auf schmalem Raum untereinander. Die Trennlinien
  bleiben erhalten, damit die Gruppe als zusammengehörig erkennbar bleibt.
- Kartenvarianten stapeln sich in einer Spalte. Icon und Beschreibung bleiben linksbündig.

## Mit Icons

```
┌─────────────────────────────────────────┐
│ (•) Option 1   [Icon]                   │
│ ( ) Option 2   [Icon]                   │
│ ( ) Option 3   [Icon]                   │
└─────────────────────────────────────────┘
```

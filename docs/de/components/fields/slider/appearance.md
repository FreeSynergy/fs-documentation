# Slider - Aussehen

## Grundlayout
Ein Slider ist ein Wertebereich mit Schieberegler.

```
┌─────────────────────────────────────────┐
│ Lautstärke                              │
├─────────────────────────────────────────┤
│ 0% [●━━━━━━━━━━━━━━━━━━━━━━━━━━━━━] 100%│
└─────────────────────────────────────────┘
```

## Varianten

| Variante | Aussehen |
|----------|----------|
| **einfach** | ein Knopf, links gefüllter Bereich |
| **bereich** | zwei Knöpfe, der Abschnitt dazwischen ist gefüllt |

Senkrechte Regler sind keine eigene Variante, sondern `orientation = vertikal`.

## Größen

| Größe | Breite | Verwendung |
|-------|--------|------------|
| Small | 200px | Inline |
| Medium | 300px | Standard |
| Large | 400px | Featured |
| Full | 100% | Volle Breite |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Track** | Grau | Track-Farbe |
| **Filled** | Primärfarbe | Filled-Farbe |
| **Thumb** | Primärfarbe | Thumb-Farbe |
| **Disabled** | Grau | Deaktiviert |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `scale` | Vergrößerung |
| `shadow` | Schatten stärker |

## With Labels

```
┌─────────────────────────────────────────┐
│ 10                     [●━━━━━━━━━━]    │
│     50                  100             │
└─────────────────────────────────────────┘
```

## Vertical Slider

```
┌─────────────────────────────────────────┐
│ 100                                     │
│   ●                                     │
│  75                                     │
│  50                                     │
│  25                                     │
│   0                                     │
└─────────────────────────────────────────┘
```

## Reaktiv

- Der Track füllt die verfügbare Breite (`Full` in Werkzeugleisten), die Knöpfe bleiben
  16 px (Desktop) bzw. 24 px (Touch) groß; die Trefferfläche um den Knopf bleibt 44 px.
- Auf schmalen Bildschirmen rutschen Wert und Skalenenden über bzw. unter den Track,
  nicht daneben.
- Ein Tipp auf den Track springt zum getroffenen Punkt, der Knopf folgt `elastic`.

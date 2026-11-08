# Tick Draw - Erscheinungsbild

## Grundaufbau

Das Häkchen sitzt auf einer vorbereiteten Fläche (einem Kreis oder einem Kasten) und wird als
ein zusammenhängender Strich aufgebaut: zuerst der kurze Schenkel nach unten, dann der lange nach
oben rechts. Die Strichstärke bleibt beim Zeichnen gleich.

## Visueller Ablauf

```
┌──────────────────────────────────────────────────────┐
│  0 ms        150 ms        320 ms        550 ms      │
│                                                      │
│   ( )         ( )          ( /          ( ✓ )        │
│  leer      Kreis sichtbar  Schenkel     fertig       │
│             α = 1          wird gezeichnet           │
│                                                      │
│  Kreis: 200 ms  ·  Strich: 400 ms, von links nach    │
│  oben rechts, ohne den Stift abzusetzen              │
└──────────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|---------|-------------|
| **Standard** | der Kreis erscheint, dann das Häkchen in 400 ms |
| **Nur Strich** | `hintergrund: none` – das Häkchen zeichnet direkt auf die Fläche |
| **Kasten** | `hintergrund: flaeche` – passt zu Kontrollkästchen |
| **Betont** | `nachziehen: 1.5` – der Strich schießt am Ende minimal über das Ziel hinaus |

## Dauer

- Typisch: 300–500 ms für den Strich, plus 150–250 ms Anlauf
- Standardwert: 400 ms

## Siehe auch

- [Übersicht Animationen](../../index.md)
- [Ripple](../ripple/description.md)
- [Highlight](../highlight/description.md)
- [Checkbox](../../../../components/primitives/fields/checkbox/description.md)

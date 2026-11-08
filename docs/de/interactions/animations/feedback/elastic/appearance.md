# Elastic - Erscheinungsbild

## Grundaufbau

Ein sichtbares Element bewegt sich auf eine feste Endposition zu, schießt über sie hinaus und
pendelt sich dann ein (`|` = Zielposition).

## Visueller Ablauf

```
┌──────────────────────────────────────────────────────┐
│Ruhe          Überschwingen   zurück         Endstand  │
│                                                      │
│[■]·····|      ·····|·[■]     ···[■]··|      ····[■]| │
│                                                      │
│über das Ziel hinaus, dann sanft einpendelnd          │
└──────────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|---------|-------------|
| **Sanft** | `overshoot: 10`, eine Schwingung |
| **Stark** | `overshoot: 40`, drei Schwingungen (Spielgefühl) |
| **Skala** | federt in der Größe statt in der Position |
| **Gedämpft** | `abklingfaktor: 0.2`, pendelt sich schnell ein |
| **Achse** | nur `x`, nur `y` oder diagonal |

## Dauer

- Typisch: 400–800 ms

## Siehe auch

- [Übersicht Animationen](../../index.md)
- [Rubber Band](../rubber-band/description.md)
- [Cross Fade](../../transition/cross-fade/description.md)

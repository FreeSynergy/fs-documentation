# Elastic - Aussehen

## Grundlayout

Ein sichtbares Element wandert in eine feste Endposition, schießt über sie hinaus und pendelt dann ein (`|` = Zielposition).

## Visueller Verlauf

```
┌──────────────────────────────────────────────────────┐
│Ruhe          Überschuss      Zurück          Endlage │
│                                                      │
│[■]·····|      ·····|·[■]     ···[■]··|      ····[■]| │
│                                                      │
│über das Ziel hinaus, dann sanft einschwingen         │
└──────────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Sanft** | `overshoot: 10`, eine Schwingung |
| **Stark** | `overshoot: 40`, drei Schwingungen (Spiellok) |
| **Skala** | federt in der Größe statt in der Position |
| **Gedämpft** | `abklingfaktor: 0.2`, schnelles Einschießen |
| **Achse** | nur `x`, nur `y` oder diagonal |

## Dauer

- Typisch: 400–800 ms

## Siehe auch

- [Animationen Übersicht](../index.md)
- [Rubber Band](../rubber-band/description.md)
- [Cross Fade](../cross-fade/description.md)

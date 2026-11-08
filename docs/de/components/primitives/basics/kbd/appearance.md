# Kbd – Erscheinungsbild

## Grundlayout

```
einzeln:        kombination:

┌─────┐         ┌──────┐   ┌───┐
│ Esc │         │ Ctrl │ + │ S │
└─────┘         └──────┘   └───┘
```

## Varianten

| Variante | Erscheinungsbild |
|---------|------------|
| **einzeln** | kleine Tastenkappe: 1 px Rahmen, 4 px Rundung, dezenter Schatten unten |
| **kombination** | Tastenkappen mit einem „+“ in der Sekundärfarbe dazwischen |

## Größen

| Größe | Höhe | Schrift |
|------|------|--------|
| `small` | 18 px | 11 px |
| `medium` | 22 px | 12 px |
| `large` | 26 px | 14 px |

## Farben und Zustände

| Zustand | Erscheinungsbild |
|-------|------------|
| `default` | helle Fläche, Primärtext, Rahmen in der Trennlinienfarbe |
| `active` | Fläche in der Primärfarbe, Text invertiert, Schatten reduziert |

## Hover- und Fokuseffekte

| Effekt | Beschreibung |
|--------|-------------|
| – | keine; Kbd dient nur der Anzeige |

## Responsiv

- Kbd bricht zusammen mit dem Text um; Kombinationen werden nicht auseinandergerissen
  (`white-space: nowrap` pro Tastenkappe).

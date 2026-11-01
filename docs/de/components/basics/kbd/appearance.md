# Kbd (Tastenkennung) - Aussehen

## Grundlayout

```
einzeln:        kombination:

┌─────┐         ┌──────┐   ┌───┐
│ Esc │         │ Strg │ + │ S │
└─────┘         └──────┘   └───┘
```

## Varianten

| Variante | Aussehen |
|----------|----------|
| **einzeln** | kleine Kappe: 1 px Rand, 4 px Rundung, dezenter Schatten unten |
| **kombination** | Kappen mit „+“ in Sekundärfarbe dazwischen |

## Größen

| Größe | Höhe | Schrift |
|-------|------|---------|
| `small` | 18 px | 11 px |
| `medium` | 22 px | 12 px |
| `large` | 26 px | 14 px |

## Farben und Zustände

| Zustand | Aussehen |
|---------|----------|
| `default` | helle Fläche, Primärtext, Rand in Trennfarbe |
| `active` | Fläche in Primärfarbe, Text invertiert, Schatten reduziert |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| – | keine; Kbd ist reine Anzeige |

## Reaktiv

- Kbd bricht mit dem Text um; Kombinationen werden nicht zerrissen
  (`white-space: nowrap` je Kappe).

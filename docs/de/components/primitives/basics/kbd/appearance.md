# Kbd – Aussehen

## Grundlayout

```
einzeln:        kombination:

┌─────┐         ┌──────┐   ┌───┐
│ Esc │         │ Ctrl │ + │ S │
└─────┘         └──────┘   └───┘
```

## Varianten

| Variante | Aussehen |
|----------|----------|
| **einzeln** | kleine Tastenkappe: 1 px Rahmen, 4 px Rundung, leichter Schatten darunter |
| **kombination** | Tastenkappen mit einem "+" in der Sekundärfarbe dazwischen |

## Größen

| Größe | Höhe | Schrift |
|-------|------|---------|
| `small` | 18 px | 11 px |
| `medium` | 22 px | 12 px |
| `large` | 26 px | 14 px |

## Farben und Zustände

| Zustand | Aussehen |
|---------|----------|
| `default` | helle Fläche, Primärtext, Rahmen in der Trennlinienfarbe |
| `active` | Fläche in der Primärfarbe, Text invertiert, Schatten reduziert |

## Effekte bei Hover und Fokus

| Effekt | Beschreibung |
|--------|--------------|
| – | keine; Kbd dient nur der Anzeige |

## Responsiv

- Kbd bricht mit dem Text um; Kombinationen werden nicht auseinandergerissen
  (`white-space: nowrap` pro Tastenkappe).

# Dashboard - Appearance

## Base layout
A dashboard is an overview page with widgets.

```
┌─────────────────────────────────────────┐
│ [Widget 1] [Widget 2] [Widget 3]        │
│                                         │
│ [Widget 4] [Widget 5] [Widget 6]        │
│                                         │
│ [Widget 7] [Widget 8] [Widget 9]        │
└─────────────────────────────────────────┘
```

## Variants

| Variant | Appearance |
| ---------- | ---------- |
| **vorlage** | Widgets ohne Greifpunkte, Raster unveränderlich |
| **anordbar** | Greifpunkt oben links, Rahmen zum Ziehen, Rasterlinien im Bearbeiten-Modus |
| **bericht** | wie `vorlage`, ohne Bearbeiten-Knopf, dafür Drucken/Aktualisieren |

## Sizes

| Size | Width | Use |
| ------- | -------- | ------------ |
| Small | 800px | Kleines Dashboard |
| Medium | 1200px | Standard |
| Large | 1600px | Großes Dashboard |

## Colours and states

| State | Colour | Description |
| -------- | ------- | -------------- |
| **Background** | Hell | Hintergrund |
| **Widget** | Weiß | Widget-Hintergrund |
| **Border** | Grau | Rand |

## Hover and focus effects

| Effect | Description |
| -------- | -------------- |
| `shadow` | stronger shadow |
| `border` | the border lights up |

## Responsive

- Four columns from 1600 px, three from 1200 px, two from 800 px, below that a single
  column; the saved order is kept.
- Widgets keep their row span as far as it fits the new column count; otherwise they grow
  in height.
- On touch devices moving only starts after a long press (`long-press`), the neighbours move
  aside with `reorder`.

## Widget types

| Type | Description |
|------------|-------------|
| **Card** | card |
| **Chart** | chart |
| **List** | list |
| **Table** | table |
| **Stat** | statistic |
| **Calendar** | calendar |

## Drag & Drop

```
┌─────────────────────────────────────────┐
│ [Widget 1] [Widget 2] [Widget 3]        │
│      📦                                 │
│ [Widget 4] [Widget 5] [Widget 6]        │
│                                         │
│ [Widget 7] [Widget 8] [Widget 9]        │
└─────────────────────────────────────────┘
```

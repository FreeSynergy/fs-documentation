# Chart - Appearance

## Base layout

A chart is a data visualisation (diagrams).

## Variants

| Variant | Description |
|---------|-------------|
| **Line** | course over time |
| **Bar** | comparing individual values |
| **Pie** | share of a whole |
| **Doughnut** | share with free space for a total |
| **Scatter** | two quantities against each other |
| **Heatmap** | density across two axes |
| **Radar** | several dimensions of one entity |

### Line chart

```
┌─────────────────────────────────────────┐
│  100 ┤  ╱╲                               │
│      │ ╱  ╲                              │
│   50 ┤╱    ╲                             │
│      │      ╲                            │
│    0 ┼────────╲────────                  │
│      └───────────────────                │
└─────────────────────────────────────────┘
```

### Bar chart

```
┌─────────────────────────────────────────┐
│  100 ┤  ▓▓                               │
│      │  ▓▓                               │
│   50 ┤  ▓▓  ▓▓                           │
│      │  ▓▓  ▓▓  ▓▓                       │
│    0 ┤  ▓▓  ▓▓  ▓▓  ▓▓                   │
│      └───────────────────                │
└─────────────────────────────────────────┘
```

### Pie chart

```
┌─────────────────────────────────────────┐
│      ╱─────╲                            │
│    ╱         ╲                          │
│   │    50%    │                         │
│    ╲         ╱                          │
│      ╲_____/                            │
└─────────────────────────────────────────┘
```

## Sizes

| Size | Width/height | Use |
|------|--------------|-----|
| small | 300x200px | inline |
| medium | 500x300px | standard |
| large | 700x400px | featured |

## Colours and states

| Status | Colour | Description |
|--------|--------|-------------|
| **Background** | white | background |
| **Grid** | grey | grid lines |
| **Data** | colours | data series |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `tooltip` | a tooltip appears |
| `highlight` | highlights a segment |

## Responsive

- The chart scales in width with the container; the height stays proportional,
  but at least 200 px.
- Below `small` screen width the legend moves below the drawing, axis labels
  are thinned out (every other label).
- Too many bars or points are grouped together instead of being drawn overlapping;
  `pinch` enlarges the time section of a line, `drag` moves it.

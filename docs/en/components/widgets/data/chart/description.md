# Chart

| Field | Value |
|-------|-------|
| **Category** | `data` |
| **Inherits from** | `base` |
| **Variants** | `line`, `bar`, `pie`, `doughnut`, `scatter`, `heatmap`, `radar` |
| **States** | `leer`, `wartend` |
| **Gestures** | `tap`, `drag`, `pinch`, `swipe` |
| **Animations** | `highlight`, `fade-in`, `progress` |
| **Related** | `table`, `description-list`, `dashboard`, `skeleton` |
| **Status** | documented |

## Description
A chart is a data visualisation (diagrams).

## Purpose

- Statistics
- Diagrams
- Graphics

## Variants

| Variant | Description |
|---------|-------------|
| **line** | course over time |
| **bar** | comparing individual values |
| **pie** | share of a whole |
| **doughnut** | share with free space for a total |
| **scatter** | two quantities against each other |
| **heatmap** | density across two axes |
| **radar** | several dimensions of one entity |

## Features

- Interactive
- Responsive
- Animations
- Export

## Distinction

- **Do not confuse with** [table](../table/): the table is the reliable way to see numbers,
  the chart only the complementary form. Both together is right, the chart alone is not.
- **Do not confuse with** [progress](../../../primitives/feedback/progress/): a bar shows a share,
  a chart compares values.
- **Do not confuse with** [dashboard](../../../workbenches/special/dashboard/): the dashboard arranges several
  charts and cards, it draws nothing itself.

## Best Practices

- Time series as a line, comparisons as bars, shares as a pie only with at most five categories.
- Label the axes and units; a chart without axis labels is decoration.
- Take the colours from the application's colour tokens, do not mix them freely; put the legend
  next to the drawing.
- Always offer a numeric alternative (table or individual values) so the information
  is not available only visually.
- Label empty data as `leer` with a note, do not leave it as an empty surface.

## See also

- [data – overview](../index.md)
- [Table](../table/) — numbers in rows and columns
- [Dashboard](../../../workbenches/special/dashboard/) — arranging several charts
- [Base component](../../../primitives/basics/base.md)

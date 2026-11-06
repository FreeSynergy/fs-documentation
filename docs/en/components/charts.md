# Charts

**Status: proposal (2026-11-06).** Charts are components, needed by surveys, project management, ERP and more. We list
all of them, without implying we build all of them. The interface is to be a standard, so charts can be plugins.

[Full catalogue](https://github.com/FreeSynergy/fs-documentation/blob/main/temp/research/charts-catalogue.md): about 235
chart types, sorted by the question they answer, each with the data shape it needs and a priority.

## Priority A, by purpose

| Purpose | Charts |
|---------|--------|
| Compare | Column, bar, grouped and stacked bar, 100 % stacked bar, bullet, diverging bar |
| Change over time | Line, area, stacked area, sparkline |
| Part of a whole | Pie, donut |
| Distribution | Histogram, boxplot |
| Relationship | Scatter, heatmap |
| Project | Gantt, milestones, burn-down and burn-up, resource load, risk matrix |
| Decisions | Parliament, ranked-choice rounds, resistance bar, Likert diverging bar, matrix heat map, quorum gauge |
| Status | KPI card, gauge, progress ring, red-amber-green status |
| Money | Waterfall, budget vs actual, S-curve, aging buckets |

## What Blinc has

Line, area, bar (stacked and horizontal), sparkline, threshold line, histogram, comparison bar, pie and donut.

Two gaps: [our chart component page](widgets/data/chart/description.md) lists scatter, heatmap and radar, which Blinc does
not have, and Blinc's chart code has no text alternative or ARIA support, which our docs require. Both are candidates
for contributing to Blinc.

## Interface proposal

- **Base vocabulary: a validated subset of Vega-Lite** (BSD-3-Clause), which separates data and presentation.
- **Own registry for what it lacks,** such as Gantt, gauge, parliament and KPI card.
- **A mandatory accessibility block,** so every chart has a description.
- **Our own Rust interpreter,** since the existing Rust options embed a JavaScript engine.
- **As plugins:** a chart returns a scene description, and the host draws it. See [plugin form](../interfaces/index.md#plugin-form).

This has not been tried or measured yet.

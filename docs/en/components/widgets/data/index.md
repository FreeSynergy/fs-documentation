# data

Band [widgets](../) – knows its contents when it is built.

Elements that present data: lists, tables, grids, trees, timelines and charts. They do
not edit values but show them — the fields are what changes them.

## Elements

- [**avatar**](./avatar/) – an avatar is a visual representation element for a user.
- [**calendar-view**](./calendar-view/) – a calendar view shows appointments in a calendar.
- [**chart**](./chart/) – a chart is a data visualisation (diagrams).
- [**description-list**](./description-list/) – a description list shows pairs of a label and a value — the detail view of a data record.
- [**grid-view**](./grid-view/) – a grid view is a card/grid display of elements.
- [**list-view**](./list-view/) – a list view is a simple list display of elements.
- [**repeater**](./repeater/) – a repeater is a repeating layout for lists.
- [**table**](./table/) – a table is a tabular display with rows and columns.
- [**table-of-contents**](./table-of-contents/) – a table of contents is an overview of chapters/sections.
- [**timeline**](./timeline/) – a timeline is a chronological display of events.
- [**tree-view**](./tree-view/) – a tree view is a hierarchical directory structure with collapse/expand.

## Profiles

| Component | Inherits from | Variants | Role | Status |
|-----------|---------------|----------|------|--------|
| [avatar](./avatar/) | `base` | `image`, `initials`, `icon`, `placeholder` | - | documented |
| [calendar-view](./calendar-view/) | `base` | `Monthly View`, `Weekly View`, `Daily View`, `Agenda View` | - | documented |
| [chart](./chart/) | `base` | `line`, `bar`, `pie`, `doughnut`, `scatter`, `heatmap`, `radar` | - | documented |
| [description-list](./description-list/) | `base` | `zweispaltig`, `gestapelt`, `inline` | `list` | documented |
| [grid-view](./grid-view/) | `base` | `Fixed Grid`, `Responsive Grid`, `Masonry Grid` | - | documented |
| [list-view](./list-view/) | `base` | `Simple`, `With Icons`, `With Avatars`, `With Badges`, `With Actions` | - | documented |
| [repeater](./repeater/) | `base` | `liste`, `raster`, `eingabe` | - | documented |
| [table](./table/) | `base` | `Simple`, `Data`, `Tree`, `Inline Edit` | - | documented |
| [table-of-contents](./table-of-contents/) | `base` | `randspalte`, `block`, `aufklappbar` | - | documented |
| [timeline](./timeline/) | `base` | `senkrecht`, `waagerecht`, `karten`, `ereignisse` | - | documented |
| [tree-view](./tree-view/) | `base` | `Simple`, `With Icons`, `With Checkboxes`, `Draggable` | - | documented |

## See also

- [Component overview](../../index.md)
- [Band widgets](../)
- [Base component](../../primitives/basics/base.md)
- [Fields](../../primitives/fields/) for making changes

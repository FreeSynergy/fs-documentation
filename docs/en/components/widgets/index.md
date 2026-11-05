# widgets – building blocks with known content

It knows its contents when it is built: it binds a known data model, has finite children and its own state. Test question: *knows its contents when it is built*.

## Type groups (7) — 53 components

### [navigation](./navigation/) — navigation (10)

Elements that show or switch the way through the program: menus, bars, tabs, sidebars and path indications.

[bottom-navigation](./navigation/bottom-navigation/), [breadcrumb](./navigation/breadcrumb/), [command](./navigation/command/), [language-switcher](./navigation/language-switcher/), [menu](./navigation/menu/), [pagination](./navigation/pagination/), [radial-menu](./navigation/radial-menu/), [sidebar](./navigation/sidebar/), [tabs](./navigation/tabs/), [toolbar](./navigation/toolbar/)

### [containers](./containers/) — containers (6)

Boxes and surfaces that hold other content: cards, panels, collapsible groups, split views and assistants.

[accordion](./containers/accordion/), [card](./containers/card/), [panel](./containers/panel/), [scroll-area](./containers/scroll-area/), [split-view](./containers/split-view/), [wizard](./containers/wizard/)

### [overlays](./overlays/) — overlays (8)

Elements that appear above other content and get their own focus. They have a lifetime of their own and close with `Esc` or a click outside.

[alert-dialog](./overlays/alert-dialog/), [context-menu](./overlays/context-menu/), [drawer](./overlays/drawer/), [hover-card](./overlays/hover-card/), [key-verification](./overlays/key-verification/), [modal](./overlays/modal/), [popover](./overlays/popover/), [tooltip](./overlays/tooltip/)

### [fields](./fields/) — fields (6)

Elements for entering and selecting values. The field (`field`) holds the label, help text and error message together.

[date-picker](./fields/date-picker/), [emoji-picker](./fields/emoji-picker/), [file-upload](./fields/file-upload/), [range-calendar](./fields/range-calendar/), [rule-editor](./fields/rule-editor/), [time-picker](./fields/time-picker/)

### [data](./data/) — data (16)

Elements that present data: lists, tables, grids, trees, timelines and charts. They do not edit values but show them — the fields are what changes them.

[avatar](./data/avatar/), [calendar-view](./data/calendar-view/), [chart](./data/chart/), [description-list](./data/description-list/), [grid-view](./data/grid-view/), [link-preview](./data/link-preview/), [list-view](./data/list-view/), [mail-view](./data/mail-view/), [message-bubble](./data/message-bubble/), [message-list](./data/message-list/), [reaction-bar](./data/reaction-bar/), [repeater](./data/repeater/), [table](./data/table/), [table-of-contents](./data/table-of-contents/), [timeline](./data/timeline/), [tree-view](./data/tree-view/)

### [media](./media/) — media (6)

Elements that play or show media. `media-player` is the parent class of `audio` and `video`.

[audio](./media/audio/), [video](./media/video/), [media-player](./media/media-player/), [call-controls](./media/call-controls/), [carousel](./media/carousel/), [gallery](./media/gallery/)

### [special](./special/) — special elements (1)

Composite elements with a data structure of their own: editors, embeds, maps and views that generic libraries do not offer.

[map-view](./special/map-view/)

## See also

- [Component overview](../index.md)
- [Base class](../primitives/basics/base.md)
- [primitives](../primitives/) – building blocks
- [workbenches](../workbenches/) – open work surfaces
- [Gestures](../../interactions/gestures/) and [Animations](../../interactions/animations/)

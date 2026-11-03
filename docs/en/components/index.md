# UI components & elements

This documentation describes the UI elements used in FreeSynergy programs. They
are sorted by level: `primitives` → `widgets` → `workbenches` (decisions 0001 and
0004); the type groups (basics, fields, …) are kept inside the bands.

## Fundamentals

All components inherit from the **base class** [base](primitives/basics/base.md):
inherited attributes, size grid, states, accessibility, file set and naming
convention. A component file lists only its **own** attributes.

## Bands (3) — 84 components, 10 type groups

### [primitives](./primitives/) — building blocks (34)

Cannot be broken down further: one value, one gesture, one state. No band
contains content it only receives at runtime.

#### [basics](./primitives/basics/) — fundamentals (4)

[kbd](./primitives/basics/kbd/), [label](./primitives/basics/label/), [link](./primitives/basics/link/), [separator](./primitives/basics/separator/)

#### [actions](./primitives/actions/) — actions (3)

[button](./primitives/actions/button/), [button-group](./primitives/actions/button-group/), [floating-action-button](./primitives/actions/floating-action-button/)

#### [feedback](./primitives/feedback/) — feedback (7)

[alert](./primitives/feedback/alert/), [badge](./primitives/feedback/badge/), [empty-state](./primitives/feedback/empty-state/), [progress](./primitives/feedback/progress/), [skeleton](./primitives/feedback/skeleton/), [spinner](./primitives/feedback/spinner/), [toast](./primitives/feedback/toast/)

#### [fields](./primitives/fields/) — fields (18)

[checkbox](./primitives/fields/checkbox/), [color-input](./primitives/fields/color-input/), [combobox](./primitives/fields/combobox/), [date-input](./primitives/fields/date-input/), [field](./primitives/fields/field/), [input-group](./primitives/fields/input-group/), [mention-input](./primitives/fields/mention-input/), [number-input](./primitives/fields/number-input/), [otp-input](./primitives/fields/otp-input/), [radio-group](./primitives/fields/radio-group/), [rating](./primitives/fields/rating/), [search-field](./primitives/fields/search-field/), [select](./primitives/fields/select/), [slider](./primitives/fields/slider/), [switch](./primitives/fields/switch/), [tags-input](./primitives/fields/tags-input/), [text-input](./primitives/fields/text-input/), [textarea](./primitives/fields/textarea/)

#### [media](./primitives/media/) — media (2)

[icon](./primitives/media/icon/), [image](./primitives/media/image/)

### [widgets](./widgets/) — building blocks with known content (45)

It knows its contents when it is built: it binds a known data model, has finite
children and its own state.

#### [navigation](./widgets/navigation/) — navigation (10)

[bottom-navigation](./widgets/navigation/bottom-navigation/), [breadcrumb](./widgets/navigation/breadcrumb/), [command](./widgets/navigation/command/), [language-switcher](./widgets/navigation/language-switcher/), [menu](./widgets/navigation/menu/), [pagination](./widgets/navigation/pagination/), [radial-menu](./widgets/navigation/radial-menu/), [sidebar](./widgets/navigation/sidebar/), [tabs](./widgets/navigation/tabs/), [toolbar](./widgets/navigation/toolbar/)

#### [containers](./widgets/containers/) — containers (6)

[accordion](./widgets/containers/accordion/), [card](./widgets/containers/card/), [panel](./widgets/containers/panel/), [scroll-area](./widgets/containers/scroll-area/), [split-view](./widgets/containers/split-view/), [wizard](./widgets/containers/wizard/)

#### [overlays](./widgets/overlays/) — overlays (7)

[alert-dialog](./widgets/overlays/alert-dialog/), [context-menu](./widgets/overlays/context-menu/), [drawer](./widgets/overlays/drawer/), [hover-card](./widgets/overlays/hover-card/), [modal](./widgets/overlays/modal/), [popover](./widgets/overlays/popover/), [tooltip](./widgets/overlays/tooltip/)

#### [fields](./widgets/fields/) — fields (5)

[date-picker](./widgets/fields/date-picker/), [emoji-picker](./widgets/fields/emoji-picker/), [file-upload](./widgets/fields/file-upload/), [range-calendar](./widgets/fields/range-calendar/), [time-picker](./widgets/fields/time-picker/)

#### [data](./widgets/data/) — data (11)

[avatar](./widgets/data/avatar/), [calendar-view](./widgets/data/calendar-view/), [chart](./widgets/data/chart/), [description-list](./widgets/data/description-list/), [grid-view](./widgets/data/grid-view/), [list-view](./widgets/data/list-view/), [repeater](./widgets/data/repeater/), [table](./widgets/data/table/), [table-of-contents](./widgets/data/table-of-contents/), [timeline](./widgets/data/timeline/), [tree-view](./widgets/data/tree-view/)

#### [media](./widgets/media/) — media (5)

[audio](./widgets/media/audio/), [video](./widgets/media/video/), [media-player](./widgets/media/media-player/), [carousel](./widgets/media/carousel/), [gallery](./widgets/media/gallery/)

#### [special](./widgets/special/) — special elements (1)

[map-view](./widgets/special/map-view/)

### [workbenches](./workbenches/) — open work surfaces (5)

It receives its content only at runtime: an open surface that may itself hold
primitives and widgets.

#### [fields](./workbenches/fields/) — fields (1)

[rich-text-editor](./workbenches/fields/rich-text-editor/)

#### [special](./workbenches/special/) — special elements (4)

[code-editor](./workbenches/special/code-editor/), [dashboard](./workbenches/special/dashboard/), [embed](./workbenches/special/embed/), [whiteboard](./workbenches/special/whiteboard/)

## What is documented here?

Every component has a fixed file set:

- **description.md** – profile, description, purpose, variants, distinction
- **appearance.md** – looks: layout, sizes, colours, states, responsive
- **attributes.md** – only **own** attributes + reference to `primitives/basics/base.md`
- **usage.md** – application, scenarios and examples

The lists and numbers on this page are generated by `scripts/gen_component_indexes.py`. `scripts/check_components.py` checks the standard.

## See also

- [Gestures](../interactions/gestures/) and [Animations](../interactions/animations/)
- [Standardised data](../data/)
- [Programs](../programs/)

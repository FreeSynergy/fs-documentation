# UI-Komponenten & Elemente

Diese Dokumentation beschreibt die UI-Elemente, die in FreeSynergy-Programmen
verwendet werden. Sie sind nach Ebene sortiert: `primitives` → `widgets` →
`workbenches` (Beschlüsse 0001 und 0004); die Typgruppen (basics, fields, …)
bleiben innerhalb der Bänder erhalten.

## Grundlagen

Alle Komponenten erben von der **Basisklasse** [base](primitives/basics/base.md): geerbte Attribute, Größen-Raster, Zustände,
Barrierefreiheit, Dateisatz und Namenskonvention. Eine Komponentendatei
listet nur ihre **eigenen** Attribute.

## Bänder (3) — 97 Komponenten, 10 Typgruppen

### [primitives](./primitives/) — Grundbausteine (36)

Nicht weiter zerlegbar: ein Wert, eine Geste, ein Zustand. Kein Band enthält Inhalte, die es erst zur Laufzeit bekommt.

#### [basics](./primitives/basics/) — Grundlagen (4)

[kbd](./primitives/basics/kbd/), [label](./primitives/basics/label/), [link](./primitives/basics/link/), [separator](./primitives/basics/separator/)

#### [actions](./primitives/actions/) — Aktionen (3)

[button](./primitives/actions/button/), [button-group](./primitives/actions/button-group/), [floating-action-button](./primitives/actions/floating-action-button/)

#### [feedback](./primitives/feedback/) — Rückmeldung (9)

[alert](./primitives/feedback/alert/), [badge](./primitives/feedback/badge/), [empty-state](./primitives/feedback/empty-state/), [encryption-state](./primitives/feedback/encryption-state/), [message-status](./primitives/feedback/message-status/), [progress](./primitives/feedback/progress/), [skeleton](./primitives/feedback/skeleton/), [spinner](./primitives/feedback/spinner/), [toast](./primitives/feedback/toast/)

#### [fields](./primitives/fields/) — Felder (18)

[checkbox](./primitives/fields/checkbox/), [color-input](./primitives/fields/color-input/), [combobox](./primitives/fields/combobox/), [date-input](./primitives/fields/date-input/), [field](./primitives/fields/field/), [input-group](./primitives/fields/input-group/), [mention-input](./primitives/fields/mention-input/), [number-input](./primitives/fields/number-input/), [otp-input](./primitives/fields/otp-input/), [radio-group](./primitives/fields/radio-group/), [rating](./primitives/fields/rating/), [search-field](./primitives/fields/search-field/), [select](./primitives/fields/select/), [slider](./primitives/fields/slider/), [switch](./primitives/fields/switch/), [tags-input](./primitives/fields/tags-input/), [text-input](./primitives/fields/text-input/), [textarea](./primitives/fields/textarea/)

#### [media](./primitives/media/) — Medien (2)

[icon](./primitives/media/icon/), [image](./primitives/media/image/)

### [widgets](./widgets/) — Bausteine mit bekanntem Inhalt (53)

Kennt seine Inhalte beim Bauen: bindet ein bekanntes Datenmodell, hat endliche Kinder und eigenen Zustand.

#### [navigation](./widgets/navigation/) — Navigation (10)

[bottom-navigation](./widgets/navigation/bottom-navigation/), [breadcrumb](./widgets/navigation/breadcrumb/), [command](./widgets/navigation/command/), [language-switcher](./widgets/navigation/language-switcher/), [menu](./widgets/navigation/menu/), [pagination](./widgets/navigation/pagination/), [radial-menu](./widgets/navigation/radial-menu/), [sidebar](./widgets/navigation/sidebar/), [tabs](./widgets/navigation/tabs/), [toolbar](./widgets/navigation/toolbar/)

#### [containers](./widgets/containers/) — Container (6)

[accordion](./widgets/containers/accordion/), [card](./widgets/containers/card/), [panel](./widgets/containers/panel/), [scroll-area](./widgets/containers/scroll-area/), [split-view](./widgets/containers/split-view/), [wizard](./widgets/containers/wizard/)

#### [overlays](./widgets/overlays/) — Overlays (8)

[alert-dialog](./widgets/overlays/alert-dialog/), [context-menu](./widgets/overlays/context-menu/), [drawer](./widgets/overlays/drawer/), [hover-card](./widgets/overlays/hover-card/), [key-verification](./widgets/overlays/key-verification/), [modal](./widgets/overlays/modal/), [popover](./widgets/overlays/popover/), [tooltip](./widgets/overlays/tooltip/)

#### [fields](./widgets/fields/) — Felder (6)

[date-picker](./widgets/fields/date-picker/), [emoji-picker](./widgets/fields/emoji-picker/), [file-upload](./widgets/fields/file-upload/), [range-calendar](./widgets/fields/range-calendar/), [rule-editor](./widgets/fields/rule-editor/), [time-picker](./widgets/fields/time-picker/)

#### [data](./widgets/data/) — Daten (16)

[avatar](./widgets/data/avatar/), [calendar-view](./widgets/data/calendar-view/), [chart](./widgets/data/chart/), [description-list](./widgets/data/description-list/), [grid-view](./widgets/data/grid-view/), [link-preview](./widgets/data/link-preview/), [list-view](./widgets/data/list-view/), [mail-view](./widgets/data/mail-view/), [message-bubble](./widgets/data/message-bubble/), [message-list](./widgets/data/message-list/), [reaction-bar](./widgets/data/reaction-bar/), [repeater](./widgets/data/repeater/), [table](./widgets/data/table/), [table-of-contents](./widgets/data/table-of-contents/), [timeline](./widgets/data/timeline/), [tree-view](./widgets/data/tree-view/)

#### [media](./widgets/media/) — Medien (6)

[audio](./widgets/media/audio/), [video](./widgets/media/video/), [media-player](./widgets/media/media-player/), [call-controls](./widgets/media/call-controls/), [carousel](./widgets/media/carousel/), [gallery](./widgets/media/gallery/)

#### [special](./widgets/special/) — Spezielle Elemente (1)

[map-view](./widgets/special/map-view/)

### [workbenches](./workbenches/) — Offene Arbeitsflaechen (8)

Erhält seinen Inhalt erst zur Laufzeit: offene Fläche, die selbst primitives und widgets aufnehmen darf.

#### [fields](./workbenches/fields/) — Felder (2)

[block-editor](./workbenches/fields/block-editor/), [rich-text-editor](./workbenches/fields/rich-text-editor/)

#### [special](./workbenches/special/) — Spezielle Elemente (6)

[code-editor](./workbenches/special/code-editor/), [dashboard](./workbenches/special/dashboard/), [embed](./workbenches/special/embed/), [html-view](./workbenches/special/html-view/), [message-composer](./workbenches/special/message-composer/), [whiteboard](./workbenches/special/whiteboard/)

## Was ist hier dokumentiert?

Jede Komponente hat einen festen Dateisatz:

- **description.md** – Steckbrief, Beschreibung, Verwendungszweck, Varianten, Abgrenzung
- **appearance.md** – Aussehen: Layout, Größen, Farben, Zustände, Reaktiv
- **attributes.md** – nur **eigene** Attribute + Verweis auf `primitives/basics/base.md`
- **usage.md** – Anwendung, Szenarien und Beispiele

Die Listen und Zahlen auf dieser Seite erzeugt `scripts/gen_component_indexes.py`. `scripts/check_components.py` prüft den Standard.

## Siehe auch

- [Gesten](../interactions/gestures/) und [Animationen](../interactions/animations/)
- [Standardisierte Daten](../data/)
- [Programs](../programs/)

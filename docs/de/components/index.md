# UI-Komponenten & Elemente

Diese Dokumentation beschreibt die UI-Elemente, die in FreeSynergy-Programmen
verwendet werden.

## Grundlagen

Alle Komponenten erben von der **Basisklasse** [base](basics/base.md): geerbte Attribute, Größen-Raster, Zustände,
Barrierefreiheit, Dateisatz und Namenskonvention. Eine Komponentendatei
listet nur ihre **eigenen** Attribute.

## Kategorien (10) — 84 Komponenten

### [basics](./basics/) — Grundlagen (4)

Grundlagen, von denen alle anderen Komponenten ausgehen: die Basisklasse mit ihren geerbten Attributen, Zuständen und Tokens sowie die kleinsten Bausteine.

[kbd](./basics/kbd/), [label](./basics/label/), [link](./basics/link/), [separator](./basics/separator/)

### [actions](./actions/) — Aktionen (3)

Action-Elemente lösen eine einzelne Handlung aus oder bündeln zusammengehörige Handlungen. Sie verändern Daten oder Zustände, aber nicht die Adresse.

[button](./actions/button/), [button-group](./actions/button-group/), [floating-action-button](./actions/floating-action-button/)

### [navigation](./navigation/) — Navigation (10)

Elemente, die den Weg durch das Programm zeigen oder umschalten: Menüs, Leisten, Reiter, Seitenleisten und Pfadangaben.

[bottom-navigation](./navigation/bottom-navigation/), [breadcrumb](./navigation/breadcrumb/), [command](./navigation/command/), [language-switcher](./navigation/language-switcher/), [menu](./navigation/menu/), [pagination](./navigation/pagination/), [radial-menu](./navigation/radial-menu/), [sidebar](./navigation/sidebar/), [tabs](./navigation/tabs/), [toolbar](./navigation/toolbar/)

### [containers](./containers/) — Container (6)

Boxen und Flächen, die anderen Inhalt aufnehmen: Karten, Panels, aufklappbare Gruppen, geteilte Ansichten und Assistenten.

[accordion](./containers/accordion/), [card](./containers/card/), [panel](./containers/panel/), [scroll-area](./containers/scroll-area/), [split-view](./containers/split-view/), [wizard](./containers/wizard/)

### [overlays](./overlays/) — Overlays (7)

Elemente, die über anderem Inhalt erscheinen und eigenen Fokus bekommen. Sie haben eine eigene Lebensdauer und schließen mit `Esc` oder Klick außerhalb.

[alert-dialog](./overlays/alert-dialog/), [context-menu](./overlays/context-menu/), [drawer](./overlays/drawer/), [hover-card](./overlays/hover-card/), [modal](./overlays/modal/), [popover](./overlays/popover/), [tooltip](./overlays/tooltip/)

### [feedback](./feedback/) — Rückmeldung (7)

Elemente, die den Zustand einer Anwendung sichtbar machen: Meldungen, Fortschritt, Ladezustände und Kennzeichnungen.

[alert](./feedback/alert/), [badge](./feedback/badge/), [empty-state](./feedback/empty-state/), [progress](./feedback/progress/), [skeleton](./feedback/skeleton/), [spinner](./feedback/spinner/), [toast](./feedback/toast/)

### [fields](./fields/) — Felder (24)

Elemente zum Eingeben und Auswählen von Werten. Das Feld (`field`) hält dabei Beschriftung, Hilfetext und Fehlermeldung zusammen.

[checkbox](./fields/checkbox/), [color-input](./fields/color-input/), [combobox](./fields/combobox/), [date-input](./fields/date-input/), [date-picker](./fields/date-picker/), [emoji-picker](./fields/emoji-picker/), [field](./fields/field/), [file-upload](./fields/file-upload/), [input-group](./fields/input-group/), [mention-input](./fields/mention-input/), [number-input](./fields/number-input/), [otp-input](./fields/otp-input/), [radio-group](./fields/radio-group/), [range-calendar](./fields/range-calendar/), [rating](./fields/rating/), [rich-text-editor](./fields/rich-text-editor/), [search-field](./fields/search-field/), [select](./fields/select/), [slider](./fields/slider/), [switch](./fields/switch/), [tags-input](./fields/tags-input/), [text-input](./fields/text-input/), [textarea](./fields/textarea/), [time-picker](./fields/time-picker/)

### [data](./data/) — Daten (11)

Elemente, die Daten darstellen: Listen, Tabellen, Raster, Bäume, Zeitachsen und Diagramme. Sie bearbeiten Werte, sondern zeigen sie — zum Ändern kommen die [Felder](../fields/) zum Einsatz.

[avatar](./data/avatar/), [calendar-view](./data/calendar-view/), [chart](./data/chart/), [description-list](./data/description-list/), [grid-view](./data/grid-view/), [list-view](./data/list-view/), [repeater](./data/repeater/), [table](./data/table/), [table-of-contents](./data/table-of-contents/), [timeline](./data/timeline/), [tree-view](./data/tree-view/)

### [media](./media/) — Medien (7)

Elemente, die Medien wiedergeben oder darstellen. `media-player` ist die Elternklasse von `audio` und `video`.

[audio](./media/audio/), [carousel](./media/carousel/), [gallery](./media/gallery/), [icon](./media/icon/), [image](./media/image/), [media-player](./media/media-player/), [video](./media/video/)

### [special](./special/) — Spezielle Elemente (5)

Zusammengesetzte Elemente mit eigener Datenstruktur: Editoren, Einbettungen, Karten und Ansichten, die es bei generischen Bibliotheken nicht gibt.

[code-editor](./special/code-editor/), [dashboard](./special/dashboard/), [embed](./special/embed/), [map-view](./special/map-view/), [whiteboard](./special/whiteboard/)

## Was ist hier dokumentiert?

Jede Komponente hat einen festen Dateisatz:

- **description.md** – Steckbrief, Beschreibung, Verwendungszweck, Varianten, Abgrenzung
- **appearance.md** – Aussehen: Layout, Größen, Farben, Zustände, Reaktiv
- **attributes.md** – nur **eigene** Attribute + Verweis auf `basics/base.md`
- **usage.md** – Anwendung, Szenarien und Beispiele

Die Listen und Zahlen auf dieser Seite erzeugt `tools/gen_component_indexes.py`. `tools/check_components.py` prüft den Standard.

## Siehe auch

- [Konzept und Plan](konzept-und-plan.md) – Standardisierung, Kategorien, Merges
- [Gesten](../gestures/) und [Animationen](../animations/)
- [Standardisierte Daten](../data/)
- [Apps](../apps/)

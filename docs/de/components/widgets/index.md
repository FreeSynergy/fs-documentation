# widgets – Bausteine mit bekanntem Inhalt

Kennt seine Inhalte beim Bauen: bindet ein bekanntes Datenmodell, hat endliche Kinder und eigenen Zustand. Testfrage: *kennt seine Inhalte beim Bauen*.

## Typgruppen (7) — 53 Komponenten

### [navigation](./navigation/) — Navigation (10)

Elemente, die den Weg durch das Programm zeigen oder umschalten: Menüs, Leisten, Reiter, Seitenleisten und Pfadangaben.

[bottom-navigation](./navigation/bottom-navigation/), [breadcrumb](./navigation/breadcrumb/), [command](./navigation/command/), [language-switcher](./navigation/language-switcher/), [menu](./navigation/menu/), [pagination](./navigation/pagination/), [radial-menu](./navigation/radial-menu/), [sidebar](./navigation/sidebar/), [tabs](./navigation/tabs/), [toolbar](./navigation/toolbar/)

### [containers](./containers/) — Container (6)

Boxen und Flächen, die anderen Inhalt aufnehmen: Karten, Panels, aufklappbare Gruppen, geteilte Ansichten und Assistenten.

[accordion](./containers/accordion/), [card](./containers/card/), [panel](./containers/panel/), [scroll-area](./containers/scroll-area/), [split-view](./containers/split-view/), [wizard](./containers/wizard/)

### [overlays](./overlays/) — Overlays (8)

Elemente, die über anderem Inhalt erscheinen und eigenen Fokus bekommen. Sie haben eine eigene Lebensdauer und schließen mit `Esc` oder Klick außerhalb.

[alert-dialog](./overlays/alert-dialog/), [context-menu](./overlays/context-menu/), [drawer](./overlays/drawer/), [hover-card](./overlays/hover-card/), [key-verification](./overlays/key-verification/), [modal](./overlays/modal/), [popover](./overlays/popover/), [tooltip](./overlays/tooltip/)

### [fields](./fields/) — Felder (6)

Elemente zum Eingeben und Auswählen von Werten. Das Feld (`field`) hält dabei Beschriftung, Hilfetext und Fehlermeldung zusammen.

[date-picker](./fields/date-picker/), [emoji-picker](./fields/emoji-picker/), [file-upload](./fields/file-upload/), [range-calendar](./fields/range-calendar/), [rule-editor](./fields/rule-editor/), [time-picker](./fields/time-picker/)

### [data](./data/) — Daten (16)

Elemente, die Daten darstellen: Listen, Tabellen, Raster, Bäume, Zeitachsen und Diagramme. Sie bearbeiten Werte, sondern zeigen sie — zum Ändern kommen die Felder zum Einsatz.

[avatar](./data/avatar/), [calendar-view](./data/calendar-view/), [chart](./data/chart/), [description-list](./data/description-list/), [grid-view](./data/grid-view/), [link-preview](./data/link-preview/), [list-view](./data/list-view/), [mail-view](./data/mail-view/), [message-bubble](./data/message-bubble/), [message-list](./data/message-list/), [reaction-bar](./data/reaction-bar/), [repeater](./data/repeater/), [table](./data/table/), [table-of-contents](./data/table-of-contents/), [timeline](./data/timeline/), [tree-view](./data/tree-view/)

### [media](./media/) — Medien (6)

Elemente, die Medien wiedergeben oder darstellen. `media-player` ist die Elternklasse von `audio` und `video`.

[audio](./media/audio/), [video](./media/video/), [media-player](./media/media-player/), [call-controls](./media/call-controls/), [carousel](./media/carousel/), [gallery](./media/gallery/)

### [special](./special/) — Spezielle Elemente (1)

Zusammengesetzte Elemente mit eigener Datenstruktur: Editoren, Einbettungen, Karten und Ansichten, die es bei generischen Bibliotheken nicht gibt.

[map-view](./special/map-view/)

## Siehe auch

- [Komponenten-Übersicht](../index.md)
- [Basisklasse](../primitives/basics/base.md)
- [primitives](../primitives/) – Grundbausteine
- [workbenches](../workbenches/) – Offene Arbeitsflaechen
- [Gesten](../../interactions/gestures/) und [Animationen](../../interactions/animations/)

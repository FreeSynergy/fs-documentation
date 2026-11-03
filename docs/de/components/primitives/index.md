# primitives – Grundbausteine

Nicht weiter zerlegbar: ein Wert, eine Geste, ein Zustand. Kein Band enthält Inhalte, die es erst zur Laufzeit bekommt. Testfrage: *nicht weiter zerlegbar*.

## Typgruppen (5) — 34 Komponenten

### [basics](./basics/) — Grundlagen (4)

Grundlagen, von denen alle anderen Komponenten ausgehen: die Basisklasse mit ihren geerbten Attributen, Zuständen und Tokens sowie die kleinsten Bausteine.

[kbd](./basics/kbd/), [label](./basics/label/), [link](./basics/link/), [separator](./basics/separator/)

### [actions](./actions/) — Aktionen (3)

Action-Elemente lösen eine einzelne Handlung aus oder bündeln zusammengehörige Handlungen. Sie verändern Daten oder Zustände, aber nicht die Adresse.

[button](./actions/button/), [button-group](./actions/button-group/), [floating-action-button](./actions/floating-action-button/)

### [feedback](./feedback/) — Rückmeldung (7)

Elemente, die den Zustand einer Anwendung sichtbar machen: Meldungen, Fortschritt, Ladezustände und Kennzeichnungen.

[alert](./feedback/alert/), [badge](./feedback/badge/), [empty-state](./feedback/empty-state/), [progress](./feedback/progress/), [skeleton](./feedback/skeleton/), [spinner](./feedback/spinner/), [toast](./feedback/toast/)

### [fields](./fields/) — Felder (18)

Elemente zum Eingeben und Auswählen von Werten. Das Feld (`field`) hält dabei Beschriftung, Hilfetext und Fehlermeldung zusammen.

[checkbox](./fields/checkbox/), [color-input](./fields/color-input/), [combobox](./fields/combobox/), [date-input](./fields/date-input/), [field](./fields/field/), [input-group](./fields/input-group/), [mention-input](./fields/mention-input/), [number-input](./fields/number-input/), [otp-input](./fields/otp-input/), [radio-group](./fields/radio-group/), [rating](./fields/rating/), [search-field](./fields/search-field/), [select](./fields/select/), [slider](./fields/slider/), [switch](./fields/switch/), [tags-input](./fields/tags-input/), [text-input](./fields/text-input/), [textarea](./fields/textarea/)

### [media](./media/) — Medien (2)

Elemente, die Medien wiedergeben oder darstellen. `media-player` ist die Elternklasse von `audio` und `video`.

[icon](./media/icon/), [image](./media/image/)

## Siehe auch

- [Komponenten-Übersicht](../index.md)
- [Basisklasse](./basics/base.md)
- [widgets](../widgets/) – Bausteine mit bekanntem Inhalt
- [workbenches](../workbenches/) – Offene Arbeitsflaechen
- [Gesten](../../interactions/gestures/) und [Animationen](../../interactions/animations/)

# fields (Felder)

Elemente zum Eingeben und Auswählen von Werten. Das Feld (`field`) hält dabei Beschriftung, Hilfetext und Fehlermeldung zusammen.

## Elemente

- [**checkbox**](./checkbox/) – Ein Checkbox ist ein Ja/Nein- oder Mehrfachauswahlfeld.
- [**color-input**](./color-input/) – Ein Color Input ist ein Farbauswahl-Feld mit Farbpicker.
- [**combobox**](./combobox/) – Ein Combobox ist ein Textfeld + Dropdown.
- [**date-input**](./date-input/) – Ein Date Input ist ein Datumsauswahl-Feld mit Kalender.
- [**date-picker**](./date-picker/) – Der Datumswähler öffnet ein Kalenderoverlay, in dem ein Datum oder ein Bereich ausgewählt wird.
- [**emoji-picker**](./emoji-picker/) – Ein Emoji Picker ist eine Emoji-Auswahl für Chat/Kommentare.
- [**field**](./field/) – Ein Field ist der Wrapper um ein Eingabefeld: Er verbindet Beschriftung, Hilfetext, Fehlermeldung und Pflicht-Markierung zu einer barrierefreien Einheit.
- [**file-upload**](./file-upload/) – Ein File Upload ist ein Element für Dateiauswahl und Upload.
- [**input-group**](./input-group/) – Eine Input Group fügt ein Eingabefeld und die Teile, die unmittelbar dazugehören, zu einer zusammenhängenden Fläche zusammen: ein Vorsatz-Zeichen, eine Einheit, ein Dropdown für die Landesvorwahl oder eine Schaltfläche direkt am Feld.
- [**mention-input**](./mention-input/) – Ein Mention Input ist ein Textfeld mit Benutzer-/Kontakt-Erwähnung.
- [**number-input**](./number-input/) – Ein Number Input ist ein Eingabefeld für Zahlen.
- [**otp-input**](./otp-input/) – Das Einmalpasswortfeld nimmt einen kurzen numerischen Code auf — je Zeichen ein Feld.
- [**radio-group**](./radio-group/) – Eine Radio Group ist eine Gruppe von Optionsfeldern (einzelfach).
- [**range-calendar**](./range-calendar/) – Der Bereichskalender wählt einen zusammenhängenden Zeitraum.
- [**rating**](./rating/) – Ein Rating ist eine Sterne- oder Punktebewertung.
- [**rich-text-editor**](./rich-text-editor/) – Ein Rich Text Editor ist ein Editor für formatierten Text.
- [**search-field**](./search-field/) – Ein Search Field ist ein Suchfeld mit Filtermöglichkeiten.
- [**select**](./select/) – Eine Auswahlliste: das Feld zeigt den gewählten Wert, die Optionen liegen hinter einem Klick.
- [**slider**](./slider/) – Ein Slider ist ein Wertebereich mit Schieberegler.
- [**switch**](./switch/) – Ein Switch ist ein Ein/Aus-Schalter (Toggle).
- [**tags-input**](./tags-input/) – Ein Tags Input ist eine Liste von Tags/Etiketten.
- [**text-input**](./text-input/) – Ein Text Input ist ein einzeiliges Eingabefeld für Text.
- [**textarea**](./textarea/) – Ein Textarea ist ein mehrzeiliges Eingabefeld für Text.
- [**time-picker**](./time-picker/) – Die Zeitauswahl wählt eine Uhrzeit aus einer Liste möglicher Zeiten.

## Steckbriefe

| Komponente | Erbt von | Varianten | Rolle | Status |
|------------|----------|-----------|-------|--------|
| [checkbox](./checkbox/) | `base` | `Default`, `Toggle`, `Indeterminate` | - | dokumentiert |
| [color-input](./color-input/) | `base` | `palette`, `spectrum`, `code` | - | dokumentiert |
| [combobox](./combobox/) | `base`, `select` | `einzeln`, `freitext`, `mehrfach` | - | dokumentiert |
| [date-input](./date-input/) | `base` | `date`, `time`, `datetime` | - | dokumentiert |
| [date-picker](./date-picker/) | `base`, `date-input` | `einzeln`, `bereich`, `wiederkehrend` | `dialog` | dokumentiert |
| [emoji-picker](./emoji-picker/) | `base` | `inline`, `overlay`, `reaktion` | - | dokumentiert |
| [field](./field/) | `base` | `vertikal`, `horizontal`, `inline` | - | dokumentiert |
| [file-upload](./file-upload/) | `base` | `File Picker`, `Drag & Drop`, `Image Preview` | - | dokumentiert |
| [input-group](./input-group/) | `base` | `praefix`, `suffix`, `aktion`, `auswahl` | `group` | dokumentiert |
| [mention-input](./mention-input/) | `base`, `text-input` | `feld`, `inline`, `mehrzeilig` | - | dokumentiert |
| [number-input](./number-input/) | `base` | `einfach`, `stepper`, `formatiert` | - | dokumentiert |
| [otp-input](./otp-input/) | `base`, `text-input` | `einzelboxen`, `block` | `group` | dokumentiert |
| [radio-group](./radio-group/) | `base` | `einzeln`, `toggle`, `karte` | - | dokumentiert |
| [range-calendar](./range-calendar/) | `base`, `date-picker` | `zwei-monate`, `ein-monat` | `dialog` | dokumentiert |
| [rating](./rating/) | `base` | `Star Rating`, `Heart Rating`, `Number Rating` | - | dokumentiert |
| [rich-text-editor](./rich-text-editor/) | `base`, `textarea` | `wysiwyg`, `wiki-syntax` | - | dokumentiert |
| [search-field](./search-field/) | `base`, `text-input` | `Simple`, `Filter`, `Auto-complete` | - | dokumentiert |
| [select](./select/) | `base` | `Simple`, `Multi-select`, `Searchable`, `Custom` | - | dokumentiert |
| [slider](./slider/) | `base`, `number-input` | `einfach`, `bereich` | - | dokumentiert |
| [switch](./switch/) | `base` | `Standard`, `Round`, `Pill` | - | dokumentiert |
| [tags-input](./tags-input/) | `base`, `text-input` | `frei`, `vorschlag`, `nur-lesbar` | - | dokumentiert |
| [text-input](./text-input/) | `base` | `Standard`, `Floating Label`, `Underline` | - | dokumentiert |
| [textarea](./textarea/) | `base` | `fix`, `mitwachsend`, `chat` | - | dokumentiert |
| [time-picker](./time-picker/) | `base`, `date-input` | `liste`, `ziffernblatt` | `listbox` | dokumentiert |

## Siehe auch

- [Komponenten-Übersicht](../index.md)
- [Basiskomponente](../basics/base/)

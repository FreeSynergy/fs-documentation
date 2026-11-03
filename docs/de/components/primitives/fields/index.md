# fields (Felder)

Band [primitives](../) – nicht weiter zerlegbar.

Elemente zum Eingeben und Auswählen von Werten. Das Feld (`field`) hält dabei Beschriftung, Hilfetext und Fehlermeldung zusammen.

## Elemente

- [**checkbox**](./checkbox/) – Ein Checkbox ist ein Ja/Nein- oder Mehrfachauswahlfeld.
- [**color-input**](./color-input/) – Ein Color Input ist ein Farbauswahl-Feld mit Farbpicker.
- [**combobox**](./combobox/) – Ein Combobox ist ein Textfeld + Dropdown.
- [**date-input**](./date-input/) – Ein Date Input ist ein Datumsauswahl-Feld mit Kalender.
- [**field**](./field/) – Ein Field ist der Wrapper um ein Eingabefeld: Er verbindet Beschriftung, Hilfetext, Fehlermeldung und Pflicht-Markierung zu einer barrierefreien Einheit.
- [**input-group**](./input-group/) – Eine Input Group fügt ein Eingabefeld und die Teile, die unmittelbar dazugehören, zu einer zusammenhängenden Fläche zusammen: ein Vorsatz-Zeichen, eine Einheit, ein Dropdown für die Landesvorwahl oder eine Schaltfläche direkt am Feld.
- [**mention-input**](./mention-input/) – Ein Mention Input ist ein Textfeld mit Benutzer-/Kontakt-Erwähnung.
- [**number-input**](./number-input/) – Ein Number Input ist ein Eingabefeld für Zahlen.
- [**otp-input**](./otp-input/) – Das Einmalpasswortfeld nimmt einen kurzen numerischen Code auf — je Zeichen ein Feld.
- [**radio-group**](./radio-group/) – Eine Radio Group ist eine Gruppe von Optionsfeldern (einzelfach).
- [**rating**](./rating/) – Ein Rating ist eine Sterne- oder Punktebewertung.
- [**search-field**](./search-field/) – Ein Search Field ist ein Suchfeld mit Filtermöglichkeiten.
- [**select**](./select/) – Eine Auswahlliste: das Feld zeigt den gewählten Wert, die Optionen liegen hinter einem Klick.
- [**slider**](./slider/) – Ein Slider ist ein Wertebereich mit Schieberegler.
- [**switch**](./switch/) – Ein Switch ist ein Ein/Aus-Schalter (Toggle).
- [**tags-input**](./tags-input/) – Ein Tags Input ist eine Liste von Tags/Etiketten.
- [**text-input**](./text-input/) – Ein Text Input ist ein einzeiliges Eingabefeld für Text.
- [**textarea**](./textarea/) – Ein Textarea ist ein mehrzeiliges Eingabefeld für Text.

## Steckbriefe

| Komponente | Erbt von | Varianten | Rolle | Status |
|------------|----------|-----------|-------|--------|
| [checkbox](./checkbox/) | `base` | `Default`, `Toggle`, `Indeterminate` | - | dokumentiert |
| [color-input](./color-input/) | `base` | `palette`, `spectrum`, `code` | - | dokumentiert |
| [combobox](./combobox/) | `base`, `select` | `einzeln`, `freitext`, `mehrfach` | - | dokumentiert |
| [date-input](./date-input/) | `base` | `date`, `time`, `datetime` | - | dokumentiert |
| [field](./field/) | `base` | `vertikal`, `horizontal`, `inline` | - | dokumentiert |
| [input-group](./input-group/) | `base` | `praefix`, `suffix`, `aktion`, `auswahl` | `group` | dokumentiert |
| [mention-input](./mention-input/) | `base`, `text-input` | `feld`, `inline`, `mehrzeilig` | - | dokumentiert |
| [number-input](./number-input/) | `base` | `einfach`, `stepper`, `formatiert` | - | dokumentiert |
| [otp-input](./otp-input/) | `base`, `text-input` | `einzelboxen`, `block` | `group` | dokumentiert |
| [radio-group](./radio-group/) | `base` | `einzeln`, `toggle`, `karte` | - | dokumentiert |
| [rating](./rating/) | `base` | `Star Rating`, `Heart Rating`, `Number Rating` | - | dokumentiert |
| [search-field](./search-field/) | `base`, `text-input` | `Simple`, `Filter`, `Auto-complete` | - | dokumentiert |
| [select](./select/) | `base` | `Simple`, `Multi-select`, `Searchable`, `Custom` | - | dokumentiert |
| [slider](./slider/) | `base`, `number-input` | `einfach`, `bereich` | - | dokumentiert |
| [switch](./switch/) | `base` | `Standard`, `Round`, `Pill` | - | dokumentiert |
| [tags-input](./tags-input/) | `base`, `text-input` | `frei`, `vorschlag`, `nur-lesbar` | - | dokumentiert |
| [text-input](./text-input/) | `base` | `Standard`, `Floating Label`, `Underline` | - | dokumentiert |
| [textarea](./textarea/) | `base` | `fix`, `mitwachsend`, `chat` | - | dokumentiert |

## Siehe auch

- [Komponenten-Übersicht](../../index.md)
- [Band primitives](../)
- [Basiskomponente](../basics/base.md)

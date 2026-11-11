# fields (Felder)

Band [primitives](../) – nicht weiter zerlegbar.

Elemente zum Eingeben und Auswählen von Werten. Das Feld (`field`) hält dabei Beschriftung, Hilfetext und Fehlermeldung zusammen.

## Elemente

- [**checkbox**](./checkbox/) – Eine Checkbox ist ein Ja/Nein- oder Mehrfachauswahl-Feld.
- [**color-input**](./color-input/) – Ein Farbfeld ist ein Feld zur Farbauswahl mit einem Farbwähler.
- [**combobox**](./combobox/) – Eine Combobox ist ein Textfeld plus eine Auswahlliste.
- [**date-input**](./date-input/) – Ein Datumsfeld ist ein Feld zur Datumsauswahl mit einem Kalender.
- [**field**](./field/) – Ein Field ist der Wrapper um ein Eingabefeld.
- [**input-group**](./input-group/) – Eine Input Group verbindet ein Eingabefeld mit den Teilen, die direkt dazugehören, zu einer zusammenhängenden Fläche.
- [**mention-input**](./mention-input/) – Ein Mention Input ist ein Textfeld mit Erwähnungen von Benutzern oder Kontakten.
- [**number-input**](./number-input/) – Ein Number Input ist ein Eingabefeld für Zahlen.
- [**otp-input**](./otp-input/) – Das Feld für ein Einmalpasswort nimmt einen kurzen numerischen Code entgegen.
- [**radio-group**](./radio-group/) – Eine Radio Group ist eine Gruppe von Optionsfeldern (Einfachauswahl).
- [**rating**](./rating/) – Eine Bewertung ist eine Beurteilung mit Sternen oder Punkten.
- [**search-field**](./search-field/) – Ein Search Field ist ein Suchfeld mit Filtermöglichkeiten.
- [**select**](./select/) – Eine Auswahlliste: das Feld zeigt den gewählten Wert, die Optionen liegen hinter einem Klick.
- [**slider**](./slider/) – Ein Slider ist ein Wertebereich mit einem verschiebbaren Regler.
- [**switch**](./switch/) – Ein Switch ist ein Ein-/Aus-Schalter (Toggle).
- [**tags-input**](./tags-input/) – Ein Tags Input ist eine Liste aus Tags/Labels.
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
| [rating](./rating/) | `base` | `Sternbewertung`, `Herzbewertung`, `Zahlenbewertung` | - | dokumentiert |
| [search-field](./search-field/) | `base`, `text-input` | `simple`, `filter`, `auto-complete` | - | dokumentiert |
| [select](./select/) | `base` | `simple`, `multi-select`, `searchable`, `custom` | - | dokumentiert |
| [slider](./slider/) | `base`, `number-input` | `einfach`, `bereich` | - | dokumentiert |
| [switch](./switch/) | `base` | `standard`, `round`, `pill` | - | dokumentiert |
| [tags-input](./tags-input/) | `base`, `text-input` | `frei`, `vorschlag`, `nur-lesbar` | - | dokumentiert |
| [text-input](./text-input/) | `base` | `standard`, `floating label`, `underline` | - | dokumentiert |
| [textarea](./textarea/) | `base` | `fix`, `mitwachsend`, `chat` | - | dokumentiert |

## Siehe auch

- [Komponenten-Übersicht](../../index.md)
- [Band primitives](../)
- [Basiskomponente](../basics/base.md)

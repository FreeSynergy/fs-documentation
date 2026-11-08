# fields

Band [primitives](../) – lässt sich nicht weiter aufteilen.

Elemente zum Eingeben und Auswählen von Werten. Das Feld (`field`) hält Label, Hilfetext und Fehlermeldung zusammen.

## Elemente

- [**checkbox**](./checkbox/) – Eine Checkbox ist ein Ja/Nein- oder Mehrfachauswahl-Feld.
- [**color-input**](./color-input/) – Ein Farbfeld ist ein Feld zur Farbauswahl mit einem Farbwähler.
- [**combobox**](./combobox/) – Eine Combobox ist ein Textfeld mit einer Auswahlliste.
- [**date-input**](./date-input/) – Ein Datumsfeld ist ein Feld zur Datumsauswahl mit einem Kalender.
- [**field**](./field/) – Ein Feld ist die Hülle um ein Eingabefeld: Es verbindet Label, Hilfetext, Fehlermeldung und Pflichtmarkierung zu einer zugänglichen Einheit.
- [**input-group**](./input-group/) – Eine Eingabegruppe verbindet ein Eingabefeld und die Teile, die direkt dazugehören, zu einer zusammenhängenden Fläche: ein Präfixzeichen, eine Einheit, eine Auswahlliste für die Ländervorwahl oder ein Button direkt am Feld.
- [**mention-input**](./mention-input/) – Ein Mention-Feld ist ein Textfeld mit Erwähnungen von Benutzern oder Kontakten.
- [**number-input**](./number-input/) – Ein Zahlenfeld ist ein Eingabefeld für Zahlen.
- [**otp-input**](./otp-input/) – Das Einmalpasswort-Feld nimmt einen kurzen numerischen Code auf – ein Feld pro Zeichen.
- [**radio-group**](./radio-group/) – Eine Radio-Gruppe ist eine Gruppe von Optionsfeldern (Einfachauswahl).
- [**rating**](./rating/) – Eine Bewertung ist eine Stern- oder Punktebewertung.
- [**search-field**](./search-field/) – Ein Suchfeld ist ein Suchkasten mit Filteroptionen.
- [**select**](./select/) – Eine Auswahlliste: Das Feld zeigt den gewählten Wert, die Optionen liegen hinter einem Klick.
- [**slider**](./slider/) – Ein Schieberegler ist ein Wertebereich mit einem verschiebbaren Regler.
- [**switch**](./switch/) – Ein Schalter ist ein Ein-/Aus-Schalter (Toggle).
- [**tags-input**](./tags-input/) – Ein Tag-Feld ist eine Liste von Tags/Labels.
- [**text-input**](./text-input/) – Ein Texteingabefeld ist ein einzeiliges Eingabefeld für Text.
- [**textarea**](./textarea/) – Ein Textbereich ist ein mehrzeiliges Eingabefeld für Text.

## Profile

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
| [rating](./rating/) | `base` | `star rating`, `heart rating`, `number rating` | - | dokumentiert |
| [search-field](./search-field/) | `base`, `text-input` | `simple`, `filter`, `auto-complete` | - | dokumentiert |
| [select](./select/) | `base` | `simple`, `multi-select`, `searchable`, `custom` | - | dokumentiert |
| [slider](./slider/) | `base`, `number-input` | `einfach`, `bereich` | - | dokumentiert |
| [switch](./switch/) | `base` | `standard`, `round`, `pill` | - | dokumentiert |
| [tags-input](./tags-input/) | `base`, `text-input` | `frei`, `vorschlag`, `nur-lesbar` | - | dokumentiert |
| [text-input](./text-input/) | `base` | `standard`, `floating label`, `underline` | - | dokumentiert |
| [textarea](./textarea/) | `base` | `fix`, `mitwachsend`, `chat` | - | dokumentiert |

## Siehe auch

- [Komponentenübersicht](../../index.md)
- [Band Primitives](../)
- [Basiskomponente](../basics/base.md)

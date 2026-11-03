# fields

Band [primitives](../) – cannot be broken down further.

Elements for entering and choosing values. The field (`field`) holds the label,
help text and error message together.

## Elements

- [**checkbox**](./checkbox/) – a checkbox is a yes/no or multiple-choice field.
- [**color-input**](./color-input/) – a color input is a colour selection field with a colour picker.
- [**combobox**](./combobox/) – a combobox is a text field plus a dropdown.
- [**date-input**](./date-input/) – a date input is a date selection field with a calendar.
- [**field**](./field/) – a field is the wrapper around an input field: it joins label, help text, error message and required marking into one accessible unit.
- [**input-group**](./input-group/) – an input group joins an input field and the parts that immediately belong to it into one connected surface: a prefix character, a unit, a dropdown for the country code, or a button directly on the field.
- [**mention-input**](./mention-input/) – a mention input is a text field with user/contact mentions.
- [**number-input**](./number-input/) – a number input is an input field for numbers.
- [**otp-input**](./otp-input/) – the one-time-password field takes a short numeric code – one field per character.
- [**radio-group**](./radio-group/) – a radio group is a group of radio buttons (single choice).
- [**rating**](./rating/) – a rating is a star or point evaluation.
- [**search-field**](./search-field/) – a search field is a search box with filter options.
- [**select**](./select/) – a selection list: the field shows the chosen value, the options sit behind a click.
- [**slider**](./slider/) – a slider is a value range with a sliding control.
- [**switch**](./switch/) – a switch is an on/off toggle.
- [**tags-input**](./tags-input/) – a tags input is a list of tags/labels.
- [**text-input**](./text-input/) – a text input is a single-line input field for text.
- [**textarea**](./textarea/) – a textarea is a multi-line input field for text.

## Profiles

| Component | Inherits from | Variants | Role | Status |
|-----------|---------------|----------|------|--------|
| [checkbox](./checkbox/) | `base` | `Default`, `Toggle`, `Indeterminate` | - | documented |
| [color-input](./color-input/) | `base` | `palette`, `spectrum`, `code` | - | documented |
| [combobox](./combobox/) | `base`, `select` | `einzeln`, `freitext`, `mehrfach` | - | documented |
| [date-input](./date-input/) | `base` | `date`, `time`, `datetime` | - | documented |
| [field](./field/) | `base` | `vertikal`, `horizontal`, `inline` | - | documented |
| [input-group](./input-group/) | `base` | `praefix`, `suffix`, `aktion`, `auswahl` | `group` | documented |
| [mention-input](./mention-input/) | `base`, `text-input` | `feld`, `inline`, `mehrzeilig` | - | documented |
| [number-input](./number-input/) | `base` | `einfach`, `stepper`, `formatiert` | - | documented |
| [otp-input](./otp-input/) | `base`, `text-input` | `einzelboxen`, `block` | `group` | documented |
| [radio-group](./radio-group/) | `base` | `einzeln`, `toggle`, `karte` | - | documented |
| [rating](./rating/) | `base` | `star rating`, `heart rating`, `number rating` | - | documented |
| [search-field](./search-field/) | `base`, `text-input` | `simple`, `filter`, `auto-complete` | - | documented |
| [select](./select/) | `base` | `simple`, `multi-select`, `searchable`, `custom` | - | documented |
| [slider](./slider/) | `base`, `number-input` | `einfach`, `bereich` | - | documented |
| [switch](./switch/) | `base` | `standard`, `round`, `pill` | - | documented |
| [tags-input](./tags-input/) | `base`, `text-input` | `frei`, `vorschlag`, `nur-lesbar` | - | documented |
| [text-input](./text-input/) | `base` | `standard`, `floating label`, `underline` | - | documented |
| [textarea](./textarea/) | `base` | `fix`, `mitwachsend`, `chat` | - | documented |

## See also

- [Component overview](../../index.md)
- [Band primitives](../)
- [Base component](../basics/base.md)

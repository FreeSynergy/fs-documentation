# Text Input (Einzeiliges Textfeld) - Verwendung

Umsetzung in Blinc: `cn::input(&data)` aus `blinc_cn`, ein thematisierter
Wrapper um `TextInput` aus `blinc_layout`. Der Text liegt in einem
`SharedTextInputData`-Handle, das die App hält; das Feld liest und schreibt
daran.

```rust
use blinc_cn::prelude::*;
use blinc_layout::widgets::text_input::text_input_data;

let name = text_input_data();

cn::input(&name)
    .label("Name")
    .placeholder("Max Mustermann")
```

## Typen

Die ganze `type`-Liste ist **eine** Komponente; der Typ ist ein Builder-Aufruf,
kein eigener Baustein. `InputType` kommt aus `blinc_layout`:

```rust
use blinc_layout::widgets::text_input::InputType;

cn::input(&email).input_type(InputType::Email).placeholder("name@example.com");
cn::input(&site).input_type(InputType::Url);
cn::input(&tel).input_type(InputType::Tel);
cn::input(&age).input_type(InputType::Number);
cn::input(&count).input_type(InputType::Integer);
cn::input(&query).input_type(InputType::Search);
cn::input(&secret).password();          // maskiert, ohne InputType
```

`InputType::{Text, Number, Integer, Email, Password, Url, Tel, Search}`. Die
Maskierung setzt `password()`, unabhängig von `InputType::Password`.

## Beschriftung, Hilfe, Fehler

Das Feld selbst ist die Eingabezeile. Beschriftung, Hilfetext und Fehlerzeile
kommen vom Builder – so wird `field` in Blinc realisiert, ohne zusätzlichen
Wrapper:

```rust
cn::input(&email)
    .label("E-Mail")
    .required()
    .description("Wir geben sie nie weiter")
    .error(email_error)                  // String, Signal oder Computed
```

Ist die Fehlermeldung nicht leer, verdrängt sie den Hilfetext und markiert das
Feld mit `data-invalid`. Alle drei folgen Signals und wechseln an Ort und Stelle.

## Größe, Breite, Form

```rust
use blinc_cn::components::InputSize;

cn::input(&name)
    .size(InputSize::Small)              // Small 32px, Medium 40px, Large 48px
    .w(240.0)
    .w_full()
    .rounded(6.0)
    .border_width(1.0);
```

## Auf Eingabe reagieren

```rust
cn::input(&query).on_change(|value: &str| {
    // Liste beim Tippen filtern
});
```

Von der App-Seite lesen und setzen über das Handle:

```rust
let data = text_input_data();
cn::input(&data).bind(&input_ref);       // Fokus, Auswahl, gesetzter Wert
```

## Zustände

`disabled` nimmt bool, Signal oder Computed, das Feld folgt also dem
Formularzustand:

```rust
cn::input(&name).disabled(locked);       // locked: Signal<bool>
```

## Aussehen

Das Feld trägt die Klasse `cn-input` und je nach Größe `cn-input--sm|md|lg`.
Hover, Fokus, ungültig und deaktiviert sind CSS-Regeln (`:hover`, `:focus`,
`[data-invalid]`, `:disabled`), durch eine `transition` weichgezogen – nach
eigenen Regeln umbiegen statt über Setter:

```css
.my-field:focus { border-color: #16a34a; outline-color: #16a34a; }
```

```rust
cn::input(&name).class("my-field");
```

Idle-Farben sind Setter (`idle_bg_color`, `idle_border_color`, `text_color`,
`placeholder_color`, `cursor_color`, `selection_color`).

## In Blinc noch nicht vorhanden

- Varianten `floating label` und `underline`: kein Setter. Entweder eine
  CSS-Regel auf `cn-input` oder eine eigene Komponente.
- Prefix/Suffix-Icon und angesetzte Buttons: zusammen mit
  [input-group](../input-group/); dafür hat Blinc kein Gegenstück.

## Siehe auch

- [field](../field/) — Beschriftung, Hilfe und Fehler als eigene Komponente
- [input-group](../input-group/) — Vorsilbe, Einheit, angesetzter Button
- [Basiskomponente](../../basics/base.md)

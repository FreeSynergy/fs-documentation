# Text Input - Usage

Blinc implementation: `cn::input(&data)` from `blinc_cn`, a themed wrapper
around `blinc_layout`'s `TextInput`. The text lives in a
`SharedTextInputData` handle the app owns and the field reads and writes.

```rust
use blinc_cn::prelude::*;
use blinc_layout::widgets::text_input::text_input_data;

let name = text_input_data();

cn::input(&name)
    .label("Name")
    .placeholder("John Doe")
```

## Types

One component covers the whole `type` list; the type is a builder call, not a
separate component. `InputType` comes from `blinc_layout`:

```rust
use blinc_layout::widgets::text_input::InputType;

cn::input(&email).input_type(InputType::Email).placeholder("name@example.com");
cn::input(&site).input_type(InputType::Url);
cn::input(&tel).input_type(InputType::Tel);
cn::input(&age).input_type(InputType::Number);
cn::input(&count).input_type(InputType::Integer);
cn::input(&query).input_type(InputType::Search);
cn::input(&secret).password();          // masked, no InputType needed
```

`InputType::{Text, Number, Integer, Email, Password, Url, Tel, Search}`. The
masked `password()` setter is separate from `InputType::Password` and is what
hides the characters.

## Label, help and error

The field itself is the line. Label, help text and the error line come from the
builder, which is how [field](../field/) is realised in Blinc — no extra
wrapper element is needed for the common case:

```rust
cn::input(&email)
    .label("Email")
    .required()
    .description("We never share it")
    .error(email_error)                  // a string, Signal or Computed
```

While the error is non-empty it replaces the description and marks the box
`data-invalid`. All three follow signals, so they change in place without a
rebuild.

## Size, width, shape

```rust
use blinc_cn::components::InputSize;

cn::input(&name)
    .size(InputSize::Small)              // Small 32px, Medium 40px, Large 48px
    .w(240.0)
    .w_full()
    .rounded(6.0)
    .border_width(1.0);
```

## Reacting to input

```rust
cn::input(&query).on_change(|value: &str| {
    // filter the list as the user types
});
```

To read or set the text from the app side, use the handle:

```rust
let data = text_input_data();
cn::input(&data).bind(&input_ref);       // focus, selection, programmatic access
```

## States

`disabled` takes a bool, Signal or Computed, so the field can follow form state
reactively:

```rust
cn::input(&name).disabled(locked);       // locked: Signal<bool>
```

## Look

The field carries the class `cn-input`, plus `cn-input--sm|md|lg` for the size.
Hover, focus, invalid and disabled are CSS rules (`:hover`, `:focus`,
`[data-invalid]`, `:disabled`) eased by a `transition` — restyle them with
rules of your own rather than with setters:

```css
.my-field:focus { border-color: #16a34a; outline-color: #16a34a; }
```

```rust
cn::input(&name).class("my-field");
```

Only the idle colours are setters (`idle_bg_color`, `idle_border_color`,
`text_color`, `placeholder_color`, `cursor_color`, `selection_color`).

## Not in Blinc yet

- `floating label` and `underline` variants: no setter. Either a CSS rule on
  `cn-input` or a component of our own.
- Prefix/suffix icons and attached buttons: combine with
  [input-group](../input-group/), which Blinc has no equivalent for.

## See also

- [field](../field/) — label, help and error as their own component
- [input-group](../input-group/) — prefix, unit, attached button
- [Base component](../../basics/base.md)

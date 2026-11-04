# Blinc Components (`cn::`)

Bilingual quick reference for the component primitives in `blinc_cn`
(`cn::…`) and, where noted, `blinc_layout`. Each entry gives the create
call, its parameters, and the main companion helpers. Signatures follow the
Blinc source in the research clone (`.research-blinc/`).

---

### text-input

#### English
A single-line text field bound to shared input state. The state handle owns the value, cursor, placeholder and validation, so the field survives rebuilds and can be read or written from anywhere.

**Create:**
    cn::input(data)

| Parameter | Type | Description |
|-----------|------|-------------|
| `data` | `&SharedTextInputData` | Handle to the shared input state (`Arc<Mutex<TextInputData>>`); create it with `text_input_data()` or `text_input_data_with_placeholder(placeholder)`. |

Common builder methods: `.class(name)`, `.id(id)`, `.size(InputSize)` (`Small`/`Medium`/`Large`), `.label(text)`, `.error(text)`, `.required()`, `.disabled(flag)`, `.password()`, `.input_type(InputType)` (`Text`, `Number`, `Integer`, `Email`, `Password`, `Url`, `Tel`, `Search`), `.bind(input_ref)`, `.w(width)`, `.w_full()`, `.rounded(radius)`, `.border_width(width)`, `.idle_border_color(color)`, `.idle_bg_color(color)`, `.text_color(color)`, `.placeholder_color(color)`, `.cursor_color(color)`, `.selection_color(color)`.

#### Deutsch
Ein einzeiliges Textfeld, das an einen gemeinsamen Eingabe-State gebunden ist. Der State-Handle hält Wert, Cursor, Platzhalter und Validierung, sodass das Feld Neuaufbauten übersteht und überall gelesen und geschrieben werden kann.

**Create:**
    cn::input(data)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `data` | `&SharedTextInputData` | Handle auf den gemeinsamen Eingabe-State (`Arc<Mutex<TextInputData>>`); erzeugt mit `text_input_data()` oder `text_input_data_with_placeholder(Platzhalter)`. |

Häufige Builder-Methoden: `.class(name)`, `.id(id)`, `.size(InputSize)` (`Small`/`Medium`/`Large`), `.label(text)`, `.error(text)`, `.required()`, `.disabled(flag)`, `.password()`, `.input_type(InputType)` (`Text`, `Number`, `Integer`, `Email`, `Password`, `Url`, `Tel`, `Search`), `.bind(input_ref)`, `.w(width)`, `.w_full()`, `.rounded(radius)`, `.border_width(width)`, `.idle_border_color(color)`, `.idle_bg_color(color)`, `.text_color(color)`, `.placeholder_color(color)`, `.cursor_color(color)`, `.selection_color(color)`.

---

### textarea

#### English
A multi-line text field bound to shared text-area state, with row/column sizing, optional wrapping and the same field affordances as `cn::input` (label, error, required).

**Create:**
    cn::textarea(state)

| Parameter | Type | Description |
|-----------|------|-------------|
| `state` | `&SharedTextAreaState` | Handle to the shared area state (`Arc<Mutex<TextAreaState>>`); create it with `text_area_state()` or `text_area_state_with_placeholder(placeholder)`. |

Common builder methods: `.class(name)`, `.id(id)`, `.size(TextareaSize)` (`Small`/`Medium`/`Large`), `.rows(n)`, `.cols(n)`, `.max_length(max)`, `.wrap(flag)` / `.no_wrap()`, `.label(text)`, `.error(text)`, `.required()`, `.disabled(flag)`, `.bind(textarea_ref)`, `.w(width)`, `.h(height)`, `.w_full()`, `.border_width(width)`, `.rounded(radius)`.

#### Deutsch
Ein mehrzeiliges Textfeld mit gemeinsamem TextArea-State, inklusive Zeilen-/Spaltengröße, optionalem Zeilenumbruch und denselben Feld-Features wie `cn::input` (Label, Fehler, Pflichtfeld).

**Create:**
    cn::textarea(state)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `state` | `&SharedTextAreaState` | Handle auf den gemeinsamen TextArea-State (`Arc<Mutex<TextAreaState>>`); erzeugt mit `text_area_state()` oder `text_area_state_with_placeholder(Platzhalter)`. |

Häufige Builder-Methoden: `.class(name)`, `.id(id)`, `.size(TextareaSize)` (`Small`/`Medium`/`Large`), `.rows(n)`, `.cols(n)`, `.max_length(max)`, `.wrap(flag)` / `.no_wrap()`, `.label(text)`, `.error(text)`, `.required()`, `.disabled(flag)`, `.bind(textarea_ref)`, `.w(width)`, `.h(height)`, `.w_full()`, `.border_width(width)`, `.rounded(radius)`.

---

### number-input

#### English
A numeric field bound directly to a reactive `Signal<f64>`, with min/max clamping, stepping and keyboard increments (↑/↓, +/−). No separate shared-state handle is needed — the signal is the value.

**Create:**
    cn::number_input(state)

| Parameter | Type | Description |
|-----------|------|-------------|
| `state` | `Signal<f64>` | Reactive value the field shows and edits. |

Builder methods: `.min(min)`, `.max(max)`, `.step(step)`, `.precision(digits)`, `.size(InputSize)`, `.placeholder(text)`, `.disabled(flag)`, `.w(px)`, `.max_w(px)`, `.on_change(handler)`.

#### Deutsch
Ein Zahlenfeld, das direkt an einen reaktiven `Signal<f64>` gebunden ist, mit Min/Max-Begrenzung, Schrittweite und Tastatur-Inkrement (↑/↓, +/−). Kein separater Shared-State nötig — das Signal ist der Wert.

**Create:**
    cn::number_input(state)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `state` | `Signal<f64>` | Reaktiver Wert, den das Feld anzeigt und bearbeitet. |

Builder-Methoden: `.min(min)`, `.max(max)`, `.step(step)`, `.precision(digits)`, `.size(InputSize)`, `.placeholder(text)`, `.disabled(flag)`, `.w(px)`, `.max_w(px)`, `.on_change(handler)`.

---

### select

#### English
A dropdown for choosing one option from a list, bound to a reactive `Signal<String>` holding the selected value. Options are supplied as value/label pairs and can carry custom content or be individually disabled.

**Create:**
    cn::select(value)

| Parameter | Type | Description |
|-----------|------|-------------|
| `value` | `Signal<String>` | Reactive currently-selected value; updated when the user picks an option. |

Builder methods: `.option(value, label)`, `.option_disabled(value, label)`, `.options(vec)` (items of `SelectOption::new(value, label)` with `.content(f)` / `.disabled()`), `.placeholder(text)`, `.label(text)`, `.size(SelectSize)` (`Small`/`Medium`/`Large`), `.disabled(flag)`, `.w(width)`, `.virtual_rows(row_height)`, `.on_change(callback)`, `.with_key(key, value)` for keyed instances.

#### Deutsch
Ein Dropdown zur Auswahl genau einer Option aus einer Liste, gebunden an einen reaktiven `Signal<String>` mit dem gewählten Wert. Optionen werden als Wert/Beschriftung-Paare übergeben und können eigenen Inhalt tragen oder einzeln deaktiviert sein.

**Create:**
    cn::select(value)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `value` | `Signal<String>` | Reaktiv ausgewählter Wert; wird bei der Auswahl einer Option aktualisiert. |

Builder-Methoden: `.option(value, label)`, `.option_disabled(value, label)`, `.options(vec)` (Elemente aus `SelectOption::new(value, label)` mit `.content(f)` / `.disabled()`), `.placeholder(text)`, `.label(text)`, `.size(SelectSize)` (`Small`/`Medium`/`Large`), `.disabled(flag)`, `.w(width)`, `.virtual_rows(row_height)`, `.on_change(callback)`, `.with_key(key, value)` für schlüsselbasierte Instanzen.

---

### combobox

#### English
An editable input with a filtered dropdown list, bound to a `Signal<String>`. The user can search the options as they type, and `allow_custom` lets them enter a value that is not in the list.

**Create:**
    cn::combobox(value)

| Parameter | Type | Description |
|-----------|------|-------------|
| `value` | `Signal<String>` | Reactive current text/selection; updated on pick or typing. |

Builder methods: `.option(value, label)`, `.option_disabled(value, label)`, `.options(vec)` (items of `ComboboxOption::new(value, label)` with `.content(f)` / `.disabled()`), `.placeholder(text)`, `.label(text)`, `.size(ComboboxSize)` (`Small`/`Medium`/`Large`), `.allow_custom(flag)`, `.disabled(flag)`, `.w(width)`, `.on_change(callback)`, `.with_key(key, value)`.

#### Deutsch
Ein editierbares Eingabefeld mit gefiltertem Dropdown, gebunden an ein `Signal<String>`. Beim Tippen wird die Optionsliste durchsucht; mit `allow_custom` sind auch Werte außerhalb der Liste erlaubt.

**Create:**
    cn::combobox(value)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `value` | `Signal<String>` | Reaktiver aktueller Text/die aktuelle Auswahl; wird bei Auswahl oder Eingabe aktualisiert. |

Builder-Methoden: `.option(value, label)`, `.option_disabled(value, label)`, `.options(vec)` (Elemente aus `ComboboxOption::new(value, label)` mit `.content(f)` / `.disabled()`), `.placeholder(text)`, `.label(text)`, `.size(ComboboxSize)` (`Small`/`Medium`/`Large`), `.allow_custom(flag)`, `.disabled(flag)`, `.w(width)`, `.on_change(callback)`, `.with_key(key, value)`.

---

### checkbox

#### English
A two-state toggle box bound to a `Signal<bool>`, optionally with a clickable label next to the box.

**Create:**
    cn::checkbox(checked)

| Parameter | Type | Description |
|-----------|------|-------------|
| `checked` | `Signal<bool>` | Reactive checked state; flipped by user interaction. |

Builder methods: `.label(text)`, `.size(CheckboxSize)` (`Small` 14px / `Medium` 18px / `Large` 22px), `.disabled(flag)`, `.on_change(callback)`, `.with_key(key, checked)`, `.class(name)`, `.id(id)`.

#### Deutsch
Eine Zweizustands-Checkbox, gebunden an ein `Signal<bool>`, optional mit klickbarer Beschriftung neben der Box.

**Create:**
    cn::checkbox(checked)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `checked` | `Signal<bool>` | Reaktiver Häkchen-Zustand; wird durch Benutzeraktion geändert. |

Builder-Methoden: `.label(text)`, `.size(CheckboxSize)` (`Small` 14 px / `Medium` 18 px / `Large` 22 px), `.disabled(flag)`, `.on_change(callback)`, `.with_key(key, checked)`, `.class(name)`, `.id(id)`.

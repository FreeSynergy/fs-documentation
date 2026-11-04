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

---

### radio-group

#### English
A set of mutually exclusive options bound to a `Signal<String>` holding the selected value. Options are laid out vertically or horizontally and can be individually disabled.

**Create:**
    cn::radio_group(selected)

| Parameter | Type | Description |
|-----------|------|-------------|
| `selected` | `Signal<String>` | Reactive value of the chosen option; set to the option's value on click. |

Builder methods: `.option(value, label)`, `.option_disabled(value, label)`, `.size(RadioSize)` (`Small` 14px / `Medium` 18px / `Large` 22px), `.layout(RadioLayout)` / `.vertical()` / `.horizontal()`, `.label(text)`, `.gap(px)`, `.disabled(flag)`, `.on_change(callback)`, `.key(key)`, `.class(name)`, `.id(id)`.

#### Deutsch
Eine Menge sich gegenseitig ausschließender Optionen, gebunden an ein `Signal<String>` mit dem gewählten Wert. Optionen werden vertikal oder horizontal angeordnet und können einzeln deaktiviert werden.

**Create:**
    cn::radio_group(selected)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `selected` | `Signal<String>` | Reaktiver Wert der gewählten Option; wird beim Klick auf den Optionswert gesetzt. |

Builder-Methoden: `.option(value, label)`, `.option_disabled(value, label)`, `.size(RadioSize)` (`Small` 14 px / `Medium` 18 px / `Large` 22 px), `.layout(RadioLayout)` / `.vertical()` / `.horizontal()`, `.label(text)`, `.gap(px)`, `.disabled(flag)`, `.on_change(callback)`, `.key(key)`, `.class(name)`, `.id(id)`.

---

### switch

#### English
An on/off toggle rendered as a sliding thumb, bound to a `Signal<bool>`, with an optional label.

**Create:**
    cn::switch(on)

| Parameter | Type | Description |
|-----------|------|-------------|
| `on` | `Signal<bool>` | Reactive on state; flipped by user interaction. |

Builder methods: `.label(text)`, `.size(SwitchSize)` (`Small` 32×18 / `Medium` 44×24 / `Large` 52×28), `.disabled(flag)`, `.on_change(callback)`, `.class(name)`, `.id(id)`.

#### Deutsch
Ein Ein/Aus-Schalter als gleitender Griff, gebunden an ein `Signal<bool>`, optional mit Beschriftung.

**Create:**
    cn::switch(on)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `on` | `Signal<bool>` | Reaktiver An-Zustand; wird durch Benutzeraktion umgeschaltet. |

Builder-Methoden: `.label(text)`, `.size(SwitchSize)` (`Small` 32×18 / `Medium` 44×24 / `Large` 52×28), `.disabled(flag)`, `.on_change(callback)`, `.class(name)`, `.id(id)`.

---

### slider

#### English
A draggable track for picking a number in a range. It accepts a `NumberValue`, so the same field can be bound to a `Signal<f32>` or `Signal<f64>` without a lossy copy — a slider and a `number_input` can share one value.

**Create:**
    cn::slider(value)

| Parameter | Type | Description |
|-----------|------|-------------|
| `value` | `impl Into<NumberValue>` | Reactive number to edit — pass a `Signal<f32>` or `Signal<f64>`; both convert into `NumberValue`. |

Builder methods: `.min(min)`, `.max(max)`, `.step(step)`, `.size(SliderSize)` (`Small` track 3px/thumb 12px, `Medium` 4px/16px, `Large` 6px/22px), `.label(text)`, `.show_value()`, `.disabled(flag)`, `.w(width)`, `.class(name)`, `.on_change(callback)`, `.with_key(key, value)`.

#### Deutsch
Eine ziehbare Leiste zur Wahl einer Zahl in einem Bereich. Sie nimmt ein `NumberValue` an und kann deshalb wahlweise an ein `Signal<f32>` oder `Signal<f64>` gebunden werden — ohne verlustlose Kopie: Slider und `number_input` können denselben Wert teilen.

**Create:**
    cn::slider(value)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `value` | `impl Into<NumberValue>` | Reaktive Zahl; ein `Signal<f32>` oder `Signal<f64>` wird in ein `NumberValue` konvertiert. |

Builder-Methoden: `.min(min)`, `.max(max)`, `.step(step)`, `.size(SliderSize)` (`Small` Spur 3 px/Griff 12 px, `Medium` 4 px/16 px, `Large` 6 px/22 px), `.label(text)`, `.show_value()`, `.disabled(flag)`, `.w(width)`, `.class(name)`, `.on_change(callback)`, `.with_key(key, value)`.

---

### otp-input

#### English
A one-code-per-cell verification input of fixed length. Digits go into the cell under the caret, Backspace on an empty cell steps back, and `on_complete` fires once every cell is filled.

**Create:**
    cn::input_otp(value, length)

| Parameter | Type | Description |
|-----------|------|-------------|
| `value` | `Signal<String>` | Reactive string holding the whole code (read it when complete). |
| `length` | `usize` | Number of cells / maximum code length. |

Builder methods: `.numeric_only(flag)`, `.masked(flag)`, `.error(flag)`, `.size(InputSize)`, `.group_every(n)` (visual grouping, e.g. `3 3 2`), `.disabled(flag)`, `.on_change(handler)`, `.on_complete(handler)`.

#### Deutsch
Eine Bestätigungs-Eingabe mit fester Länge, ein Zeichen pro Feld. Zeichen landen im Feld an der Einfügemarke, Backspace im leeren Feld springt zurück, und `on_complete` feuert, sobald alle Felder gefüllt sind.

**Create:**
    cn::input_otp(value, length)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `value` | `Signal<String>` | Reaktiver String mit dem gesamten Code (bei Vollständigkeit auslesen). |
| `length` | `usize` | Anzahl der Felder bzw. maximale Codelänge. |

Builder-Methoden: `.numeric_only(flag)`, `.masked(flag)`, `.error(flag)`, `.size(InputSize)`, `.group_every(n)` (optische Gruppierung, z. B. `3 3 2`), `.disabled(flag)`, `.on_change(handler)`, `.on_complete(handler)`.

---

### field

#### English
No dedicated `field` component. A labelled form field is built by composing the field affordances on the input itself: `.label()` puts text above, `.description()` adds helper text below, `.error()` replaces that helper text with a message and marks the box invalid, and `.required()` flags it. Available on `cn::input`, `cn::textarea`, `cn::select`, `cn::combobox`, `cn::radio_group`, `cn::checkbox` and `cn::switch`.

**Create:**
    cn::input(data).label(name).description(hint).error(message).required()

| Parameter | Type | Description |
|-----------|------|-------------|
| `label` | `impl IntoReactive<String>` | Text rendered above the control. |
| `description` | `impl IntoReactive<String>` | Helper text below the control; a signal replaces it in place. |
| `error` | `impl IntoReactive<String>` | Message shown in place of the description while non-empty; also sets `data-invalid` on the box. An empty signal clears the error. |
| `required` | — | Marks the control as required (no argument). |

#### Deutsch
Keine eigene Komponente `field`. Ein beschriftetes Formularfeld entsteht durch die Kombination der Feld-Features am Eingabeelement selbst: `.label()` setzt Text darüber, `.description()` ergänzt Hilfetext darunter, `.error()` ersetzt den Hilfetext durch eine Meldung und markiert das Feld als ungültig, `.required()` kennzeichnet es als Pflichtfeld. Verfügbar bei `cn::input`, `cn::textarea`, `cn::select`, `cn::combobox`, `cn::radio_group`, `cn::checkbox` und `cn::switch`.

**Create:**
    cn::input(data).label(name).description(hint).error(message).required()

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `label` | `impl IntoReactive<String>` | Text oberhalb des Steuerelements. |
| `description` | `impl IntoReactive<String>` | Hilfetext unterhalb des Steuerelements; ein Signal ersetzt ihn vor Ort. |
| `error` | `impl IntoReactive<String>` | Meldung anstelle des Hilfetexts, solange sie nicht leer ist; setzt zusätzlich `data-invalid` am Feld. Ein leeres Signal löscht den Fehler. |
| `required` | — | Kennzeichnet das Steuerelement als Pflichtfeld (ohne Argument). |

---

### input-group

#### English
No direct Blinc equivalent. There is no `input_group` primitive; compose an input with adjacent buttons or icons by hand in a flex container (`.class("input-group")` plus your own border and radius on the wrapper), and drive the parts from the same `SharedTextInputData` / `InputRef`.

#### Deutsch
Kein direktes Blinc-Äquivalent. Es gibt kein Primitiv `input_group`; ein Eingabefeld mit angrenzenden Buttons oder Icons wird per Hand in einem Flex-Container zusammengesetzt (`.class("input-group")` mit eigenem Rand und Radius am umgebenden Element), die Teile werden aus demselben `SharedTextInputData` / `InputRef` gesteuert.

---

### search-field

#### English
No dedicated search component. Use a text input with `.input_type(InputType::Search)` for search affordances, or `cn::combobox(value)` when the query should filter and pick from a list.

**Create:**
    cn::input(data).input_type(InputType::Search)

| Parameter | Type | Description |
|-----------|------|-------------|
| `data` | `&SharedTextInputData` | Shared input state; set `constraints` on it to limit query length. |

#### Deutsch
Keine eigene Such-Komponente. Ein Textfeld mit `.input_type(InputType::Search)` liefert die Such-Features, `cn::combobox(value)` passt, wenn die Eingabe eine Liste filtern und daraus auswählen soll.

**Create:**
    cn::input(data).input_type(InputType::Search)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `data` | `&SharedTextInputData` | Gemeinsamer Eingabe-State; über `constraints` lässt sich die Abfragelänge begrenzen. |

---

### tags-input

#### English
No direct Blinc equivalent. There is no chip/tag input primitive. Closest workaround: keep the tags in your own `Vec<String>` state and render each tag as a `cn::badge` with a remove button next to a `cn::input` that appends on Enter (`.on_change` plus the input's submit hook).

#### Deutsch
Kein direktes Blinc-Äquivalent. Es gibt kein Chip-/Tag-Eingabeprimitiv. Nächste Lösung: Tags im eigenen `Vec<String>`-State halten, jedes Tag als `cn::badge` mit Entf-Button neben einem `cn::input` rendern, der bei Enter anhängt (`.on_change` plus Submit-Hook des Feldes).

---

### rating

#### English
No direct Blinc equivalent. There is no star-rating primitive. Closest workaround: a `cn::radio_group` with one option per star and star icons as the option content, or a `cn::slider(value).min(1.0).max(5.0).step(1.0)` for a compact continuous rating.

#### Deutsch
Kein direktes Blinc-Äquivalent. Es gibt kein Sternbewertungs-Primitiv. Nächste Lösung: ein `cn::radio_group` mit einer Option je Stern und Stern-Icons als Optionsinhalt, oder `cn::slider(value).min(1.0).max(5.0).step(1.0)` für eine kompakte durchgehende Bewertung.

---

### color-input

#### English
No direct Blinc equivalent. There is no color picker or swatch input. Closest workaround: a `cn::input` bound to a hex string plus `InputConstraints`/a pattern for validation, with a `cn::icon` or a plain div whose background is set from the value.

#### Deutsch
Kein direktes Blinc-Äquivalent. Es gibt keinen Farbwähler und keine Farbpalette. Nächste Lösung: ein `cn::input` an einem Hex-String mit `InputConstraints`/Pattern zur Validierung, dazu ein `cn::icon` oder ein Div, dessen Hintergrund aus dem Wert gesetzt wird.

---

### mention-input

#### English
No direct Blinc equivalent. There is no mention/@-input. Closest workaround: `blinc_layout::widgets::rich_text_editor` for the rich text part plus your own overlay (`cn::popover` or `cn::dropdown_menu`) opened when `@` is typed; the plain `cn::input` cannot render inline entities.

#### Deutsch
Kein direktes Blinc-Äquivalent. Es gibt keine Mention-/@-Eingabe. Nächste Lösung: `blinc_layout::widgets::rich_text_editor` für den Rich-Text-Teil plus ein eigenes Overlay (`cn::popover` oder `cn::dropdown_menu`), das bei Eingabe von `@` geöffnet wird; das einfache `cn::input` kann keine Inline-Entitäten darstellen.

---

### date-input

#### English
No standalone date-field widget; Blinc's date picker is `cn::calendar` — a month grid whose selected day is held in a `Signal<Option<CalendarDay>>`. Pair it with a `cn::input` (or a popover trigger) if you also need a typed text representation.

**Create:**
    cn::calendar(value)

| Parameter | Type | Description |
|-----------|------|-------------|
| `value` | `Signal<Option<CalendarDay>>` | Reactive selected date (`CalendarDay::new(year, month, day)` or `CalendarDay::today()`); `None` means nothing selected. |

Builder methods: `.today(day)` (what counts as today), `.week_start(weekday)` (0 = Sunday), `.min_year(year)`, `.max_year(year)`, `.events(events)` (`impl IntoReactive<Vec<CalendarEvent>>`; `CalendarEvent::new(day, title).kind(k).icon(svg)`), `.on_change(callback)`, `.class(name)`, `.id(id)`.

#### Deutsch
Kein eigenständiges Datumsfeld; Blincs Datumsauswahl ist `cn::calendar` — ein Monatsraster, dessen gewählter Tag in einem `Signal<Option<CalendarDay>>` liegt. Für eine getippte Textdarstellung mit einem `cn::input` (oder Popover-Trigger) kombinieren.

**Create:**
    cn::calendar(value)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `value` | `Signal<Option<CalendarDay>>` | Reaktives gewähltes Datum (`CalendarDay::new(Jahr, Monat, Tag)` oder `CalendarDay::today()`); `None` = nichts ausgewählt. |

Builder-Methoden: `.today(day)` (was als heute gilt), `.week_start(weekday)` (0 = Sonntag), `.min_year(year)`, `.max_year(year)`, `.events(events)` (`impl IntoReactive<Vec<CalendarEvent>>`; `CalendarEvent::new(day, titel).kind(k).icon(svg)`), `.on_change(callback)`, `.class(name)`, `.id(id)`.

---

### label

#### English
A caption for a control or a group of controls. The text may be a plain string or a signal that updates it in place; `required()` appends the required marker.

**Create:**
    cn::label(text)

| Parameter | Type | Description |
|-----------|------|-------------|
| `text` | `impl IntoReactive<String>` | Caption — a string or a `Signal<String>` followed in place. |

Builder methods: `.size(LabelSize)` (`Small` 12px / `Medium` 14px / `Large` 16px), `.required()`, `.disabled(flag)`, `.class(name)`, `.id(id)`.

#### Deutsch
Eine Beschriftung für ein Steuerelement oder eine Steuerelementgruppe. Der Text kann ein String oder ein Signal sein, das ihn vor Ort aktualisiert; `.required()` ergänzt die Pflichtfeld-Markierung.

**Create:**
    cn::label(text)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `text` | `impl IntoReactive<String>` | Beschriftung — ein String oder ein `Signal<String>`, das vor Ort verfolgt wird. |

Builder-Methoden: `.size(LabelSize)` (`Small` 12 px / `Medium` 14 px / `Large` 16 px), `.required()`, `.disabled(flag)`, `.class(name)`, `.id(id)`.

---

### kbd

#### English
A key-cap styled inline label for keyboard shortcuts, e.g. `Ctrl` `K`.

**Create:**
    cn::kbd(text)

| Parameter | Type | Description |
|-----------|------|-------------|
| `text` | `impl IntoReactive<String>` | The key or shortcut to show. |

Builder methods: `.size(KbdSize)` (`Small` 10px / `Medium` 12px / `Large` 14px text), `.class(name)`, `.id(id)`.

#### Deutsch
Eine wie eine Taste gestaltete Inline-Beschriftung für Tastaturkürzel, z. B. `Ctrl` `K`.

**Create:**
    cn::kbd(text)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `text` | `impl IntoReactive<String>` | Anzuzeigende Taste bzw. Kombination. |

Builder-Methoden: `.size(KbdSize)` (`Small` 10 px / `Medium` 12 px / `Large` 14 px Text), `.class(name)`, `.id(id)`.

---

### separator

#### English
A thin dividing line, horizontal by default, used to group content.

**Create:**
    cn::separator()

No parameters. Call `.vertical()` or `.horizontal()` for the orientation (`SeparatorOrientation`). Sizing and colour: `.w(width)`, `.h(height)`, `.m/mx/my/mt/mb/ml/mr(margin)`, `.bg(color)`, `.opacity(value)`, `.class(name)`, `.id(id)`.

#### Deutsch
Eine dünne Trennlinie, standardmäßig waagerecht, zur Gruppierung von Inhalt.

**Create:**
    cn::separator()

Keine Parameter. Ausrichtung mit `.vertical()` oder `.horizontal()` (`SeparatorOrientation`). Größe und Farbe: `.w(width)`, `.h(height)`, `.m/mx/my/mt/mb/ml/mr(margin)`, `.bg(color)`, `.opacity(value)`, `.class(name)`, `.id(id)`.

---

### link

#### English
A clickable hyperlink that opens a URL. Lives in `blinc_layout`, not `cn::`, and is also reachable through the `open_url(url)` free function when you only need the navigation.

**Create:**
    blinc_layout::widgets::link::link(label, url)

| Parameter | Type | Description |
|-----------|------|-------------|
| `label` | `impl Into<String>` | Visible link text. |
| `url` | `impl Into<String>` | Target URL opened on click. |

Builder methods: `.on_click(handler)` (replaces the default open behaviour), `.text_color(color)`, `.font_size(size)`, `.underline(flag)` / `.no_underline()` / `.underline_on_hover()`, `.class(name)`, `.id(id)`.

#### Deutsch
Ein anklickbarer Hyperlink, der eine URL öffnet. Er liegt in `blinc_layout`, nicht in `cn::`, und ist über die freie Funktion `open_url(url)` erreichbar, wenn nur die Navigation gebraucht wird.

**Create:**
    blinc_layout::widgets::link::link(label, url)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `label` | `impl Into<String>` | Sichtbarer Linktext. |
| `url` | `impl Into<String>` | Ziel-URL, die beim Klick geöffnet wird. |

Builder-Methoden: `.on_click(handler)` (ersetzt das Standardverhalten), `.text_color(color)`, `.font_size(size)`, `.underline(flag)` / `.no_underline()` / `.underline_on_hover()`, `.class(name)`, `.id(id)`.

---

### button

#### English
The standard action button, with six visual variants, a size ladder (including icon-only and custom dimensions), an optional leading or trailing icon, and a click handler.

**Create:**
    cn::button(label)

| Parameter | Type | Description |
|-----------|------|-------------|
| `label` | `impl IntoReactive<String>` | Button text — a string or a `Signal<String>` followed in place. |

Builder methods: `.variant(ButtonVariant)` (`Primary` default, `Secondary`, `Destructive`, `Outline`, `Ghost`, `Link`), `.size(ButtonSize)` (`Small`/`Medium` default/`Large`, `Icon` for square icon-only, `Custom(width, height)`), `.icon(svg_markup)`, `.icon_position(IconPosition)` (`Start`/`End`), `.icon_size(px)`, `.color(color)`, `.disabled(flag)`, `.on_click(handler)`, `.with_key(key, label)`, `.class(name)`, `.id(id)`.

#### Deutsch
Der Standard-Aktionsbutton mit sechsoptischen Varianten, einer Größentreppe (inkl. nur-Icon und eigenen Maßen), optionalem führendem oder folgendem Icon und Klick-Handler.

**Create:**
    cn::button(label)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `label` | `impl IntoReactive<String>` | Button-Text — ein String oder ein `Signal<String>`, das vor Ort verfolgt wird. |

Builder-Methoden: `.variant(ButtonVariant)` (`Primary` Standard, `Secondary`, `Destructive`, `Outline`, `Ghost`, `Link`), `.size(ButtonSize)` (`Small`/`Medium` Standard/`Large`, `Icon` als quadratischer Icon-Button, `Custom(width, height)`), `.icon(svg_markup)`, `.icon_position(IconPosition)` (`Start`/`End`), `.icon_size(px)`, `.color(color)`, `.disabled(flag)`, `.on_click(handler)`, `.with_key(key, label)`, `.class(name)`, `.id(id)`.

---

### button-group

#### English
No component named button-group; the closest is `cn::toggle_group(value)` — a row of mutually exclusive toggle items where the selected value is held in a `Signal<String>`. Multi-select is not implemented yet, and single toggles exist as `cn::toggle`.

**Create:**
    cn::toggle_group(value)

| Parameter | Type | Description |
|-----------|------|-------------|
| `value` | `Signal<String>` | Reactive value of the active item; set to the item's value on click. |

Builder methods: `.item(ToggleItem)` — built with `cn::toggle_item(value).label(l).icon(svg).aria_label(a).disabled(flag)` —, `.variant(ToggleVariant)` (`Default`/`Outline`), `.size(ToggleSize)` (`Small`/`Medium`/`Large`), `.gap(px)`, `.disabled(flag)`, `.on_change(handler)`, `.key(key)`.

#### Deutsch
Keine Komponente namens button-group; am nächsten kommt `cn::toggle_group(value)` — eine Zeile sich gegenseitig ausschließender Toggle-Elemente, deren gewählter Wert in einem `Signal<String>` liegt. Mehrfachauswahl ist noch nicht umgesetzt, Einzel-Toggles gibt es als `cn::toggle`.

**Create:**
    cn::toggle_group(value)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `value` | `Signal<String>` | Reaktiver Wert des aktiven Eintrags; wird beim Klick auf den Elementwert gesetzt. |

Builder-Methoden: `.item(ToggleItem)` — erzeugt mit `cn::toggle_item(value).label(l).icon(svg).aria_label(a).disabled(flag)` —, `.variant(ToggleVariant)` (`Default`/`Outline`), `.size(ToggleSize)` (`Small`/`Medium`/`Large`), `.gap(px)`, `.disabled(flag)`, `.on_change(handler)`, `.key(key)`.

---

### floating-action-button

#### English
No direct Blinc equivalent. There is no FAB primitive. Closest workaround: a `cn::button("…").size(ButtonSize::Custom(56.0, 56.0)).icon(svg)` (or `ButtonSize::Icon`) placed in an absolutely positioned wrapper near the corner of the view.

#### Deutsch
Kein direktes Blinc-Äquivalent. Es gibt kein FAB-Primitiv. Nächste Lösung: ein `cn::button("…").size(ButtonSize::Custom(56.0, 56.0)).icon(svg)` (oder `ButtonSize::Icon`) in einem absolut positionierten Container nahe der Ecke der Ansicht.

---

### alert

#### English
An inline status banner. `cn::alert(message)` is the one-line form; `cn::alert_box()` is the fuller block with a title and description.

**Create:**
    cn::alert(message)
    cn::alert_box()

| Parameter | Type | Description |
|-----------|------|-------------|
| `message` | `impl IntoReactive<String>` | The alert text; bind a signal and the message follows it. (`alert` only) |

Builder methods — `alert`: `.variant(AlertVariant)` (`Default`/`Info`, `Success`, `Warning`, `Destructive`/`Error`), `.class(name)`, `.id(id)`.
`alert_box` (no create argument): `.title(text)`, `.description(text)`, `.variant(…)`, `.class(name)`, `.id(id)`.

#### Deutsch
Ein inline angezeigter Statusbanner. `cn::alert(message)` ist die einzeilige Form; `cn::alert_box()` ist der ausführlichere Block mit Titel und Beschreibung.

**Create:**
    cn::alert(message)
    cn::alert_box()

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `message` | `impl IntoReactive<String>` | Alert-Text; an ein Signal gebunden folgt der Text mit. (nur `alert`) |

Builder-Methoden — `alert`: `.variant(AlertVariant)` (`Default`/`Info`, `Success`, `Warning`, `Destructive`/`Error`), `.class(name)`, `.id(id)`.
`alert_box` (kein Create-Argument): `.title(text)`, `.description(text)`, `.variant(…)`, `.class(name)`, `.id(id)`.

---

### badge

#### English
A small status label or counter pill. It has independent colour semantics (`BadgeVariant`) and fill treatment (`BadgeStyle`), plus an optional icon on either side.

**Create:**
    cn::badge(label)

| Parameter | Type | Description |
|-----------|------|-------------|
| `label` | `impl Into<String>` | Text shown in the badge. For a reactive label use `.reactive_label(Reactive<String>)`. |

Builder methods: `.variant(BadgeVariant)` (`Default` accent, `Secondary`, `Success`, `Warning`, `Destructive`), `.style(BadgeStyle)` (`Soft` default tinted fill, `Solid`, `Outline`), `.icon(icon)`, `.icon_position(IconPosition)` (`Start`/`End`), `.class(name)`, `.id(id)`.

#### Deutsch
Eine kleine Status- oder Zähler-Medaille. Sie hat unabhängige Farbsymbolik (`BadgeVariant`) und Füllstil (`BadgeStyle`) sowie optional ein Icon auf einer der beiden Seiten.

**Create:**
    cn::badge(label)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `label` | `impl Into<String>` | Text in der Medaille. Für einen reaktiven Text `.reactive_label(Reactive<String>)` verwenden. |

Builder-Methoden: `.variant(BadgeVariant)` (`Default` Akzent, `Secondary`, `Success`, `Warning`, `Destructive`), `.style(BadgeStyle)` (`Soft` Standard mit Getön, `Solid`, `Outline`), `.icon(icon)`, `.icon_position(IconPosition)` (`Start`/`End`), `.class(name)`, `.id(id)`.

---

### progress

#### English
A horizontal progress bar filled to a percentage. Bind a signal to watch the value change; `cn::progress_indeterminate()` renders the looping "busy" bar with no value.

**Create:**
    cn::progress(value)

| Parameter | Type | Description |
|-----------|------|-------------|
| `value` | `impl IntoReactive<f32>` | Fill percentage in `0..=100` — a number, `Signal<f32>` or `Computed`. |

Builder methods: `.size(ProgressSize)` (`Small` 4px / `Medium` 8px / `Large` 12px height), `.w(width)`, `.indicator_color(color)`, `.track_color(color)`, `.rounded(radius)`, `.class(name)`, `.id(id)`.

**Variant:** `cn::progress_indeterminate()` — same builder methods, no value argument.

#### Deutsch
Ein waagerechter Fortschrittsbalken, gefüllt bis zu einem Prozentsatz. Ein Signal gebunden verfolgt Wertänderungen; `cn::progress_indeterminate()` rendert den laufenden "Beschäftigt"-Balken ohne Wert.

**Create:**
    cn::progress(value)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `value` | `impl IntoReactive<f32>` | Füllgrad in `0..=100` — eine Zahl, ein `Signal<f32>` oder ein `Computed`. |

Builder-Methoden: `.size(ProgressSize)` (`Small` 4 px / `Medium` 8 px / `Large` 12 px Höhe), `.w(width)`, `.indicator_color(color)`, `.track_color(color)`, `.rounded(radius)`, `.class(name)`, `.id(id)`.

**Variante:** `cn::progress_indeterminate()` — gleiche Builder-Methoden, ohne Wert-Argument.

---

### spinner

#### English
A rotating loading indicator, sized by preset and colourable separately from its track.

**Create:**
    cn::spinner()

No parameters.

Builder methods: `.size(SpinnerSize)` (`Small` 16px / `Medium` 24px / `Large` 32px), `.color(color)`, `.track_color(color)`, `.class(name)`, `.id(id)`.

#### Deutsch
Ein rotierendes Lade-Indikator-Element, nach Preset skaliert und getrennt von seiner Spur einfärbbar.

**Create:**
    cn::spinner()

Keine Parameter.

Builder-Methoden: `.size(SpinnerSize)` (`Small` 16 px / `Medium` 24 px / `Large` 32 px), `.color(color)`, `.track_color(color)`, `.class(name)`, `.id(id)`.

---

### skeleton

#### English
A placeholder block that shimmers while content loads. Use the default rectangle, or `cn::skeleton_circle(size)` for avatars and initials.

**Create:**
    cn::skeleton()
    cn::skeleton_circle(size)

| Parameter | Type | Description |
|-----------|------|-------------|
| `size` | `f32` | Diameter of the circle (`skeleton_circle` only). |

Builder methods: `.w(width)`, `.h(height)`, `.w_full()`, `.rounded(radius)`, `.class(name)`, `.id(id)`.

#### Deutsch
Ein Platzhalterblock, der beim Laden schimmert. Standard ist das Rechteck; für Avatare und Initialen `cn::skeleton_circle(size)`.

**Create:**
    cn::skeleton()
    cn::skeleton_circle(size)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `size` | `f32` | Durchmesser des Kreises (nur `skeleton_circle`). |

Builder-Methoden: `.w(width)`, `.h(height)`, `.w_full()`, `.rounded(radius)`, `.class(name)`, `.id(id)`.

---

### toast

#### English
A transient notification pushed into a corner tray. Built with a title and optional description, action button or custom body, then `.show()` returns a handle that can dismiss it. `toast_success` / `toast_warning` / `toast_error` set the variant in one call.

**Create:**
    cn::toast(title)

| Parameter | Type | Description |
|-----------|------|-------------|
| `title` | `impl Into<String>` | Headline of the toast. |

Builder methods: `.description(text)`, `.body(content_fn)` / `cn::toast_custom(content_fn)`, `.variant(ToastVariant)` (`Default`, `Success`, `Warning`, `Destructive`), `.duration_ms(ms)`, `.persistent()`, `.corner(Corner)` (which screen corner the tray sits in), `.action(label, callback)`, `.show_close(flag)`, `.show() -> ToastHandle`.

#### Deutsch
Eine kurzlebige Meldung, die in eine Eckablage eingeblendet wird. Sie wird mit Titel sowie optionalem Beschreibungstext, Aktionsbutton oder eigenem Inhalt aufgebaut; `.show()` gibt ein Handle zum Schließen zurück. `toast_success` / `toast_warning` / `toast_error` setzen die Variante direkt.

**Create:**
    cn::toast(title)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `title` | `impl Into<String>` | Überschrift der Meldung. |

Builder-Methoden: `.description(text)`, `.body(inhalt_fn)` / `cn::toast_custom(inhalt_fn)`, `.variant(ToastVariant)` (`Default`, `Success`, `Warning`, `Destructive`), `.duration_ms(ms)`, `.persistent()`, `.corner(Corner)` (Ecke der Ablage), `.action(label, callback)`, `.show_close(flag)`, `.show() -> ToastHandle`.

---

### empty-state

#### English
No direct Blinc equivalent. There is no empty-state primitive. Compose one from `cn::icon`, `cn::label` and a `cn::button`, wrapped in a centred column — or a `cn::card` when the state sits inside a panel.

#### Deutsch
Kein direktes Blinc-Äquivalent. Es gibt kein Empty-State-Primitiv. Zusammensetzen aus `cn::icon`, `cn::label` und `cn::button` in einer zentrierten Spalte — oder in einer `cn::card`, wenn der Zustand in einem Panel liegt.

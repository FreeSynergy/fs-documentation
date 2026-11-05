# Blinc Components (`cn::`)

Quick reference for the component primitives in `blinc_cn` (`cn::…`) and,
where noted, `blinc_layout`. Each entry gives the create call, its
parameters, and the main companion helpers. Signatures follow the Blinc
source in the research clone (`.research-blinc/`).

---

### text-input

A single-line text field bound to shared input state. The state handle owns the value, cursor, placeholder and validation, so the field survives rebuilds and can be read or written from anywhere.

**Create:**
    cn::input(data)

| Parameter | Type | Description |
|-----------|------|-------------|
| `data` | `&SharedTextInputData` | Handle to the shared input state (`Arc<Mutex<TextInputData>>`); create it with `text_input_data()` or `text_input_data_with_placeholder(placeholder)`. |

Common builder methods: `.class(name)`, `.id(id)`, `.size(InputSize)` (`Small`/`Medium`/`Large`), `.label(text)`, `.error(text)`, `.required()`, `.disabled(flag)`, `.password()`, `.input_type(InputType)` (`Text`, `Number`, `Integer`, `Email`, `Password`, `Url`, `Tel`, `Search`), `.bind(input_ref)`, `.w(width)`, `.w_full()`, `.rounded(radius)`, `.border_width(width)`, `.idle_border_color(color)`, `.idle_bg_color(color)`, `.text_color(color)`, `.placeholder_color(color)`, `.cursor_color(color)`, `.selection_color(color)`.

---

### textarea

A multi-line text field bound to shared text-area state, with row/column sizing, optional wrapping and the same field affordances as `cn::input` (label, error, required).

**Create:**
    cn::textarea(state)

| Parameter | Type | Description |
|-----------|------|-------------|
| `state` | `&SharedTextAreaState` | Handle to the shared area state (`Arc<Mutex<TextAreaState>>`); create it with `text_area_state()` or `text_area_state_with_placeholder(placeholder)`. |

Common builder methods: `.class(name)`, `.id(id)`, `.size(TextareaSize)` (`Small`/`Medium`/`Large`), `.rows(n)`, `.cols(n)`, `.max_length(max)`, `.wrap(flag)` / `.no_wrap()`, `.label(text)`, `.error(text)`, `.required()`, `.disabled(flag)`, `.bind(textarea_ref)`, `.w(width)`, `.h(height)`, `.w_full()`, `.border_width(width)`, `.rounded(radius)`.

---

### number-input

A numeric field bound directly to a reactive `Signal<f64>`, with min/max clamping, stepping and keyboard increments (↑/↓, +/−). No separate shared-state handle is needed — the signal is the value.

**Create:**
    cn::number_input(state)

| Parameter | Type | Description |
|-----------|------|-------------|
| `state` | `Signal<f64>` | Reactive value the field shows and edits. |

Builder methods: `.min(min)`, `.max(max)`, `.step(step)`, `.precision(digits)`, `.size(InputSize)`, `.placeholder(text)`, `.disabled(flag)`, `.w(px)`, `.max_w(px)`, `.on_change(handler)`.

---

### select

A dropdown for choosing one option from a list, bound to a reactive `Signal<String>` holding the selected value. Options are supplied as value/label pairs and can carry custom content or be individually disabled.

**Create:**
    cn::select(value)

| Parameter | Type | Description |
|-----------|------|-------------|
| `value` | `Signal<String>` | Reactive currently-selected value; updated when the user picks an option. |

Builder methods: `.option(value, label)`, `.option_disabled(value, label)`, `.options(vec)` (items of `SelectOption::new(value, label)` with `.content(f)` / `.disabled()`), `.placeholder(text)`, `.label(text)`, `.size(SelectSize)` (`Small`/`Medium`/`Large`), `.disabled(flag)`, `.w(width)`, `.virtual_rows(row_height)`, `.on_change(callback)`, `.with_key(key, value)` for keyed instances.

---

### combobox

An editable input with a filtered dropdown list, bound to a `Signal<String>`. The user can search the options as they type, and `allow_custom` lets them enter a value that is not in the list.

**Create:**
    cn::combobox(value)

| Parameter | Type | Description |
|-----------|------|-------------|
| `value` | `Signal<String>` | Reactive current text/selection; updated on pick or typing. |

Builder methods: `.option(value, label)`, `.option_disabled(value, label)`, `.options(vec)` (items of `ComboboxOption::new(value, label)` with `.content(f)` / `.disabled()`), `.placeholder(text)`, `.label(text)`, `.size(ComboboxSize)` (`Small`/`Medium`/`Large`), `.allow_custom(flag)`, `.disabled(flag)`, `.w(width)`, `.on_change(callback)`, `.with_key(key, value)`.

---

### checkbox

A two-state toggle box bound to a `Signal<bool>`, optionally with a clickable label next to the box.

**Create:**
    cn::checkbox(checked)

| Parameter | Type | Description |
|-----------|------|-------------|
| `checked` | `Signal<bool>` | Reactive checked state; flipped by user interaction. |

Builder methods: `.label(text)`, `.size(CheckboxSize)` (`Small` 14px / `Medium` 18px / `Large` 22px), `.disabled(flag)`, `.on_change(callback)`, `.with_key(key, checked)`, `.class(name)`, `.id(id)`.

---

### radio-group

A set of mutually exclusive options bound to a `Signal<String>` holding the selected value. Options are laid out vertically or horizontally and can be individually disabled.

**Create:**
    cn::radio_group(selected)

| Parameter | Type | Description |
|-----------|------|-------------|
| `selected` | `Signal<String>` | Reactive value of the chosen option; set to the option's value on click. |

Builder methods: `.option(value, label)`, `.option_disabled(value, label)`, `.size(RadioSize)` (`Small` 14px / `Medium` 18px / `Large` 22px), `.layout(RadioLayout)` / `.vertical()` / `.horizontal()`, `.label(text)`, `.gap(px)`, `.disabled(flag)`, `.on_change(callback)`, `.key(key)`, `.class(name)`, `.id(id)`.

---

### switch

An on/off toggle rendered as a sliding thumb, bound to a `Signal<bool>`, with an optional label.

**Create:**
    cn::switch(on)

| Parameter | Type | Description |
|-----------|------|-------------|
| `on` | `Signal<bool>` | Reactive on state; flipped by user interaction. |

Builder methods: `.label(text)`, `.size(SwitchSize)` (`Small` 32×18 / `Medium` 44×24 / `Large` 52×28), `.disabled(flag)`, `.on_change(callback)`, `.class(name)`, `.id(id)`.

---

### slider

A draggable track for picking a number in a range. It accepts a `NumberValue`, so the same field can be bound to a `Signal<f32>` or `Signal<f64>` without a lossy copy — a slider and a `number_input` can share one value.

**Create:**
    cn::slider(value)

| Parameter | Type | Description |
|-----------|------|-------------|
| `value` | `impl Into<NumberValue>` | Reactive number to edit — pass a `Signal<f32>` or `Signal<f64>`; both convert into `NumberValue`. |

Builder methods: `.min(min)`, `.max(max)`, `.step(step)`, `.size(SliderSize)` (`Small` track 3px/thumb 12px, `Medium` 4px/16px, `Large` 6px/22px), `.label(text)`, `.show_value()`, `.disabled(flag)`, `.w(width)`, `.class(name)`, `.on_change(callback)`, `.with_key(key, value)`.

---

### otp-input

A one-code-per-cell verification input of fixed length. Digits go into the cell under the caret, Backspace on an empty cell steps back, and `on_complete` fires once every cell is filled.

**Create:**
    cn::input_otp(value, length)

| Parameter | Type | Description |
|-----------|------|-------------|
| `value` | `Signal<String>` | Reactive string holding the whole code (read it when complete). |
| `length` | `usize` | Number of cells / maximum code length. |

Builder methods: `.numeric_only(flag)`, `.masked(flag)`, `.error(flag)`, `.size(InputSize)`, `.group_every(n)` (visual grouping, e.g. `3 3 2`), `.disabled(flag)`, `.on_change(handler)`, `.on_complete(handler)`.

---

### field

No dedicated `field` component. A labelled form field is built by composing the field affordances on the input itself: `.label()` puts text above, `.description()` adds helper text below, `.error()` replaces that helper text with a message and marks the box invalid, and `.required()` flags it. `cn::input` and `cn::textarea` carry all four; `.label()` alone is also on `cn::select`, `cn::combobox`, `cn::radio_group`, `cn::checkbox`, `cn::switch` and `cn::slider`.

**Create:**
    cn::input(data).label(name).description(hint).error(message).required()

| Parameter | Type | Description |
|-----------|------|-------------|
| `label` | `impl IntoReactive<String>` | Text rendered above the control. |
| `description` | `impl IntoReactive<String>` | Helper text below the control; a signal replaces it in place. |
| `error` | `impl IntoReactive<String>` | Message shown in place of the description while non-empty; also sets `data-invalid` on the box. An empty signal clears the error. |
| `required` | — | Marks the control as required (no argument). |

---

### input-group

No direct Blinc equivalent. There is no `input_group` primitive; compose an input with adjacent buttons or icons by hand in a flex container (`.class("input-group")` plus your own border and radius on the wrapper), and drive the parts from the same `SharedTextInputData` / `InputRef`.

---

### search-field

No dedicated search component. Use a text input with `.input_type(InputType::Search)` for search affordances, or `cn::combobox(value)` when the query should filter and pick from a list.

**Create:**
    cn::input(data).input_type(InputType::Search)

| Parameter | Type | Description |
|-----------|------|-------------|
| `data` | `&SharedTextInputData` | Shared input state; set `constraints` on it to limit query length. |

---

### tags-input

No direct Blinc equivalent. There is no chip/tag input primitive. Closest workaround: keep the tags in your own `Vec<String>` state and render each tag as a `cn::badge` with a remove button next to a `cn::input` that appends on Enter (`.on_change` plus the input's submit hook).

---

### rating

No direct Blinc equivalent. There is no star-rating primitive. Closest workaround: a `cn::radio_group` with one option per star and star icons as the option content, or a `cn::slider(value).min(1.0).max(5.0).step(1.0)` for a compact continuous rating.

---

### color-input

No direct Blinc equivalent. There is no color picker or swatch input. Closest workaround: a `cn::input` bound to a hex string plus `InputConstraints`/a pattern for validation, with a `cn::icon` or a plain div whose background is set from the value.

---

### mention-input

No direct Blinc equivalent. There is no mention/@-input. Closest workaround: `blinc_layout::widgets::rich_text_editor` for the rich text part plus your own overlay (`cn::popover` or `cn::dropdown_menu`) opened when `@` is typed; the plain `cn::input` cannot render inline entities.

---

### date-input

No standalone date-field widget; Blinc's date picker is `cn::calendar` — a month grid whose selected day is held in a `Signal<Option<CalendarDay>>`. Pair it with a `cn::input` (or a popover trigger) if you also need a typed text representation.

**Create:**
    cn::calendar(value)

| Parameter | Type | Description |
|-----------|------|-------------|
| `value` | `Signal<Option<CalendarDay>>` | Reactive selected date (`CalendarDay::new(year, month, day)` or `CalendarDay::today()`); `None` means nothing selected. |

Builder methods: `.today(day)` (what counts as today), `.week_start(weekday)` (0 = Sunday), `.min_year(year)`, `.max_year(year)`, `.events(events)` (`impl IntoReactive<Vec<CalendarEvent>>`; `CalendarEvent::new(day, title).kind(k).icon(svg)`), `.on_change(callback)`, `.class(name)`, `.id(id)`.

---

### label

A caption for a control or a group of controls. The text may be a plain string or a signal that updates it in place; `required()` appends the required marker.

**Create:**
    cn::label(text)

| Parameter | Type | Description |
|-----------|------|-------------|
| `text` | `impl IntoReactive<String>` | Caption — a string or a `Signal<String>` followed in place. |

Builder methods: `.size(LabelSize)` (`Small` 12px / `Medium` 14px / `Large` 16px), `.required()`, `.disabled(flag)`, `.class(name)`, `.id(id)`.

---

### kbd

A key-cap styled inline label for keyboard shortcuts, e.g. `Ctrl` `K`.

**Create:**
    cn::kbd(text)

| Parameter | Type | Description |
|-----------|------|-------------|
| `text` | `impl IntoReactive<String>` | The key or shortcut to show. |

Builder methods: `.size(KbdSize)` (`Small` 10px / `Medium` 12px / `Large` 14px text), `.class(name)`, `.id(id)`.

---

### separator

A thin dividing line, horizontal by default, used to group content.

**Create:**
    cn::separator()

No parameters. Call `.vertical()` or `.horizontal()` for the orientation (`SeparatorOrientation`). Sizing and colour: `.w(width)`, `.h(height)`, `.m/mx/my/mt/mb/ml/mr(margin)`, `.bg(color)`, `.opacity(value)`, `.class(name)`, `.id(id)`.

---

### link

A clickable hyperlink that opens a URL. Lives in `blinc_layout`, not `cn::`, and is also reachable through the `open_url(url)` free function when you only need the navigation.

**Create:**
    blinc_layout::widgets::link::link(label, url)

| Parameter | Type | Description |
|-----------|------|-------------|
| `label` | `impl Into<String>` | Visible link text. |
| `url` | `impl Into<String>` | Target URL opened on click. |

Builder methods: `.on_click(handler)` (replaces the default open behaviour), `.text_color(color)`, `.font_size(size)`, `.underline(flag)` / `.no_underline()` / `.underline_on_hover()`, `.class(name)`, `.id(id)`.

---

### button

The standard action button, with six visual variants, a size ladder (including icon-only and custom dimensions), an optional leading or trailing icon, and a click handler.

**Create:**
    cn::button(label)

| Parameter | Type | Description |
|-----------|------|-------------|
| `label` | `impl IntoReactive<String>` | Button text — a string or a `Signal<String>` followed in place. |

Builder methods: `.variant(ButtonVariant)` (`Primary` default, `Secondary`, `Destructive`, `Outline`, `Ghost`, `Link`), `.size(ButtonSize)` (`Small`/`Medium` default/`Large`, `Icon` for square icon-only, `Custom(width, height)`), `.icon(svg_markup)`, `.icon_position(IconPosition)` (`Start`/`End`), `.icon_size(px)`, `.color(color)`, `.disabled(flag)`, `.on_click(handler)`, `.with_key(key, label)`, `.class(name)`, `.id(id)`.

---

### button-group

No component named button-group; the closest is `cn::toggle_group(value)` — a row of mutually exclusive toggle items where the selected value is held in a `Signal<String>`. Multi-select is not implemented yet, and single toggles exist as `cn::toggle`.

**Create:**
    cn::toggle_group(value)

| Parameter | Type | Description |
|-----------|------|-------------|
| `value` | `Signal<String>` | Reactive value of the active item; set to the item's value on click. |

Builder methods: `.item(ToggleItem)` — built with `cn::toggle_item(value).label(l).icon(svg).aria_label(a).disabled(flag)` —, `.variant(ToggleVariant)` (`Default`/`Outline`), `.size(ToggleSize)` (`Small`/`Medium`/`Large`), `.gap(px)`, `.disabled(flag)`, `.on_change(handler)`, `.key(key)`.

---

### floating-action-button

No direct Blinc equivalent. There is no FAB primitive. Closest workaround: a `cn::button("…").size(ButtonSize::Custom(56.0, 56.0)).icon(svg)` (or `ButtonSize::Icon`) placed in an absolutely positioned wrapper near the corner of the view.

---

### alert

An inline status banner. `cn::alert(message)` is the one-line form; `cn::alert_box()` is the fuller block with a title and description.

**Create:**
    cn::alert(message)
    cn::alert_box()

| Parameter | Type | Description |
|-----------|------|-------------|
| `message` | `impl IntoReactive<String>` | The alert text; bind a signal and the message follows it. (`alert` only) |

Builder methods — `alert`: `.variant(AlertVariant)` (`Default`/`Info`, `Success`, `Warning`, `Destructive`/`Error`), `.class(name)`, `.id(id)`.
`alert_box` (no create argument): `.title(text)`, `.description(text)`, `.variant(…)`, `.class(name)`, `.id(id)`.

---

### badge

A small status label or counter pill. It has independent colour semantics (`BadgeVariant`) and fill treatment (`BadgeStyle`), plus an optional icon on either side.

**Create:**
    cn::badge(label)

| Parameter | Type | Description |
|-----------|------|-------------|
| `label` | `impl Into<String>` | Text shown in the badge. For a reactive label use `.reactive_label(Reactive<String>)`. |

Builder methods: `.variant(BadgeVariant)` (`Default` accent, `Secondary`, `Success`, `Warning`, `Destructive`), `.style(BadgeStyle)` (`Soft` default tinted fill, `Solid`, `Outline`), `.icon(icon)`, `.icon_position(IconPosition)` (`Start`/`End`), `.class(name)`, `.id(id)`.

---

### progress

A horizontal progress bar filled to a percentage. Bind a signal to watch the value change; `cn::progress_indeterminate()` renders the looping "busy" bar with no value.

**Create:**
    cn::progress(value)

| Parameter | Type | Description |
|-----------|------|-------------|
| `value` | `impl IntoReactive<f32>` | Fill percentage in `0..=100` — a number, `Signal<f32>` or `Computed`. |

Builder methods: `.size(ProgressSize)` (`Small` 4px / `Medium` 8px / `Large` 12px height), `.w(width)`, `.indicator_color(color)`, `.track_color(color)`, `.rounded(radius)`, `.class(name)`, `.id(id)`.

**Variant:** `cn::progress_indeterminate()` — same builder methods, no value argument.

---

### spinner

A rotating loading indicator, sized by preset and colourable separately from its track.

**Create:**
    cn::spinner()

No parameters.

Builder methods: `.size(SpinnerSize)` (`Small` 16px / `Medium` 24px / `Large` 32px), `.color(color)`, `.track_color(color)`, `.class(name)`, `.id(id)`.

---

### skeleton

A placeholder block that shimmers while content loads. Use the default rectangle, or `cn::skeleton_circle(size)` for avatars and initials.

**Create:**
    cn::skeleton()
    cn::skeleton_circle(size)

| Parameter | Type | Description |
|-----------|------|-------------|
| `size` | `f32` | Diameter of the circle (`skeleton_circle` only). |

Builder methods: `.w(width)`, `.h(height)`, `.w_full()`, `.rounded(radius)`, `.class(name)`, `.id(id)`.

---

### toast

A transient notification pushed into a corner tray. Built with a title and optional description, action button or custom body, then `.show()` returns a handle that can dismiss it. `toast_success` / `toast_warning` / `toast_error` set the variant in one call.

**Create:**
    cn::toast(title)

| Parameter | Type | Description |
|-----------|------|-------------|
| `title` | `impl Into<String>` | Headline of the toast. |

Builder methods: `.description(text)`, `.body(content_fn)` / `cn::toast_custom(content_fn)`, `.variant(ToastVariant)` (`Default`, `Success`, `Warning`, `Destructive`), `.duration_ms(ms)`, `.persistent()`, `.corner(Corner)` (which screen corner the tray sits in), `.action(label, callback)`, `.show_close(flag)`, `.show() -> ToastHandle`.

---

### empty-state

No direct Blinc equivalent. There is no empty-state primitive. Compose one from `cn::icon`, `cn::label` and a `cn::button`, wrapped in a centred column — or a `cn::card` when the state sits inside a panel.

---

### modal

A centred modal dialog over a dimmed backdrop, driven through the overlay stack. It is imperative: build it inside a handler and `.show()` it, which returns an `OverlayHandle` for programmatic closing.

**Create:**
    cn::dialog()

No create parameters — content is supplied through the builder.

Builder methods: `.title(text)`, `.description(text)`, `.content(child_fn)`, `.footer(child_fn)`, `.size(DialogSize)` (`Small` 400px / `Medium` 500px / `Large` 600px / `Full` 800px max-width), `.confirm_text(text)`, `.cancel_text(text)`, `.confirm_destructive(flag)`, `.hide_cancel()`, `.on_confirm(cb)`, `.on_cancel(cb)`, `.on_close(cb)`, `.class(name)`, `.id(id)`, `.show() -> OverlayHandle`.

---

### alert-dialog

A simplified modal for confirmations and interruptions: title, description and one confirm button, with the same backdrop and dismissal behaviour as `cn::dialog`.

**Create:**
    cn::alert_dialog()

No create parameters.

Builder methods: `.title(text)`, `.description(text)`, `.confirm_text(text)`, `.on_confirm(cb)`, `.size(DialogSize)`, `.show() -> OverlayHandle`.

---

### drawer

A panel that slides in from the left or right edge, used for navigation and detail panes. Built imperatively and shown through the overlay stack.

**Create:**
    cn::drawer()

No create parameters. Shorthands: `cn::drawer_left()`, `cn::drawer_right()`.

Builder methods: `.side(DrawerSide)` (`Left` default / `Right`), `.size(DrawerSize)` (`Narrow` 240px / `Medium` 280px / `Wide` 320px), `.title(text)`, `.header(child_fn)`, `.child(child_fn)` / `.child_builder(builder)`, `.footer(child_fn)`, `.show_close(flag)`, `.on_close(cb)`, `.class(name)`, `.id(id)`, `.show() -> OverlayHandle`.

---

### sheet

A slide-in panel anchored to any of the four edges — a drawer with more room, including a full-screen option. Built imperatively and shown through the overlay stack.

**Create:**
    cn::sheet()

No create parameters. Shorthands: `cn::sheet_left()`, `cn::sheet_right()`, `cn::sheet_top()`, `cn::sheet_bottom()`.

Builder methods: `.side(SheetSide)` (`Left` / `Right` default / `Top` / `Bottom`), `.size(SheetSize)` (`Small` 320px / `Medium` 400px / `Large` 540px for left-right, 200/300/400px for top-bottom, `Full` for the viewport), `.title(text)`, `.description(text)`, `.content(child_fn)`, `.footer(child_fn)`, `.show_close(flag)`, `.on_close(cb)`, `.show() -> OverlayHandle`.

---

### popover

A floating panel anchored to a trigger element you build yourself. The trigger function receives whether the popover is open so it can reflect the state, and `.content()` supplies the panel.

**Create:**
    cn::popover(trigger_fn)

| Parameter | Type | Description |
|-----------|------|-------------|
| `trigger_fn` | `Fn(bool) -> Div` | Builds the trigger element; the argument says whether the popover is currently open. |

Builder methods: `.content(content_fn)` (required), `.side(PopoverSide)` (`Top` / `Bottom` default / `Right` / `Left`), `.align(PopoverAlign)` (`Start` default / `Center` / `End`), `.offset(px)` (default 4.0), `.class(name)`, `.id(id)`, `.with_key(trigger_fn, key)`.

---

### tooltip

A short hover label attached to a trigger element, with adjustable delay and placement. Unlike the popover it carries plain text rather than arbitrary content.

**Create:**
    cn::tooltip(trigger_fn)

| Parameter | Type | Description |
|-----------|------|-------------|
| `trigger_fn` | `Fn(bool) -> Div` | Builds the trigger element; the argument says whether the tooltip is showing. |

Builder methods: `.text(text)` (required; `impl IntoReactive<String>`), `.side(TooltipSide)` (`Top` default / `Bottom` / `Right` / `Left`), `.align(TooltipAlign)` (`Start` / `Center` default / `End`), `.open_delay_ms(ms)`, `.close_delay_ms(ms)`, `.offset(px)`, `.class(name)`, `.id(id)`, `.with_key(trigger_fn, key)`.

---

### hover-card

A preview card that opens when the pointer rests on the trigger — like a popover with arbitrary content, but hover-driven with open/close delays.

**Create:**
    cn::hover_card(trigger_fn)

| Parameter | Type | Description |
|-----------|------|-------------|
| `trigger_fn` | `Fn(bool) -> Div` | Builds the trigger element; the argument says whether the card is open. |

Builder methods: `.content(content_fn)` (required), `.side(HoverCardSide)` (`Top` / `Bottom` default / `Right` / `Left`), `.align(HoverCardAlign)` (`Start` default / `Center` / `End`), `.open_delay_ms(ms)`, `.close_delay_ms(ms)`, `.offset(px)`, `.class(name)`, `.id(id)`, `.with_key(trigger_fn, key)`.

---

### context-menu

A right-click menu positioned at explicit coordinates, usually the pointer position from the event context. Items carry click handlers, shortcuts, icons, separators and nested submenus.

**Create:**
    cn::context_menu()

No create parameters — call `.at(x, y)` to place it.

Builder methods: `.at(x, y)`, `.item(label, on_click)`, `.item_with_shortcut(label, shortcut, on_click)`, `.item_with_icon(label, svg, on_click)`, `.item_disabled(label)`, `.separator()`, `.submenu(label, builder_fn)` (the builder receives a `SubmenuBuilder` with the same `.item*`/`.separator` methods), `.add_item(ContextMenuItem)`, `.min_width(width)`, `.class(name)`, `.id(id)`, `.show() -> OverlayHandle`.
`ContextMenuItem` is public: `ContextMenuItem::new(label).on_click(f).shortcut(s).icon(svg).disabled()`, plus `ContextMenuItem::separator()` and `.submenu(items)`.

---

### menu

There is no single `menu` component — the name covers three: `cn::dropdown_menu(label)` for a trigger-button menu, `cn::menubar()` for an application menu bar, and `cn::navigation_menu()` for site/app navigation. All share the same row vocabulary (`.item`, `.item_with_shortcut`, `.item_with_icon`, `.item_disabled`, `.separator`, `.submenu`).

**Create:**
    cn::dropdown_menu(label)
    cn::menubar()
    cn::navigation_menu()

| Parameter | Type | Description |
|-----------|------|-------------|
| `label` | `impl Into<String>` | Trigger button text for the dropdown; use `cn::dropdown_menu_custom(trigger_fn)` for a custom trigger. Menubar and navigation menu take no argument. |

Dropdown builder: `.item(label, on_click)`, `.item_with_shortcut(label, shortcut, f)`, `.item_with_icon(label, svg, f)`, `.item_disabled(label)`, `.separator()`, `.submenu(label, builder_fn)`, `.position(DropdownPosition)` (`Bottom` default/`Top`/`Right`/`Left`), `.align(DropdownAlign)` (`Start` default/`Center`/`End`), `.offset(px)`, `.min_width(width)`.
Menubar builder: `.menu(label, builder_fn)` (per top-level menu), `.menu_custom(trigger, builder_fn)`, `.trigger_mode(MenuTriggerMode)` (`Click` default/`Hover`), `.trigger_style(MenuTriggerStyle)`.
Navigation menu builder: `.item(label, on_click)`, `.trigger(label, content_fn)` (dropdown panel of nav content), `.min_content_width(width)`; links via `cn::navigation_link(label).description(text).on_click(f)`.

---

### card

A bordered, themed surface for grouped content. The card itself takes children; `card_header`, `card_content` and `card_footer` are the standard structural parts you put inside it.

**Create:**
    cn::card()
    cn::card_header().title(t).description(d)
    cn::card_content().child(c)
    cn::card_footer().child(c)

No create parameters.

Builder methods — `card`: `.child(content)` (repeatable), `.w(width)`, `.h(height)`, `.w_full()`, `.p/px/py(padding)`, `.m(margin)`, `.shadow_md()`, `.shadow_lg()`, `.bg(color)`, `.class(name)`, `.id(id)`.
`card_header`: `.title(text)`, `.description(text)` (`impl IntoReactive<String>` each).
`card_content` / `card_footer`: `.child(content)`.

---

### accordion

Stacked sections where clicking a header expands its body. By default one section is open at a time; `multi_open()` allows several, and `item_with_state` binds a section's open state to your own `Signal<bool>`.

**Create:**
    cn::accordion()

No create parameters.

Builder methods: `.item(key, label, content_fn)`, `.item_with_state(key, label, is_open, content_fn)` (`is_open: Signal<bool>`), `.multi_open()` (switches `AccordionMode::Single` → `Multi`), `.default_open(key)`, `.class(name)`, `.id(id)`.

---

### collapsible

A single show/hide region driven by an open signal. `cn::collapsible(is_open)` is just the animated body; `cn::collapsible_section(label, is_open, content)` adds the bordered trigger header on top.

**Create:**
    cn::collapsible(is_open)
    cn::collapsible_section(trigger_label, is_open, content_fn)

| Parameter | Type | Description |
|-----------|------|-------------|
| `is_open` | `Signal<bool>` | Reactive open state; the builder also exposes `.toggle()` and `.set_open(open)` to drive it. |
| `trigger_label` | `impl Into<String>` | Header text of the section variant. |
| `content_fn` | content builder | The body that folds open and closed. |

Builder methods (`collapsible`): `.content(content_fn)`, `.toggle()`, `.set_open(open)`, `.class(name)`, `.id(id)`.

---

### scroll-area

A clipped, scrollable viewport with themed scrollbars. Direction, scrollbar visibility, thumb and track colours are all configurable, and the content is added as children.

**Create:**
    cn::scroll_area()

No create parameters.

Builder methods: `.child(content)`, `.direction(ScrollDirection)` with shorthands `.vertical()` (default) / `.horizontal()` / `.both_directions()`, `.scrollbar(ScrollbarVisibility)` (`Always`, `Hover`, `Auto` default, `Never`), `.size(ScrollAreaSize)` (`Small` 4px / `Medium` 6px / `Large` 10px scrollbar width), `.scrollbar_width(width)`, `.thumb_color(color)`, `.track_color(color)`, `.bounce(flag)` / `.no_bounce()`, `.w(width)`, `.h(height)`, `.rounded(radius)`, `.bg(color)`, `.class(name)`, `.id(id)`.

---

### split-view

Resizable panes side by side (or stacked). The group holds the panes and picks the divider direction with `ResizeDirection`; each panel declares its initial size and its min/max limits.

**Create:**
    cn::resizable_group()
    cn::resizable_panel()

No create parameters. Panels are handed to the group with `.panel(...)`.

Builder methods — group: `.direction(ResizeDirection)` (`Horizontal` default, panes side by side / `Vertical`, stacked) with shorthands `.horizontal()` / `.vertical()`, `.panel(panel_builder)` (repeatable), `.handle_thickness(px)`, `.on_resize(callback)`, `.key(key)`, `.class(name)`, `.id(id)`, `.build()`.
Panel: `.default_size(px)`, `.min_size(px)`, `.max_size(px)`, `.flex(factor)` / `.flex_grow()` (`PanelSize::Flex`, default `Flex(1.0)`), `.child(content)`, `.id(id)`.

---

### panel

No direct Blinc equivalent. A plain panel is just `blinc_layout`'s `div()` — set width, padding, background and radius directly (`div().w(320.0).p(16.0).bg(color).rounded(8.0)`). Reach for `cn::card()` when you want the themed surface and shadow for free.

---

### wizard

No direct Blinc equivalent. There is no multi-step wizard primitive. Build it from `cn::tabs` for the step header (disabled until reachable), a state machine in your own signal for the current step, and `cn::button` for back/next.

---

### table

A themed data table assembled from structural parts rather than configured by one call: a table element with a header row, body rows and optional footer and caption.

**Create:**
    cn::table()
    cn::table_header() / cn::table_body() / cn::table_footer()
    cn::table_row()
    cn::table_head(content) / cn::table_cell()
    cn::table_caption(content)

| Parameter | Type | Description |
|-----------|------|-------------|
| `content` | `impl Into<String>` | Text for a header cell (`table_head`) or the caption (`table_caption`). |

Builder methods — `TableRow`: `.selected(flag)` (`impl IntoReactive<bool>`; highlights the row), `.child(cell)` (repeatable), `.child_box(cell)` for a boxed builder. Cells are added to `table_row()` in column order; the row converts with `.into_div()`.

---

### tree-view

A hierarchical tree of expandable nodes. Nodes are declared inline with `cn::tree_view().node(key, label, children_fn)` or passed as a prepared `TreeNodeConfig`; one node is highlighted as selected and selection is reported through a callback.

**Create:**
    cn::tree_view()

No create parameters.

Builder methods: `.node(key, label, children_fn)` (repeatable; `children_fn` builds the nested nodes), `.add_node(TreeNodeConfig)`, `.selected(key)` (key of the highlighted node), `.on_select(callback)` (receives the key of the clicked node), `.indent(px)`, `.with_guides()` / `.guides(flag)` (connector lines), `.class(name)`, `.id(id)`.
`TreeNodeConfig` is public: `TreeNodeConfig::new(key, label).expanded().icon(svg).child(key, label, builder)`, plus `.diff(TreeNodeDiff)` — `None`/`Added`/`Removed`/`Modified` — which colours the row to show what changed (used by the debugger).

---

### chart

A chart family rather than one component: line, area and bar charts share a builder, and pie, histogram, comparison-bar, threshold-line and sparkline have their own. All take reactive data — a plain `Vec`, a `Signal` or a `Computed` — so charts follow their data.

**Create:**
    cn::line_chart()
    cn::area_chart()
    cn::bar_chart()
    cn::threshold_line_chart()
    cn::spark_line(values)
    cn::pie_chart()
    cn::histogram(values)
    cn::comparison_bar_chart()

| Parameter | Type | Description |
|-----------|------|-------------|
| `values` | `impl IntoReactive<Vec<f64>>` | The numbers for the single-series charts: a list, `Signal` or `Computed` (`spark_line`, `histogram`). |

Builder methods — line/area/bar (`ChartBuilder`): `.series(name, &[f64])` (repeatable), `.series_colored(name, values, color)`, `.data(impl IntoReactive<Vec<ChartSeries>>)`, `.values(impl IntoReactive<Vec<f64>>)` for one series, `.labels(impl IntoReactive<Vec<String>>)`, `.width(px)`, `.height(px)`, `.curve(ChartCurve)`, `.dots()`, `.horizontal()`, `.stacked()`, `.no_grid()`, `.no_axes()`, `.legend(flag)`, `.no_tooltip()`, `.min(min)` / `.max(max)`, `.color(css)`, `.format(fmt_fn)`, `.class(name)`.
Pie: `.slice(label, value)`, `.slice_colored(label, value, color)`, `.data(impl IntoReactive<Vec<PieSlice>>)`, `.donut(hole)`, `.total(caption)`, `.size(px)`, `.legend(flag)`, `.no_tooltip()`, `.format(fmt_fn)`.
Histogram: `.bins(n)` (default 20), `.log_scale()`, `.marker(value)` / `.marker_colored(value, css)`, `.color(css)`, `.height(px)`, `.format(fmt_fn)`.
Comparison: `.item(label, baseline, current)` / `.data(impl IntoReactive<Vec<ComparisonItem>>)` where `ComparisonItem::new(label, baseline, current)`, `.threshold(percent)` (default 10.0), `.height(px)`, `.format(fmt_fn)`.
Threshold line: `.band(band)` for each band and `.baseline(value)` for a dashed target.
Sparkline: comes without axes, grid, legend or tooltip at 100×24; `.filled()` fades it to its lowest value, `.color(..)` recolours it.

---

### avatar

A round or square identity tile showing an image, with initials or other text as fallback and an optional presence dot. `cn::avatar_group()` stacks several avatars with overlap and a "+N" overflow badge.

**Create:**
    cn::avatar()
    cn::avatar_group()

No create parameters.

Builder methods — `avatar`: `.src(url)` (`impl IntoReactive<String>`), `.alt(text)`, `.fallback(text)` (shown until/instead of the image), `.size(AvatarSize)` (`ExtraSmall` 24px … `ExtraLarge` 64px, `Medium` 40px default; shorthands `.xs() .sm() .md() .lg() .xl()`), `.shape(AvatarShape)` (`Circle` default / `Square`, or `.circle()` / `.square()`), `.status(AvatarStatus)` (`Online` green / `Offline` grey / `Away` yellow / `Busy` red, or `.online()` etc.), `.fallback_bg(color)`, `.fallback_color(color)`, `.ring(color, width)`, `.class(name)`, `.id(id)`.
`avatar_group`: `.child(avatar_builder)` (repeatable), `.size(AvatarSize)`, `.max(count)` (renders "+N" beyond it), `.overlap(px)`, `.class(name)`, `.id(id)`.

---

### breadcrumb

A trail of clickable path segments ending in the current location. Every segment but the last fires a click handler; the separator between segments is configurable.

**Create:**
    cn::breadcrumb()

No create parameters.

Builder methods: `.item(label, on_click)` (repeatable; `label: impl IntoReactive<String>`), `.item_with_icon(label, svg, on_click)`, `.current(label)` / `.current_with_icon(label, svg)` for the final non-clickable segment, `.separator(BreadcrumbSeparator)` (`Chevron` default, `Slash`, `Text(String)`, `Svg(String)`) with shorthands `.slash_separator()` / `.text_separator(text)`, `.size(BreadcrumbSize)` (`Small` 12px / `Medium` 14px default / `Large` 16px) with `.small()` / `.large()`, `.class(name)`, `.id(id)`.
`BreadcrumbItem::new(label).icon(svg).on_click(f)` is public for prepared items.

---

### pagination

Page-number buttons with first/previous/next/last controls, driven by a total page count and a page signal. `PageValue` accepts several signal widths — `usize`, `i32` or any number signal — so the page counter stays in the caller's precision.

**Create:**
    cn::pagination(total_pages, current_page)

| Parameter | Type | Description |
|-----------|------|-------------|
| `total_pages` | `usize` | How many pages exist. |
| `current_page` | `impl Into<PageValue>` | The page counter, 1-based: pass a `Signal<usize>`, `Signal<i32>` or a `NumberValue` (rounded at the boundary). |

Builder methods: `.visible_pages(count)` (how many numbers to show around the current one), `.show_first_last(flag)`, `.size(PaginationSize)` (`Small` 28px / `Medium` 32px default / `Large` 40px buttons) with `.small()` / `.large()`, `.on_page_change(handler)`, `.class(name)`, `.id(id)`. Call `.signal_id()` on the `PageValue` when something else must depend on the page reactively.

---

### sidebar

A navigation rail with animated collapse, grouped into titled sections, optionally paired with the content area beside it. Its collapsed state is a signal you own, so any button can fold the rail.

**Create:**
    cn::sidebar(is_collapsed)

| Parameter | Type | Description |
|-----------|------|-------------|
| `is_collapsed` | `Signal<bool>` | Reactive collapsed state; the built-in toggle button writes to it, and so can you. |

Builder methods: `.item(label, icon_svg, on_click)`, `.item_active(label, icon_svg, on_click)` (renders as selected), `.section(title)` / `.section_untitled()` (each following item joins the current section), `.show_toggle(flag)`, `.content(\|selected\| -> Div)` (the area next to the rail; built once, so drive it from a signal the click handlers write), `.class(name)`, `.id(id)`.
`SidebarItem::new(label, icon_svg, on_click).active(flag)` and `SidebarSection` are public for prepared rails.

---

### tabs

A tab strip plus the panel of the active tab, with the selected value held in a `Signal<String>`. Tabs can carry icons and badges, be disabled, and switch panels with a fade or slide transition.

**Create:**
    cn::tabs(state)

| Parameter | Type | Description |
|-----------|------|-------------|
| `state` | `Signal<String>` | Reactive value of the active tab; updated when a tab is clicked. |

Builder methods: `.tab(value, label, content_fn)` (repeatable), `.tab_item(TabMenuItem, content_fn)`, `.tab_disabled(value, label, content_fn)`, `.default_value(value)`, `.size(TabsSize)` (`Small` 32px / `Medium` 40px default / `Large` 48px), `.transition(TabsTransition)` (`None`, `Fade`, `Slide` default, `SlideLeft`, `SlideRight`), `.on_change(callback)`, `.class(name)`, `.id(id)`, `.with_key(key, state)`.
`cn::tab_item(value)` builds a prepared tab: `.label(l)`, `.icon(svg)`, `.badge(text)`, `.disabled()`, `.content(f)`.

---

### calendar-view

A month grid with day cells, event markers and month navigation. The selected day is a signal, events arrive as a reactive list, and today's date is injectable so tests and non-local time zones stay deterministic.

**Create:**
    cn::calendar(value)

| Parameter | Type | Description |
|-----------|------|-------------|
| `value` | `Signal<Option<CalendarDay>>` | Reactive selected date (`CalendarDay::new(year, month, day)`, or `CalendarDay::today()`); `None` means no selection. |

Builder methods: `.today(day)` (`CalendarDay` — what counts as today), `.week_start(weekday)` (0 = Sunday), `.min_year(year)` / `.max_year(year)`, `.events(impl IntoReactive<Vec<CalendarEvent>>)`, `.on_change(callback)`, `.class(name)`, `.id(id)`.
`CalendarEvent::new(day, title).kind(k).icon(svg)` describes one marker; `events_on(&events, day)` returns the events for a day.

---

### list-view

Two tools for lists. `blinc_layout`'s `ul()` / `ol()` render a small fixed set of items with markers and indentation; `virtual_list` renders only the rows in view, so lists of thousands stay cheap.

**Create:**
    blinc_layout::widgets::list::ul()
    blinc_layout::widgets::list::ol()          // ol_start(n) to begin elsewhere
    blinc_layout::widgets::list::li()          // one item; task_item(checked) for a checkbox row
    blinc_layout::widgets::virtual_list::virtual_list(item_count, builder)

| Parameter | Type | Description |
|-----------|------|-------------|
| `item_count` | `usize` | Total number of rows in the virtual list. |
| `builder` | `Fn(usize) -> impl ElementBuilder` | Builds the row at a given index; called only for visible indices. |

Builder methods — lists: `.child(ListItem)` (built with `li()`), `.child_element(element)` / `.child_box(builder)`, `.marker(ListMarker)`, `.indent(px)`, `.spacing(px)`, `.class(name)`, `.id(id)`; ordered lists also `.start(n)` (`ol_start(n)` at creation).
`virtual_list`: `.estimated_item_height(px)` (how tall an unseen row is assumed to be), `.window_size(n)` (rows kept beyond the viewport), `.w(px)` / `.h(px)` / `.w_full()` / `.h_full()`, `.gap_px(px)`, `.p(px)`, `.bg(color)`, `.rounded(r)`, `.border(width, color)`, `.item_class(class)` / `.content_class(class)`, `.class(name)`, `.id(id)`, `.into_div()`.

---

### description-list

No direct Blinc equivalent. There is no term/value list primitive. Compose one with `cn::table()` (two columns, no `table_header`), or a column of flex rows: `div().flex().child(cn::label(term)).child(text(value))`.

---

### grid-view

No direct Blinc equivalent. There is no grid/tile view component. A responsive tile layout is done with the layout primitives — `div()` with a wrap/flex or grid style and `cn::card()` children — inside a `cn::scroll_area()` when it needs to scroll.

---

### repeater

No dedicated repeater component. Repetition is done in Rust: map over the data and `.child()` one element per item, or use `blinc_layout::widgets::virtual_list::virtual_list(count, builder)` when the item count is large. A reactive list can also drive a `computed` child.

---

### table-of-contents

No direct Blinc equivalent. There is no outline/anchor component. Build the outline from `cn::breadcrumb()` or a `cn::sidebar()` (`.section()` per heading level) and scroll to anchors yourself; there is no built-in scroll-into-view target.

---

### timeline

No direct Blinc equivalent for the data-display timeline. Note the name clash: `TimelineHandle` and `TimelineRotation` in `blinc_layout::motion` / `stateful` are animation timelines, not event timelines. Render an event timeline as a `cn::scroll_area()` of rows, each a `cn::avatar()` or dot plus `cn::label`s, with a `cn::separator()` between entries.

---

### bottom-navigation

No dedicated bottom bar. Partially covered by `cn::navigation_menu()` — a horizontal row of items and content triggers, which can be placed at the bottom of a column — but it has no mobile bottom-bar affordances (safe-area inset, badge per item, active-route tracking).

**Create (closest):**
    cn::navigation_menu().item(label, on_click)

| Parameter | Type | Description |
|-----------|------|-------------|
| `label` / `on_click` | `impl Into<String>` / handler | One destination in the row; `.trigger(label, content_fn)` adds a dropdown panel instead. |

---

### command

No direct Blinc equivalent. There is no command palette (Cmd/Ctrl-K) component. Compose one: a `cn::combobox(value).allow_custom(true)` for the query plus a filtered `cn::dropdown_menu`, or a `cn::dialog()` opened from a key binding with the list inside.

---

### language-switcher

No direct Blinc equivalent. There is no locale switcher. Build it from `cn::select(value)` (or `cn::dropdown_menu`) over the language codes and write the choice into whatever signal drives your translations.

---

### radial-menu

No direct Blinc equivalent. There is no radial/pie menu. The nearest is `cn::context_menu()` or `cn::dropdown_menu()` for the same actions in a conventional list; a true radial layout needs hand-placed children with trigonometric offsets.

---

### toolbar

No direct Blinc equivalent as a general component. There is no toolbar container; the only toolbar in the framework is the editor-specific `selection_toolbar` inside `blinc_layout::widgets::rich_text_editor`. Compose a toolbar from `cn::toggle_group(value)` for grouped modes, `cn::button(…).size(ButtonSize::Icon)` for single actions and `cn::separator().vertical()` between clusters.

---

### icon

A stroke icon drawn from path data, sized by preset or in pixels and coloured either by theme token or an explicit colour. The path data comes from the icon crates — `blinc_icons` (Lucide) or `blinc_tabler_icons` (~5000 outline plus ~1000 filled constants).

**Create:**
    cn::icon(path_data)

| Parameter | Type | Description |
|-----------|------|-------------|
| `path_data` | `&'static str` | SVG path data, e.g. `blinc_icons::icons::CHECK` or a `blinc_tabler_icons` constant. |

Builder methods: `.size(IconSize)` (`ExtraSmall` 12px / `Small` 16px / `Medium` 20px default / `Large` 24px / larger presets), `.size_px(px)`, `.color(ColorToken)`, `.color_value(color)`, `.stroke_width(width)`, `.class(name)`, `.id(id)`.
Where only markup is wanted instead of an element, `blinc_tabler_icons::to_svg(path, size)` (and the `_filled`, `_colored`, `_with_stroke` variants) returns an SVG string.

---

### image

An image element loaded from a path, URL, base64 or data URI, with object-fit and position controls and a software filter chain (brightness, contrast, saturate, hue-rotate, grayscale, sepia, invert, blur).

**Create:**
    blinc_layout::image(source)      // module path: blinc_layout::image::image

| Parameter | Type | Description |
|-----------|------|-------------|
| `source` | `impl Into<String>` | File path, URL, base64 or data URI. |

Builder methods: `.size(width, height)` / `.square(size)` / `.w(px)` / `.h(px)` / `.w_full()` / `.h_full()`, `.fit(ObjectFit)` with shorthands `.cover()`, `.contain()`, `.fill()`, `.scale_down()`, `.no_scale()`, `.position(ObjectPosition)` / `.position_xy(x, y)` with `.top_left()` … `.bottom_right()`, `.opacity(value)`, `.rounded(radius)` / `.circular()`, `.border(width, color)`, `.filter(ImageFilter)` — built from `ImageFilter::none()` by setting `grayscale`, `sepia`, `brightness`, `contrast`, `saturate`, `hue_rotate`, `invert`, `blur`.

---

### audio-player

An audio player with transport controls and optional waveform. It wraps a player you create in `blinc_media`, so loading, decoding and playback state stay outside the widget.

**Create:**
    blinc_layout::widgets::media::audio_player(player)

| Parameter | Type | Description |
|-----------|------|-------------|
| `player` | `Rc<blinc_media::AudioPlayer>` | The player instance the widget controls and displays. |

Builder methods: `.waveform_data(&AudioSamples)` (draws the waveform; multi-channel samples are mixed to mono), `.w(px)` / `.h(px)` / `.w_full()`, `.bg(color)`, `.rounded(r)`, `.class(class)`, `.id(id)`, `.into_div()`. Standalone controls are available through `MediaControls::new(player)`.

---

### video-player

A video player with transport controls around a `blinc_media` video player instance.

**Create:**
    blinc_layout::widgets::media::video_player(player)

| Parameter | Type | Description |
|-----------|------|-------------|
| `player` | `Rc<blinc_media::VideoPlayer>` | The player instance the widget controls and displays. |

Builder methods: `.show_dimensions()` (overlay the frame size), `.w(px)` / `.h(px)`, `.bg(color)`, `.rounded(r)`, `.class(class)`, `.id(id)`, `.into_div()`.

---

### carousel

No direct Blinc equivalent. There is no carousel or slide component. Build one from a `cn::scroll_area()` in horizontal mode (with `.no_bounce()` and one slide per page width) plus `cn::button` arrows that change an index signal, or a `cn::tabs(value)` strip whose panels act as slides.

---

### gallery

No direct Blinc equivalent. There is no photo-gallery/lightbox component. Compose a grid of `blinc_layout::image(source).square(n)` tiles and open the full view in a `cn::dialog()` or `cn::sheet()` on click.

---

### rich-text-editor

A block-based WYSIWYG editor: headings, lists, dividers and inline marks, with a floating selection toolbar. Document state is owned outside the widget in an `Arc<Mutex<…>>`, so it survives rebuilds; each edit rebuilds only the block it touched.

**Create:**
    blinc_layout::widgets::rich_text_editor::rich_text_editor(state, theme, content_width)

| Parameter | Type | Description |
|-----------|------|-------------|
| `state` | `&RichTextState` | Shared document state (`Arc<Mutex<RichTextData>>`); create with `rich_text_state(RichDocument)`. |
| `theme` | `RichTextTheme` | Visual styling for blocks, marks and the toolbar. |
| `content_width` | `f32` | Pixel width of the column the document is laid out in — must match the parent's width. |

Companion API: `rich_text_editor::selection_toolbar(state, version, theme) -> Option<Div>` builds the floating toolbar over the current selection (returns `None` when nothing is selected); block and edit operations (`set_block_kind`, `toggle_block_kind`, `indent_blocks`, `outdent_blocks`, `insert_divider_after`) mutate the document directly. Put the editor in a parent with an explicit width to control its footprint.

---

### code-editor

An editable code surface with line numbers, undo/redo, selection and optional syntax highlighting, driven by shared editor state. For read-only display there are the lighter `code()` / `pre()` elements, and `code_minimap()` adds a scrollbar minimap.

**Create:**
    blinc_layout::widgets::code::code_editor(state)

| Parameter | Type | Description |
|-----------|------|-------------|
| `state` | `&SharedCodeEditorState` | Shared editor state (`Arc<Mutex<CodeEditorData>>`); create with `code_editor_state(content)`. |

Builder methods (both the editor and the read-only `code()` / `pre()` block): `.syntax(SyntaxConfig)` — installs a highlighter and its colours, `.line_numbers(flag)`, `.font_size(px)`, and on the editor `.on_change(\|text\|)` to observe edits. `code_minimap(state)` builds the minimap next to the editor.

---

### embed

Not covered by Blinc. There is no iframe, web-view or third-party embed element — the framework renders its own scene graph and has no browser surface to embed. Render fetched content with `blinc_layout::image` and `cn::card`, or open external content in the system browser via `blinc_layout::widgets::link::open_url(url)`.

---

### dashboard

No direct Blinc equivalent. A dashboard is a layout, not a component: arrange `cn::card()` tiles in a grid or `cn::resizable_group()` of panels and fill them with the `cn::line_chart` / `bar_chart` / `pie_chart` / `histogram` family plus `cn::progress` and `cn::badge` for KPIs.

---

### whiteboard

No direct Blinc equivalent. There is no canvas, stroke or freeform-drawing component in the documented component set. A whiteboard needs a custom drawing element; the practical building blocks are a fixed-size `div()` container plus the paint/renderer layer and pointer events.

---

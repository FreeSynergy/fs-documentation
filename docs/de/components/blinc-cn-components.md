# Blinc Components (`cn::`)

Kurzreferenz der Komponenten-Primitives in `blinc_cn` (`cn::…`) und, wo
vermerkt, `blinc_layout`. Jeder Eintrag nennt den Erzeugungsaufruf, seine
Parameter und die wichtigsten Begleit-Helfer. Signaturen folgen dem
Blinc-Quelltext im Forschungs-Klon (`.research-blinc/`).

---

### text-input

Ein einzeiliges Textfeld, das an einen gemeinsamen Eingabe-State gebunden ist. Der State-Handle hält Wert, Cursor, Platzhalter und Validierung, sodass das Feld Neuaufbauten übersteht und überall gelesen und geschrieben werden kann.

**Create:**
    cn::input(data)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `data` | `&SharedTextInputData` | Handle auf den gemeinsamen Eingabe-State (`Arc<Mutex<TextInputData>>`); erzeugt mit `text_input_data()` oder `text_input_data_with_placeholder(Platzhalter)`. |

Häufige Builder-Methoden: `.class(name)`, `.id(id)`, `.size(InputSize)` (`Small`/`Medium`/`Large`), `.label(text)`, `.error(text)`, `.required()`, `.disabled(flag)`, `.password()`, `.input_type(InputType)` (`Text`, `Number`, `Integer`, `Email`, `Password`, `Url`, `Tel`, `Search`), `.bind(input_ref)`, `.w(width)`, `.w_full()`, `.rounded(radius)`, `.border_width(width)`, `.idle_border_color(color)`, `.idle_bg_color(color)`, `.text_color(color)`, `.placeholder_color(color)`, `.cursor_color(color)`, `.selection_color(color)`.

---

### textarea

Ein mehrzeiliges Textfeld mit gemeinsamem TextArea-State, inklusive Zeilen-/Spaltengröße, optionalem Zeilenumbruch und denselben Feld-Features wie `cn::input` (Label, Fehler, Pflichtfeld).

**Create:**
    cn::textarea(state)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `state` | `&SharedTextAreaState` | Handle auf den gemeinsamen TextArea-State (`Arc<Mutex<TextAreaState>>`); erzeugt mit `text_area_state()` oder `text_area_state_with_placeholder(Platzhalter)`. |

Häufige Builder-Methoden: `.class(name)`, `.id(id)`, `.size(TextareaSize)` (`Small`/`Medium`/`Large`), `.rows(n)`, `.cols(n)`, `.max_length(max)`, `.wrap(flag)` / `.no_wrap()`, `.label(text)`, `.error(text)`, `.required()`, `.disabled(flag)`, `.bind(textarea_ref)`, `.w(width)`, `.h(height)`, `.w_full()`, `.border_width(width)`, `.rounded(radius)`.

---

### number-input

Ein Zahlenfeld, das direkt an einen reaktiven `Signal<f64>` gebunden ist, mit Min/Max-Begrenzung, Schrittweite und Tastatur-Inkrement (↑/↓, +/−). Kein separater Shared-State nötig — das Signal ist der Wert.

**Create:**
    cn::number_input(state)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `state` | `Signal<f64>` | Reaktiver Wert, den das Feld anzeigt und bearbeitet. |

Builder-Methoden: `.min(min)`, `.max(max)`, `.step(step)`, `.precision(digits)`, `.size(InputSize)`, `.placeholder(text)`, `.disabled(flag)`, `.w(px)`, `.max_w(px)`, `.on_change(handler)`.

---

### select

Ein Dropdown zur Auswahl genau einer Option aus einer Liste, gebunden an einen reaktiven `Signal<String>` mit dem gewählten Wert. Optionen werden als Wert/Beschriftung-Paare übergeben und können eigenen Inhalt tragen oder einzeln deaktiviert sein.

**Create:**
    cn::select(value)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `value` | `Signal<String>` | Reaktiv ausgewählter Wert; wird bei der Auswahl einer Option aktualisiert. |

Builder-Methoden: `.option(value, label)`, `.option_disabled(value, label)`, `.options(vec)` (Elemente aus `SelectOption::new(value, label)` mit `.content(f)` / `.disabled()`), `.placeholder(text)`, `.label(text)`, `.size(SelectSize)` (`Small`/`Medium`/`Large`), `.disabled(flag)`, `.w(width)`, `.virtual_rows(row_height)`, `.on_change(callback)`, `.with_key(key, value)` für schlüsselbasierte Instanzen.

---

### combobox

Ein editierbares Eingabefeld mit gefiltertem Dropdown, gebunden an ein `Signal<String>`. Beim Tippen wird die Optionsliste durchsucht; mit `allow_custom` sind auch Werte außerhalb der Liste erlaubt.

**Create:**
    cn::combobox(value)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `value` | `Signal<String>` | Reaktiver aktueller Text/die aktuelle Auswahl; wird bei Auswahl oder Eingabe aktualisiert. |

Builder-Methoden: `.option(value, label)`, `.option_disabled(value, label)`, `.options(vec)` (Elemente aus `ComboboxOption::new(value, label)` mit `.content(f)` / `.disabled()`), `.placeholder(text)`, `.label(text)`, `.size(ComboboxSize)` (`Small`/`Medium`/`Large`), `.allow_custom(flag)`, `.disabled(flag)`, `.w(width)`, `.on_change(callback)`, `.with_key(key, value)`.

---

### checkbox

Eine Zweizustands-Checkbox, gebunden an ein `Signal<bool>`, optional mit klickbarer Beschriftung neben der Box.

**Create:**
    cn::checkbox(checked)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `checked` | `Signal<bool>` | Reaktiver Häkchen-Zustand; wird durch Benutzeraktion geändert. |

Builder-Methoden: `.label(text)`, `.size(CheckboxSize)` (`Small` 14 px / `Medium` 18 px / `Large` 22 px), `.disabled(flag)`, `.on_change(callback)`, `.with_key(key, checked)`, `.class(name)`, `.id(id)`.

---

### radio-group

Eine Menge sich gegenseitig ausschließender Optionen, gebunden an ein `Signal<String>` mit dem gewählten Wert. Optionen werden vertikal oder horizontal angeordnet und können einzeln deaktiviert werden.

**Create:**
    cn::radio_group(selected)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `selected` | `Signal<String>` | Reaktiver Wert der gewählten Option; wird beim Klick auf den Optionswert gesetzt. |

Builder-Methoden: `.option(value, label)`, `.option_disabled(value, label)`, `.size(RadioSize)` (`Small` 14 px / `Medium` 18 px / `Large` 22 px), `.layout(RadioLayout)` / `.vertical()` / `.horizontal()`, `.label(text)`, `.gap(px)`, `.disabled(flag)`, `.on_change(callback)`, `.key(key)`, `.class(name)`, `.id(id)`.

---

### switch

Ein Ein/Aus-Schalter als gleitender Griff, gebunden an ein `Signal<bool>`, optional mit Beschriftung.

**Create:**
    cn::switch(on)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `on` | `Signal<bool>` | Reaktiver An-Zustand; wird durch Benutzeraktion umgeschaltet. |

Builder-Methoden: `.label(text)`, `.size(SwitchSize)` (`Small` 32×18 / `Medium` 44×24 / `Large` 52×28), `.disabled(flag)`, `.on_change(callback)`, `.class(name)`, `.id(id)`.

---

### slider

Eine ziehbare Leiste zur Wahl einer Zahl in einem Bereich. Sie nimmt ein `NumberValue` an und kann deshalb wahlweise an ein `Signal<f32>` oder `Signal<f64>` gebunden werden — ohne verlustlose Kopie: Slider und `number_input` können denselben Wert teilen.

**Create:**
    cn::slider(value)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `value` | `impl Into<NumberValue>` | Reaktive Zahl; ein `Signal<f32>` oder `Signal<f64>` wird in ein `NumberValue` konvertiert. |

Builder-Methoden: `.min(min)`, `.max(max)`, `.step(step)`, `.size(SliderSize)` (`Small` Spur 3 px/Griff 12 px, `Medium` 4 px/16 px, `Large` 6 px/22 px), `.label(text)`, `.show_value()`, `.disabled(flag)`, `.w(width)`, `.class(name)`, `.on_change(callback)`, `.with_key(key, value)`.

---

### otp-input

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

Keine eigene Komponente `field`. Ein beschriftetes Formularfeld entsteht durch die Kombination der Feld-Features am Eingabeelement selbst: `.label()` setzt Text darüber, `.description()` ergänzt Hilfetext darunter, `.error()` ersetzt den Hilfetext durch eine Meldung und markiert das Feld als ungültig, `.required()` kennzeichnet es als Pflichtfeld. `cn::input` und `cn::textarea` haben alle vier; nur `.label()` gibt es zusätzlich bei `cn::select`, `cn::combobox`, `cn::radio_group`, `cn::checkbox`, `cn::switch` und `cn::slider`.

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

Kein direktes Blinc-Äquivalent. Es gibt kein Primitiv `input_group`; ein Eingabefeld mit angrenzenden Buttons oder Icons wird per Hand in einem Flex-Container zusammengesetzt (`.class("input-group")` mit eigenem Rand und Radius am umgebenden Element), die Teile werden aus demselben `SharedTextInputData` / `InputRef` gesteuert.

---

### search-field

Keine eigene Such-Komponente. Ein Textfeld mit `.input_type(InputType::Search)` liefert die Such-Features, `cn::combobox(value)` passt, wenn die Eingabe eine Liste filtern und daraus auswählen soll.

**Create:**
    cn::input(data).input_type(InputType::Search)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `data` | `&SharedTextInputData` | Gemeinsamer Eingabe-State; über `constraints` lässt sich die Abfragelänge begrenzen. |

---

### tags-input

Kein direktes Blinc-Äquivalent. Es gibt kein Chip-/Tag-Eingabeprimitiv. Nächste Lösung: Tags im eigenen `Vec<String>`-State halten, jedes Tag als `cn::badge` mit Entf-Button neben einem `cn::input` rendern, der bei Enter anhängt (`.on_change` plus Submit-Hook des Feldes).

---

### rating

Kein direktes Blinc-Äquivalent. Es gibt kein Sternbewertungs-Primitiv. Nächste Lösung: ein `cn::radio_group` mit einer Option je Stern und Stern-Icons als Optionsinhalt, oder `cn::slider(value).min(1.0).max(5.0).step(1.0)` für eine kompakte durchgehende Bewertung.

---

### color-input

Kein direktes Blinc-Äquivalent. Es gibt keinen Farbwähler und keine Farbpalette. Nächste Lösung: ein `cn::input` an einem Hex-String mit `InputConstraints`/Pattern zur Validierung, dazu ein `cn::icon` oder ein Div, dessen Hintergrund aus dem Wert gesetzt wird.

---

### mention-input

Kein direktes Blinc-Äquivalent. Es gibt keine Mention-/@-Eingabe. Nächste Lösung: `blinc_layout::widgets::rich_text_editor` für den Rich-Text-Teil plus ein eigenes Overlay (`cn::popover` oder `cn::dropdown_menu`), das bei Eingabe von `@` geöffnet wird; das einfache `cn::input` kann keine Inline-Entitäten darstellen.

---

### date-input

Kein eigenständiges Datumsfeld; Blincs Datumsauswahl ist `cn::calendar` — ein Monatsraster, dessen gewählter Tag in einem `Signal<Option<CalendarDay>>` liegt. Für eine getippte Textdarstellung mit einem `cn::input` (oder Popover-Trigger) kombinieren.

**Create:**
    cn::calendar(value)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `value` | `Signal<Option<CalendarDay>>` | Reaktives gewähltes Datum (`CalendarDay::new(Jahr, Monat, Tag)` oder `CalendarDay::today()`); `None` = nichts ausgewählt. |

Builder-Methoden: `.today(day)` (was als heute gilt), `.week_start(weekday)` (0 = Sonntag), `.min_year(year)`, `.max_year(year)`, `.events(events)` (`impl IntoReactive<Vec<CalendarEvent>>`; `CalendarEvent::new(day, titel).kind(k).icon(svg)`), `.on_change(callback)`, `.class(name)`, `.id(id)`.

---

### label

Eine Beschriftung für ein Steuerelement oder eine Steuerelementgruppe. Der Text kann ein String oder ein Signal sein, das ihn vor Ort aktualisiert; `.required()` ergänzt die Pflichtfeld-Markierung.

**Create:**
    cn::label(text)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `text` | `impl IntoReactive<String>` | Beschriftung — ein String oder ein `Signal<String>`, das vor Ort verfolgt wird. |

Builder-Methoden: `.size(LabelSize)` (`Small` 12 px / `Medium` 14 px / `Large` 16 px), `.required()`, `.disabled(flag)`, `.class(name)`, `.id(id)`.

---

### kbd

Eine wie eine Taste gestaltete Inline-Beschriftung für Tastaturkürzel, z. B. `Ctrl` `K`.

**Create:**
    cn::kbd(text)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `text` | `impl IntoReactive<String>` | Anzuzeigende Taste bzw. Kombination. |

Builder-Methoden: `.size(KbdSize)` (`Small` 10 px / `Medium` 12 px / `Large` 14 px Text), `.class(name)`, `.id(id)`.

---

### separator

Eine dünne Trennlinie, standardmäßig waagerecht, zur Gruppierung von Inhalt.

**Create:**
    cn::separator()

Keine Parameter. Ausrichtung mit `.vertical()` oder `.horizontal()` (`SeparatorOrientation`). Größe und Farbe: `.w(width)`, `.h(height)`, `.m/mx/my/mt/mb/ml/mr(margin)`, `.bg(color)`, `.opacity(value)`, `.class(name)`, `.id(id)`.

---

### link

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

Der Standard-Aktionsbutton mit sechsoptischen Varianten, einer Größentreppe (inkl. nur-Icon und eigenen Maßen), optionalem führendem oder folgendem Icon und Klick-Handler.

**Create:**
    cn::button(label)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `label` | `impl IntoReactive<String>` | Button-Text — ein String oder ein `Signal<String>`, das vor Ort verfolgt wird. |

Builder-Methoden: `.variant(ButtonVariant)` (`Primary` Standard, `Secondary`, `Destructive`, `Outline`, `Ghost`, `Link`), `.size(ButtonSize)` (`Small`/`Medium` Standard/`Large`, `Icon` als quadratischer Icon-Button, `Custom(width, height)`), `.icon(svg_markup)`, `.icon_position(IconPosition)` (`Start`/`End`), `.icon_size(px)`, `.color(color)`, `.disabled(flag)`, `.on_click(handler)`, `.with_key(key, label)`, `.class(name)`, `.id(id)`.

---

### button-group

Keine Komponente namens button-group; am nächsten kommt `cn::toggle_group(value)` — eine Zeile sich gegenseitig ausschließender Toggle-Elemente, deren gewählter Wert in einem `Signal<String>` liegt. Mehrfachauswahl ist noch nicht umgesetzt, Einzel-Toggles gibt es als `cn::toggle`.

**Create:**
    cn::toggle_group(value)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `value` | `Signal<String>` | Reaktiver Wert des aktiven Eintrags; wird beim Klick auf den Elementwert gesetzt. |

Builder-Methoden: `.item(ToggleItem)` — erzeugt mit `cn::toggle_item(value).label(l).icon(svg).aria_label(a).disabled(flag)` —, `.variant(ToggleVariant)` (`Default`/`Outline`), `.size(ToggleSize)` (`Small`/`Medium`/`Large`), `.gap(px)`, `.disabled(flag)`, `.on_change(handler)`, `.key(key)`.

---

### floating-action-button

Kein direktes Blinc-Äquivalent. Es gibt kein FAB-Primitiv. Nächste Lösung: ein `cn::button("…").size(ButtonSize::Custom(56.0, 56.0)).icon(svg)` (oder `ButtonSize::Icon`) in einem absolut positionierten Container nahe der Ecke der Ansicht.

---

### alert

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

Eine kleine Status- oder Zähler-Medaille. Sie hat unabhängige Farbsymbolik (`BadgeVariant`) und Füllstil (`BadgeStyle`) sowie optional ein Icon auf einer der beiden Seiten.

**Create:**
    cn::badge(label)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `label` | `impl Into<String>` | Text in der Medaille. Für einen reaktiven Text `.reactive_label(Reactive<String>)` verwenden. |

Builder-Methoden: `.variant(BadgeVariant)` (`Default` Akzent, `Secondary`, `Success`, `Warning`, `Destructive`), `.style(BadgeStyle)` (`Soft` Standard mit Getön, `Solid`, `Outline`), `.icon(icon)`, `.icon_position(IconPosition)` (`Start`/`End`), `.class(name)`, `.id(id)`.

---

### progress

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

Ein rotierendes Lade-Indikator-Element, nach Preset skaliert und getrennt von seiner Spur einfärbbar.

**Create:**
    cn::spinner()

Keine Parameter.

Builder-Methoden: `.size(SpinnerSize)` (`Small` 16 px / `Medium` 24 px / `Large` 32 px), `.color(color)`, `.track_color(color)`, `.class(name)`, `.id(id)`.

---

### skeleton

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

Eine kurzlebige Meldung, die in eine Eckablage eingeblendet wird. Sie wird mit Titel sowie optionalem Beschreibungstext, Aktionsbutton oder eigenem Inhalt aufgebaut; `.show()` gibt ein Handle zum Schließen zurück. `toast_success` / `toast_warning` / `toast_error` setzen die Variante direkt.

**Create:**
    cn::toast(title)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `title` | `impl Into<String>` | Überschrift der Meldung. |

Builder-Methoden: `.description(text)`, `.body(inhalt_fn)` / `cn::toast_custom(inhalt_fn)`, `.variant(ToastVariant)` (`Default`, `Success`, `Warning`, `Destructive`), `.duration_ms(ms)`, `.persistent()`, `.corner(Corner)` (Ecke der Ablage), `.action(label, callback)`, `.show_close(flag)`, `.show() -> ToastHandle`.

---

### empty-state

Kein direktes Blinc-Äquivalent. Es gibt kein Empty-State-Primitiv. Zusammensetzen aus `cn::icon`, `cn::label` und `cn::button` in einer zentrierten Spalte — oder in einer `cn::card`, wenn der Zustand in einem Panel liegt.

---

### modal

Ein zentrierter modaler Dialog über einem abgedunkelten Hintergrund, gesteuert über den Overlay-Stack. Er ist imperativ: im Handler aufbauen und `.show()` aufrufen — das gibt ein `OverlayHandle` zum programmatischen Schließen zurück.

**Create:**
    cn::dialog()

Keine Create-Parameter — der Inhalt kommt aus dem Builder.

Builder-Methoden: `.title(text)`, `.description(text)`, `.content(kind_fn)`, `.footer(kind_fn)`, `.size(DialogSize)` (`Small` 400 px / `Medium` 500 px / `Large` 600 px / `Full` 800 px maximale Breite), `.confirm_text(text)`, `.cancel_text(text)`, `.confirm_destructive(flag)`, `.hide_cancel()`, `.on_confirm(cb)`, `.on_cancel(cb)`, `.on_close(cb)`, `.class(name)`, `.id(id)`, `.show() -> OverlayHandle`.

---

### alert-dialog

Ein vereinfachter Modal für Bestätigungen und Unterbrechungen: Titel, Beschreibung und ein Bestätigungsbutton, mit demselben Hintergrund- und Abbruchverhalten wie `cn::dialog`.

**Create:**
    cn::alert_dialog()

Keine Create-Parameter.

Builder-Methoden: `.title(text)`, `.description(text)`, `.confirm_text(text)`, `.on_confirm(cb)`, `.size(DialogSize)`, `.show() -> OverlayHandle`.

---

### drawer

Ein Panel, das von links oder rechts hereingleitet, für Navigation und Detailbereiche. Es wird imperativ aufgebaut und über den Overlay-Stack gezeigt.

**Create:**
    cn::drawer()

Keine Create-Parameter. Kurzformen: `cn::drawer_left()`, `cn::drawer_right()`.

Builder-Methoden: `.side(DrawerSide)` (`Left` Standard / `Right`), `.size(DrawerSize)` (`Narrow` 240 px / `Medium` 280 px / `Wide` 320 px), `.title(text)`, `.header(kind_fn)`, `.child(kind_fn)` / `.child_builder(builder)`, `.footer(kind_fn)`, `.show_close(flag)`, `.on_close(cb)`, `.class(name)`, `.id(id)`, `.show() -> OverlayHandle`.

---

### sheet

Ein Slide-in-Panel an einer der vier Kanten — ein Drawer mit mehr Platz, inklusive Vollbild-Option. Wird imperativ aufgebaut und über den Overlay-Stack gezeigt.

**Create:**
    cn::sheet()

Keine Create-Parameter. Kurzformen: `cn::sheet_left()`, `cn::sheet_right()`, `cn::sheet_top()`, `cn::sheet_bottom()`.

Builder-Methoden: `.side(SheetSide)` (`Left` / `Right` Standard / `Top` / `Bottom`), `.size(SheetSize)` (`Small` 320 px / `Medium` 400 px / `Large` 540 px bei links-rechts, 200/300/400 px bei oben-unten, `Full` für den Viewport), `.title(text)`, `.description(text)`, `.content(kind_fn)`, `.footer(kind_fn)`, `.show_close(flag)`, `.on_close(cb)`, `.show() -> OverlayHandle`.

---

### popover

Ein schwebendes Panel, verankert an einem selbst gebauten Auslöse-Element. Die Trigger-Funktion erhält, ob der Popover offen ist, und `.content()` liefert das Panel.

**Create:**
    cn::popover(trigger_fn)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `trigger_fn` | `Fn(bool) -> Div` | Baut das Auslöse-Element; das Argument zeigt an, ob der Popover gerade offen ist. |

Builder-Methoden: `.content(kind_fn)` (erforderlich), `.side(PopoverSide)` (`Top` / `Bottom` Standard / `Right` / `Left`), `.align(PopoverAlign)` (`Start` Standard / `Center` / `End`), `.offset(px)` (Standard 4,0), `.class(name)`, `.id(id)`, `.with_key(trigger_fn, key)`.

---

### tooltip

Ein kurzer Hover-Hinweis an einem Auslöse-Element, mit einstellbarer Verzögerung und Platzierung. Anders als der Popover trägt er reinen Text statt beliebiger Inhalte.

**Create:**
    cn::tooltip(trigger_fn)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `trigger_fn` | `Fn(bool) -> Div` | Baut das Auslöse-Element; das Argument zeigt an, ob der Hinweis gerade sichtbar ist. |

Builder-Methoden: `.text(text)` (erforderlich; `impl IntoReactive<String>`), `.side(TooltipSide)` (`Top` Standard / `Bottom` / `Right` / `Left`), `.align(TooltipAlign)` (`Start` / `Center` Standard / `End`), `.open_delay_ms(ms)`, `.close_delay_ms(ms)`, `.offset(px)`, `.class(name)`, `.id(id)`, `.with_key(trigger_fn, key)`.

---

### hover-card

Eine Vorschaukarte, die sich öffnet, wenn der Zeiger auf dem Auslöse-Element ruht — wie ein Popover mit beliebigen Inhalten, aber per Hover mit Öffnungs-/Schließverzögerung.

**Create:**
    cn::hover_card(trigger_fn)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `trigger_fn` | `Fn(bool) -> Div` | Baut das Auslöse-Element; das Argument zeigt an, ob die Karte offen ist. |

Builder-Methoden: `.content(kind_fn)` (erforderlich), `.side(HoverCardSide)` (`Top` / `Bottom` Standard / `Right` / `Left`), `.align(HoverCardAlign)` (`Start` Standard / `Center` / `End`), `.open_delay_ms(ms)`, `.close_delay_ms(ms)`, `.offset(px)`, `.class(name)`, `.id(id)`, `.with_key(trigger_fn, key)`.

---

### context-menu

Ein Rechtsklick-Menü an expliziten Koordinaten, üblicherweise der Zeigerposition aus dem Event-Kontext. Einträge haben Klick-Handler, Tastenkürzel, Icons, Trenner und verschachtelte Untermenüs.

**Create:**
    cn::context_menu()

Keine Create-Parameter — zum Platzieren `.at(x, y)` aufrufen.

Builder-Methoden: `.at(x, y)`, `.item(label, on_click)`, `.item_with_shortcut(label, shortcut, on_click)`, `.item_with_icon(label, svg, on_click)`, `.item_disabled(label)`, `.separator()`, `.submenu(label, builder_fn)` (der Builder erhält einen `SubmenuBuilder` mit denselben `.item*`-/`.separator`-Methoden), `.add_item(ContextMenuItem)`, `.min_width(width)`, `.class(name)`, `.id(id)`, `.show() -> OverlayHandle`.
`ContextMenuItem` ist öffentlich: `ContextMenuItem::new(label).on_click(f).shortcut(s).icon(svg).disabled()`, dazu `ContextMenuItem::separator()` und `.submenu(items)`.

---

### menu

Es gibt keine einzelne Komponente `menu` — der Name fasst drei zusammen: `cn::dropdown_menu(label)` für ein Trigger-Button-Menü, `cn::menubar()` für eine Anwendungs-Menüleiste und `cn::navigation_menu()` für die Seiten-/App-Navigation. Alle teilen dieselbe Eintragssprache (`.item`, `.item_with_shortcut`, `.item_with_icon`, `.item_disabled`, `.separator`, `.submenu`).

**Create:**
    cn::dropdown_menu(label)
    cn::menubar()
    cn::navigation_menu()

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `label` | `impl Into<String>` | Trigger-Text des Dropdowns; für einen eigenen Trigger `cn::dropdown_menu_custom(trigger_fn)`. Menüleiste und Navigationsmenü haben kein Argument. |

Dropdown-Builder: `.item(label, on_click)`, `.item_with_shortcut(label, shortcut, f)`, `.item_with_icon(label, svg, f)`, `.item_disabled(label)`, `.separator()`, `.submenu(label, builder_fn)`, `.position(DropdownPosition)` (`Bottom` Standard/`Top`/`Right`/`Left`), `.align(DropdownAlign)` (`Start` Standard/`Center`/`End`), `.offset(px)`, `.min_width(width)`.
Menubar-Builder: `.menu(label, builder_fn)` (pro Top-Level-Menü), `.menu_custom(trigger, builder_fn)`, `.trigger_mode(MenuTriggerMode)` (`Click` Standard/`Hover`), `.trigger_style(MenuTriggerStyle)`.
Navigationsmenü-Builder: `.item(label, on_click)`, `.trigger(label, content_fn)` (Dropdown-Panel mit Navigationsinhalt), `.min_content_width(width)`; Links über `cn::navigation_link(label).description(text).on_click(f)`.

---

### card

Eine gerahmte, themierte Fläche für gruppierten Inhalt. Die Card nimmt Kinder an; `card_header`, `card_content` und `card_footer` sind die Standard-Bausteine darin.

**Create:**
    cn::card()
    cn::card_header().title(t).description(d)
    cn::card_content().child(c)
    cn::card_footer().child(c)

Keine Create-Parameter.

Builder-Methoden — `card`: `.child(content)` (wiederholbar), `.w(width)`, `.h(height)`, `.w_full()`, `.p/px/py(padding)`, `.m(margin)`, `.shadow_md()`, `.shadow_lg()`, `.bg(color)`, `.class(name)`, `.id(id)`.
`card_header`: `.title(text)`, `.description(text)` (je `impl IntoReactive<String>`).
`card_content` / `card_footer`: `.child(content)`.

---

### accordion

Gestapelte Abschnitte, deren Inhalt sich per Klick auf die Kopfzeile öffnet. Standardmäßig ist ein Abschnitt offen; `multi_open()` erlaubt mehrere, und `item_with_state` bindet den geöffneten Zustand an ein eigenes `Signal<bool>`.

**Create:**
    cn::accordion()

Keine Create-Parameter.

Builder-Methoden: `.item(key, label, content_fn)`, `.item_with_state(key, label, is_open, content_fn)` (`is_open: Signal<bool>`), `.multi_open()` (wechselt `AccordionMode::Single` → `Multi`), `.default_open(key)`, `.class(name)`, `.id(id)`.

---

### collapsible

Ein einzelner Ein-/Ausblendbereich, gesteuert über ein Öffnungssignal. `cn::collapsible(is_open)` ist nur der animierte Inhalt; `cn::collapsible_section(label, is_open, content)` setzt den gerahmten Trigger-Kopf darüber.

**Create:**
    cn::collapsible(is_open)
    cn::collapsible_section(trigger_label, is_open, content_fn)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `is_open` | `Signal<bool>` | Reaktiver Öffnungszustand; der Builder bietet zusätzlich `.toggle()` und `.set_open(open)`. |
| `trigger_label` | `impl Into<String>` | Kopfzeilentext der Sections-Variante. |
| `content_fn` | Content-Builder | Der Inhalt, der auf- und zugeklappt wird. |

Builder-Methoden (`collapsible`): `.content(content_fn)`, `.toggle()`, `.set_open(open)`, `.class(name)`, `.id(id)`.

---

### scroll-area

Ein beschnittener, scrollbarer Viewport mit themierten Scrollbalken. Richtung, Sichtbarkeit, Daumen- und Spur­farbe sind konfigurierbar; der Inhalt wird als Kind hinzugefügt.

**Create:**
    cn::scroll_area()

Keine Create-Parameter.

Builder-Methoden: `.child(content)`, `.direction(ScrollDirection)` mit Kurzformen `.vertical()` (Standard) / `.horizontal()` / `.both_directions()`, `.scrollbar(ScrollbarVisibility)` (`Always`, `Hover`, `Auto` Standard, `Never`), `.size(ScrollAreaSize)` (`Small` 4 px / `Medium` 6 px / `Large` 10 px Balkenbreite), `.scrollbar_width(width)`, `.thumb_color(color)`, `.track_color(color)`, `.bounce(flag)` / `.no_bounce()`, `.w(width)`, `.h(height)`, `.rounded(radius)`, `.bg(color)`, `.class(name)`, `.id(id)`.

---

### split-view

Größenveränderliche Panels nebeneinander oder untereinander. Die Gruppe hält die Panels und wählt die Richtung des Teilers über `ResizeDirection`; jedes Panel deklariert Anfangsgröße sowie Min-/Max-Grenzen.

**Create:**
    cn::resizable_group()
    cn::resizable_panel()

Keine Create-Parameter. Panels werden der Gruppe mit `.panel(...)` übergeben.

Builder-Methoden — Gruppe: `.direction(ResizeDirection)` (`Horizontal` Standard, Panels nebeneinander / `Vertical`, untereinander) mit Kurzformen `.horizontal()` / `.vertical()`, `.panel(panel_builder)` (wiederholbar), `.handle_thickness(px)`, `.on_resize(callback)`, `.key(key)`, `.class(name)`, `.id(id)`, `.build()`.
Panel: `.default_size(px)`, `.min_size(px)`, `.max_size(px)`, `.flex(factor)` / `.flex_grow()` (`PanelSize::Flex`, Standard `Flex(1.0)`), `.child(content)`, `.id(id)`.

---

### panel

Kein direktes Blinc-Äquivalent. Ein einfaches Panel ist schlicht `div()` aus `blinc_layout` — Breite, Padding, Hintergrund und Radius direkt setzen (`div().w(320.0).p(16.0).bg(color).rounded(8.0)`). Für die themierte Fläche mit Schattierung `cn::card()` verwenden.

---

### wizard

Kein direktes Blinc-Äquivalent. Es gibt kein Wizard-Primitiv. Zusammensetzen aus `cn::tabs` für den Schritt-Header (bis zur Erreichbarkeit deaktiviert), einer eigenen Zustandsmaschine im Signal für den aktuellen Schritt und `cn::button` für zurück/weiter.

---

### table

Eine themierte Datentabelle, die aus Strukturteilen zusammengesetzt wird statt über einen einzigen Aufruf konfiguriert zu werden: ein Tabellenelement mit Kopfbeile, Körperzeilen und optional Fußzeile und Caption.

**Create:**
    cn::table()
    cn::table_header() / cn::table_body() / cn::table_footer()
    cn::table_row()
    cn::table_head(content) / cn::table_cell()
    cn::table_caption(content)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `content` | `impl Into<String>` | Text für eine Kopfzelle (`table_head`) bzw. die Caption (`table_caption`). |

Builder-Methoden — `TableRow`: `.selected(flag)` (`impl IntoReactive<bool>`; hebt die Zeile hervor), `.child(cell)` (wiederholbar), `.child_box(cell)` für einen Box-Builder. Zellen werden in Spaltenreihenfolge in `table_row()` eingefügt; die Zeile wird mit `.into_div()` überführt.

---

### tree-view

Ein hierarchischer Baum aus aufklappbaren Knoten. Knoten werden inline mit `cn::tree_view().node(key, label, children_fn)` deklariert oder als vorbereitetes `TreeNodeConfig` übergeben; ein Knoten wird als ausgewählt hervorgehoben, die Auswahl wird per Callback gemeldet.

**Create:**
    cn::tree_view()

Keine Create-Parameter.

Builder-Methoden: `.node(key, label, children_fn)` (wiederholbar; `children_fn` baut die verschachtelten Knoten), `.add_node(TreeNodeConfig)`, `.selected(key)` (Schlüssel des hervorgehobenen Knotens), `.on_select(callback)` (erhält den Schlüssel des angeklickten Knotens), `.indent(px)`, `.with_guides()` / `.guides(flag)` (Verbindungslinien), `.class(name)`, `.id(id)`.
`TreeNodeConfig` ist öffentlich: `TreeNodeConfig::new(key, label).expanded().icon(svg).child(key, label, builder)`, dazu `.diff(TreeNodeDiff)` — `None`/`Added`/`Removed`/`Modified` — was die Zeile je nach Änderung einfärbt (vom Debugger genutzt).

---

### chart

Eine Chart-Familie statt einer Komponente: Linien-, Flächen- und Balkendiagramm teilen sich einen Builder, Kreis-, Histogramm-, Vergleichs-, Schwellenwert- und Sparkline-Chart haben je einen eigenen. Alle nehmen reaktive Daten — eine Liste, ein `Signal` oder ein `Computed` — und folgen damit ihren Werten.

**Create:**
    cn::line_chart()
    cn::area_chart()
    cn::bar_chart()
    cn::threshold_line_chart()
    cn::spark_line(values)
    cn::pie_chart()
    cn::histogram(values)
    cn::comparison_bar_chart()

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `values` | `impl IntoReactive<Vec<f64>>` | Die Zahlen der Ein-Serien-Charts: Liste, `Signal` oder `Computed` (`spark_line`, `histogram`). |

Builder-Methoden — Linie/Fläche/Balken (`ChartBuilder`): `.series(name, &[f64])` (wiederholbar), `.series_colored(name, values, color)`, `.data(impl IntoReactive<Vec<ChartSeries>>)`, `.values(impl IntoReactive<Vec<f64>>)` für eine Serie, `.labels(impl IntoReactive<Vec<String>>)`, `.width(px)`, `.height(px)`, `.curve(ChartCurve)`, `.dots()`, `.horizontal()`, `.stacked()`, `.no_grid()`, `.no_axes()`, `.legend(flag)`, `.no_tooltip()`, `.min(min)` / `.max(max)`, `.color(css)`, `.format(fmt_fn)`, `.class(name)`.
Kreis: `.slice(label, value)`, `.slice_colored(label, value, color)`, `.data(impl IntoReactive<Vec<PieSlice>>)`, `.donut(hole)`, `.total(caption)`, `.size(px)`, `.legend(flag)`, `.no_tooltip()`, `.format(fmt_fn)`.
Histogramm: `.bins(n)` (Standard 20), `.log_scale()`, `.marker(wert)` / `.marker_colored(wert, css)`, `.color(css)`, `.height(px)`, `.format(fmt_fn)`.
Vergleich: `.item(label, baseline, current)` / `.data(impl IntoReactive<Vec<ComparisonItem>>)` mit `ComparisonItem::new(label, baseline, current)`, `.threshold(prozent)` (Standard 10,0), `.height(px)`, `.format(fmt_fn)`.
Schwellenwert-Linie: `.band(band)` je Band und `.baseline(wert)` für ein gestricheltes Ziel.
Sparkline: ohne Achsen, Gitter, Legende und Tooltip, 100×24; `.filled()` füllt sie bis zu ihrem tiefsten Wert, `.color(..)` färbt sie um.

---

### avatar

Eine runde oder eckige Identitätskachel mit Bild, Text-Fallback (z. B. Initialen) und optionalem Statuspunkt. `cn::avatar_group()` stapelt mehrere Avatare mit Überlappung und "+N"-Überlauf.

**Create:**
    cn::avatar()
    cn::avatar_group()

Keine Create-Parameter.

Builder-Methoden — `avatar`: `.src(url)` (`impl IntoReactive<String>`), `.alt(text)`, `.fallback(text)` (bis/statt des Bildes), `.size(AvatarSize)` (`ExtraSmall` 24 px … `ExtraLarge` 64 px, `Medium` 40 px Standard; Kurzformen `.xs() .sm() .md() .lg() .xl()`), `.shape(AvatarShape)` (`Circle` Standard / `Square`, oder `.circle()` / `.square()`), `.status(AvatarStatus)` (`Online` grün / `Offline` grau / `Away` gelb / `Busy` rot, oder `.online()` usw.), `.fallback_bg(color)`, `.fallback_color(color)`, `.ring(color, width)`, `.class(name)`, `.id(id)`.
`avatar_group`: `.child(avatar_builder)` (wiederholbar), `.size(AvatarSize)`, `.max(anzahl)` (darüber "+N"), `.overlap(px)`, `.class(name)`, `.id(id)`.

---

### breadcrumb

Eine Kette anklickbarer Pfadabschnitte, abgeschlossen vom aktuellen Ort. Alle Abschnitte außer dem letzten lösen einen Klick-Handler aus; das Trennzeichen ist konfigurierbar.

**Create:**
    cn::breadcrumb()

Keine Create-Parameter.

Builder-Methoden: `.item(label, on_click)` (wiederholbar; `label: impl IntoReactive<String>`), `.item_with_icon(label, svg, on_click)`, `.current(label)` / `.current_with_icon(label, svg)` für den letzten nicht anklickbaren Abschnitt, `.separator(BreadcrumbSeparator)` (`Chevron` Standard, `Slash`, `Text(String)`, `Svg(String)`) mit Kurzformen `.slash_separator()` / `.text_separator(text)`, `.size(BreadcrumbSize)` (`Small` 12 px / `Medium` 14 px Standard / `Large` 16 px) mit `.small()` / `.large()`, `.class(name)`, `.id(id)`.
`BreadcrumbItem::new(label).icon(svg).on_click(f)` ist öffentlich für vorbereitete Einträge.

---

### pagination

Seitenzahlen-Buttons mit Erste/Zurück/Weiter/Letzte-Steuerung, getrieben von Gesamtseitenzahl und einem Seitenzähler-Signal. `PageValue` nimmt mehrere Signalbreiten — `usize`, `i32` oder ein Zahlen-Signal — der Zähler bleibt also in der Präzision des Aufrufers.

**Create:**
    cn::pagination(total_pages, current_page)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `total_pages` | `usize` | Anzahl der Seiten. |
| `current_page` | `impl Into<PageValue>` | Seitenzähler, beginnend bei 1: ein `Signal<usize>`, `Signal<i32>` oder `NumberValue` (an der Grenze gerundet). |

Builder-Methoden: `.visible_pages(anzahl)` (wie viele Zahlen um die aktuelle gezeigt werden), `.show_first_last(flag)`, `.size(PaginationSize)` (`Small` 28 px / `Medium` 32 px Standard / `Large` 40 px Buttons) mit `.small()` / `.large()`, `.on_page_change(handler)`, `.class(name)`, `.id(id)`. Auf dem `PageValue` `.signal_id()` aufrufen, wenn etwas anderes reaktiv von der Seite abhängen muss.

---

### sidebar

Eine Navigationsleiste mit animiertem Einklappen, gegliedert in betitelte Abschnitte, optional gepaart mit dem Inhaltsbereich daneben. Der eingeklappte Zustand liegt in einem eigenen Signal, damit jeder Button die Leiste einziehen kann.

**Create:**
    cn::sidebar(is_collapsed)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `is_collapsed` | `Signal<bool>` | Reaktiver Einklapp-Zustand; der eingebaute Toggle schreibt daran, man selbst auch. |

Builder-Methoden: `.item(label, icon_svg, on_click)`, `.item_active(label, icon_svg, on_click)` (dargestellt als ausgewählt), `.section(titel)` / `.section_untitled()` (jeder folgende Eintrag kommt in den aktuellen Abschnitt), `.show_toggle(flag)`, `.content(\|auswahl\| -> Div)` (der Bereich neben der Leiste; wird einmal gebaut, also aus einem Signal der Klick-Handler steuern), `.class(name)`, `.id(id)`.
`SidebarItem::new(label, icon_svg, on_click).active(flag)` und `SidebarSection` sind öffentlich für vorbereitete Leisten.

---

### tabs

Eine Tab-Leiste plus das Panel des aktiven Tabs, mit dem gewählten Wert in einem `Signal<String>`. Tabs können Icons und Badges tragen, deaktiviert sein, und der Panelwechsel nutzt Fade- oder Slide-Übergang.

**Create:**
    cn::tabs(state)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `state` | `Signal<String>` | Reaktiver Wert des aktiven Tabs; wird beim Klick aktualisiert. |

Builder-Methoden: `.tab(value, label, content_fn)` (wiederholbar), `.tab_item(TabMenuItem, content_fn)`, `.tab_disabled(value, label, content_fn)`, `.default_value(value)`, `.size(TabsSize)` (`Small` 32 px / `Medium` 40 px Standard / `Large` 48 px), `.transition(TabsTransition)` (`None`, `Fade`, `Slide` Standard, `SlideLeft`, `SlideRight`), `.on_change(callback)`, `.class(name)`, `.id(id)`, `.with_key(key, state)`.
`cn::tab_item(value)` baut einen vorbereiteten Tab: `.label(l)`, `.icon(svg)`, `.badge(text)`, `.disabled()`, `.content(f)`.

---

### calendar-view

Ein Monatsraster mit Tageszellen, Event-Markierungen und Monatsnavigation. Der gewählte Tag ist ein Signal, Events kommen als reaktive Liste, und das heutige Datum lässt sich vorgeben — deterministisch für Tests und andere Zeitonen.

**Create:**
    cn::calendar(value)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `value` | `Signal<Option<CalendarDay>>` | Reaktives gewähltes Datum (`CalendarDay::new(Jahr, Monat, Tag)` oder `CalendarDay::today()`); `None` = keine Auswahl. |

Builder-Methoden: `.today(day)` (`CalendarDay` — was als heute gilt), `.week_start(weekday)` (0 = Sonntag), `.min_year(jahr)` / `.max_year(jahr)`, `.events(impl IntoReactive<Vec<CalendarEvent>>)`, `.on_change(callback)`, `.class(name)`, `.id(id)`.
`CalendarEvent::new(tag, titel).kind(k).icon(svg)` beschreibt eine Markierung; `events_on(&events, tag)` liefert die Events eines Tages.

---

### list-view

Zwei Werkzeuge für Listen. `ul()` / `ol()` aus `blinc_layout` rendern eine kleine feste Menge Einträge mit Markern und Einrückung; `virtual_list` rendert nur die sichtbaren Zeilen, damit Listen mit tausenden Einträgen günstig bleiben.

**Create:**
    blinc_layout::widgets::list::ul()
    blinc_layout::widgets::list::ol()          // mit ol_start(n) beginnt die Nummerierung anders
    blinc_layout::widgets::list::li()          // ein Eintrag; task_item(checked) mit Checkbox
    blinc_layout::widgets::virtual_list::virtual_list(item_count, builder)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `item_count` | `usize` | Gesamtzahl der Zeilen der virtuellen Liste. |
| `builder` | `Fn(usize) -> impl ElementBuilder` | Baut die Zeile am Index; wird nur für sichtbare Indizes aufgerufen. |

Builder-Methoden — Listen: `.child(ListItem)` (erzeugt mit `li()`), `.child_element(element)` / `.child_box(builder)`, `.marker(ListMarker)`, `.indent(px)`, `.spacing(px)`, `.class(name)`, `.id(id)`; geordnete Listen zusätzlich `.start(n)` (beim Erzeugen `ol_start(n)`).
`virtual_list`: `.estimated_item_height(px)` (angenommene Höhe einer ungesehenen Zeile), `.window_size(n)` (zusätzlich gehaltene Zeilen), `.w(px)` / `.h(px)` / `.w_full()` / `.h_full()`, `.gap_px(px)`, `.p(px)`, `.bg(color)`, `.rounded(r)`, `.border(width, color)`, `.item_class(class)` / `.content_class(class)`, `.class(name)`, `.id(id)`, `.into_div()`.

---

### description-list

Kein direktes Blinc-Äquivalent. Es gibt kein Primitiv für Begriff/Wert-Listen. Mit `cn::table()` (zwei Spalten, ohne `table_header`) oder einer Spalte aus Flex-Zeilen bauen: `div().flex().child(cn::label(term)).child(text(value))`.

---

### grid-view

Kein direktes Blinc-Äquivalent. Es gibt keine Raster-/Kachelansicht. Ein responsives Kachellayout entsteht mit den Layout-Primitiven — `div()` mit Wrap/Flex- oder Grid-Style und `cn::card()`-Kindern — in einem `cn::scroll_area()`, falls es scrollen muss.

---

### repeater

Keine eigene Repeater-Komponente. Wiederholung geschieht in Rust: über die Daten mappen und je Element ein `.child()`, oder `blinc_layout::widgets::virtual_list::virtual_list(anzahl, builder)` bei vielen Einträgen. Eine reaktive Liste kann auch ein `computed`-Kind steuern.

---

### table-of-contents

Kein direktes Blinc-Äquivalent. Es gibt kein Gliederungs-/Anker-Primitiv. Die Gliederung aus `cn::breadcrumb()` oder einer `cn::sidebar()` (`.section()` je Überschriftenebene) bauen und selbst zu den Ankern scrollen — ein eingebautes Scroll-into-View-Ziel gibt es nicht.

---

### timeline

Kein direktes Blinc-Äquivalent für die Ereignis-Timeline. Achtung Namensdopplung: `TimelineHandle` und `TimelineRotation` in `blinc_layout::motion` / `stateful` sind Animations-Timelines, keine Event-Timelines. Eine Event-Timeline als `cn::scroll_area()` aus Zeilen rendern, je mit `cn::avatar()` oder Punkt und `cn::label`s, getrennt durch `cn::separator()`.

---

### bottom-navigation

Keine eigene Bottom-Bar. Teilweise von `cn::navigation_menu()` abgedeckt — eine waagerechte Zeile aus Einträgen und Content-Triggern, die unten in einer Spalte platziert werden kann — aber ohne Mobile-Bottom-Bar-Features (Safe-Area, Badge je Eintrag, aktive Route).

**Create (nächste Lösung):**
    cn::navigation_menu().item(label, on_click)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `label` / `on_click` | `impl Into<String>` / Handler | Ein Ziel in der Zeile; `.trigger(label, content_fn)` ergibt stattdessen ein Dropdown-Panel. |

---

### command

Kein direktes Blinc-Äquivalent. Es gibt keine Command-Palette (Cmd/Ctrl-K). Zusammensetzen: ein `cn::combobox(value).allow_custom(true)` für die Abfrage plus gefiltertes `cn::dropdown_menu`, oder ein per Tastaturbindung geöffnetes `cn::dialog()` mit der Liste darin.

---

### language-switcher

Kein direktes Blinc-Äquivalent. Es gibt keinen Sprachumschalter. Aus `cn::select(value)` (oder `cn::dropdown_menu`) über den Sprachcodes bauen und die Wahl in das Signal schreiben, das die Übersetzungen steuert.

---

### radial-menu

Kein direktes Blinc-Äquivalent. Es gibt kein Radial-/Kreis-Menü. Am nächsten kommen `cn::context_menu()` oder `cn::dropdown_menu()` mit denselben Aktionen als klassische Liste; eine echte Radial-Anordnung braucht per Hand platzierte Kinder mit trigonometrischen Abständen.

---

### toolbar

Kein direktes Blinc-Äquivalent als allgemeine Komponente. Es gibt keinen Toolbar-Container; die einzige Toolbar im Framework ist die Editor-spezifische `selection_toolbar` in `blinc_layout::widgets::rich_text_editor`. Eine Toolbar aus `cn::toggle_group(value)` für Gruppen von Modi, `cn::button(…).size(ButtonSize::Icon)` für Einzelaktionen und `cn::separator().vertical()` zwischen Blöcken bauen.

---

### icon

Ein Strich-Icon aus Pfaddaten, nach Preset oder in Pixeln skaliert und über Theme-Token oder explizite Farbe eingefärbt. Die Pfaddaten kommen aus den Icon-Crates — `blinc_icons` (Lucide) oder `blinc_tabler_icons` (rund 5000 Outline- plus 1000 Fill-Konstanten).

**Create:**
    cn::icon(path_data)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `path_data` | `&'static str` | SVG-Pfaddaten, z. B. `blinc_icons::icons::CHECK` oder eine Konstante aus `blinc_tabler_icons`. |

Builder-Methoden: `.size(IconSize)` (`ExtraSmall` 12 px / `Small` 16 px / `Medium` 20 px Standard / `Large` 24 px / größere Presets), `.size_px(px)`, `.color(ColorToken)`, `.color_value(color)`, `.stroke_width(width)`, `.class(name)`, `.id(id)`.
Wo nur Markup statt eines Elements gebraucht wird, gibt `blinc_tabler_icons::to_svg(pfad, groesse)` (und die Varianten `_filled`, `_colored`, `_with_stroke`) einen SVG-String.

---

### image

Ein Bildelement aus Pfad, URL, Base64 oder Data-URI, mit Object-Fit- und Positionssteuerung sowie einer Software-Filterkette (Helligkeit, Kontrast, Sättigung, Farbton, Graustufen, Sepia, Inversion, Weichzeichnung).

**Create:**
    blinc_layout::image(source)      // Modulpfad: blinc_layout::image::image

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `source` | `impl Into<String>` | Dateipfad, URL, Base64 oder Data-URI. |

Builder-Methoden: `.size(breite, hoehe)` / `.square(groesse)` / `.w(px)` / `.h(px)` / `.w_full()` / `.h_full()`, `.fit(ObjectFit)` mit Kurzformen `.cover()`, `.contain()`, `.fill()`, `.scale_down()`, `.no_scale()`, `.position(ObjectPosition)` / `.position_xy(x, y)` mit `.top_left()` … `.bottom_right()`, `.opacity(wert)`, `.rounded(radius)` / `.circular()`, `.border(breite, farbe)`, `.filter(ImageFilter)` — aus `ImageFilter::none()` durch Setzen von `grayscale`, `sepia`, `brightness`, `contrast`, `saturate`, `hue_rotate`, `invert`, `blur`.

---

### audio-player

Ein Audio-Player mit Transport-Steuerung und optionalem Wellenbild. Er umschließt einen in `blinc_media` erzeugten Player — Laden, Dekodieren und Wiedergabestatus bleiben also außerhalb des Widgets.

**Create:**
    blinc_layout::widgets::media::audio_player(player)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `player` | `Rc<blinc_media::AudioPlayer>` | Die Player-Instanz, die das Widget steuert und anzeigt. |

Builder-Methoden: `.waveform_data(&AudioSamples)` (zeichnet das Wellenbild; mehrkanalige Samples werden zu Mono gemischt), `.w(px)` / `.h(px)` / `.w_full()`, `.bg(color)`, `.rounded(r)`, `.class(class)`, `.id(id)`, `.into_div()`. Einzelne Steuerungs-Elemente gibt es über `MediaControls::new(player)`.

---

### video-player

Ein Video-Player mit Transport-Steuerung um eine `blinc_media`-Player-Instanz.

**Create:**
    blinc_layout::widgets::media::video_player(player)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `player` | `Rc<blinc_media::VideoPlayer>` | Die Player-Instanz, die das Widget steuert und anzeigt. |

Builder-Methoden: `.show_dimensions()` (Blendet die Bildgröße ein), `.w(px)` / `.h(px)`, `.bg(color)`, `.rounded(r)`, `.class(class)`, `.id(id)`, `.into_div()`.

---

### carousel

Kein direktes Blinc-Äquivalent. Es gibt keinen Carousel- oder Slide-Component. Aus einem horizontalen `cn::scroll_area()` (mit `.no_bounce()` und einer Seite je Breite) plus `cn::button`-Pfeilen, die ein Index-Signal ändern, oder einer `cn::tabs(value)`-Leiste, deren Panels als Folien dienen.

---

### gallery

Kein direktes Blinc-Äquivalent. Es gibt keine Galerie-/Lightbox-Komponente. Ein Raster aus `blinc_layout::image(source).square(n)`-Kacheln, Vollansicht per Klick in einem `cn::dialog()` oder `cn::sheet()`.

---

### rich-text-editor

Ein blockbasierter WYSIWYG-Editor: Überschriften, Listen, Trenner und Inline-Auszeichnungen, mit schwebender Auswahl-Toolbar. Der Dokumentzustand liegt außerhalb des Widgets in einem `Arc<Mutex<…>>` und übersteht Neuaufbauten; jeder Edit baut nur den betroffenen Block neu.

**Create:**
    blinc_layout::widgets::rich_text_editor::rich_text_editor(state, theme, content_width)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `state` | `&RichTextState` | Gemeinsamer Dokumentzustand (`Arc<Mutex<RichTextData>>`); erzeugen mit `rich_text_state(RichDocument)`. |
| `theme` | `RichTextTheme` | Visuelle Gestaltung von Blöcken, Auszeichnungen und Toolbar. |
| `content_width` | `f32` | Pixelbreite der Spalte, in der das Dokument gesetzt wird — muss zur Breite des Eltern-Elements passen. |

Zugehörige API: `rich_text_editor::selection_toolbar(state, version, theme) -> Option<Div>` baut die schwebende Toolbar über der aktuellen Auswahl (`None` ohne Auswahl); Block- und Editieroperationen (`set_block_kind`, `toggle_block_kind`, `indent_blocks`, `outdent_blocks`, `insert_divider_after`) ändern das Dokument direkt. Für die Größe ein Eltern-Element mit expliziter Breite verwenden.

---

### code-editor

Eine editierbare Code-Fläche mit Zeilennummern, Undo/Redo, Auswahl und optionaler Syntaxhervorhebung, gesteuert über gemeinsamen Editor-State. Für schreibgeschützte Anzeige gibt es die leichtgewichtigen `code()` / `pre()`-Elemente; `code_minimap()` ergänzt eine MiniMap.

**Create:**
    blinc_layout::widgets::code::code_editor(state)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `state` | `&SharedCodeEditorState` | Gemeinsamer Editor-State (`Arc<Mutex<CodeEditorData>>`); erzeugen mit `code_editor_state(inhalt)`. |

Builder-Methoden (am Editor wie am schreibgeschützten `code()` / `pre()`-Block): `.syntax(SyntaxConfig)` — setzt Highlighter und dessen Farben, `.line_numbers(flag)`, `.font_size(px)`, am Editor zusätzlich `.on_change(\|text\|)` zur Beobachtung von Editierungen. `code_minimap(state)` baut die MiniMap neben dem Editor.

---

### embed

Nicht von Blinc abgedeckt. Es gibt kein Iframe-, Webview- oder Drittanbieter-Embed — das Framework rendert einen eigenen Szenengraphen und hat keine Browser-Oberfläche zum Einbetten. Geladene Inhalte mit `blinc_layout::image` und `cn::card` darstellen oder externe Inhalte über `blinc_layout::widgets::link::open_url(url)` im System-Browser öffnen.

---

### dashboard

Kein direktes Blinc-Äquivalent. Ein Dashboard ist ein Layout, keine Komponente: `cn::card()`-Kacheln in einem Raster oder einer `cn::resizable_group()` anordnen und sie mit der `cn::line_chart`- / `bar_chart`- / `pie_chart`- / `histogram`-Familie sowie `cn::progress` und `cn::badge` für Kennzahlen füllen.

---

### whiteboard

Kein direktes Blinc-Äquivalent. Es gibt kein Leinwand-, Strich- oder Freiformzeichnungs-Primitiv im dokumentierten Komponentenumfang. Ein Whiteboard braucht ein eigenes Zeichenelement; die brauchbaren Bausteine sind ein `div()`-Container fester Größe plus Paint-/Renderer-Ebene und Zeiger-Events.

---

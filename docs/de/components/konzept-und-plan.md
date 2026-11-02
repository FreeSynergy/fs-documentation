# Komponenten: Sortierung, Varianten und Standardisierung

!!! info "Arbeitspapier (Entwurf)"
    Diese Seite ist eine Analyse- und Entscheidungsgrundlage, keine Komponenten-Dokumentation.
    Nach der Freigabe wird sie in `SYSTEM.md` überführt und kann hier gelöscht werden.

Stand der Analyse: `docs/de/components/` (74 Komponenten, 287 Markdown-Dateien) und
Abgleich mit <https://tailgrids.com/docs/components> (61 Komponenten, 600+ Varianten-Beispiele).

!!! info "Umsetzung abgeschlossen (2026-11-01)"
    Aktuell: **10 Kategorien, 83 Komponenten**. Umsortierung, Merges, Welle 1 und 2,
    Standardisierung des Bestands und die Werkzeuge sind fertig — Einzelheiten in
    Abschnitt 10. Die verbindliche Kurzform des Standards steht inzwischen im Abschnitt
    „UI Components“ von `SYSTEM.md` im Hauptverzeichnis.

---

## 1. Was gemeint ist (Kurzfassung)

1. **Weniger Doppelstücke:** Komponenten, die sich nur in einer Kleinigkeit unterscheiden, sind
   keine eigenen Komponenten, sondern **Varianten** einer Komponente.

2. **Beispiel TailGrids:** dort gibt es *weniger* Komponenten als bei uns (61 statt 74), aber
   **dafür zu jeder Komponente 1–11 Varianten auf derselben Seite** (Combobox 10, Date Picker 11,
   Skeleton 9, Select 9). Sortiert wird dort alphabetisch flach — die Tiefe entsteht über Varianten,
   nicht über Ordner.

3. **Lücken finden:** alles, was TailGrids hat und wir nicht (z. B. **Button**, Badge, Tooltip,
   Progress, Skeleton, Label …), wird nachgetragen.

4. **Standardisierung nach OOP-Vorbild:** eine **Basiskomponente** (Elternklasse) definiert
   Attribute, Zustände und Abschnitte, die *alle* Komponenten erben. Jede Komponentendatei
   dokumentiert nur noch das, was **dazukommt** (Override) oder **abweicht**.

---

## 2. Ist-Zustand (gemessen)

| Befund | Zahl |
|--------|------|
| Komponentenordner | **74** (Index behauptet 73) |
| Markdown-Dateien allein unter `components/` | **287** (Index behauptet 97) |
| Komponenten mit `usage.md` + `examples.md` | 29 von 74 |
| Kategorien | 6 (containers, inputs, lists, media, navigation, special) |
| Seiten in `mkdocs.yml`-Nav | **1** (`de/components/index.md`) → 286 Seiten haben keinen Navigationspfad |
| Englische Spiegelversion (`docs/en/components/`) | **0 Dateien** |

**Attribute, die heute schon fast alle mitschreiben** (Kandidaten für die Basisklasse):

| Attribut | Nutzung |
|----------|---------|
| `aria-label` | 73/74 |
| `role` | 69/74 |
| `size` | 68/74 |
| `rounded` | 66/74 |
| `theme` | 65/74 |
| `disabled` | 62/74 |
| `onChange` | 39/74 |
| `variant` | 34/74 |

**Abschnitte, die fast jede Datei hat** (Standard-Gerüst):
`description.md` → Beschreibung (73), Verwendungszweck (72), Features (68), Varianten (nur 29), Best Practices (32).
`attributes.md` → Hauptattribute (74), Event-Attribute (75), Accessibility (73), Styling (68), Verhaltens-Attribute (66).
`appearance.md` → Grundlayout (74), Größe-Varianten (72), Hover-Effekte (71), Farb-Varianten (65).
Daneben existieren 40+ Abschnittsnamen, die nur 1–3× vorkommen — das ist die eigentliche Uneinheitlichkeit.

---

## 3. Das Vererbungsmodell (Elternklasse → Familien → Varianten)

```
Basiskomponente (components/basics/base.md)
   │  vererbt: id, label, visible, enabled/disabled, size, theme, rounded,
   │           variant, state (default/hover/active/focus/disabled/loading/error),
   │           tabIndex, aria-*, role, events (onFocus/onBlur/onClick), animation, gesture
   ├── Feld-Familie (extends base)      → text-input, number-input, textarea, select, combobox, …
   ├── Auswahl-Familie (extends base)   → checkbox, radio-group, switch, rating, slider
   ├── Overlay-Familie (extends base)   → modal, drawer, popover, tooltip, context-menu
   ├── Status-Familie (extends base)    → alert, banner, toast, progress, badge, skeleton
   ├── Medien-Familie (extends base)    → media-player → audio, video, image
   └── Menü-Familie (extends base)      → menu → context-menu, menubar, hamburger
```

Jede Komponenten-Tabelle in `attributes.md` zeigt dann **nur noch eigene Attribute** plus eine
Zeile `Geerbt von: [[basics/base]]`. Geschätzter Effekt: ca. 4–6 Tabellenzeilen pro Komponente
weniger, also rund **350 doppelte Zeilen** weniger Text, die heute bei jeder Änderung 74-mal
angepflegt werden müssten.

### Wann Variante, wann eigene Komponente? (Entscheidungsregel)

| Kriterium | → **Variante** (Attribut `variant`/`type`) | → **eigene Komponente** |
|-----------|-------------------------------------------|--------------------------|
| Gleicher Datensatz, gleiche Events | ja | |
| Nur Aussehen/Andockung ändert sich | ja (`size`, `placement`, `orientation`) | |
| Eigene Datenstruktur nötig (z. B. Vorschlagsliste, Dateistrom) | | ja |
| Eigene Lebensdauer/Fokus-Verhalten (Overlay, Modal) | | ja |
| Accessible Role ändert sich (`button` → `menu`) | | ja |
| Attribute-Überschneidung ≥ 75 % | ja | |

Zusätzlich: **`extends:`-Metadatum** für echte Vererbung (z. B. `context-menu extends menu`,
`audio extends media-player`). Das Ordner bleibt, die duplizierten geerbten Zeilen entfallen.

---

## 4. Doppelstücke und Synonyme (Merge-Vorschläge)

Ähnlichkeit = Überlappung der Attributmengen (Jaccard), automatisch berechnet.

| # | Komponenten | Ähnlichkeit | Empfehlung |
|---|-------------|-------------|------------|
| 1 | `inputs/slider` + `inputs/range-slider` | **0,95** | zusammenlegen → `slider`, Variante `einfach \| bereich` |
| 2 | `inputs/email-input` + `inputs/url-input` (+ `phone-input`) | **0,89 / 0,75** | zusammenlegen → `text-input` mit `type = text, email, url, phone, password` |
| 3 | `inputs/rich-text-editor` + `special/wiki-editor` | **0,89** | zusammenlegen → `rich-text-editor`, Variante `wysiwyg \| wiki-syntax` |
| 4 | `inputs/date-input` + `inputs/datetime-input` (+ `time-input`) | **0,86 / 0,76** | zusammenlegen → `date-input` mit `type = date \| time \| datetime` |
| 5 | `inputs/combobox` + `inputs/dropdown` | **0,80** | beide behalten, aber klar machen: `select` (Liste) und `combobox` (Liste **mit** Freitext) — `native-select` als Variante von `select` |
| 6 | `special/app-embed` + `special/widget-embed` + `special/iframe-embed` | **0,81** | zusammenlegen → `embed` mit `source = iframe \| app \| widget` |
| 7 | `inputs/search-input` + `inputs/search-field` | **0,81** | zusammenlegen → `search-field` mit `variant = simple \| autocomplete \| filter` |
| 8 | `containers/alert` + `containers/banner` | **0,74** | zusammenlegen → `alert` mit `variant = inline \| banner` (Toast bleibt eigen) |
| 9 | `inputs/checkbox` + `inputs/switch` | **0,76** | **beide behalten** (Semantik sofort/anwenden vs. bestätigen), gemeinsame `boolean-input`-Basis |
| 10 | `containers/stepper` + `containers/wizard` | **0,60** | zusammenlegen → `wizard` mit `variant = mit-assistent \| nur-schrittanzeige` |
| 11 | `navigation/toolbar` + `navigation/context-toolbar` + `navigation/ribbon` | 0,56 / mittel | zusammenlegen → `toolbar` mit `variant = standard \| kontext \| ribbon` |
| 12 | `navigation/menu` + `navigation/context-menu` + `navigation/hamburger-menu` | mittel | `menu` als Eltern; `context-menu` (eigene ARIA-Rolle) bleibt eigener Ordner mit `extends: menu`, `hamburger-menu` → Variante `hamburger` |
| 13 | `media/audio` + `media/video` + `special/media-player` | hoch | `media-player` in die Kategorie `media` als **Elternklasse**; `audio`/`video` erben und listen nur Differenzen |
| 14 | `lists/slideshow` + `media/gallery` | mittel | `slideshow` → `media/carousel`; `gallery` bleibt eigen (Galerie ≠ Karussell) |
| 15 | `inputs/number-input` + `inputs/range-slider`/`slider` | 0,59/0,57 | getrennt lassen, aber `number-input` als Datenbasis für `slider` dokumentieren |
| 16 | `containers/card` + `containers/panel` | mittel | beide behalten, gemeinsame `container`-Basis (`collapsible`, `draggable`) |

**Ergebnis:** 74 → **rund 66 eigene Komponenten**, dafür ~35 neue Varianten-Einträge.

Zwei Datenfehler nebenbei: `navigation/menu/description.md` enthält eine Kategorie-Übersicht statt
einer Komponentenbeschreibung (fängt mit `# Navigation` an), und die Zahlangaben im
Komponenten-Index sind veraltet.

---

## 5. Fehlende Komponenten (Abgleich mit TailGrids)

Von den 61 TailGrids-Komponenten haben wir begrifflich ~35 abgedeckt. Lücken, priorisiert:

### Welle 1 — ohne sie ist keine App vollständig (P0)

| Neu | Warum wichtig | Variante-Beispiele |
|-----|---------------|--------------------|
| **button** | fehlt komplett — die meistgenutzte Komponente überhaupt | `primary, secondary, outline, ghost, danger, link`, Größen, `icon-only`, `loading`, `disabled` |
| **button-group** / segmented control | Toolbar-Zusammengehörigkeit, Editoren | zusammengehörige Buttons, aufgeteilt mit Dropdown-Pfeil |
| **label** + **field** (Feld-Wrapper) | Barrierefreiheit, Hilfetext, Fehleranzeige | `visible`, `required`, `help`, `error`, `horizontal/vertical` |
| **separator** / divider | Trennlinie horizontal/vertikal, in Menüs | |
| **link** | Navigation/Routing als eigener Typ mit `href`, `external` | |
| **badge** | Status, Zähler, Tags (Anzeige, nicht Eingabe) | `status, counter, dot, outline` |
| **progress** | Fortschritt (heute nur als *Animation* dokumentiert) | `linear, circular, mit-label, unbestimmt` |
| **spinner** | Ladezustand | |
| **skeleton** | Ladeplatzhalter (heute nur *Animation*) | |
| **tooltip** | Kurzerklärung bei Hover/Langdruck | |
| **popover** | Inhalts-Popover (Unterschied zu tooltip) | |

### Welle 2 — Interaktion und Formulare (P1)

| Neu | Notiz |
|-----|-------|
| **command** (Befehlspalette) | zentral für FreeSynergy-Desktop/Launcher; verwandt mit `search-field` |
| **date-picker** / **time-picker** / **range-calendar** | Auswahl-Overlay + Kalender; ergänzt `date-input` |
| **alert-dialog** | Bestätigungsdialog = `modal` + `alert` (zerstörerische Aktionen) |
| **hover-card** | Vorschau-Karte (Profil, Link-Ziel) |
| **otp-input** | Einmalpasswort bei Anmeldung |
| **scroll-area**, **resizable**, **aspect-ratio** | Layout-Bausteine (`resizable` = Variante von `split-view`) |
| **menubar**, **navigation-menu** (Navbar) | `menubar` = Variante von `menu`, Navbar = Variante von `bottom-navigation`/`menu` |
| **description-list** | Label-Wert-Paare (Detailansichten, Metadaten) |
| **collapsible** | Accordion ohne Gruppierung = Variante von `accordion` |
| **sheet** | Drawer-Variante von der Seite |

### Welle 3 — FreeSynergy-eigene (P2, nur bei Bedarf)

`avatar-group`, `empty-state`, `status-bar`, `onboarding-tour`, `chip`, `breadcrumb-dropdown`,
`file-preview`, `notification-center`.

Umgekehrt: ~39 unserer Komponenten hat TailGrids nicht (whiteboard, wiki-editor, app-embed,
map-view, mention-input, repeater, tree-view, language-switcher …). Die bleiben — sie sind unser
Mehrwert. Nur **media-player** und **wiki-editor** wandern (siehe Tabelle oben).

---

## 6. Neue Sortierung (Vorschlag)

6 Kategorien reichen nicht mehr, weil Overlay-Typen über `containers` *und* `navigation`
verstreut sind und Aktionen (FAB) in `navigation` liegen.

| Kategorie | Inhalt | Änderungen gegenüber heute |
|-----------|--------|----------------------------|
| `basics` | **`base.md` (Basisklasse)**, Design-Tokens, Größen-Raster, Zustände, Barrierefreiheit; `label`, `separator`, `link` | neu |
| `actions` | `button`, `button-group`, `floating-action-button`, `social-button` | FAB zieht von `navigation` um |
| `navigation` | `menu`, `breadcrumb`, `tabs`, `pagination`, `sidebar`, `bottom-navigation`, `language-switcher`, `toolbar`, `command` | `context-toolbar` + `ribbon` → Varianten von `toolbar`; `hamburger-menu` → Variante von `menu` |
| `containers` | `card`, `panel`, `accordion`, `split-view`, `wizard` | `modal`, `drawer` → `overlays`; `toast`, `alert`, `banner` → `feedback`; `stepper` → Variante von `wizard` |
| `overlays` | `modal`, `drawer`, `popover`, `tooltip`, `hover-card`, `context-menu`, `alert-dialog` | neu (zieht aus `containers` + `navigation`) |
| `feedback` | `alert`, `toast`, `progress`, `spinner`, `skeleton`, `badge`, `empty-state` | neu |
| `fields` | `field`, `text-input`, `number-input`, `textarea`, `select`, `combobox`, `checkbox`, `radio-group`, `switch`, `slider`, `rating`, `tags-input`, `*-picker`, `file-upload`, `otp-input`, `mention-input` | wie bisher `inputs`, plus Picker |
| `data` | `list-view`, `table`, `grid-view`, `tree-view`, `timeline`, `calendar-view`, `repeater`, `table-of-contents`, `description-list`, `avatar`, `chart` | wie bisher `lists` + Anzeigeelemente |
| `media` | `media-player` (Eltern), `audio`, `video`, `image`, `icon`, `gallery`, `carousel` | `slideshow` → `carousel`; `media-player` zieht von `special` her |
| `special` | `embed`, `code-editor`, `whiteboard`, `map-view`, `dashboard` | Editoren zusammengelegt, Embeds zusammengelegt |

**Namenskonvention** (einheitlich, Kleinbuchstaben mit Bindestrich):

- `-input` für Felder mit Datentyp, `-picker` für Auswahl mit Overlay/Dialog, `-editor` für
  Editoren, `-view` für Datenansichten, `-menu` / `-bar` für Navigationsleisten.

- Verzeichnisse englisch (wie heute), Abschnittsüberschriften deutsch, Attributnamen
  `camelCase` englisch. Singular einheitlich: `breadcrumbs` → `breadcrumb` lassen wir, weil
  der Ordnername bereits gesetzt ist, dokumentieren aber den englischen Fachbegriff.

---

## 7. Standardisierung des Dateisatzes

**Dateien pro Komponente (Ziel):**

| Datei | Pflicht? | Inhalt |
|-------|----------|--------|
| `description.md` | ja | Beschreibung, Verwendungszweck, Varianten-Tabelle, Abgrenzung („nicht verwechseln mit“), Best Practices |
| `appearance.md` | ja | Grundlayout (ASCII), Größen, Farben/Zustände, reaktives Verhalten |
| `attributes.md` | ja | **nur eigene Attribute** + Verweis auf die geerbten Basis-Attribute |
| `usage.md` | ja | Anwendung, Szenarien **und** Beispiele (heute `usage.md` + `examples.md` getrennt → zusammenlegen, die Überlappung ist groß) |

Fixe Abschnittsreihenfolge (damit 74 Dateien vergleichbar sind):
`Beschreibung → Verwendungszweck → Varianten → Features → Abgrenzung → Best Practices → Siehe auch`
bzw. `Grundlayout → Varianten → Größen → Farben und Zustände → Hover/Fokus → Reaktiv`
bzw. `Hauptattribute → Verhalten → Darstellung → Events → Barrierefreiheit → Geerbt von`.

**Der „Steckbrief“ als Maske (das ist die Elternklasse in Dokumentform):**
zu Beginn jeder `description.md` eine kleine Tabelle — bewusst keine YAML-Frontmatter, weil
Frontmatter in diesem Repo bereits bewusst entfernt wurde (Commit `24ba83c`), die Tabelle kann
ein Mensch lesen *und* ein Skript auswerten:

| Feld | Beispiel (`search-field`) |
|------|---------------------------|
| Kategorie | `fields` |
| Erbt von | `base`, `text-input` |
| Kategorien-Eltern | `fields/index.md` |
| Varianten | `simple`, `autocomplete`, `filter` |
| Zustände | `default`, `focus`, `loading`, `error`, `disabled` |
| Gesten | `tap`, `type`, `swipe` (Vorschläge) |
| Animationen | `fade-in`, `expand` |
| Verwandt | `search-input` (→ Variante), `combobox`, `command` |
| Status | dokumentiert / nur Skizze / fehlt |

Damit wird auch die Querverbindung zu `gestures/` und `animations/` endlich Maschinen-lesbar —
heute existieren diese Querverweise nur als Fließtext.

---

## 8. Werkzeuge (damit es nicht wieder auseinanderläuft)

Angelehnt an `tools/gen_skin_indexes.py` schlagen wir zwei Skripte vor:

1. `tools/gen_component_indexes.py` — baut `components/index.md` und die `*/index.md` der
   Kategorien aus den Steckbriefen neu (Zahlen stimmen dann automatisch).

2. `tools/check_components.py` — prüft und meldet:
   - fehlende Pflichtdateien / fehlende Pflichtabschnitte,
   - Attribute, die nicht in der Basisklasse stehen, aber in ≥ 60 % der Komponenten (→ hochziehen),
   - Doppelstücke (Ähnlichkeitswert wie oben) und Synonyme,
   - Seiten, die nicht in `mkdocs.yml` stehen.

---

## 9. Vorgeschlagene Reihenfolge der Umsetzung

1. **Basisklasse schreiben** (`basics/base.md`) + Steckbrief-Feld definieren — Grundlage für alles Weitere.
2. **Merges aus Tabelle 4** (15 Schritte, je ein Ordner + `variants`-Tabelle, Verweis-Seite für alte Pfade).
3. **Neue Komponenten Welle 1** (11 Stück) mit dem neuen Standard-Gerüst.
4. **Umsortierung** (Tabelle 6) + `mkdocs.yml`-Nav für die Kategorien und die wichtigsten Komponenten ergänzen.
5. **Welle 2**, danach `docs/en/components/` gespiegelt anlegen.
6. Skripte aus Abschnitt 8 in den CI-Workflow (`deploy.yml`) aufnehmen.

## 10. Entscheidungen (Stand 2026-11-01, abgestimmt)

1. **Alte Ordnernamen:** ersatzlos streichen, keine Weiterleitungs-Seiten.
2. **`usage.md` + `examples.md` zusammenlegen:** ja. Die Inhalte werden ohnehin
   demnächst überschrieben, weil die Umsetzung auf Rust (voraussichtlich Blinc)
   umgestellt wird; die Diskussion dazu folgt separat.

3. **Kategorien:** voller Umbau auf die 10 Kategorien aus Abschnitt 6.
4. **Bestandskomponenten:** sofort alle auf das „nur eigene Attribute“-Modell
   umstellen. Die Basisklasse dokumentiert das in `basics/base.md`; die Migration
   erfolgt über `tools/standardize_components.py`.

5. **Englische Spiegelung:** erst nach Abschluss der deutschen Version.

### Umgesetzt

**Grundlagen**

- `basics/base.md` — Basisklasse mit geerbten Attributen, Größen-Raster,
  Zuständen, Steckbrief-Maske, Namenskonvention und Entscheidungsregel
- Die zehn Zielkategorien aus Abschnitt 6 sind angelegt, jede mit `index.md`

**Umsortierung und Merges (Abschnitte 4 und 6)** — `tools/restructure_components.py`

- 36 Komponentenordner in die Zielkategorien verschoben,
  dabei umbenannt: `inputs/dropdown` → `fields/select`,
  `lists/slideshow` → `media/carousel`, `special/media-player` → `media/media-player`
- 16 Merges aus Tabelle 4 mit Varianten-Tabelle und Standardisierungshinweis:
  `banner` → `alert`, `range-slider` → `slider`, `email-input`/`url-input`/`phone-input`
  → `text-input`, `datetime-input`/`time-input` → `date-input`,
  `search-input` → `search-field`, `stepper` → `wizard`,
  `context-toolbar`/`ribbon` → `toolbar`, `hamburger-menu` → `menu`,
  `wiki-editor` → `rich-text-editor`, `app-embed`/`widget-embed`/`iframe-embed` → `embed`
- Alte Ordnernamen ersatzlos gestrichen (Beschluss 1); alle internen Verweise
  im gesamten `docs/`-Baum auf die neuen Pfade gezogen
- `inputs/` und `lists/` als Kategorien aufgelöst

**Bestand standardisiert**

- `examples.md` → `usage.md`, generische Basis-Attribute aus `attributes.md` entfernt
  (`tools/standardize_components.py`)
- Steckbrief-Tabelle in allen Komponenten ergänzt, `Siehe auch` überall vorhanden
  (`tools/add_steckbrief.py`)
- Abschnittsnamen vereinheitlicht, Reihenfolge genormt, Tabellen mit fehlender
  `Default`-Spalte repariert (`tools/standardize_sections.py`)
- Fehlende `usage.md` ergänzt (32 Dateien, abgeleitet aus Beschreibung und
  Attributen; `tools/gen_usage_pages.py`)

**Welle 1** (12): `basics/label`, `basics/separator`, `basics/link`,
`actions/button`, `actions/button-group`, `feedback/badge`, `feedback/progress`,
`feedback/spinner`, `feedback/skeleton`, `fields/field`, `overlays/tooltip`,
`overlays/popover` — zusätzlich `basics/kbd`, `fields/input-group`

**Welle 2** — neu angelegt: `navigation/command`, `fields/date-picker`,
`fields/time-picker`, `fields/range-calendar`, `fields/otp-input`,
`overlays/alert-dialog`, `overlays/hover-card`, `containers/scroll-area`,
`data/description-list`. Als **Varianten** dokumentiert (keine eigenen Ordner):
`resizable` → `split-view`, `collapsible` → `accordion`, `sheet` → `drawer`,
`menubar` → `menu`, Navbar → `bottom-navigation`.

**Welle 3** — `feedback/empty-state` angelegt; die übrigen Vorschläge bleiben
zurückgestellt (siehe unten).

**Werkzeuge und CI (Abschnitt 8)**

- `tools/gen_component_indexes.py` — schreibt `components/index.md`, jede
  Kategorien-Übersicht und den Nav-Abschnitt in `mkdocs.yml` aus den Steckbriefen;
  damit stimmen Zahlen und Navigation automatisch
- `tools/check_components.py` — prüft Pflichtdateien, Steckbrief, Abschnitte,
  Tabellenzellen, tote Links, fehlende Basis-Attribute, Doppelstücke und
  Nav-Vollständigkeit; läuft mit `gen_component_indexes.py --check` in CI
- `mkdocs.yml`: Nav für alle Kategorien und alle Komponenten (keine Seite ohne Nav-Pfad)

### Ausstehend

**Arbeitsstand optionale Abschnitte (Fortsetzungspunkt, Stand 2026-11-01)**

Von den 193 fehlenden optionalen Abschnitten sind **177 ergänzt**; es bleiben **16 Abschnitte
in 9 Komponenten**. Vollständig fertig sind `fields` (18), `data` (10), `media` (7),
`special` (4), `navigation` (9) sowie `containers/accordion` und `containers/card`.

Offen — je Komponente die noch fehlenden Abschnitte:

| Komponente | fehlt |
|------------|-------|
| `actions/floating-action-button` | `Abgrenzung`, `Reaktiv` |
| `containers/panel` | `Reaktiv` |
| `containers/split-view` | `Abgrenzung` |
| `containers/wizard` | `Abgrenzung`, `Reaktiv` |
| `feedback/alert` | `Reaktiv` |
| `feedback/toast` | `Abgrenzung`, `Reaktiv` |
| `overlays/context-menu` | `Abgrenzung`, `Reaktiv` |
| `overlays/drawer` | `Abgrenzung`, `Reaktiv` |
| `overlays/modal` | `Abgrenzung`, `Größen`, `Reaktiv` |

Dazu die noch leeren Steckbrief-Felder: **Zustände 19, Gesten 21, Animationen 16** —
betroffen sind vor allem die jungen Komponenten aus Welle 1 und 2 (`button`, `button-group`,
`label`, `link`, `separator`, `kbd`, `field`, `badge`, `progress`, `spinner`, `skeleton`,
`tooltip`, `popover`, `embed`) sowie die oben genannten neun.
Erlaubte Namen: Gesten aus `docs/de/gestures/<kategorie>/` (`tap`, `double-tap`, `long-press`,
`drag`, `swipe`, `flick`, `edge-swipe`, `force-press`, `hover`, `draw-gesture`, `pinch`,
`spread`, `rotate`, `two-finger-tap`, `two-finger-long-press`, `three-finger-swipe`,
`shake`, `tilt`, `flip`, `wave`, `pull-to-refresh`, `drag-and-drop`), Animationen aus `docs/de/animations/`
(`fade-in`, `expand`, `slide-in`, `stagger`, `collapse`, `highlight`, `press`, `pulse`,
`spin`, `progress`, `skeleton`, `tick-draw`, `reorder`, …).

**So wird weitergemacht**

Die exakte Liste liefert jederzeit `python3 tools/_tmp_missing_sections.py`
(fehlende Abschnitte pro Komponente plus leere Steckbrief-Felder).

1. Abschnitte in der Reihenfolge aus [`basics/base.md`](./basics/base/) einfügen
   (`description.md`: Beschreibung → Verwendungszweck → Varianten → Features → Abgrenzung →
   Best Practices → Siehe auch; `appearance.md`: Grundlayout → Varianten → Größen →
   Farben und Zustände → Hover- und Fokus-Effekte → Reaktiv).
2. `python3 tools/standardize_sections.py --apply` — ordnet Abschnitte, mappt Aliasnamen.
3. `python3 tools/gen_component_indexes.py` — Index, Kategorie-Übersichten und mkdocs-Nav neu.
4. `python3 tools/check_components.py` (und mit `--strict`), danach `mkdocs build`.

**Nebenbei bereits gefixt** (Datenfehler im Bestand):

- kaputte oder doppelte Varianten-Tabellen: `date-input`, `avatar`, `chart`, `gallery`,
  `radio-group`, `list-view`, `table`, `timeline`, `audio`, `video`, `icon`, `image`
- doppelte Beispiel-Blöcke aus `description.md`/`appearance.md` entfernt (gehören nach
  `usage.md`, Beschluss 2): `image`, `video`
- Varianten- und Abschnittsnamen deutsch vereinheitlicht, veraltete Titel berichtigt
  (`list-view`, `calendar-view`, `carousel`, `select`, `media/audio`)
- **Welle 3, Rest:** `avatar-group`, `status-bar`, `onboarding-tour`, `chip`,
  `breadcrumb-dropdown`, `file-preview`, `notification-center` — nur bei Bedarf
- **Englische Spiegelung** `docs/en/components/` (Beschluss 5)
- **`usage.md` auf Rust/Blinc umstellen** (Beschluss 2): die Beispiele sind bewusst
  syntaxneutral gehalten
- **Einzelprüfung erledigt:** `combobox` und `select` erreichen 0,75 Ähnlichkeit; beide bleiben
  eigen. Die Abgrenzung steht jetzt in beiden `description.md`
  (`select` = nur vorhandene Optionen, `combobox` = zusätzlich Freitext und Vorschläge).

## Siehe auch

- [Komponenten-Übersicht](./index.md)
- [Standardisierte Daten](../data/) — Felder, Typen, Konventionen (dasselbe Prinzip, nur für Daten)
- [Gesten](../gestures/) und [Animationen](../animations/)

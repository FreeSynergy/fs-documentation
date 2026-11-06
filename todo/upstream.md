# ToDo – Upstream (Issues/Feature-Requests, schreibt der Nutzer)

Wünsche an Fremdprojekte aus ADR 0015. Agenten tragen hier ein, der Nutzer schreibt das Issue.
Muster: `Projekt · Wunsch · Begründung · Status (offen / Issue #… / erledigt)`.

## Blinc
### Fehler aus fs-components (Blinc 0.6.0, Thread 1, 2026-11-06; noch nicht gemeldet, Nachstellung im Bericht und in `fs-components/DESIGN.md`)
- Rich Text: Umbruch wird in einer Schnittstärke gemessen, Fett und Kursiv werden in anderer gezeichnet; Zeilen laufen über oder überlappen (`rich_text_styled` mit fettem Abschnitt über einen Umbruch, Box 400 px).
- `text("x").italic()` zeichnet aufrecht; kursiv geht nur im Rich Text.
- `RichText`-Links rufen immer `open_url`; kein Klick-Handler für interne Links.
- Emoji ohne Schrift: leer gezeichnet, aber mit Breite; mit `blinc_noto_emoji::register()` viele als Kästchen.
- 3000 Absätze ohne `min_h(0)`: Abbruch mit wgpu-`write_buffer`-Validierungsfehler statt Fehlermeldung.
- Ein Absatz mit 30 KB: Sekunden beim Textmessen (vorher 8,7 s im Release).
- `BlincContextState::init` löst beim zweiten Aufruf einen Panic aus, auch über Threads hinweg.
- **Kein Haken beim Schließen des Fensters:** Entwürfe gehen ohne eigene Sicherung verloren (wir sichern deshalb selbst).
- Kleinere: `Scroll` hat kein `flex_1`; `min_w` neben `w(0.0)` wird ignoriert; Textfeld bricht enger um als seine Box; `cn_styles`-Doku nennt das nicht vorhandene `register_cn_styles`.
(Befunde `temp/research/blinc-health-and-parsers.md`; Antwort des Autors 2026-11-05 in ADR 0009)

**Ablauf beim Autor:** git-bug-Issue anlegen → im GitHub-Issue erwähnen → bei neuen Funktionen
zuerst im RFC-Kanal (Discord) besprechen → PR.

- IME: mobil geplant (evtl. 0.6.1), Desktop-Preedit nachfragen · beim Autor in Arbeit
- Barrierefreiheit: Tastatur-Navigation in 0.6.0; mobil geplant 0.6.1; Screenreader (AccessKit) nachfragen · beim Autor in Arbeit
- `code_editor`: Hervorhebung per eigenem Trait einhängbar → **wir** bauen syntect-Adapter (pure Rust); Messung Puffer vs. Zeile · unsere Aufgabe
- Text-Shaping: harfrust — Autor sieht es sich an · beim Autor
- `wgpu` auf 26 festgenagelt · offen
- Roadmap = git-bug · erledigt (gelesen: `temp/research/blinc-issues.md`)
- **Gesten: Stift (Druck, Neigung), generischer Swipe, Zwei-Finger-Pan/Rotate** — Autor: Beiträge willkommen · **unser Beitrag** (RFC-Kanal zuerst)
- **cn-Komponenten** aus dem Rückstand (bf7c901) und unsere neuen (Messenger) — Autor: Beiträge willkommen · **unser Beitrag**
- **Beitrags-Kandidaten aus der Messenger-Zerlegung** (je erst git-bug-Issue + RFC-Kanal):
  - Wisch-/Zieh-Gesten an Listenzeilen (vorher 9ab9dc6 klären) · kein Issue
  - umgekehrte, unten verankerte `virtual_list` (Chat, oben nachladen) · kein Issue
  - `html_view()` mit Sperre für Fernladen · a782b47
  - Chips / `tags-input` · Teil von bf7c901 prüfen
  - `date_picker`, `time-picker` · bf7c901
  - Inline-Elemente (Erwähnung, Emoji) im Rich-Text-Editor · kein Issue
  - allgemeine `toolbar`, `command`-Palette, `empty-state`, Dropfläche für `file-upload` · kein Issue
  - Combobox-Hover · 8115bf5
- **Befunde Thread 4, 0.6.0** (Reproduktion und Fundstellen: `fs-components/DESIGN.md`, „Blinc notes“; alle aus dem Lesen des Codes, nicht vor dem Autor nachgestellt) · kein Issue:
  - Elemente, die außerhalb eines Build-Durchlaufs entstehen (`stateful`-Callback baut `stateful` oder `cn`), bekommen jedes Mal neue Keys, und `STATEFUL_DEPS` schrumpft nie; alte Callbacks laufen weiter. Umgangen: Bildschirmwechsel in der Hülle ist ein voller Rebuild.
  - `State::update` erreicht `stateful` nur über einen Callback, den `BlincContextState::init` nicht setzt; das Fenster überspringt seine Init, wenn zuvor ein Bild lief. `Signal::update` geht. Umgangen.
  - Auf dem Visual-Pfad behält der eigene Knoten eines Live-Bereichs die Klassen des ersten Zeichnens, und ein Kind ohne Handler den Handler des ersetzten Knotens. Klassen umgangen (inneres Element), Handler nicht.
  - `blinc_noto_emoji::register()` fügt die Schrift bei jedem Aufruf erneut hinzu, entgegen der Doku. Umgangen (`Once`).
  - `ThemeState::init` reiht alle CSS-Quellen bei jedem Aufruf neu ein; nur ein Fenster leert die Warteschlange. Nicht umgangen, harmlos.
  - `BlincContextState::init` panikt, wenn zwei Threads gleichzeitig zum ersten Mal initialisieren. Umgangen durch eine gemeinsame Sperre in `fs-components-render`, sobald der Reader darauf umgestellt ist.
  - Kein Weg, von einem Arbeits-Thread aus auf den Oberflächen-Thread zu posten und die Ereignisschleife zu wecken. Für uns offen: `fs-components-app` kann Hintergrundarbeit nicht melden.
- Ansehen: Repo `blinc_abi` (IDE auf Blinc-Teilmenge) als Referenz für den Code-Editor · offen

## rPGP
- Panik bei unbekanntem AEAD-Byte (`pgp-0.21.0/src/crypto/aead.rs:276`), ausgelöst durch eine fremde Mail; in `fs-messenger-mail` abgefangen · Nutzer schreibt · offen

## Turso / libSQL
## Web of Trust
## Kanidm
## Zentinel

## RustFS
- Zusammenarbeit anfragen: `fs-files` nutzt RustFS als optionales S3-Backend, auch für Zustellung online (ADR 0044) · Nutzer schreibt · offen. Hinweis: Das Repo hat eine `CLA.md`, vor Beiträgen lesen.

## Kanidm
- SCIM für Gruppen, auch verschachtelt: Form der API ändert sich noch (ADR 0024, kanidm#4638); für `fs-groups` nachfragen · offen

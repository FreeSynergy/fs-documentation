# ToDo – Upstream (Issues/Feature-Requests, schreibt der Nutzer)

Wünsche an Fremdprojekte aus ADR 0015. Agenten tragen hier ein, der Nutzer schreibt das Issue.
Muster: `Projekt · Wunsch · Begründung · Status (offen / Issue #… / erledigt)`.

## Blinc
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
- Ansehen: Repo `blinc_abi` (IDE auf Blinc-Teilmenge) als Referenz für den Code-Editor · offen

## Turso / libSQL
## Web of Trust
## Kanidm
## Zentinel

## RustFS
- Zusammenarbeit anfragen: `fs-files` nutzt RustFS als optionales S3-Backend, auch für Zustellung online (ADR 0044) · Nutzer schreibt · offen. Hinweis: Das Repo hat eine `CLA.md`, vor Beiträgen lesen.

## Kanidm
- SCIM für Gruppen, auch verschachtelt: Form der API ändert sich noch (ADR 0024, kanidm#4638); für `fs-groups` nachfragen · offen

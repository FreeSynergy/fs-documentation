# CONVENTIONS

Dieses Verzeichnis ist das **Gedächtnis des Repos**. Ein Agent (Opus, Sonnet, llama, Leo)
liest **zuerst** diese Datei. Es gibt kein Session-Gedächtnis über Sitzungen hinweg –
deshalb gilt: **jede neue Festlegung wird sofort hier eingetragen.** Was hier steht,
gültig für alle Repos, bis ausdrücklich geändert.

Das konkrete Dateisatz- und Layout-Handwerk steht in `doku-standard.md` (hier im Verzeichnis).

Stand: 2026-11-05 (ADRs 0011–0039: nur `en`, `frontends/`, nichts kopieren, Standards/AS2,
Fremdprojekte, Lizenz, Repos, Messenger)

---

## 0. Grundsätze (Kurzfassung, Details in den ADRs)

- **Funktionen analysieren, nichts kopieren** — auch nicht aus OSS (ADR 0013); nur im äußersten
  Notfall aus offenen Projekten, nie Closed Source, Lizenz/Urheber bleiben (ADR 0025).
- **Immer die neueste tragfähige Technik**, Altes nur als Brücke nach außen (ADR 0026).
- **Beschlossenes bleibt.** Erweist sich ein Beschluss als falsch, ersetzt ihn ein neuer ADR
  ausdrücklich — nie stilles Abweichen (ADR 0032).
- **Standards zuerst**, ActivityStreams 2.0 als Basis; fehlt ein Standard → eigener Entwurf
  → IETF/W3C (ADR 0014).
- **100 % Rust**, keine doppelten Crates; Blinc, Turso, Web of Trust, Kanidm, Zentinel werden
  genutzt und unterstützt (ADR 0015).
- **`MIT OR Apache-2.0`, für immer kostenlos**, keine Armutsdiskriminierung (ADR 0016).
- **Programm = Kategorie**: `FreeSynergy.Messenger`, Repo `fs-messenger`; jedes Programm läuft
  allein, zusammen teilen sie die Arbeit über Standarddaten (ADR 0017).
- **Nur `docs/en/` wird gepflegt**, `de/` übersetzt llama (ADR 0011).
- **Daten:** `fs-store` je Programm, `fs-hub` je Gerät, Abgleich auf Objektebene (ADR 0019);
  Objekt = AS2-Hülle + Fachstandard + Aktivitätsprotokoll, Leihen = Live-Verweis, Regeln werden
  angesagt (ADR 0020). Programm ohne Hub speichert lokal, wahlweise verschlüsselt (ADR 0024).
- **Schnittstelle:** Cap'n Proto ist der Vertrag, JSON/CLI/MCP daraus erzeugt (ADR 0021);
  bis zu vier Referenz-Frontends je Programm, am besten Suiten (ADR 0038); jedes Programm ist mindestens eine Workbench (ADR 0037); drei Text-Editoren (ADR 0039); Verteilung über Git/gix (ADR 0036); Darstellungs-Register Datentyp ↔ Element (ADR 0023).

## 1. Was veröffentlicht wird und was nicht

- `docs/` ist der **einzige** veröffentlichte Teil (was `mkdocs build` zu `site/` baut).
  In `fs-documentation` kommen nur Dokumentationen hin – auch technische. Offen und
  transparent, kein bezahlter Anteil.
- Alles außerhalb von `docs/` ist Repo-Unterstützung und wird **nicht** gebaut:
  `conventions/` (Regeln), `todo/` (Aufgaben), `temp/` (unsortiert), `scripts/` (Werkzeuge).
- Grundsatz: **Plan, Beschluss, Vorgabe, Entwurf, Werkzeug → nicht in `docs/`.**

Dieselbe Schale (`conventions/`, `todo/`, `temp/`, `scripts/`) steht in **jedem** Repo.
Andere Repos (Code) enthalten keine Doku, bestenfalls Hilfs-Doku.

## 2. Architektur – sechs Ebenen

Eine Leiter. Achse: zunehmende Offenheit und Lauffähigkeit. Die Achse wechselt bei
Ebene 4 den Charakter (Werkzeug → Produkt).

| Ebene | Ordner | läuft allein? | Beispiele |
|-------|--------|---------------|-----------|
| 1 | `primitives` | nein | text-input, slider, button, badge |
| 2 | `widgets` | nein | Kanban, calendar-view, vCard, map-view, table |
| 3 | `workbenches` | nein | whiteboard, code-editor, dashboard |
| 4 | `apps` | ja | Kalender-App, Editor-App (Menü, Speichern) |
| 5 | `suites` | ja, mehrere zusammen | ERP, CRM, Demokratie, Groupware |
| 6 | `platform` | trägt alles | Shell, Identität (Kanidm), Envelope |

Zwei Schirm-Ordner in der Doku:

- `components/` = Bauebene → `primitives/`, `widgets/`, `workbenches/`
- `programs/` = Laufebene → `apps/`, `suites/`, `platform/`

Querschnitt (eigene Top-Level-Zweige, **nicht** unter `components`):

- `interactions/` → `gestures/`, `animations/` (Querband durch alle Ebenen)
- `data/` → standardisierte Daten (macht Ebene 5 erst möglich)

Unter jeder Programmkategorie: `frontends/<programm>/<version>/` (Dateisatz ADR 0012,
Vorlage `conventions/templates/frontend/`) und `requirements.md` (Pflichtmenge + Kür aus den
Frontends, mit unserem Umsetzungsstatus, ADR 0006/0013).

Jede Ebene hat ihren eigenen `index.md`.

**Test Frage pro Band:**
- primitive: nicht weiter zerlegbar
- widget: *kennt seine Inhalte beim Bauen* (bindet ein bekanntes `data/`-Modell), endliche Kinder, eigener Zustand
- workbench: *erhält Inhalte erst zur Laufzeit*, offen, darf selbst primitives+widgets aufnehmen

### Grenze Bauebene ↔ Laufebene (beschlossen 2026-11-03, ADR 0005)

App und Widget sind **derselbe Kern in unterschiedlicher Größe**. Die App bettet das Widget
ganzzahlig und baut keine zweite Darstellung. Was die App zusätzlich bringt, ist die Hülle:

| | Widget (Ebene 2) | App (Ebene 4) |
|---|---|---|
| Ergebnis | ein **Wert** (Tag, Zeitraum, Auswahl) für ein Feld | ein lauffähiges Programm |
| Fläche | eingebettet, Größe vom Aufrufer | ganzer Bildschirm, eigene Aufteilung |
| Menü, Toolbar | nein | ja |
| Fenster, Adresse, Sichten | nein | ja |
| Bearbeiten | nur im Dienst des Wertes, bei Schreibrecht | eigene Bearbeitungsflächen |
| Export, Ausgabeformate, Druck | nein | ja (ICS, CSV, Drucklayout) |
| Einstellungen, Weckrufe, Teilen | nein | ja |

Faustregel: *Alles, was das Widget zeigt, kann die App größer.* Alles, was ein Menü, eine
Adresse, eine Datei oder eine Einstellung braucht, ist App. Wächst einem Widget das an,
verlässt es die Bauebene (offen + lauffähig → `workbenches/`, mit Menü und Fenster →
`programs/apps/`). Darstellung wird nicht doppelt beschrieben: sie steht im Widget, die
App-Doku hält nur die Hülle fest.

## 3. Komponenten-Einteilung (beschlossen 2026-11-03)

Zuordnung der 84 Komponenten. Bei Abweichung beim physischen Umsortieren korrigieren.

**primitives/**
- basics: `base`, `kbd`, `label`, `link`, `separator`
- actions: `button`, `button-group`, `floating-action-button`
- feedback: `alert`, `badge`, `empty-state`, `progress`, `skeleton`, `spinner`, `toast`
- fields: `checkbox`, `color-input`, `combobox`, `date-input`, `field`, `input-group`,
  `mention-input`, `number-input`, `otp-input`, `radio-group`, `rating`, `search-field`,
  `select`, `slider`, `switch`, `tags-input`, `text-input`, `textarea`
- media: `icon`, `image`

**widgets/**
- containers: `accordion`, `card`, `panel`, `scroll-area`, `split-view`, `wizard`
- navigation: `bottom-navigation`, `breadcrumb`, `command`, `language-switcher`, `menu`,
  `pagination`, `radial-menu`, `sidebar`, `tabs`, `toolbar`
- overlays: `alert-dialog`, `context-menu`, `drawer`, `hover-card`, `modal`, `popover`, `tooltip`
- data: `avatar`, `calendar-view`, `chart`, `description-list`, `grid-view`, `list-view`,
  `repeater`, `table`, `table-of-contents`, `timeline`, `tree-view`
- fields (aus fields): `file-upload`
- pickers (aus fields): `date-picker`, `emoji-picker`, `range-calendar`, `time-picker`
- media (Player): `audio`, `video`, `media-player`, `carousel`, `gallery`
- special: `map-view`

**workbenches/**
- special: `code-editor`, `dashboard`, `embed`, `whiteboard`
- fields: `rich-text-editor`

**Neu geplant (Messenger-Zerlegung 2026-11-05, `temp/messenger-components.md`) — Doku fehlt noch:**
- primitives/feedback: `message-status` (wird gesendet/gesendet/zugestellt/gelesen/Fehler),
  `encryption-state` (Verschlüsselungsart; unverschlüsselt markiert; **anklickbar**, führt zur Anleitung — darum kein `badge`)
- widgets/data: `message-list` (Konversation, unten verankert, nachladend, Trenner ⚠️ evtl. Variante von `timeline`),
  `message-bubble`, `mail-view`, `reaction-bar`, `link-preview`
- widgets/fields: `rule-editor` (Regeln „wenn … dann …“, gespeichert als Sieve)
- widgets/overlays: `key-verification` (Schlüssel/Gerät prüfen, Vertrauen bestätigen)
- widgets/media: `call-controls` (gehört zum eigenen Anruf-Programm, ADR 0037)
- workbenches/special: `message-composer` (Empfänger, Betreff, einfacher Editor, Anhänge, Emoji, Erwähnung),
  `html-view` (fremdes HTML bereinigt, ohne Fernladen)
- workbenches/fields: `block-editor` (ADR 0039)

**Drei Text-Editoren (ADR 0039):** `code-editor` = einfacher Editor (Markdown + Code),
`rich-text-editor` = erweiterter Editor (WYSIWYG, ODF), `block-editor` = Block-Editor (neu).

**Änderungsbedarf an vorhandenen Components (Messenger):**
`list-view` (Mehrfachauswahl, Wisch-Aktionen je Richtung — Gesten kommen aus dem Frontend, ADR 0037 —,
„nächste ungelesene“, virtuelle Zeilen) · `tags-input` (Variante `recipients`: JSContact-Vorschlag,
Schlüsselstatus je Chip) · `mention-input` (auch als Inline-Element im Editor) · `rich-text-editor`
(Nur-Lese-Modus, Ausgabe HTML und Markdown) · `emoji-picker` (Variante Reaktion, zuletzt benutzt) ·
`toolbar` (schwebend; Ribbon mit `tabs`) · `separator` (Beschriftung mittig) · `avatar` (Anwesenheit
an Datenfeld binden) · `badge` (Abgrenzung zu `encryption-state` vermerken) · `file-upload`
(verschlüsselter Upload, Zwischenablage) · `embed` (Verweis auf `html-view`) · `timeline` (Verhältnis zu `message-list`).

**Wo gebaut wird (Leitlinie):** interaktive Grundbausteine **ohne Fachwissen → Beitrag zu Blinc**
(passt zu Blincs Plan c422b97); alles, was ein **Datenmodell bindet** (Nachricht, Konversation,
Verschlüsselung, Sieve) → **unsere Schicht** (ADR 0023). Liste: `todo/upstream.md`.

Festgelegte Grenzfälle:
- `*-picker`, `range-calendar` → **widget** (Overlay + Liste, endliche Auswahl)
- Overlays (`modal`, `drawer`, …) → **widget** (eigene Lebensdauer, kein offenes Editieren)
- `map-view` → **widget** (bindet Geodata-Modell, Inhalt bekannt)
- `dashboard`, `embed` → **workbench** (offener Container / fremder Inhalt)
- `rich-text-editor` → **workbench** (offene Editierfläche)
- `combobox`, `tags-input`, `search-field`, `mention-input` → **primitive** (Feldfamilie)
- `link` → **primitive** (zerlegbar wie `label`/`kbd`, bei Umzug 2026-11-03 ergänzt)
- `file-upload` → **widget** (endliche Kinder: Picker, Dropfläche, Vorschau; eigene
  Zustände; keine offene Bearbeitungsfläche — bei Umzug 2026-11-03 ergänzt)
- `message-composer` → **workbench** (enthält den Editor, selbst eine Workbench; 2026-11-05)
- `html-view` → **workbench** (fremder Inhalt erst zur Laufzeit, wie `embed`; 2026-11-05)
- `encryption-state` → **primitive**, nicht `badge` (bedienbar; 2026-11-05)

## 4. Sprache (ADR 0011 — nur Englisch wird gepflegt)

- **Immer englisch:** Dateinamen, Pfade, Ordner, Bezeichner, Code, Kommentare, Commits.
- **Gearbeitet wird nur in `docs/en/`.** `docs/de/` (und weitere Sprachen) erzeugt llama als
  Übersetzung. `de/` darf als Informationsquelle gelesen werden; fehlt es dort auch → in `en/`
  neu schreiben.
- **Nicht übersetzt:** `temp/`, `todo/`, `conventions/`, `scripts/`.
- **Deutsch erlaubt und erwünscht:** Beschlüsse, Pläne, Prompts, Fragen an Agenten
  (`conventions/`, `temp/`, `todo/`) und der Gesprächsverkehr.
- Nie über Sprachbäume hinweg verlinken: in `en/` zeigt jeder Verweis auf `en/`.

## 5. Skripte (`scripts/`) – Schattenbaum

Der Pfad eines Skripts zeigt, worauf es wirkt (Spiegel von `docs/`):

```
scripts/check.py                       -> ganzer Baum
scripts/components/check.py            -> alles unter components/
scripts/components/actions/check.py    -> nur actions/
```

Namenspräfix = Zweck:

| Präfix | Tun | Exit |
|--------|-----|------|
| `check_*` | prüft gegen Vorgabe, meldet Verstoß | !=0 bei Fehler |
| `gen_*` | erzeugt index.md / Dateien / Nav | 0 |
| `fix_*` | repariert automatisch | 0 |

Bestehende Generatoren/Prüfer liegen noch oben in `scripts/` (Pfad-Mathematik unverändert);
neue Bereichs-Prüfer kommen in den Schattenbaum. Wegwerf-Skripte: `_tmp_*.py` (gelöscht),
Einmal-Migrationen in `scripts/_archive/`.

**Skripte statt Handarbeit (2026-11-05).** Wiederkehrendes wird als Skript gebaut — spart
Tokens und ist wieder verwendbar. Erst prüfen, ob es schon ein Werkzeug gibt; dann
erweitern statt neu schreiben. **Keine neuen Einmal-Skripte für Umzüge/Umbenennungen**, sondern
eine Regeldatei für die allgemeinen Werkzeuge:

| Werkzeug | Zweck |
|----------|-------|
| `scripts/move.py` | Dateien per Regex-Regeln verschieben/umbenennen, Links exakt mitziehen, `mkdocs.yml`-Nav und `temp/sync_state.json` umschlüsseln, `git mv`. Dry-Run ohne `--apply`; `--links-only`, `--moves-only` (Fortsetzen) |
| `scripts/replace.py` | Text per Regex-Regeln ersetzen (Begriffe, Pfadtexte, Linkbeschriftungen), Bericht je Regel, `--skip-code` |
| `scripts/rules/*.rules` | Regeldateien (`REGEX => ERSATZ`), je Umbau eine Datei — dokumentiert zugleich, was geändert wurde |
| `scripts/fix_links.py` | heuristische Reparatur kaputter Links über Namensregister (Notnagel, wenn Regeln nicht reichen) |

Nach jedem Umbau: `mkdocs build` und die Zahl der Link-Warnungen vorher/nachher vergleichen.
Hintergrundjobs benutzen Git parallel; `move.py` wiederholt `git mv`, solange `index.lock`
belegt ist.

Skripte dürfen ein LLM anstoßen: lokales Modell = llama.cpp unter `http://localhost:8080`
(höchstens 2 parallele Anfragen, §7), Prompt per POST. Kein Netz, keine Kosten.
Schlüssel/Adresse in nicht veröffentlichte Config, nie in den Code.

## 6. temp/ – unsortiert

`temp/` ist der Eingangskorb: Dateien, deren endgültiger Platz noch offen ist. Von hier
werden sie später einsortiert. Nicht in `docs/` belassen, bis der Platz feststeht.

## 7. todo/ – Aufgaben nach Modell

Drei KIs, um Tokens zu sparen — jede bekommt nur, was sie gut kann:

| Liste | Wer | Wofür |
|-------|-----|-------|
| `todo/opus.md` | Claude Opus (Plan) + Sonnet (Umsetzung) | Architektur, Beschlüsse, Spezifikation, Review (Opus); Skripte, Umbauten, Code nach fertiger Spezifikation (Sonnet) |
| `todo/llama.md` | llama.cpp lokal (`http://localhost:8080`, Qwen3.8-Flash-Next) | Übersetzung `en → de`, kleine Massenaufgaben (Umformatieren, Zusammenfassen). **Höchstens 2 parallele Anfragen** — läuft eine Übersetzung, ist nur noch ein Platz frei |
| `todo/leo.md` | Brave Leo (vom Nutzer per Hand bedient) | Recherche: Rohmaterial zu Programmen, Standards, Crates. Ergebnisse sind ungeprüft (⚠️), Opus prüft |
| `todo/upstream.md` | Nutzer | Issues/Feature-Requests an Fremdprojekte (ADR 0015) |

Eintrag im gleichen Muster: `Aufgabe · Ebene · Dateien · Status`.

## 8. Ablauf

- Nach jeder Änderung: **commit und push**. Push durch Agenten ist nur in der laufenden
  Umbauphase erlaubt (Stand 2026-11-05); danach fragt der Agent vor jedem Push.
- **Keine eigenen Agenten anlegen.** Bei Bedarf legt der Nutzer etwas Neues an.
- Beschlüsse als nummerierte ADRs in `conventions/decisions/` (Format: Kontext →
  Entscheidung → Folgen, mit Verweis auf betroffene Doku).

## 9. Sprach- und Link-Technik (wichtig fürs Umbauen)

Die Doku verlinkt **relativ und tiefsensitiv** (`../textarea/`, `../../basics/base/`,
`../../../animations/...`). Jeder Umzug, der die Ordner**tiefe** ändert, bricht diese
Links. Deshalb tiefe Umzüge (components-Bänder, programs-Level, interactions) nur mit
Link-Mitschrift + `mkdocs build` als Verifikation, Baum für Baum.

Der Komponenten-Nav in `mkdocs.yml` wird von `scripts/gen_component_indexes.py` zwischen
den Markern `# BEGIN/END components nav` neu geschrieben.

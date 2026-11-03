# CONVENTIONS

Dieses Verzeichnis ist das **Gedächtnis des Repos**. Ein Agent (qwen, Übersetzer, Opus)
liest **zuerst** diese Datei. Es gibt kein Session-Gedächtnis über Sitzungen hinweg –
deshalb gilt: **jede neue Festlegung wird sofort hier eingetragen.** Was hier steht,
gültig für alle Repos, bis ausdrücklich geändert.

Stand: 2026-11-03

---

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

Jede Ebene hat ihren eigenen `index.md`.

**Test Frage pro Band:**
- primitive: nicht weiter zerlegbar
- widget: *kennt seine Inhalte beim Bauen* (bindet ein bekanntes `data/`-Modell), endliche Kinder, eigener Zustand
- workbench: *erhält Inhalte erst zur Laufzeit*, offen, darf selbst primitives+widgets aufnehmen

## 3. Komponenten-Einteilung (beschlossen 2026-11-03)

Zuordnung der 84 Komponenten. Bei Abweichung beim physischen Umsortieren korrigieren.

**primitives/**
- basics: `base`, `kbd`, `label`, `separator`
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
- pickers (aus fields): `date-picker`, `emoji-picker`, `range-calendar`, `time-picker`
- media (Player): `audio`, `video`, `media-player`, `carousel`, `gallery`
- special: `map-view`

**workbenches/**
- special: `code-editor`, `dashboard`, `embed`, `whiteboard`
- fields: `rich-text-editor`

Festgelegte Grenzfälle:
- `*-picker`, `range-calendar` → **widget** (Overlay + Liste, endliche Auswahl)
- Overlays (`modal`, `drawer`, …) → **widget** (eigene Lebensdauer, kein offenes Editieren)
- `map-view` → **widget** (bindet Geodata-Modell, Inhalt bekannt)
- `dashboard`, `embed` → **workbench** (offener Container / fremder Inhalt)
- `rich-text-editor` → **workbench** (offene Editierfläche)
- `combobox`, `tags-input`, `search-field`, `mention-input` → **primitive** (Feldfamilie)

## 4. Sprache

- **Immer englisch:** Dateinamen, Pfade, Ordner, Bezeichner, Code, Kommentare, Commits.
- **Deutsch erlaubt:** Prosa in `docs/de/`, Beschlüsse, Prompts, Fragen an Agenten.
- **Keine manuelle Übersetzung nötig:** um Hilfe bitten geht auf Deutsch. Die englische
  Doku (`en/`) wird vom Übersetzer-Modell aus `de/` erzeugt (siehe `todo/translator.md`),
  nicht von Hand. Deutsch ist Quelle der Wahrheit, Englisch Ableitung.
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

Skripte dürfen ein LLM anstoßen: lokales Modell = lokaler HTTP-Endpunkt (z. B.
`http://localhost:11434/api/generate`), Prompt per POST. Kein Netz, keine Kosten.
Schlüssel/Adresse in nicht veröffentlichte Config, nie in den Code.

## 6. temp/ – unsortiert

`temp/` ist der Eingangskorb: Dateien, deren endgültiger Platz noch offen ist. Von hier
werden sie später einsortiert. Nicht in `docs/` belassen, bis der Platz feststeht.

## 7. todo/ – Aufgaben nach Modell

Drei Listen, je eine pro LLM:

- `todo/qwen.md` – aktuell: Struktur, Vorgaben, Umzüge
- `todo/translator.md` – NPU-Modell: nur Übersetzung
- `todo/opus.md` – später: Plan + Programmierung (schweres Zeug)

Eintrag im gleichen Muster: `Aufgabe · Ebene · Dateien · Status`.

## 8. Ablauf

- Nach jeder Änderung: **commit und push** (immer).
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

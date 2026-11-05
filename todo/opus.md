# ToDo – Opus (Plan) + Sonnet (Umsetzung)

Opus: Architektur, Beschlüsse, Spezifikation, Review. Sonnet: Skripte, Umbauten, Code nach
fertiger Spezifikation. Muster: `Aufgabe · Ebene · Dateien · Status · Wer`.
Grundsätze: `conventions/CONVENTIONS.md` §0, ADRs 0011–0018.

---

## Phase 0 – Beschlüsse festhalten (2026-11-05)

- [x] ADRs 0011–0018 (nur en, frontends+Version, nichts kopieren, Standards/AS2, Fremdprojekte,
      Lizenz, Repos, Messenger) · conventions/decisions · Opus
- [x] CONVENTIONS.md §0/§2/§4/§7/§8 nachgezogen · Opus
- [x] Vorlagen `conventions/templates/frontend/`, `…/suite/` · Opus
- [x] todo/ neu: opus, llama, leo, upstream · Opus
- [x] Lizenz: `LICENSE-APACHE` + `LICENSE-MIT`, README · Opus
- [ ] `conventions/doku-standard.md`: Abschnitt „6-File-Per-Program“ durch ADR-0012-Dateisatz
      ersetzen, Pfade `masks/` → `frontends/` · Sonnet · offen
- [x] `temp/architektur-protokoll.md`: Kopfhinweis „Maske“ → „Frontend“, §20 P4 „kopieren“ ersetzt · Opus

## Phase 1 – Umbau der Struktur (nur `docs/en/`, de folgt per Skript)

- [x] Allgemeine Werkzeuge `scripts/move.py` + `scripts/replace.py` + `scripts/rules/` (2026-11-05) · Opus
- [x] `masks/<p>/` → `frontends/<p>/latest/` in `en/` **und** `de/` (1231 Dateien, 1897+213 Links,
      850 sync-state-Schlüssel), `menu`→`menus`, `structure`→`layout`; Regeln
      `scripts/rules/masks_to_frontends.rules` · Opus
- [x] Wortlaut in `en/`: mask/skin → frontend (`scripts/rules/masks_to_frontends_text.rules`,
      Formular-„masks“, CSS-Masken, Emoji-Hautfarben ausgenommen) · Opus
- [x] Build-Prüfung: Warnungen vorher 223, nachher gleich; die 213 in `programs/` sind Links auf
      noch nicht übersetzte `en`-Dateien (Ziel existiert in `de/`) — Übersetzung, kein Umbaufehler
- [ ] **Versionsnummern**: Ordner heißen vorerst `latest/` (dokumentiert ist die aktuellste Version).
      Liste: `temp/frontend-versions-missing.txt` (119). Nummern → `temp/frontend-versions.tsv`
      (`programm<TAB>version`), dann umbenennen mit
      `python3 scripts/move.py --scope docs/en --scope docs/de --rules scripts/rules/frontend_versions.rules --table version=temp/frontend-versions.tsv --default version=latest --sync-state temp/sync_state.json [--apply]`
      · Recherche Leo/llama, Ausführung Sonnet
- [x] `scripts/gen_frontend_indexes.py` (ersetzt `gen_skin_indexes.py`, archiviert): `en/`,
      Marker-Blöcke, idempotent, `--check`, `--extract-themes`, `--suggest-versions` (2026-11-05) · Opus
- [x] Alle 77 Programmseiten in `en/`: Titel, „What it is“, „Notable ideas“ (Platzhalter),
      „Documented versions“ mit fehlenden Pflichtdateien; 8 Themes aus `layout.md` ausgelagert;
      11 `requirements.md`-Gerüste; `doku-standard.md` auf ADR 0012 umgestellt · Opus
- [ ] **Notable ideas** je Programm ausfüllen — 77 Platzhalter. Nur für Programme, die bleiben;
      die anderen werden nicht gelöscht, nur nicht weiter gepflegt (ADR 0013) · Opus entscheidet je
      Kategorie, Leo recherchiert („Was kann X, was andere nicht können?“)
- [ ] **themes/** für die übrigen Programme (Generator listet sie als „Missing required files“) ·
      Leo/Sonnet; vorhandene Themes-Texte sind dünn (Element: „Clear hierarchy“) → nachrecherchieren
- [ ] `gen_frontend_indexes.py --check` in die CI, sobald die Hintergrund-Übersetzung von
      `frontends/` durch ist (sonst schlägt jeder neue `en`-Text die CI) · Sonnet
- [ ] Messenger: Protokolle (Matrix …) aus `frontends/` nach `data/messages/standards.md` (ADR 0018) · Opus
- [ ] `interactions/` aufräumen: Gesten-Achse Finger / Maus / Stift (ADR 0015), Landing-Page
      `interactions/index.md` · Opus plant, Sonnet setzt um
- [ ] Altlasten aus der früheren qwen-Liste:
      - `de/data/contacts/jscontact/`: Link `../../geodaten/` → `geodata/`
      - kaputtes Verzeichnis `docs/de/components/fields/otp-input/input-group/` (12 Fehler in
        `check_components.py`) — in `en/` prüfen, ob es dort auch existiert
      - `calendar-view` an das Muster von `date-picker` anziehen
      - Steckbrief-Felder leer (Zustände 19, Gesten 21, Animationen 16)
      - `temp/components-konzept-und-plan.md` einsortieren (Abschnitt 10 = Restoffenes)

## Phase 2 – Datenfundament (Standards, AS2)

- [x] contacts + identity (2026-11-05) · Opus
- [x] messages (2026-11-05): MIMI, Original + Hülle (ADR 0030) · Opus
- [x] events (JSCalendar 2.0) · documents (ADR 0031/0033/0034) · geodata · projects · profile · login (2026-11-05)
- [x] `data/standards.md`: AS2-Abbildung für alle Domänen, Lückenliste (Kandidaten eigener Specs)
- [x] OpenID Federation 1.0 für Föderation zwischen Instanzen (ADR 0035); Kanidm-SCIM korrigiert (ADR 0024)
- [ ] Eigene Specs (Reihenfolge festlegen): Blockformat · Markieren · Kollektionsprofil · Hilfe-Schlüssel ·
      Kanban/Aufgabenbeziehungen · DPV-Feldtabelle · WebFinger-Linkprofil · Nachrichten-Lücken · Kalender-Lücken
- [ ] Bibliothek: erster Eintrag „So verschlüsselst du deine Mails“ (ADR 0018/0031)
- [ ] Gespräch: gitoxide als Versionskontrolle überall vs. Aktivitätsprotokoll
- [ ] Gespräch mit Nutzer: Datenhaltung (zentral / pro Programm, Abgleich, Turso) — Protokoll §3/§4
- [ ] Gespräch mit Nutzer: Messenger-Backend (tuwunel/Matrix vs. SMTP/JMAP), unverschlüsselte
      Eingänge (ADR 0018)
- [ ] Einordnung Web of Trust ↔ Kanidm (Identität vs. Vertrauen) · Opus, Recherche Leo

## Phase 3 – Funktionen je Kategorie → Schnittstelle

Pro Kategorie, Reihenfolge nach Nutzen (Vorschlag: messenger, contact, calendar, wiki):
1. Frontends sichten, Programme mit **Notable ideas** auswählen/ergänzen (ADR 0013)
2. `requirements.md`: Pflicht + Kür, Status je Fähigkeit
3. Fähigkeitenliste (Protokoll §9, `temp/ableitungen/faehigkeiten.md`)
4. Schnittstellen-Spezifikation (API-Vertrag) des Programms `fs-<category>`

## Phase 4 – Programmieren (Sonnet nach Spezifikation)

- primitives → widgets → workbenches (auf Blinc 0.6.x, ADR 0009) → apps
- Repo je Programm `fs-<name>`, `MIT OR Apache-2.0`
- Fehlendes in Blinc → `todo/upstream.md`

## Phase 3 – Messenger (Brücke von beiden Seiten)

- [x] requirements.md (29 + 44 Kür + 13 nicht), Zerlegung in Components, Referenz-Frontend Nr. 1 (Entwurf),
      Outlook `m365-2026-11` + Apple Mail `ios-26` aus Bildern (2026-11-05)
- [x] Components einsortiert: 13 neu, 12 Änderungen, Blinc-Beitragsliste (CONVENTIONS §3, `todo/upstream.md`)
- [ ] Doku-Gerüste für die 13 neuen Components (Vorlage wie bestehende: description/appearance/attributes/usage) · Sonnet
- [ ] Darstellungs-Register: erste Einträge `Conversation`, `Message`, `Encryption` (ADR 0023) · Opus
- [ ] **Schnittstelle `fs-messenger`**: erstes Cap'n-Proto-Schema aus den Gruppen der requirements · Opus
- [ ] Referenz-Frontend Nr. 1 sehen und testen (Nutzer) — Gesten gelten für Mails **und** Nachrichten

## Phase 4 – Groupware (Plan 2026-11-05, Nacht)

Ziel: Wiki, Kontakte, Kalender, Karten, Messenger auf **denselben Daten**; Suite `fs-groupware` als
Container der Einzelprogramme (ADR 0017/0037). Linux zuerst, dann Windows/macOS, dann Smartphones.

**Regeln für die Nacht:** Rust-Hygiene ADR 0041 (`cargo build -j 4`, nach jeder Sitzung
`scripts/clean_rust.py --apply`); **RAM ist knapp** (≈ 6 GB frei neben llama) → höchstens zwei Builds
gleichzeitig; GitHub: `fs-store` und `fs-components` **existieren aus der alten Version** → nur lokal
bauen, nicht pushen, Nutzer entscheidet (archivieren/übernehmen); freie Namen öffentlich anlegen.

| # | Paket | Repo | Hängt ab von | Wer | Status |
|---|-------|------|--------------|-----|--------|
| 1 | Cap'n-Proto-Compiler in Rust, Orakel-Tests gegen capnpc-embedded (ADR 0040) | `fs-capnpc` (crate `capnp-compiler`) | — | Sonnet | offen |
| 2 ✅ | Objektspeicher: UUIDv7, AS2-Hülle, Turso eingebettet hinter Trait, Aktivitätsprotokoll in derselben Transaktion, begrenztes Rückgängig (ADR 0019/0020/0027/0042) | `fs-store` (lokal) | — | Sonnet | ✅ 22 Tests (2026-11-05) |
| 3 | Text-Kern: Rope + Markierungen (ADR 0033/0042), Markdown hinein/heraus (pulldown-cmark), Link-Tabelle, Vorlagen | `fs-wiki` (crate `fs-text` im Workspace) | (2) später | Sonnet | offen |
| 4 ✅ | `common.capnp` (Uuid, Timestamp, Cursor, Problem, Blob) | `fs-documentation/temp/contracts` | — | Opus | ✅ |
| 5 ✅ | Doku-Gerüste der 13 neuen Components (+ Skripte auf `en`) | `fs-documentation` | — | Sonnet | ✅ |
| 6 | Datenmodelle Kontakte (JSContact) / Kalender (JSCalendar 2.0) / Karten (GeoJSON, PMTiles on demand) | `fs-contacts`, `fs-calendar`, `fs-maps` | 2 | Sonnet | später |
| 7 | Wiki-Workbench auf Blinc (Code-Modus, liest `fs-documentation`) | `fs-wiki` | 3, Blinc | Sonnet | später |
| 8 | Suite `fs-groupware` (Container, Workbenches nebeneinander) | `fs-groupware` | 6, 7 | — | später |
| 9 | Hub (`fs-hub`): Anmeldung der Programme, Objekt-Abgleich | `fs-hub` | 2 | — | später |

**Fragen für den Morgen:**
- alte Repos `fs-store`/`fs-components` archivieren und Namen übernehmen?
- GitHub-Anbindung darf in der Org keine Repos anlegen (404) → Repos anlegen oder Berechtigung geben; lokal: fs-capnpc, fs-store, fs-wiki, fs-contacts, fs-calendar, fs-maps
- fs-store: `max_steps` global oder je Person? Schutzbedürftige Objekte in unverschlüsseltem Speicher standardmäßig ablehnen (heute so)? Grabsteine nach Abgleich + Aufräumen behalten? Aktivitäten als volle Vorher/Nachher-Bilder (heute) oder RFC-6902-Patches?


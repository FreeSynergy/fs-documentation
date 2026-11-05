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
- [ ] `scripts/gen_skin_indexes.py` → `gen_frontend_indexes.py`: auf `docs/en/`, `frontends/`,
      englische Texte (läuft heute auf `de/` mit `masks/`, ist **nicht** in der CI) · Sonnet
- [ ] Bestehende Frontends an ADR-0012-Dateisatz anpassen: `themes/` anlegen (Farbschema aus
      `layout.md` herausziehen), `index.md` um „Notable ideas“ + „Documented versions“ · Sonnet,
      pro Kategorie, nur für Programme, die bleiben (ADR 0013)
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

- [ ] `data/standards.md`: Spalte „AS2-Abbildung“ + Abschnitt „Gaps“ (ADR 0014) · Opus
- [ ] Pro Domäne (contacts, events, messages, identity, geodata, projects, profile, login):
      Standard festlegen, AS2-Abbildung, Lücken · Opus, Recherche Leo
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

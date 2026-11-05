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

- [ ] Skript `scripts/_archive/migrate_masks_to_frontends.py` (Einmal-Migration): ·Sonnet
      `programs/*/*/masks/<p>/` → `frontends/<p>/<version>/`; Version aus `index.md`/`description.md`
      lesen, sonst `unknown` + Liste für Nachrecherche; `menu.md`→`menus.md`,
      `structure.md`→`layout.md`; `index.md` bleibt auf Programmebene
- [ ] `masks/index.md` → `frontends/index.md` je Kategorie · Sonnet
- [ ] `scripts/gen_skin_indexes.py` → `gen_frontend_indexes.py`, CI/`mkdocs.yml` nachziehen · Sonnet
- [ ] `scripts/fix_links.py --force`, `mkdocs build` ohne Link-Warnungen · Sonnet
- [ ] Messenger: Unterordner prüfen, Protokolle (Matrix …) aus `frontends/` nach
      `data/messages/standards.md` (ADR 0018) · Sonnet
- [ ] Gleiches Skript auf `docs/de/` laufen lassen · Sonnet
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

# ToDo – qwen (Struktur, Vorgaben, Umzüge)

Modell: qwen3.8 · Scope: Struktur, Konventionen, physische Umzüge

## erledigt
- Repo-Schale angelegt: `conventions/`, `todo/`, `temp/`, `scripts/` (2026-11-03)
- `tools/` → `scripts/`, Wegwerf-Skripte weg, Einmal-Migrationen → `scripts/_archive/` (2026-11-03)
- Nicht-Doku-Arbeitsdateien nach `temp/` (2026-11-03)
- CONVENTIONS.md + ADRs 0001–0004 (2026-11-03)
- `scripts/migrate_links.py` geschrieben und getestet (2026-11-03)
- `interactions/` umgesetzt: gestures + animations (de+en) umgezogen, 63 Links, Nav (2026-11-03)
- `conventions/` umbenannt (konventionen -> conventions, KONVENTIONEN.md -> CONVENTIONS.md) (2026-11-03)
- `programs/` umgesetzt: apps(11)/suites(5)/platform(desktop+crates), 473 Links, Nav; `crates/` -> platform (2026-11-03)
- `SYSTEM.md` → `conventions/doku-standard.md` ueberfuehrt, Blöcke aktualisiert, Verweise nachgezogen (2026-11-03)
- `gen_skin_indexes.py` an `programs/<ebene>/<kategorie>/` angepasst (ROOT, Pfadtexte, Referenzen); 14 Skin-Indizes neu erzeugt, Pfadnotizen `docs/de/apps/...` berichtigt; von Hand gepflegte Hautseiten (wiki, messenger, desktop) bleiben verschont (2026-11-03)
- `components/` Bänder umgesetzt: 84 Komponenten + `base.md` nach primitives(34)/widgets(45)/workbenches(5) verschoben, 378 Links neu gesetzt, Generator aufs Band-Modell umgestellt, Nav neu, Build fehlerfrei (2026-11-03)
- `scripts/fix_links.py` geschrieben: LöST interne Links über Namens-Registry aus docs/ (kein Tiefen-Räsonnement), nach jedem Umzug `--force` (2026-11-03)
- Doppelstück bereinigt: `fields/otp-input/input-group/` war eine ältere Kopie von `fields/input-group/` — entfernt, `link` und `file-upload` in CONVENTIONS §3 nachgetragen
- ADR 0005 gefasst: App und Widget gleicher Kern, Huelle (Menue, Export, Einstellungen) trennt Ebene 2 von 4; Grenze in CONVENTIONS.md §2, Abgrenzung in date-picker und calendar-view nachgezogen (2026-11-03)

## offen
- `interactions/index.md` als Landing-Page ergaenzen · Status: offen (optional)
- 9 defekte Links in `en/` (fehlende `animations/`- und `components/`-Spiegel) und 1 in `de/data/contacts/jscontact/` (`../../geodaten/` → `geodata/`) · Status: offen, uebersetzer-Betreff
- `temp/components-konzept-und-plan.md` einsortieren (Abschnitte 1–9 sind abgearbeitet, Abschnitt 10 haelt Restoffene fest) · Status: offen
- Steckbrief-Felder leer: Zustaende 19, Gesten 21, Animationen 16; 16 optionale Abschnitte in 9 Komponenten · Status: offen (Inhalt, nicht Struktur)
- Kaputtes Verzeichnis aufraeumen: `docs/de/components/fields/otp-input/input-group/` (vier Doku-Dateien liegen verschachtelt in otp-input, die echte Komponente ist `fields/input-group/`) · `check_components.py` meldet dazu 12 Fehler · Status: offen
- `calendar-view` ist noch nicht standardisiert (usage.md ohne Szenarien, attributes.md ohne Datenanbindung, Steckbrief-Felder leer) — an das Muster von `date-picker` (commit 3c037a2) anziehen · Status: offen

## Hinweis
- Eigene Agenten werden nicht automatisch angelegt. Neue Aufgabe/Modell = neue Liste hier.

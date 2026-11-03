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

## offen
- `scripts/gen_skin_indexes.py` an `programs/<level>/` anpassen (ROOT + Pfadtexte), dann Skin-Indizes neu erzeugen (Pfadnotizen `docs/de/apps/...` sind veraltet, aber keine defekten Links) · Status: offen
- `interactions/index.md` als Landing-Page ergaenzen · Status: offen (optional)
- `components/` Bänder primitives/widgets/workbenches physisch umsetzen + `gen_component_indexes.py` ans Band-Modell anpassen · Ebene 1–3 · Status: offen
- `SYSTEM.md` aufloesen: normative Teile nach conventions/, Rest nach docs/de Beitragend · Status: offen

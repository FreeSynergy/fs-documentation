# ToDo – qwen (Struktur, Vorgaben, Umzüge)

Modell: qwen3.8 · Scope: Struktur, Konventionen, physische Umzüge

## erledigt
- Repo-Schale angelegt: `konventionen/`, `todo/`, `temp/`, `scripts/` (2026-11-03)
- `tools/` → `scripts/`, Wegwerf-Skripte weg, Einmal-Migrationen → `scripts/_archive/` (2026-11-03)
- Nicht-Doku-Arbeitsdateien nach `temp/` (2026-11-03)
- KONVENTIONEN.md + ADRs 0001–0004 (2026-11-03)

## offen
- `interactions/` anlegen: `gestures/` + `animations/` hinein (de+en), Verweise + Nav nachziehen · Ebene Querschnitt · Status: offen (Link-Mitschrift nötig)
- `programs/` aus `apps/`: Level apps/suites/platform vergeben, Kategorien zuordnen, Verweise + Nav · Ebene 4–6 · Status: offen
- `components/` Bänder primitives/widgets/workbenches physisch umsetzen + `gen_component_indexes.py` ans Band-Modell anpassen · Ebene 1–3 · Status: offen
- Link-Mitschrift: Helfer `scripts/migrate_links.py` schreiben (relativ, tiefsensitiv) · Status: offen
- `crates/` (untracked) später nach `programs/platform/` · Status: offen

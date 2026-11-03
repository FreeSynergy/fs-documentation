# 0003 – Repo-Schale und Skript-Schattenbaum

## Kontext
Pläne und Vorgaben lagen verstreut in `docs/` (z. B. `apps/plan.md`,
`components/konzept-und-plan.md`). Skripte hießen `tools/` ohne erkennbare Zuordnung.

## Entscheidung
- In `fs-documentation` nur Doku in `docs/`. Nur `docs/` wird gebaut.
- Jede Repo bekommt dieselbe Schale außerhalb von `docs/`:
  `conventions/` (Gedächtnis), `todo/` (Aufgaben), `temp/` (unsortiert), `scripts/`.
- `tools/` → `scripts/`. Schattenbaum: Skript-Pfad = Wirkungsbereich (Spiegel von `docs/`).
  Präfix = Zweck: `check_` / `gen_` / `fix_`.
- Nicht-Doku-Arbeitsdateien aus `docs/` nach `temp/` (unsortiert) verschoben.

## Folgen
CI (`deploy.yml`) ruft `scripts/...` auf. Vorhandene Generatoren bleiben oben in
`scripts/` (Pfad-Mathematik unverändert); neue Bereichs-Prüfer kommen in den Schattenbaum.
Wegwerf-Skripte (`_tmp_*`) gelöscht, Einmal-Migrationen nach `scripts/_archive/`.

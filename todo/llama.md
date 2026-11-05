# ToDo – llama.cpp (lokal)

Modell: Qwen3.8-Flash-Next (IQ3_S) · Endpunkt `http://localhost:8080` · Rechner Beelink GTR9 Pro
**Höchstens 2 parallele Anfragen.** Läuft die Übersetzung, ist nur noch **ein** Platz frei.

Scope: Übersetzung und kleine Massenaufgaben. Kein Planen, keine Entscheidungen.

## Regeln (ADR 0011)
- Quelle ist **nur `docs/en/`**. Übersetzt wird `en → de` (später weitere Sprachen).
- Nicht übersetzen: `temp/`, `todo/`, `conventions/`, `scripts/`.
- Nie über Sprachbäume hinweg verlinken: in `de/` zeigt jeder Link auf `de/`.
- Prüfer: `scripts/doc_sync.py` (ADR 0010), Zustand `temp/sync_state.json`.
  `python3 scripts/doc_sync.py --en docs/en --de docs/de --state temp/sync_state.json --list temp/translation-queue.md`
  Nach jeder Datei `--confirm <pfad>`.

## offen
- Hintergrund (läuft): `en/` dort aufbauen, wo es noch fehlt (aus `de/`), nur fehlende Dateien ·
  ganzer Baum · Status: läuft
- Nach dem Umbau `masks/` → `frontends/` (Phase 1): `de/` neu aus `en/` übersetzen statt von
  Hand nachzuziehen · Status: wartet auf Phase 1

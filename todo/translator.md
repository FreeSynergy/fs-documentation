# ToDo – Übersetzer (NPU-Modell)

Modell: NPU · Scope: **nur Übersetzung** `de → en` (und weitere Sprachen). Kein Planen,
kein Programmieren.

## offen
- `en/`-Spiegel an neue Struktur anpassen, sobald `components/programs/interactions`
  feststehen (Namesräume der Pfade mitziehen) · Status: wartet auf Struktur
- Bestehende Lücken `en/animations/…` (Build meldet fehlende Ziele) nachziehen · Status: offen

## Regel
- Deutsch ist Quelle. Übersetzung erzeugt/hält `en/`, nie umgekehrt.
- Nie über Sprachbäumen hinweg verlinken: in `en/` zeigt jeder Link auf `en/`.

## Arbeitsliste (seit 2026-11-04)

Übersetzung · ganzer Baum · `temp/translation-queue.md` · Status: 1492 Dateien offen

- Prüfer: `scripts/doc_sync.py` – Zustand `temp/sync_state.json` ist die Wahrheit, die Liste ist
  nur seine Ansicht.
- Lauf: `python3 scripts/doc_sync.py --en docs/en --de docs/de --state temp/sync_state.json \
    --list temp/translation-queue.md`
- Abhaken in der Liste ist Absicht; erst `--confirm <pfad>` setzt die Datei auf `VERIFIED` –
  dann fällt sie in der Liste weg und bleibt ruhig, bis sich ihr Hash ändert.
- Nach jeder übersetzten Datei: `--confirm` nicht vergessen, sonst erscheint sie erneut.

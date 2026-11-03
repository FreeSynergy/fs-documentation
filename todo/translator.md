# ToDo – Übersetzer (NPU-Modell)

Modell: NPU · Scope: **nur Übersetzung** `de → en` (und weitere Sprachen). Kein Planen,
kein Programmieren.

## offen
- `en/`-Spiegel an neue Struktur anpassen, sobald `components/programs/interactions`
  feststehen (Namesräume der Pfade mitziehen) · Status: wartet auf Struktur
- Bestehende Lücken `en/animations/…` (Build meldet fehlende Ziele) nachziehen · Status: offen

## Regel
- Deutsch ist Quelle. Übersetzung erzeugt/hält `en/`, nie umgekehrt.
- Nie über Sprachbäume hinweg verlinken: in `en/` zeigt jeder Link auf `en/`.

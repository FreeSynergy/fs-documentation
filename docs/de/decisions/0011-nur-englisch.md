# 0011 – Nur Englisch wird gepflegt, Deutsch wird übersetzt

Status: akzeptiert (2026-11-05) · ersetzt **0008**, ersetzt in **0002** den Teil „Prosa deutsch / Deutsch = Quelle“

## Kontext
ADR 0008 machte `en/` zur ersten Sprache, verlangte aber, `de/` parallel von Hand mitzuziehen.
Zwei Bäume von Hand gleich zu halten kostet doppelt Tokens und erzeugt Abweichungen
(Stand 2026-11-05: 1492 `de`- gegen 897 `en`-Dateien). Übersetzen kann das lokale Modell
(llama.cpp, siehe CONVENTIONS §7) — dafür braucht es keinen Planer.

## Entscheidung
- **Gearbeitet wird nur in `docs/en/`.** Neuer Inhalt, Korrekturen, Umbauten: nur dort.
- **`docs/de/` ist Übersetzungsergebnis** von llama.cpp. Niemand schreibt dort von Hand.
- **`de/` darf gelesen werden**, wenn in `en/` eine Information fehlt. Steht es auch in `de/`
  nicht, wird es in `en/` **neu** geschrieben — nicht erst übersetzt.
- Der Bestand ist ohnehin Platzhalter (Protokoll §1) und wird überarbeitet. Es gibt deshalb
  **keine** Pflicht, den `de`-Rest vorab nach `en/` zu übersetzen. Im Hintergrund baut llama
  `en/` nur dort auf, wo noch nichts existiert.
- **Nicht übersetzt** werden `temp/`, `todo/`, `conventions/`, `scripts/` — die sind Arbeitsraum.
- Sprache des Gesprächs, der Beschlüsse und Pläne bleibt Deutsch; Bezeichner, Pfade, Code,
  Commits bleiben Englisch (der Teil von 0002 gilt weiter).
- Weitere Sprachen (`es/`, `it/`, …) entstehen genauso: als Übersetzung von `en/`.

## Folgen
- `scripts/doc_sync.py` (ADR 0010) bleibt der Prüfer, Richtung jetzt nur `en → de`.
- Strukturumbauten (z. B. ADR 0012) werden in `en/` gemacht; `de/` zieht per Skript nach
  (gleiche Umbenennung) oder wird neu übersetzt.
- `todo/translator.md` wird zu `todo/llama.md` (ein lokales Modell, mehrere Aufgabenarten).

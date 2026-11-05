# 0008 – Englisch zuerst, Deutsch zweite Sprache

## Kontext
Bisher galt (CONVENTIONS §4, `data/requirements.md` §1): `docs/de/` ist Quelle der Wahrheit,
`docs/en/` wird vom Übersetzer-Modell nachgezogen, „zurzeit nur `de/` pflegen“. Der Bestand
hinkt hinterher: 1491 `de`- gegen 478 `en`-Dateien, davon 355 Komponenten. Der Nutzer will die
Doku an Dritte weitergeben und entscheidet am 2026-11-03 um. Der Gesprächsverkehr bleibt deutsch.

## Entscheidung
**Englisch ist die erste Sprache der Doku.** `docs/en/` ist die Fassung, die nach außen geht und
zuerst geschrieben wird. `docs/de/` ist die zweite Sprache und wird **mitgezogen**; beide werden
möglichst gleich gehalten.

- Sprachkürzel und Baumstruktur bleiben wie sie sind (`docs/en/`, `docs/de/`).
- Dateinamen, Pfade, Bezeichner: weiterhin englisch (unverändert, ADR 0002).
- Deutsch bleibt die Sprache der **Abschlüsse, Prompts, Pläne und Fragen** (`conventions/`,
  `temp/`, `todo/`) und des Verkehrs mit Agenten.
- Neue Inhalte: **en zuerst, de parallel**. Bestehende `de`-Inhalte werden übersetzt nachgezogen,
  nicht umgekehrt ignoriert.
- Der Übersetzer (`todo/translator.md`) arbeitet jetzt **beidseitig**: er füllt Lücken in `en/`
  aus `de/` und hält `de/` nach Änderungen in `en/` nach.

## Folgen
- Die 355 `en/components/`-Dateien sind **Bestand, nicht Ballast** (erledigt P11 aus §19).
- `data/requirements.md` §1 („zurzeit nur `de/` pflegen“) ist damit ersetzt.
- Verlinkung bleibt sprachbaum-getrennt (CONVENTIONS §9): aus `en/` zeigt kein Link nach `de/`.
- Bekannte Altschäden in `en/` (9 defekte Links, fehlende `animations/`- und `data/`-Spiegel)
  sind jetzt **Aufgabe**, nicht hinnehmbarer Zustand. Liste in `todo/qwen.md` und `todo/translator.md`.
- `mkdocs.yml`: `theme.language: de` bleibt (UI-Sprache der Website), die `nav`-Reihenfolge
  ordnet `en` vor `de`.

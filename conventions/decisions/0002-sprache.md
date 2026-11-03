# 0002 – Sprache: Identifikatoren englisch, Prosa deutsch

## Kontext
Der Nutzer musste beim Bitten um Hilfe immer erst übersetzen. Das nervt und ist unnötig.

## Entscheidung
- Alles Technische (Dateinamen, Pfade, Ordner, Bezeichner, Code, Kommentare, Commits): **Englisch, immer.**
- Prosa in `docs/de/`, Beschlüsse, Prompts, Fragen: **Deutsch erlaubt.**
- Hilfe anfragen geht auf Deutsch – kein Zwang zur Vorab-Übersetzung.
- `en/`-Doku wird vom Übersetzer-Modell aus `de/` erzeugt, nicht von Hand.

## Folgen
Übersetzung ist Pipeline-Aufgabe (`todo/translator.md`), keine Handarbeit. Deutsch = Quelle
der Wahrheit. Bestehende Sprachregel (nie über Sprachbäume verlinken) bleibt.

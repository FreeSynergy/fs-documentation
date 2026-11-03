# 0004 – Komponenten-Einteilung primitives / widgets / workbenches

## Kontext
Die 84 Komponenten stecken in 10 Typ-Kategorien (basics, fields, …). Die neue Architektur
sortiert nach Ebene. Die Grenze widget↔workbench war unklar.

## Entscheidung
Test-Frage: *Kennt der Baustein seine Inhalte beim Bauen?* ja → widget, nein → workbench;
primitive = nicht weiter zerlegbar. Die vollständige Zuordnung steht in
`konventionen/KONVENTIONEN.md` §3. Festgelegte Grenzfälle:

- `*-picker`, `range-calendar` → widget
- Overlays → widget (eigene Lebensdauer, kein offenes Editieren)
- `map-view` → widget (bindet Geodata-Modell)
- `dashboard`, `embed`, `rich-text-editor` → workbench
- `combobox`, `tags-input`, `search-field`, `mention-input` → primitive
- `media-player`, `audio`, `video`, `carousel`, `gallery` → widget

## Folgen
Physisches Umsortieren in `components/{primitives,widgets,workbenches}/` folgt separat
(Link-Mitschrift nötig, siehe 0001/Ablauf). Bei Abweichung beim Umsortieren korrigieren.

# 0001 – Sechs Ebenen und Namen

## Kontext
Programme bauen aufeinander auf. Es fehlte eine durchgängige Trennung von „wird verbaut“
und „läuft selbst“. Der bestehende Ordner `components/` meinte bisher die unterste Ebene.

## Entscheidung
Sechs Ebenen in zwei Schirm-Ordner plus zwei Querschnitt-Zweige:

- `components/` (Bauebene, läuft nicht allein): `primitives` → `widgets` → `workbenches`
- `programs/` (Laufebene): `apps` (4) → `suites` (5) → `platform` (6)
- Querschnitt: `interactions/` (gestures, animations) und `data/`

Der Schirm-Ordner `components/` bleibt bestehen und bekommt innen drei Bänder.
Das Gegenstück heißt `programs` (eigenes Wort im Projekt, nicht-kommerziell), nicht
`architecture`/`products`. `interactions` ist eigener Top-Level-Zweig, weil
Gesten/Animationen von allen Ebenen benutzt werden (Querschnitt, kein Component).

## Folgen
Bestehende `apps/`-Kategorien werden `programs/` zugeordnet (apps/suites/platform).
Bestehende Komponenten-Kategorien werden den drei Bändern zugeordnet (siehe 0004).
Jede Ebene bekommt eigenen `index.md`.

# Ausgang (exit)

Ausgangsanimationen lassen ein Element verschwinden und seinen Platz frei werden. Sie dürfen spürbar kürzer dauern als der zugehörige Eingang.

## Elemente

- **fade-out** - allmählich ausblenden (Deckkraft 1 → 0)
- **slide-out** - nach außen hinauszugleiten
- **zoom-out** - von voller Größe auf null skalieren
- **scale-out** - von 100 % auf 0 % schrumpfen
- **bounce-out** - vor dem Verschwinden federn
- **pop-out** - kurz ausholen und wegklappen (Chips, Badges)
- **collapse** - Höhe oder Breite auf 0 reduzieren (Akkordeon zu)

## Familien

Jede Zeile hat ihr Gegenstück in [Eingang (entrance)](../entrance/): `fade-out` ↔
`fade-in`, `slide-out` ↔ `slide-in`, `zoom-out` ↔ `zoom-in`, `scale-out` ↔ `scale-in`,
`bounce-out` ↔ `bounce-in`, `pop-out` ↔ `pop-in`, `collapse` ↔ `expand`.

## Hinweis zum Layout

Erst nach `onAnimateEnd` wird das Element aus dem Layout genommen. Vorher entfernt,
reißt die übrige Fläche abrupt auf – das wirkt stärker als jede Ausgangsanimation.

## Siehe auch

- [Animationen Übersicht](../index.md)
- [Eingang (entrance)](../entrance/)
- [Accordion](../../components/containers/accordion/description.md), [Toast](../../components/feedback/toast/description.md)

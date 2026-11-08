# Ausblenden (Exit)

Ausblend-Animationen lassen ein Element verschwinden und seinen Platz wieder frei werden. Sie dauern oft
spürbar kürzer als das passende Einblenden.

## Elemente

- **fade-out** – sanft ausblenden (Deckkraft 1 → 0)
- **slide-out** – nach außen hinausgleiten
- **zoom-out** – von voller Größe auf null skalieren
- **scale-out** – von 100 % auf 0 % schrumpfen
- **bounce-out** – vor dem Verschwinden federn
- **pop-out** – kurz vorwegnehmen und zusammenfalten (Chips, Badges)
- **collapse** – Höhe oder Breite auf 0 reduzieren (Akkordeon schließen)
- **radial-in** – Punkte wandern zurück zum Anker (Kreismenü schließen)

## Familien

Jeder Eintrag hat sein Gegenstück in [Einblenden](../entrance/): `fade-out` ↔
`fade-in`, `slide-out` ↔ `slide-in`, `zoom-out` ↔ `zoom-in`, `scale-out` ↔
`scale-in`, `bounce-out` ↔ `bounce-in`, `pop-out` ↔ `pop-in`, `collapse` ↔
`expand`, `radial-in` ↔ `radial-out`.

## Hinweis zum Layout

Das Element wird erst nach `onAnimateEnd` aus dem Layout genommen. Entfernt man es
vorher, springt der restliche Bereich abrupt auf – das wirkt stärker als jede Ausblend-Animation.

## Siehe auch

- [Übersicht Animationen](../index.md)
- [Einblenden](../entrance/)
- [Akkordeon](../../../components/widgets/containers/accordion/description.md), [Toast](../../../components/primitives/feedback/toast/description.md)
- [Radialmenü](../../../components/widgets/navigation/radial-menu/description.md) – nutzt `radial-in` beim Schließen

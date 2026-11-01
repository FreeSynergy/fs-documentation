# Bewegung (movement)

Bewegungsanimationen hängen an Scrollen oder an der Position im Dokument, nicht an einer
einzelnen Aktion. Sie verändern die Geschwindigkeit von Ebenen zueinander.

## Elemente

- **parallax** - Ebenen bewegen sich unterschiedlich schnell

## Abgrenzung

Parallax ist an den Scrollfortschritt gebunden und wiederholbar; eine einmalige
Verschiebung eines Elements gehört in [Eingang](../entrance/) oder
[Zustandswechsel](../transition/).

## Pflichtregeln

- maximal zwei Ebenen mit deutlichem Geschwindigkeitsunterschied
- bei `prefers-reduced-motion` vollständig abschalten – Bewegung im Sichtfeld ist
  für viele Nutzer der stärkste Auslöser von Unbehagen
- nie mit Textblöcken kombinieren, deren Lesefluss dadurch kippt

## Siehe auch

- [Animationen Übersicht](../index.md)
- [Stagger](../organization/stagger/description.md) - zeitliche statt räumliche Staffelung
- [Barrierefreiheit](../index.md#barrierefreiheit)

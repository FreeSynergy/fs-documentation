# Bewegung (Movement)

Bewegungs-Animationen hängen am Scrollen oder an der Position im Dokument, nicht an einer
einzelnen Aktion. Sie verändern das Tempo von Ebenen im Verhältnis zueinander.

## Elemente

- **parallax** – Ebenen bewegen sich mit unterschiedlichem Tempo

## Abgrenzung

Parallax ist an den Scroll-Fortschritt gebunden und wiederholbar; eine einmalige Verschiebung
eines Elements gehört zu [Einblenden](../entrance/) oder
[Übergang](../transition/).

## Verbindliche Regeln

- höchstens zwei Ebenen mit deutlich unterschiedlichem Tempo
- unter `prefers-reduced-motion` vollständig abschalten – Bewegung im Sichtfeld ist für viele
  Menschen der stärkste Auslöser von Unbehagen
- nie mit Textblöcken kombinieren, deren Lesefluss dadurch kippen würde

## Siehe auch

- [Übersicht Animationen](../index.md)
- [Staffelung](../organization/stagger/description.md) – eine zeitliche statt räumliche Staffelung
- [Barrierefreiheit](../index.md#accessibility)

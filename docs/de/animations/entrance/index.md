# Eingang (entrance)

Eingangsanimationen lassen ein Element erscheinen. Fast jede hat ein Spiegelstück in
[Ausgang (exit)](../exit/): gleiche Familie, nur umgekehrte Richtung.

## Elemente

- **fade-in** - allmählich einblenden (Deckkraft 0 → 1)
- **slide-in** - von außen hereingleiten
- **zoom-in** - von klein auf volle Größe skalieren
- **scale-in** - von 0 % auf 100 % wachsen
- **bounce-in** - beim Eintreffen federn
- **pop-in** - einblenden mit kurzem Overshoot (Chips, Badges, Avatare)
- **expand** - Höhe oder Breite von 0 auf Inhalt wachsen lassen
- **unfold** - wie ein Blatt ausklappen
- **radial-out** - Punkte wachsen radial aus einem Anker heraus (Kreismenü)

## Familien

`fade-in`, `slide-in`, `zoom-in`, `scale-in`, `bounce-in` und `radial-out` sind die
Eingangsseiten der Familien `fade`, `slide`, `zoom`, `scale`, `bounce` und `radial`.
Gemeinsame Attribute wie `duration`, `timingFunction` und `fillMode` stehen in der
[Übersicht](../index.md).

## Siehe auch

- [Animationen Übersicht](../index.md)
- [Ausgang (exit)](../exit/)
- [Organisation (organization)](../organization/) - gestaffelter Start mehrerer Eingänge
- [Toast](../../components/feedback/toast/description.md), [Modal](../../components/overlays/modal/description.md)
- [Radial Menu](../../components/navigation/radial-menu/description.md) - nutzt `radial-out` beim Öffnen

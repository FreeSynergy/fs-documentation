# Einblenden (Entrance)

Einblend-Animationen lassen ein Element erscheinen. Fast jede hat ein Gegenstück in [Ausblenden](../exit/): dieselbe Familie, nur in die Gegenrichtung.

## Elemente

- **fade-in** – sanft einblenden (Deckkraft 0 → 1)
- **slide-in** – von außen hereingleiten
- **zoom-in** – von klein auf volle Größe skalieren
- **scale-in** – von 0 % auf 100 % wachsen
- **bounce-in** – federn beim Erscheinen
- **pop-in** – einblenden mit kurzem Überschwingen (Chips, Badges, Avatare)
- **expand** – Höhe oder Breite von 0 auf den Inhalt wachsen lassen
- **unfold** – sich wie ein Blatt aufklappen
- **radial-out** – Punkte wachsen radial aus einem Anker heraus (Kreismenü)

## Familien

`fade-in`, `slide-in`, `zoom-in`, `scale-in`, `bounce-in` und `radial-out` sind die
Einblend-Seiten der Familien `fade`, `slide`, `zoom`, `scale`, `bounce` und `radial`.
Gemeinsame Attribute wie `duration`, `timingFunction` und `fillMode` sind in der [Übersicht](../index.md) beschrieben.

## Siehe auch

- [Übersicht Animationen](../index.md)
- [Ausblenden](../exit/)
- [Organisation](../organization/) – gestaffelter Start mehrerer Einblendungen
- [Toast](../../../components/primitives/feedback/toast/description.md), [Modal](../../../components/widgets/overlays/modal/description.md)
- [Radialmenü](../../../components/widgets/navigation/radial-menu/description.md) – nutzt `radial-out` beim Öffnen

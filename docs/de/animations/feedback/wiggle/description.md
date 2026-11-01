# Wiggle

## Beschreibung

Wiggle lässt ein Element in kleinem Winkel hin und her wippen (Rotation um etwa 1 bis 3 Grad). Es signalisiert meist „bearbeitbar“ oder „noch nicht abgelegt“ - im Gegensatz zu Shake nicht „Fehler“.

## Verwendung

- Bearbeitungsmodus auf dem Startbildschirm (Symbole wippen)
- Markierte Objekte in Editoren, die verschoben werden können
- Hinweis, dass eine Karte noch nicht abgelegt ist
- Provisorischer oder ungespeicherter Zustand
- Spielerisches Feedback in spielnahen Oberflächen
- Mehrere Objekte vor dem gemeinsamen Verschieben

## Dauer

- Typisch: 400–800 ms pro Zyklus, meist als Endlosschleife
- Standardwert: 600 ms pro Zyklus

## Unterschied zu Shake

- Shake: horizontale Verschiebung mit großer Amplitude, einmalig, als Fehlermeldung
- Elastic: einmaliges Überschießen über die Endposition und Zurückfedern, kein wiederholtes Wippen
- Pulse: Größen- oder Deckkraftänderung im Zyklus, keine Rotation

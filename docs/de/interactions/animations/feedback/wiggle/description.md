# Wiggle

## Beschreibung

Wiggle lässt ein Element um einen kleinen Winkel hin und her wackeln (eine Drehung um etwa 1 bis 3
Grad). In der Regel signalisiert es „bearbeitbar“ oder „noch nicht abgelegt“. Anders als Shake
bedeutet es keinen Fehler.

## Verwendung

- Bearbeitungsmodus auf dem Startbildschirm (Icons wackeln)
- ausgewählte Objekte in Editoren, die sich verschieben lassen
- ein Hinweis, dass eine Karte noch nicht abgelegt ist
- ein vorläufiger oder ungespeicherter Zustand
- spielerische Rückmeldung auf spielartigen Flächen
- mehrere Objekte, bevor sie gemeinsam verschoben werden

## Dauer

- Typisch: 400–800 ms pro Zyklus, meist als endlose Schleife
- Standardwert: 600 ms pro Zyklus

## Unterschied zu Shake

- Shake: eine waagerechte Verschiebung mit großer Amplitude, einmalig, als Fehlermeldung
- Elastic: ein einzelnes Überschwingen über die Endposition und ein Zurückfedern, kein
  wiederholtes Wackeln
- Pulse: eine Änderung von Größe oder Deckkraft im Zyklus, keine Drehung

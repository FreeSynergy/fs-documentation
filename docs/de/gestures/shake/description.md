# Shake (Shaking)

## Beschreibung

Ein Shake ist ein schnelles Hin- und Herbewegen des Geräts oder eines Elements.
Die Geste wird meist über den Beschleunigungssensor (Accelerometer) erkannt, bei
Maus/Touchpad auch über eine schnelle horizontale Bewegung des Zeigers.

## Verwendung

- Undo / Verwerfen (Klassiker: „Schütteln zum Rückgängigmachen“)
- Auf Fehler hinweisen (Formularfeld schütteln, wenn die Eingabe ungültig ist)
- App wechseln (iOS: Shake für „Übereinstimmung finden“)
- Inhalt neu mischen / Würfeln
- Versteckte Funktionen freigeben (Easter Eggs)

## Dauer

- Typisch: 300–1000ms
- Mindestens 2 Richtungswechsel innerhalb des Zeitfensters

## Erkennung

| Methode | Beschreibung |
|---------|--------------|
| **Accelerometer** | Sensor misst Beschleunigungswechsel (mobil) |
| **Pointer Movement** | Schnelle X-Bewegung mit Maus/Finger (Desktop) |
| **Threshold** | Abweichung vom Mittelwert muss überschritten werden |

## Unterschied zu Swipe

- **Swipe**: eine Bewegung in eine Richtung (Distanz > 50px)
- **Shake**: mehrere Bewegungen hin und zurück (Richtungswechsel zählen)

## Unterschied zu Wiggle (Animation)

- **Shake (Geste)**: der Nutzer bewegt das Gerät/Element
- **Wiggle (Animation)**: das Element bewegt sich selbst als Feedback

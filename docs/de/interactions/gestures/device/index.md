# Geräte-Gesten (device)

Geräte-Gesten erkennen keine Berührung, sondern eine **Bewegung des Geräts selbst**
über Beschleunigungs- und Gyrosensoren (Accelerometer, Gyroskop).

Die Anzahl der Zeiger spielt keine Rolle: Ein- und Mehrpunkt gibt es hier nicht,
kein Finger berührt etwas.

## Elemente

- **shake** – schnelle Hin-und-her-Bewegung (Rückgängig, Fehlerrückmeldung)
- **tilt** – Neigen des Geräts (Steuern, Kompass)
- **flip** – Umdrehen des Geräts (Stummmodus, Anruf stummschalten)
- **wave** – eine Hand vor dem Sensor bewegen (Anruf annehmen, Assistent)

## Zuordnung

| Situation | Geste |
|-----------|---------|
| Rückgängig / verwerfen | shake |
| Inhalt neigen/steuern | tilt |
| Nicht stören einschalten | flip |
| Freihändige Bedienung | wave |

## Barrierefreiheit

Geräte-Gesten fallen unter WCAG 2.5.4 (Motion Actuation): Jede sensorbasierte
Aktion **muss** eine reguläre UI-Alternative haben (Button, Menüpunkt). Sensor-
Rückmeldung (Vibration) nur mit Zustimmung und abschaltbar (`hapticFeedback`,
`respectReducedMotion`).

## Siehe auch

- [Gesten-Übersicht](../index.md)
- [Shake-Animation](../../animations/feedback/shake/description.md) – dasselbe Muster als Ausgabe-Rückmeldung
- [Wiggle-Animation](../../animations/feedback/wiggle/description.md) – Gerät ruhig halten, das Element wackelt

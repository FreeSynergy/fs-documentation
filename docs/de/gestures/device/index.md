# Geräte-Gesten (device)

Geräte-Gesten erkennen keine Berührung, sondern eine **Bewegung des Geräts
selbst** über Beschleunigungs- und Gyrosensor (Accelerometer, Gyroscope).

## Elemente

- **shake** - schnelles Hin- und Herbewegen (Undo, Fehler-Feedback)
- **tilt** - Kippen des Geräts (Steuerung, Kompass)
- **flip** - Gerät umdrehen (Ruhe-Modus, Anruf stummschalten)
- **wave** - Hand vor dem Sensor bewegen (Anruf annehmen, Assistent)

## Zuordnung

| Situation | Geste |
|-----------|-------|
| Rückgängig / Verwerfen | shake |
| Inhalt neigen/steuern | tilt |
| Nicht stören aktivieren | flip |
| Hände frei bedienen | wave |

## Barrierefreiheit

Geräte-Gesten fallen unter WCAG 2.5.4 (Motion Actuation): Zu jeder
sensorbasierten Aktion **muss** eine normale UI-Alternative existieren
(Button, Menüpunkt). Sensor-Feedback (Vibration) nur mit Zustimmung und
abschaltbar (`hapticFeedback`, `respectReducedMotion`).

## Siehe auch

- [Gesten Übersicht](../index.md)
- [Shake-Animation](../../animations/feedback/shake/description.md) - dasselbe Muster als Ausgabe-Feedback
- [Wiggle-Animation](../../animations/feedback/wiggle/description.md) - Gerät still halten, Element wackelt

# Gerätegesten (device)

Gerätegesten erkennen keine Berührung, sondern eine **Bewegung des Geräts selbst**
über Beschleunigungs- und Gyrosensoren (Beschleunigungsmesser, Gyroskop).

Die Anzahl der Zeiger spielt keine Rolle: Ein-Punkt und Mehrpunkt gibt es
hier nicht, kein Finger berührt etwas.

## Elemente

- **shake** – schnelle Hin- und Her-Bewegung (Rückgängig, Fehlerrückmeldung)
- **tilt** – Gerät kippen (Steuern, Kompass)
- **flip** – Gerät umdrehen (Lautlos-Modus, Anruf stummschalten)
- **wave** – Hand vor dem Sensor bewegen (Anruf annehmen, Assistent)

## Zuordnung

| Situation | Geste |
|-----------|-------|
| Rückgängig / verwerfen | shake |
| Inhalt kippen oder steuern | tilt |
| Nicht stören aktivieren | flip |
| Bedienung mit freien Händen | wave |

## Barrierefreiheit

Gerätegesten fallen unter WCAG 2.5.4 (Bewegungsauslösung): Jede sensorbasierte
Aktion **muss** eine reguläre Bedienalternative haben (Button, Menüpunkt). Sensor-
Rückmeldung (Vibration) nur mit Zustimmung und abschaltbar (`hapticFeedback`,
`respectReducedMotion`).

## Siehe auch

- [Übersicht der Gesten](../index.md)
- [Shake-Animation](../../animations/feedback/shake/description.md) – dasselbe Muster wie bei der Ausgabe-Rückmeldung
- [Wiggle-Animation](../../animations/feedback/wiggle/description.md) – Gerät ruhig halten, das Element wackelt

# Tilt (Kipp-Geste)

## Beschreibung

Tilt ist das **Kippen des Geräts** um eine oder zwei Achsen. Erkennung über
Beschleunigungssensor (Orientierung relativ zur Schwerkraft) oder Gyroskop.
Beim Stift misst `PointerEvent.tiltX`/`tiltY` die Neigung des Stifts – dieselbe
Idee, andere Achse.

## Verwendung

- Neigen als Steuerung (Spiele, Lenkung, Kompass)
- Inhalt „durchkippen“: Liste/Regal bewegt sich mit dem Gerät (Parallax)
- Wasserwaage, Fotograster, Panorama-Führung
- Stift-Neigung für Schraffuren/Radiergummi in Zeichen-Apps

## Neigungswinkel

| Achse | Bereich | Bezeichnung |
|-------|---------|-------------|
| Alpha | 0–360° | Kompassrichtung (Azimut) |
| Beta | -180–180° | Kippen nach vorn/hinten |
| Gamma | -90–90° | Kippen nach links/rechts |

## Dauer

- Erkennung: kontinuierlich, Ereignisse alle 10–100ms
- Deadzone: ±2–5° gegen Wackeln

## Erkennung

| Methode | Beschreibung |
|---------|--------------|
| **Accelerometer** | `deviceorientation` / SensorManager |
| **Gyroscope** | Drehrate für schnelle Kippbewegungen |
| **Stift-Tilt** | `tiltX`/`tiltY` in Pointer Events |

## Unterschied zu Shake

- **Tilt**: langsam, Richtung stabil, Zustand („Gerät liegt schräg“)
- **Shake**: schnell, wiederholt, Ereignis

## Barrierefreiheit

WCAG 2.5.4 (Motion Actuation): Kipp-Aktionen brauchen immer eine
UI-Alternative (Buttons, Slider). Kalibrierung und Empfindlichkeit konfigurierbar machen.

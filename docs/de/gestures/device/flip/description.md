# Flip (Umdreh-Geste)

## Beschreibung

Flip ist das **Umdrehen des Geräts** mit dem Display nach unten (oder die
Rückseite nach oben). Erkennung über Beschleunigungssensor: Die
Schwerkahrungsrichtung kippt von „Display zeigt vom Boden weg“ zu „Display
zeigt zum Boden“.

## Verwendung

- Anruf stummschalten (Klassiker: Handy umdrehen = Anruf annehmen und stumm)
- Nicht-Stören-Modus aktivieren (Flip to Silence / Flip to Shhh)
- Meeting-Modus: Benachrichtigungen unterdrücken
- Wecker quittieren (Smartphones mit Näherungssensor: Zudecken + Umdrehen)

## Richtung

| Bewegung | Typische Aktion |
|----------|-----------------|
| Display nach unten | Stummschalten / Nicht stören |
| Display nach oben (zurück) | Modus endet automatisch |

## Dauer

- Umdrehen: 300–1500ms
- Haltephase unten: meist ≥ 1000ms, damit es nicht versehentlich auslöst

## Erkennung

| Methode | Beschreibung |
|---------|--------------|
| **Accelerometer** | Z-Achse kehrt Vorzeichen um |
| **Gyroscope** | Drehung um eine horizontale Achse |
| **Proximity** | Zusätzlich: nichts vor dem Display (filtert Ablegen auf dem Tisch) |

## Unterschied zu Shake

- **Flip**: eine 180°-Drehung mit stabilem Endzustand
- **Shake**: schnelle Hin-und-zurück-Bewegung ohne Endzustand

## Unterschied zu Tilt

- **Flip**: vollständige Umkehr der Orientierung
- **Tilt**: Teilneigung als Steuerwert

## Barrierefreiheit

WCAG 2.5.4: Immer ein normaler Schalter (Stummschalt-Button,
Nicht-stören-Schalter) muss dieselbe Aktion auslösen.

# Fingerprint (Fingerabdruck-Geste)

## Beschreibung

Fingerprint ist das **Berühren eines Biometrie-Sensors**: entweder den Finger
still auflegen, bis der Scan abgeschlossen ist, oder ihn über den Sensor
ziehen (Swipe-Verfahren). Sensoren arbeiten kapazitiv (Oberfläche), optisch
(Kamera) oder Ultraschall (3D-Bild, unter dem Display). Registriert wird kein
Klick auf ein Element, sondern ein Authentifizierungs-Ereignis.

## Fingeranzahl

Genau 1 – der Sensor liest die Kuppe eines Fingers.

## Verwendung

- Gerät und App entsperren
- Aktionen autorisieren (Zahlungen, Konto löschen, Passwort-Manager)
- Login als Alternative zu PIN oder Passwort
- Über den Sensor ziehen als Eingabekanal (Listen scrollen)

## Dauer

- Scan: 100–500ms
- Finger bis zur Bestätigung auf dem Sensor halten (Vibration oder Häkchen)

## Erkennung

| Methode | Beschreibung |
|---------|--------------|
| **Kapazitiv** | Flächen-Sensor misst das Leistenmuster (häufig in Buttons) |
| **Optisch** | Kamera fotografiert die Fingerkuppe (im Display oder Rahmen) |
| **Ultraschall** | 3D-Tomographie der Leistenstruktur, funktioniert auch mit feuchten Fingern |

## Unterschied zu Tap

- **Tap**: richtet sich auf ein UI-Element, misst Druckpunkt und Dauer
- **Fingerprint**: richtet sich auf den Sensor, Ergebnis ist eine
  Match-Entscheidung (wahr/falsch)

## Barrierefreiheit

Biometrische Anmeldung braucht immer eine gleichwertige Alternative ohne
Biometrie (PIN, Muster, Passwort). Ein fehlgeschlagener oder blockierter
Scan (Feuchtigkeit, Schmutz) muss zum Fallback führen, nie in eine Sackgasse.

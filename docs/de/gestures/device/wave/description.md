# Wave (Wink-Geste)

## Beschreibung

Wave ist das **Bewegen der Hand vor dem Gerät**, ohne es zu berühren. Erkannt
wird sie über Radarsensoren (Google Soli / Motion Sense), ToF-Sensoren oder
Frontkamera mit Gestenerkennung. Bekannt wurde die Geste durch „Winken zum
Annehmen“ (Pixel Wave to Answer, Anruf annehmen per Winken) und
„Air Gestures“ in Android Auto.

## Verwendung

- Anruf annehmen/ablehnen ohne Bildschirmkontakt (Hände beschäftigt)
- Assistent rufen / Medien steuern in Auto- und Smart-Display-Kontexten
- Navigation ohne Touch (Küchen-, Werkstatt-, OP-Szenarien)
- Barrierefreie Steuerung für Menschen, die das Gerät nicht berühren können

## Bewegungsmuster

| Muster | Typische Aktion |
|--------|-----------------|
| Hand herbeiwinken und entfernen | Anruf annehmen |
| Faust schließen/öffnen | Anruf ablehnen |
| Hand seitlich wischen | Weiter / Stummschalten |

## Dauer

- Bewegung: 500–2000ms
- Vorbereitungsphase (Hand heben): separate Erkennungsphase

## Erkennung

| Methode | Beschreibung |
|---------|--------------|
| **Radar (mmWave)** | Soli/Motion Sense erkennt Hand im Sensorkegel |
| **Kamera + ML** | optische Handgesten-Erkennung |
| **ToF** | Tiefensensor erkennt Heranführung |

## Unterschied zu Shake

- **Wave**: Hand bewegt sich, Gerät bleibt ruhig, kein Kontakt
- **Shake**: Gerät bewegt sich, kein Kontakt zur Umgebung nötig

## Barrierefreiheit

Wave kann eine gute berührungsarme Alternative sein, ist aber nach WCAG 2.5.4
(Motion Actuation) nur zulässig mit regulärer UI-Alternative; zudem ist die
Sensorverfügbarkeit geräteabhängig und immer explizit konfigurierbar zu machen.

# Multi-Finger Tap (Mehrfinger-Tippen)

## Beschreibung

Ein Multi-Finger Tap ist das gleichzeitige kurze Berühren mit **zwei oder mehr
Fingern** (üblich zwei, mit drei, vier oder fünf Fingern genauso gültig). Auf
Geräten ohne Rechte-Maustaste dient er als Äquivalent zum Sekundärklick; Android
stellte dafür früher `onTwoFingerTapEvent` im `GestureDetector` bereit.

Die Fingeranzahl ist eine Einstellung (`pointerCount`) und kein eigener
Gestetyp: Tippen mit zwei, drei oder fünf Fingern ist dieselbe Geste.

## Verwendung

- Sekundäraktion / Kontextmenü (wie Rechtsklick)
- Zoom-Kontrolle auf Karten (Tippen = Zoom-Stufe)
- Doppeltipp-Zoom mit mehreren Fingern in Karten-Apps
- AssistiveTouch- und Accessibility-Verknüpfungen

## Dauer

- Berührung: unter 300ms
- Alle Finger müssen innerhalb von ~100ms versetzt aufsetzen

## Erkennung

| Methode | Beschreibung |
|---------|--------------|
| **Pointer Count** | Genau `pointerCount` Pointer gleichzeitig unten (Standard 2) |
| **Zeitfenster** | Down/Up aller Pointer ohne nennenswerte Bewegung |
| **Abstand** | Mindestabstand der Finger (ca. 20px) gegen versehentliches Auslösen |

## Unterschied zu Tap

- **Tap**: ein Finger, Primäraktion
- **Multi-Finger Tap**: zwei oder mehr Finger, Sekundäraktion

## Unterschied zu Pinch/Spread

- **Multi-Finger Tap**: ohne Bewegung
- **Pinch/Spread**: mit Bewegung der Finger zueinander/auseinander

## Barrierefreiheit

Da die Geste nicht selbsterklärend ist, immer sichtbare Alternative
(Kontextmenü-Button, lang gedrückt halten) anbieten (WCAG 2.5.1).

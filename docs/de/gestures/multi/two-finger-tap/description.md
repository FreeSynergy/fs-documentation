# Two-Finger Tap (Zwei-Finger-Tippen)

## Beschreibung

Ein Two-Finger Tap ist das gleichzeitige kurze Berühren mit **zwei Fingern**
(typisch Zeige- und Mittelfinger). Auf Geräten ohne Rechte-Maustaste dient er
als Äquivalent zum Sekundärklick; Android stellte dafür früher
`onTwoFingerTapEvent` im `GestureDetector` bereit.

## Verwendung

- Sekundäraktion / Kontextmenü (wie Rechtsklick)
- Zoom-Kontrolle auf Karten (Tippen = Zoom-Stufe)
- Doppeltipp-Zoom mit zwei Fingern in Karten-Apps
- AssistiveTouch- und Accessibility-Verknüpfungen

## Dauer

- Berührung: unter 300ms
- Beide Finger müssen innerhalb von ~100ms versetzt aufsetzen

## Erkennung

| Methode | Beschreibung |
|---------|--------------|
| **Pointer Count** | Genau 2 Pointer gleichzeitig unten |
| **Zeitfenster** | Down/Up beider Pointer ohne nennenswerte Bewegung |
| **Abstand** | Mindestabstand der Finger (ca. 20px) gegen versehentliches Auslösen |

## Unterschied zu Tap

- **Tap**: ein Finger, Primäraktion
- **Two-Finger Tap**: zwei Finger, Sekundäraktion

## Unterschied zu Pinch/Spread

- **Two-Finger Tap**: ohne Bewegung
- **Pinch/Spread**: mit Bewegung der Finger zueinander/auseinander

## Barrierefreiheit

Da die Geste nicht selbsterklärend ist, immer sichtbare Alternative
(Kontextmenü-Button, lang gedrückt halten) anbieten (WCAG 2.5.1).

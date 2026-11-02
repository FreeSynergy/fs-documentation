# Two-Finger Long Press (Zwei-Finger-Druck)

## Beschreibung

Ein Two-Finger Long Press ist ein **langer Druck mit zwei Fingern**. Er
kombiniert die Zeitlogik des Long Press mit dem Zwei-Finger-Kontext des
Two-Finger Tap und entspricht funktional dem Rechtsklick mit gedrückt halten
(macOS: „Sekundären Klick halten“).

## Verwendung

- Kontextmenü mit Verzögerung (verhindert versehentliches Auslösen)
- Auswahlanfang markieren und dann per Wischen Auswahl erweitern
- Mehrfachauswahl-Modus starten (mehrere Elemente auswählen)
- Drag-Start für Multiselect (beide Finger halten, dann ziehen)

## Dauer

- Halten: mindestens wie `longPressThreshold` (typisch 500ms)
- Danach wie Long Press: Callback beim Start, Bewegung optional

## Erkennung

| Methode | Beschreibung |
|---------|--------------|
| **Pointer Count + Zeit** | Zwei Pointer, keine Bewegung über Threshold |
| **Move Tolerance** | Bewegung < 10px gilt weiterhin als Druck |
| **Lift Rule** | Einer der Finger hebt sich zu früh → abgebrochen |

## Unterschied zu Two-Finger Tap

- **Two-Finger Tap**: kurz, Aktion sofort
- **Two-Finger Long Press**: halten, Aktion nach Delay, danach ziehen möglich

## Unterschied zu Long Press

- **Long Press**: ein Finger, Primär-Kontextmenü
- **Two-Finger Long Press**: zwei Finger, Sekundär-/Multiselect-Kontext

## Barrierefreiheit

Wie alle Mehrpunkt-Gesten nur mit Ein-Finger-Alternative (WCAG 2.5.1):
Long Press oder Auswahl-Button.

# Multi-Finger Long Press (Mehrfinger-Langdruck)

## Beschreibung

Ein Multi-Finger Long Press ist ein **langer Druck mit zwei oder mehr
Fingern**. Er kombiniert die Zeitlogik des Long Press mit dem
Mehrfinger-Kontext des Multi-Finger Tap und entspricht funktional dem
Rechtsklick mit gedrückt halten (macOS: „Sekundären Klick halten“).

Auch hier ist die Fingeranzahl eine Einstellung (`pointerCount`), kein eigener
Gestetyp.

## Verwendung

- Kontextmenü mit Verzögerung (verhindert versehentliches Auslösen)
- Auswahlanfang markieren und dann per Wischen Auswahl erweitern
- Mehrfachauswahl-Modus starten (mehrere Elemente auswählen)
- Drag-Start für Multiselect (alle Finger halten, dann ziehen)

## Dauer

- Halten: mindestens wie `longPressThreshold` (typisch 500ms)
- Danach wie Long Press: Callback beim Start, Bewegung optional

## Erkennung

| Methode | Beschreibung |
|---------|--------------|
| **Pointer Count + Zeit** | `pointerCount` Pointer, keine Bewegung über Threshold |
| **Move Tolerance** | Bewegung < 10px gilt weiterhin als Druck |
| **Lift Rule** | Einer der Finger hebt sich zu früh → abgebrochen |

## Unterschied zu Multi-Finger Tap

- **Multi-Finger Tap**: kurz, Aktion sofort
- **Multi-Finger Long Press**: halten, Aktion nach Delay, danach ziehen möglich

## Unterschied zu Long Press

- **Long Press**: ein Finger, Primär-Kontextmenü
- **Multi-Finger Long Press**: zwei oder mehr Finger, Sekundär-/Multiselect-Kontext

## Barrierefreiheit

Wie alle Mehrpunkt-Gesten nur mit Ein-Finger-Alternative (WCAG 2.5.1):
Long Press oder Auswahl-Button.

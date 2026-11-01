# Fade Out

## Beschreibung

Fade Out blendet ein Element allmählich aus: Die Deckkraft sinkt von 1 auf 0, bis das Element unsichtbar ist. Danach kann es aus dem Layout entfernt oder dauerhaft ausgeblendet werden.

## Verwendung

- Toasts nach der Anzeigedauer automatisch verschwinden lassen
- Modal-Overlays und Dialoge weich schließen
- Listenelemente nach dem Löschen ausblenden
- Spinner nach Abschluss einer Aktion verschwinden lassen
- Menüs und Popovers beim Klick außerhalb schließen
- Unsichtbares Element behalten, bis `display: none` greift

## Dauer

- Typisch: 150–300ms
- Ausblendungen werden meist kürzer gewählt als Einblendungen
- Große Overlays (Hintergrund): bis 400ms möglich

## Unterschied zu Fade In

- Fade Out: Die Deckkraft sinkt von 1 auf 0 – das Element verlässt die Bühne
- Fade In: Die Deckkraft steigt von 0 auf 1 – das Element betritt die Bühne

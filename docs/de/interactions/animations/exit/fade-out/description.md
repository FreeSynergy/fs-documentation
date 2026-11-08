# Fade Out

## Beschreibung

Fade Out blendet ein Element allmählich aus: Die Deckkraft sinkt von 1 auf 0, bis das Element unsichtbar ist. Danach kann es aus dem Layout entfernt werden oder dauerhaft verborgen bleiben.

## Verwendung

- Toasts nach ihrer Anzeigezeit automatisch verschwinden lassen
- modale Overlays und Dialoge sanft schließen
- Listenelemente nach dem Löschen ausblenden
- einen Spinner verschwinden lassen, sobald eine Aktion fertig ist
- Menüs und Popover bei einem Klick außerhalb schließen
- das unsichtbare Element erhalten, bis `display: none` greift

## Dauer

- Typisch: 150–300 ms
- Ausblendungen werden meist kürzer gewählt als Einblendungen
- Große Overlays (Hintergrund): bis zu 400 ms möglich

## Unterschied zu Fade In

- Fade Out: die Deckkraft sinkt von 1 auf 0 – das Element verlässt die Bühne.
- Fade In: die Deckkraft steigt von 0 auf 1 – das Element betritt die Bühne.

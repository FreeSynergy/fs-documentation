# Fade In

## Beschreibung

Fade In blendet ein Element allmählich ein, indem die Deckkraft von 0 auf 1 ansteigt. Position und Größe bleiben dabei unverändert, sodass sich nichts anderes im Layout verschiebt.

## Verwendung

- Toasts und Benachrichtigungen sanft einblenden
- Modal-Overlays und Dialoge beim Öffnen weich erscheinen lassen
- Bilder nach dem Laden einblenden statt „aufploppen“ lassen
- Tabs und Panels beim Wechsel überblenden
- Onboarding-Elemente gestaffelt einblenden (Kombination mit Stagger)
- Tooltip- und Popover-Einblendung ohne ablenkende Bewegung

## Dauer

- Typisch: 150–400ms
- Mikro-Feedback (Hover, Tooltip): 100–200ms
- Modale Flächen und Overlays: 250–400ms

## Unterschied zu Fade Out

- Fade In: Die Deckkraft steigt von 0 auf 1 – das Element erscheint und bleibt an seiner Layout-Position
- Fade Out: Die Deckkraft sinkt von 1 auf 0 – das Element verschwindet und gibt seinen Platz frei

# Fade In

## Beschreibung

Fade In blendet ein Element sanft ein, indem die Deckkraft von 0 auf 1 steigt. Position und
Größe bleiben unverändert, sodass sich im Layout nichts anderes verschiebt.

## Verwendung

- Toasts und Benachrichtigungen sanft einblenden
- Modale Overlays und Dialoge beim Öffnen weich erscheinen lassen
- Bilder nach dem Laden einblenden, statt sie „aufpoppen“ zu lassen
- Reiter und Panels beim Wechseln überblenden
- Onboarding-Elemente gestaffelt einblenden (in Kombination mit Stagger)
- Tooltip- und Popover-Einblendung ohne ablenkende Bewegung

## Dauer

- Typisch: 150–400 ms
- Mikro-Feedback (Hover, Tooltip): 100–200 ms
- Modale Bereiche und Overlays: 250–400 ms

## Unterschied zu Fade Out

- Fade In: Die Deckkraft steigt von 0 auf 1 – das Element erscheint und behält seine
  Layoutposition
- Fade Out: Die Deckkraft sinkt von 1 auf 0 – das Element verschwindet und gibt seinen
  Platz auf

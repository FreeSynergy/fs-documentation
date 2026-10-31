# Morph

## Beschreibung

Morph wandelt die Form eines Elements weich in eine andere Form: SVG-Pfade, Eckenradien und Proportionen gehen kontinuierlich ineinander über.
Das Element bleibt dabei dasselbe Objekt – es wechselt nur seine Gestalt.
Auch Größe und Farbe können in denselben Übergang einbezogen werden.

## Verwendung

- Icon-Morphing: Play ↔ Pause, Hamburger ↔ Schließen
- FAB expandiert beim Antippen zum Dialogpanel
- Avatar-Kreis wird beim Auswählen zum abgerundeten Rechteck
- Schalter- und Slider-Griff wechseln zustandsabhängig die Form
- Onboarding: ein Objekt nimmt schrittweise seine nächste Form an
- Zustands-Icons (z. B. Wolke ↔ Sonne) ohne harten Sprung

## Dauer

- Typisch: 300–600 ms

## Unterschied zu Flip und Cross Fade

- Flip: dreht das Element um 180° und zeigt eine andere Rückseite; Morph
  verformt die Silhouette selbst, ohne Drehung.
- Cross Fade: zwei eigenständige Elemente tauschen per Deckkraft; Morph ist
  ein Element, dessen Kontur durchgehend interpoliert wird.

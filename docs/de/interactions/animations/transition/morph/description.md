# Morph

## Beschreibung

Morph verwandelt die Form eines Elements weich in eine andere Form. SVG-Pfade, Eckenradien und Proportionen gehen stetig ineinander über. Das Element bleibt dabei dasselbe Objekt – es ändert nur seine Gestalt. Größe und Farbe können im selben Übergang mit verändert werden.

## Verwendung

- Icon-Morphing: Play ↔ Pause, Hamburger ↔ Schließen
- ein FAB wächst beim Tippen zu einem Dialogpanel
- ein Avatar-Kreis wird bei Auswahl zu einem abgerundeten Rechteck
- Schalter- und Schieberegler-Griffe ändern ihre Form je nach Zustand
- Onboarding: ein Objekt nimmt nach und nach seine nächste Form an
- Statusicons (z. B. Wolke ↔ Sonne) ohne harten Sprung

## Dauer

- Typisch: 300–600 ms

## Unterschied zu Flip und Cross Fade

- Flip: dreht das Element um 180° und zeigt eine andere Rückseite. Morph verformt die Silhouette selbst, ohne Drehung.
- Cross Fade: zwei unabhängige Elemente tauschen sich über die Deckkraft. Morph ist ein einzelnes Element, dessen Kontur durchgehend interpoliert wird.

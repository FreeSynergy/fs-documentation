# Tooltip

| Feld | Wert |
|------|------|
| **Kategorie** | `overlays` |
| **Erbt von** | `base` |
| **Varianten** | `top`, `bottom`, `left`, `right`, `auto` |
| **Zustände** | `open` |
| **Gesten** | `tap`, `long-press` |
| **Animationen** | `fade-in`, `fade-out` |
| **Verwandt** | `popover`, `label`, `base`, `field` |
| **Status** | dokumentiert |

## Beschreibung

Ein Tooltip zeigt eine kurze Erklärung zu einem Element — als Text, ohne interaktiven
Inhalt. Er erscheint beim Überfahren oder langen Drücken und verschwindet von selbst.

## Verwendungszweck

- Erklären von Schaltflächen nur mit Icon und abgekürzten Werten
- Ein kurzer Zusatz zu einem Feld (nicht als Ersatz für ein Label)
- Vollständiger Text, wenn ein Feld nur seinen Inhalt anzeigt

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **top** | über dem Element (Standard) |
| **bottom** | unter dem Element |
| **left** / **right** | seitlich |
| **auto** | wählt selbst die beste Seite, wenn es eng wird |

## Funktionen

- Verzögerung (`delay`) gegen versehentliches Auslösen
- Pfeil (`arrow`) markiert das Bezugselement
- Mobil: wird per langem Drücken ausgelöst

## Abgrenzung

- **Nicht verwechseln mit** [popover](../popover/): ein Popover enthält interaktive Inhalte,
  ein Tooltip nur Text.
- **Nicht verwechseln mit** [hover-card](../hover-card/): die Vorschaukarte zeigt eine Vorschau als Karte
  und bleibt offen, solange der Zeiger im Inhalt bleibt.
- **Nicht verwechseln mit** [label](../../../primitives/basics/label/): ein Label ist dauerhaft sichtbar
  und fest mit dem Element verbunden.

## Best Practices

- Unter 100 Zeichen; lieber Sätze als Absätze.
- Entscheidende Informationen nie ausschließlich im Tooltip verbergen.
- Tastaturnutzer erreichen den Tooltip über `focus`.
- Schaltflächen nur mit Icon brauchen zusätzlich ein `aria-label`.

## Siehe auch

- [overlays – Übersicht](../index.md)
- [Popover](../popover/)
- [Basiskomponente](../../../primitives/basics/base.md)
- [Gesten](../../../../interactions/gestures/)
- [Animationen](../../../../interactions/animations/)

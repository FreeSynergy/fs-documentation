# Tooltip (Kurzinfo)

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

Ein Tooltip zeigt eine kurze Erklärung zu einem Element – als Text, ohne
interaktiven Inhalt. Er erscheint bei Hover oder Langdruck und verschwindet
von selbst.

## Verwendungszweck

- Erklärung von Icon-only-Buttons und abgekürzten Werten
- Kurzer Zusatz zu einem Feld (nicht als Ersatz für ein Label)
- Vollständiger Text, wenn ein Feld den Inhalt nur anzeigt

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **top** | über dem Element (Standard) |
| **bottom** | unter dem Element |
| **left** / **right** | seitlich |
| **auto** | wählt bei Platzmangel selbst die beste Seite |

## Features

- Verzögerung (`delay`) gegen versehentliches Auslösen
- Pfeil (`arrow`) markiert das Bezugselement
- Mobil: Auslösung per Langdruck

## Abgrenzung

- **Nicht verwechseln mit** [popover](../popover/): ein Popover enthält
  interaktive Inhalte, ein Tooltip ausschließlich Text.
- **Nicht verwechseln mit** [hover-card](../hover-card/): die Hover-Card zeigt eine
  Vorschau als Karte und bleibt offen, solange der Zeiger im Inhalt bleibt.
- **Nicht verwechseln mit** [label](../../basics/label/): ein Label ist ständig
  sichtbar und mit dem Element verknüpft.

## Best Practices

- Unter 100 Zeichen; Sätze statt Absätze.
- Nie entscheidende Information ausschließlich im Tooltip verstecken.
- Tastaturnutzer erreichen den Tooltip über `focus`.
- Icon-only-Buttons brauchen zusätzlich ein `aria-label`.

## Siehe auch

- [overlays – Übersicht](../index.md)
- [Popover](../popover/)
- [Basiskomponente](../../basics/base/)
- [Gesten](../../../gestures/)
- [Animationen](../../../animations/)

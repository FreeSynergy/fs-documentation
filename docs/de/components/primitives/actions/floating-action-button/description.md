# Floating Action Button (FAB)

| Feld | Wert |
|------|------|
| **Category** | `actions` |
| **Inherits from** | `base` |
| **Variants** | `standard FAB`, `mini FAB`, `extended FAB` |
| **States** | `expanded`, `scroll-hidden` |
| **Gestures** | `tap`, `long-press` |
| **Animations** | `ripple`, `pop-in`, `press` |
| **Related** | `button`, `button-group`, `tooltip` |
| **Status** | documented |

## Beschreibung
Ein Floating Action Button (FAB) ist ein runder Hauptaktions-Button, meist unten
rechts platziert.

## Zweck

- Die wichtigste Aktion zeigen
- Schneller Zugriff auf die Hauptfunktion
- Optische Betonung

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **standard FAB** | großer Button (56px) |
| **mini FAB** | kleiner Button (40px) |
| **extended FAB** | mit Text (z. B. "Neu +") |

## Funktionen

- Hover-Effekt (Vergrößerung)
- Welleneffekt beim Klicken (ripple)
- Schatten für die Erhebung
- Badge (mit Anzahl/Status)

## Abgrenzung

- **Nicht verwechseln mit** [button](../button/): Ein Button steht in einem Layout-Kontext
  (Formular, Werkzeugleiste, Fußzeile einer Karte); der FAB schwebt über dem Inhalt und trägt die *eine*
  Hauptaktion der Ansicht.
- **Nicht verwechseln mit** [button-group](../button-group/): Mehrere gleichrangige Aktionen gehören in eine Gruppe
  oder ein Menü, nicht in mehrere FABs nebeneinander.
- Der FAB öffnet Nebenaktionen als Aktionsfächer (`expanded`), nicht als zweiten FAB.
- Auf großen Desktop-Flächen ist der FAB optional; dort gehört die Aktion in die
  [Werkzeugleiste](../../../widgets/navigation/toolbar/) oder in die Kopfzeile.

## Best Practices

- Nur ein FAB pro Bildschirm
- Die wichtigste Aktion zeigen
- Eindeutiges Icon (z. B. + für Neu)
- Hover-Text (Tooltip)

## Position

| Position | Beschreibung |
|----------|--------------|
| **unten rechts** | Standard |
| **unten links** | unten links (RTL-Sprachen) |
| **Mitte** | in der Mitte (selten) |

## Siehe auch

- [actions – Übersicht](../index.md)
- [Basiskomponente](../../basics/base.md)

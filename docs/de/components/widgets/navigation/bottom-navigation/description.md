# Bottom Navigation

| Feld | Wert |
|------|------|
| **Kategorie** | `navigation` |
| **Erbt von** | `base` |
| **Varianten** | `Active Icon`, `Text Labels`, `Icon Only` |
| **Zustände** | `aktiv` |
| **Gesten** | `tap`, `swipe` |
| **Animationen** | `highlight`, `press` |
| **Verwandt** | `tabs`, `menu`, `sidebar`, `toolbar`, `floating-action-button` |
| **Status** | dokumentiert |

## Beschreibung
Die Bottom Navigation ist eine Navigation am unteren Bildschirmrand, typisch für
Mobile-first-Design.

## Verwendungszweck

- Hauptnavigation auf dem Smartphone
- 3–5 Hauptpunkte
- Schneller Zugriff mit dem Daumen

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Active Icon** | der aktive Eintrag ist hervorgehoben |
| **Text Labels** | mit Text |
| **Icon Only** | nur Symbole (weniger Platz) |

!!! info "Einordnung"
    Die Navbar, die Bibliotheken getrennt führen (`navigation-menu`), ist hier eine Variante:
    oben angedockt mit `placement = "top"`. Die horizontale Menüleiste ist
    [`menu`](../menu/) mit der Variante `menubar`.

## Features

- Maximal 5 Hauptpunkte
- Klare Markierung (aktiver Eintrag)
- Animation (beim Wechsel)
- Barrierefreiheit

## Abgrenzung

- **Nicht verwechseln mit** [tabs](../tabs/): Tabs wechseln Inhalte **innerhalb** einer Ansicht,
  diese Leiste wechselt die Ansicht selbst.
- **Nicht verwechseln mit** [sidebar](../sidebar/): die Sidebar sitzt dauerhaft am Rand,
  diese Leiste gehört an den unteren Rand kleiner Bildschirme.
- **Nicht verwechseln mit** [toolbar](../toolbar/): eine Toolbar enthält Aktionen,
  diese Leiste enthält Ziele.
- Eine einzelne Hauptaktion gehört zum [floating-action-button](../../../primitives/actions/floating-action-button/).

## Best Practices

- Nur Hauptfunktionen; Nebensächliches gehört auf die erste Ebene der Ansicht, nicht in die Leiste.
- Höchstens fünf Einträge, jeweils mit Text, wenn Platz ist.
- Der aktive Eintrag muss erkennbar bleiben, nicht nur an der Farbe.
- Die Leiste bleibt über der Tastatur und respektiert die Gestensteuerung des Geräts.

## Siehe auch

- [navigation – Übersicht](../index.md)
- [Tabs](../tabs/) — Inhalte innerhalb einer Ansicht
- [Sidebar](../sidebar/) — Navigation am Rand
- [Basiskomponente](../../../primitives/basics/base.md)

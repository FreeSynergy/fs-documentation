# Bottom Navigation (Mobile)

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
Bottom Navigation ist eine Navigation unten am Bildschirm, typisch für Mobile-First-Design.

## Verwendungszweck

- Hauptnavigation auf Mobile
- 3-5 Hauptpunkte
- Schneller Zugriff mit Daumen

## Varianten

| Variant | Beschreibung |
|---------|--------------|
| **Active Icon** | Aktiver Punkt hervorgehoben |
| **Text Labels** | Mit Text |
| **Icon Only** | Nur Icons (weniger Platz) |

!!! info "Einordnung"
    Die in Bibliotheken eigene Navbar (`navigation-menu`) ist hier eine Variante: oben
    angedockt mit `placement = "top"`. Die horizontale Menüleiste ist
    [`menu`](../menu/) mit der Variante `menubar`.

## Features

- Maximum 5 Hauptpunkte
- Clear-Indicator (aktiver Punkt)
- Animation (bei Wechsel)
- Accessibility (Barrierefreiheit)

## Abgrenzung

- **Nicht verwechseln mit** [tabs](../tabs/): Tabs wechseln Inhalt **innerhalb** einer Ansicht,
  diese Leiste wechselt die Ansicht selbst.
- **Nicht verwechseln mit** [sidebar](../sidebar/): die Seitenleiste ist dauerhaft am Rand,
  diese Leiste gehört an den unteren Rand kleiner Bildschirme.
- **Nicht verwechseln mit** [toolbar](../toolbar/): eine Werkzeugleiste enthält Aktionen,
  diese Leiste enthält Ziele.
- Eine einzelne Hauptaktion gehört zum [floating-action-button](../../actions/floating-action-button/).

## Best Practices

- Nur Hauptfunktionen; Sekundäres in die erste Ebene der Ansicht, nicht in die Leiste.
- Höchstens fünf Punkte, jeder mit Klartext, wenn Platz ist.
- Der aktive Punkt ist dauerhaft zu erkennen, nicht nur durch Farbe.
- Leiste bleibt über der Tastatur stehen und respektiert die Gestensteuerung des Geräts.

## Siehe auch

- [navigation – Übersicht](../index.md)
- [Tabs](../tabs/) — Inhalt innerhalb einer Ansicht
- [Sidebar](../sidebar/) — Navigation am Rand
- [Basiskomponente](../../basics/base/)

# Floating Action Button (FAB)

| Feld | Wert |
|------|------|
| **Kategorie** | `actions` |
| **Erbt von** | `base` |
| **Varianten** | `Standard FAB`, `Mini FAB`, `Extended FAB` |
| **Zustände** | `expanded`, `scroll-hidden` |
| **Gesten** | `tap`, `long-press` |
| **Animationen** | `ripple`, `pop-in`, `press` |
| **Verwandt** | `button`, `button-group`, `tooltip` |
| **Status** | dokumentiert |

## Beschreibung
Ein Floating Action Button (FAB) ist ein runder Hauptaktion-Button, der meist rechts unten positioniert ist.

## Verwendungszweck

- Primäre Aktion anzeigen
- Schneller Zugriff auf Hauptfunktion
- Visueller Fokus

## Varianten

| Variant | Beschreibung |
|---------|--------------|
| **Standard FAB** | Großer Button (56px) |
| **Mini FAB** | Kleiner Button (40px) |
| **Extended FAB** | Mit Text (z.B. "Neu +") |

## Features

- Hover-Effect (Vergrößerung)
- Ripple Effect (Welleneffekt bei Klick)
- Shadow (Schatten für Hebung)
- Badge (mit Anzahl/Status)

## Abgrenzung

- **Nicht verwechseln mit** [button](../button/): ein Button sitzt im Layoutkontext
  (Formular, Toolbar, Kartenfuß); der FAB schwebt über dem Inhalt und trägt die *eine*
  Hauptaktion der Ansicht.
- **Nicht verwechseln mit** [button-group](../button-group/): mehrere gleichwertige
  Aktionen gehören in eine Gruppe oder ein Menü, nicht in mehrere FABs nebeneinander.
- Sekundäre Aktionen öffnet der FAB als Aktionsfächer (`expanded`), nicht als zweiter FAB.
- Auf großen Desktop-Flächen ist der FAB verzichtbar; dort gehört die Aktion in
  [toolbar](../../navigation/toolbar/) oder in die Kopfzeile.

## Best Practices

- Nur eine FAB pro Bildschirm
- Wichtigste Aktion anzeigen
- Clear-Icon (z.B. + für Neu)
- Hover-Text (Tooltip)

## Positionierung

| Position | Beschreibung |
|----------|--------------|
| **Bottom Right** | Standard (rechts unten) |
| **Bottom Left** | Links unten (RTL-Sprachen) |
| **Center** | In der Mitte (selten) |

## Siehe auch

- [actions – Übersicht](../index.md)
- [Basiskomponente](../../basics/base/)

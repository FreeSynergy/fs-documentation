# Split View (Geteilter Bildschirm)

| Feld | Wert |
|------|------|
| **Kategorie** | `containers` |
| **Erbt von** | `base` |
| **Varianten** | `Fixed Split`, `Resizable Split`, `Responsive` |
| **Zustände** | `dragging`, `collapsed` |
| **Gesten** | `drag`, `tap` |
| **Animationen** | `expand`, `collapse` |
| **Verwandt** | `panel`, `accordion`, `drawer`, `tabs` |
| **Status** | dokumentiert |

## Beschreibung
Ein Split View ist ein Layout mit zwei Bereichen side-by-side.

## Verwendungszweck

- Liste + Detailansicht
- Vergleichsansichten
- Sidebar + Hauptinhalt
- Previews

## Varianten

| Variant | Beschreibung |
|---------|--------------|
| **Fixed Split** | Fixe Breite |
| **Resizable Split** | Breite per Drag änderbar |
| **Responsive** | Auto-Adjustierung |

!!! info "Einordnung"
    Der in Bibliotheken übliche Baustein `resizable` ist keine eigene Komponente, sondern
    die Variante `Resizable Split` dieser Komponente (Entscheidungsregel in
    [Basiskomponente](../../basics/base/): gleicher Datensatz, anderes Verhalten beim Ziehen).

## Features

- Resizable (Breite änderbar)
- Draggable (Verschiebbar)
- Responsive (Auto-Adjustierung)
- Collapsible (Ein/Ausklappen)

## Abgrenzung

- **Nicht verwechseln mit** [panel](../panel/): ein Panel ist *ein* Behälter; der Split View
  teilt die Fläche in zwei zueinander gehörige Bereiche mit Trennlinie.
- **Nicht verwechseln mit** [drawer](../../overlays/drawer/): der Drawer legt sich über den
  Inhalt; hier bleiben beide Bereiche gleichzeitig sichtbar.
- **Nicht verwechseln mit** [tabs](../../navigation/tabs/): Tabs wechseln denselben Bereich,
  der Split View zeigt beide Bereiche zugleich (Liste und Detail).
- **Nicht verwechseln mit** [accordion](../accordion/): vertikal gestapelt und einklappbar,
  nicht seitlich geteilt.
- Einklappen eines Bereichs ist ein Zustand (`collapsed`), keine eigene Komponente.

## Best Practices

- Clear-Order
- Responsive
- Accessibility
- Feedback

## Layout

```
┌─────────────────┬──────────────────────┐
│                 │                      │
│   Bereich 1     │     Bereich 2        │
│   (Sidebar)     │     (Hauptinhalt)    │
│                 │                      │
└─────────────────┴──────────────────────┘
```

## Siehe auch

- [containers – Übersicht](../index.md)
- [Basiskomponente](../../basics/base/)

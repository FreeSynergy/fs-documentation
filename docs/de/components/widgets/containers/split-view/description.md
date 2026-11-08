# Split View

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
Eine Split View ist ein Layout mit zwei nebeneinanderliegenden Bereichen.

## Verwendungszweck

- Listen- + Detailansicht
- Vergleichsansichten
- Sidebar + Hauptinhalt
- Vorschauen

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Fixed Split** | feste Breite |
| **Resizable Split** | Breite lässt sich per Ziehen ändern |
| **Responsive** | passt sich automatisch an |

!!! info "Einordnung"
    Der Baustein, den Bibliotheken meist `resizable` nennen, ist keine eigene Komponente,
    sondern die Variante `Resizable Split` dieser Komponente (Entscheidungsregel in der
    [Basiskomponente](../../../primitives/basics/base.md): gleiche Datenmenge, unterschiedliches Verhalten beim Ziehen).

## Features

- Veränderbar (Breite ändern)
- Verschiebbar (verschieben)
- Responsiv (passt sich automatisch an)
- Einklappbar (ein- und ausklappen)

## Abgrenzung

- **Nicht verwechseln mit** [panel](../panel/): ein Panel ist *ein* Container; die Split View
  teilt die Fläche in zwei zusammengehörige Bereiche mit einer Trennlinie.
- **Nicht verwechseln mit** [drawer](../../overlays/drawer/): der Drawer liegt über dem
  Inhalt; hier bleiben beide Bereiche gleichzeitig sichtbar.
- **Nicht verwechseln mit** [tabs](../../navigation/tabs/): Tabs wechseln denselben Bereich,
  die Split View zeigt beide Bereiche auf einmal (Liste und Detail).
- **Nicht verwechseln mit** [accordion](../accordion/): dieses ist vertikal gestapelt und einklappbar,
  nicht seitlich geteilt.
- Einen Bereich einzuklappen ist ein Zustand (`collapsed`), keine eigene Komponente.

## Best Practices

- Klare Reihenfolge
- Responsiv
- Barrierefreiheit
- Rückmeldung

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
- [Basiskomponente](../../../primitives/basics/base.md)

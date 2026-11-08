# Popover

| Feld | Wert |
|------|------|
| **Kategorie** | `overlays` |
| **Erbt von** | `base` |
| **Varianten** | `inhalt`, `aktionen`, `formular` |
| **Zustände** | `open` |
| **Gesten** | `tap` |
| **Animationen** | `expand`, `fade-in` |
| **Verwandt** | `tooltip`, `modal`, `select`, `context-menu`, `base` |
| **Status** | dokumentiert |

## Beschreibung

Ein Popover ist ein kleines Overlay mit interaktivem Inhalt: Aktionen, einer Vorschau oder einem
kurzen Formular. Es hängt an einem Auslöser-Element, nimmt aber — anders als ein Modal — nicht
den ganzen Bildschirm ein.

## Verwendungszweck

- Zweitaktionen an einem Eintrag (Mehr-Menü mit Schaltflächen)
- Schnelle Eingabe ohne Seitenwechsel (Datum setzen, Markierung vergeben)
- Detaillierte Vorschau eines Eintrags (Kurzfassung vor dem Öffnen)

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **inhalt** | Text, Bilder oder Vorschau, keine Formulareingabe |
| **aktionen** | Liste von Aktionen (Unterschied zum Kontextmenü: fester Auslöser) |
| **formular** | kleines Formular, z. B. zum Setzen eines Datums oder einer Farbe |

## Funktionen

- Der Fokus wandert ins Popover und kehrt nach dem Schließen zum Auslöser zurück
- Schließt sich bei einem Klick außerhalb, bei Escape oder bei einer Aktion im Popover
- Positionierung am Auslöser wie beim [Tooltip](../tooltip/)

## Abgrenzung

- **Nicht verwechseln mit** [tooltip](../tooltip/): Tooltip = nur Text, nie interaktiv.

- **Nicht verwechseln mit** [modal](../modal/): ein Modal sperrt und steht zentriert; ein Popover bleibt
  am Auslöser und lässt den Rest bedienbar.

- **Nicht verwechseln mit** [dropdown](../../../primitives/fields/select/): ein Dropdown wählt einen
  Wert aus einer Liste, ein Popover trägt beliebigen Inhalt.

- **Nicht verwechseln mit** [context-menu](../context-menu/): das Kontextmenü folgt dem Rechtsklick,
  ein Popover folgt einem festen Auslöser.

## Best Practices

- Escape und ein Klick außerhalb müssen es schließen; der Fokus kehrt zum Auslöser zurück.
- `aria-expanded` am Auslöser ist Pflicht.
- Kein Ersatz für einen vollständigen Dialog: bei mehr als ~5 Eingabefeldern ein `modal` verwenden.

## Siehe auch

- [Tooltip](../tooltip/)
- [Modal](../modal/)
- [Context Menu](../context-menu/)
- [Basiskomponente](../../../primitives/basics/base.md)

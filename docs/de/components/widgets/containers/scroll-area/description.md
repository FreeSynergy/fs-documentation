# Scroll Area (Scrollbereich)

| Feld | Wert |
|------|------|
| **Kategorie** | `containers` |
| **Erbt von** | `base` |
| **Varianten** | `vertikal`, `horizontal`, `beides` |
| **Zustände** | `atTop`, `atBottom` |
| **Gesten** | `swipe`, `drag` |
| **Animationen** | `fade-in` |
| **Verwandt** | `split-view`, `list-view`, `sidebar` |
| **Rolle** | `group` |
| **Status** | dokumentiert |

## Beschreibung

Ein Scroll Area ist eine Fläche mit fester Abmessung, deren Inhalt scrollt. Er
ergänzt Scrollbalken, Randverläufe und Tastaturbedienung. So bleibt der Inhalt
auf einer gleichbleibenden Höhe.

## Verwendungszweck

- Chats und Verläufe mit fester Höhe in einer Spalte
- Lange Listen in einer Card oder einem Panel
- Horizontale Bereiche wie Werkzeugleisten oder Bildreihen

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **vertikal** | nur die Höhe begrenzt, Standard |
| **horizontal** | nur die Breite begrenzt |
| **beides** | Fläche mit beiden Scrollrichtungen |

## Funktionen

- Ein Randverlauf zeigt, dass es weiteren Inhalt gibt
- Das Scrollen folgt dem Inhalt automatisch (`follow`), z. B. bei neuen Nachrichten
- Der Scrollbalken blendet beim Scrollen ein und im Ruhezustand aus
- Tastatur: `Pfeiltasten`, `Bild auf/ab`, `Pos1`/`Ende`

## Abgrenzung

- **Nicht verwechseln mit** [list-view](../../data/list-view/): Die Liste ordnet Inhalte an.
  Der Scroll Area regelt nur das Scrollen.
- **Nicht verwechseln mit** `overflow: auto`: Dort gibt es keine Verläufe, keine
  Anzeigen und kein Nachziehen.

## Best Practices

- Höchstens zwei unabhängig scrollende Bereiche pro Bildschirmbereich.
- Beim Nachladen oben die Scrollposition halten. Sonst springt der Inhalt.
- Reduzierte Bewegung respektieren: kein sanftes Nachziehen mit `respectReducedMotion`.

## Siehe auch

- [Split View](../split-view/)
- [List View](../../data/list-view/)
- [Base-Komponente](../../../primitives/basics/base.md)

# Skeleton (Platzhalter)

| Feld | Wert |
|------|------|
| **Kategorie** | `feedback` |
| **Erbt von** | `base` |
| **Varianten** | `text`, `rect`, `circle`, `card`, `list-item`, `table-row`, `avatar` |
| **Zustände** | `loading` ist der einzige Zustand |
| **Gesten** | keine – nicht bedienbar |
| **Animationen** | `pulse` |
| **Verwandt** | `spinner`, `progress`, `list-view`, `base` |
| **Status** | dokumentiert |

## Beschreibung

Ein Skeleton ist ein Platzhalter in der späteren Form des Layouts. Er zeigt, wo und
wie groß Inhalte erscheinen, während sie geladen werden.

## Verwendungszweck

- Ansichten sofort gliedern, noch bevor die Daten da sind
- Form von Listen, Tabellen und Cards während des Ladens andeuten
- Die gefühlte Ladezeit verkürzen (das Layout steht, der Inhalt folgt)

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **text** | ein oder mehrere Textbalken |
| **rect** | Rechteck (Bild, Card, Diagramm) |
| **circle** | Kreis (Avatar, Statuspunkt) |
| **card** | kombinierter Platzhalter im Card-Layout |
| **list-item** | Zeile mit Icon, Text und Metadaten |
| **table-row** | Tabellenzeile mit Zellbreiten |
| **avatar** | Kreis plus zwei Textbalken |

## Funktionen

- Zwei Arten von Animation: `shimmer` (ein wandernder Glanz) und `pulse` (Atmen)
- Kombinierbar zu ganzen Gerüsten (ein Skeleton-Layout pro Ansicht)
- Breite und Höhe frei einstellbar, damit das spätere Layout nicht springt

## Abgrenzung

- **Nicht verwechseln mit** [spinner](../spinner/): Ein Spinner ist ein Signal.
  Ein Skeleton ist ein Platzhalter mit Form.

- **Nicht verwechseln mit** [empty-state](../empty-state/): Der Empty State zeigt „keine Daten“.
  Das Skeleton zeigt „Daten kommen noch“.

- **Nicht verwechseln mit** [progress](../progress/): Progress begleitet eine gestartete
  Aktion. Das Skeleton überbrückt nur das Warten auf eine Anzeige.

## Best Practices

- Die Skeleton-Formen entsprechen dem echten Layout. Sonst springt die Ansicht.
- Höchstens zwei oder drei Wiederholungen einer Zeile. Sonst wird die Liste für Inhalt gehalten.

- Nach dem Laden ohne Sprung ersetzen (Höhe beibehalten).
- Bei reduzierter Bewegung die Animation auf `none` setzen.

## Siehe auch

- [Spinner](../spinner/)
- [Progress](../progress/)
- [List View](../../../widgets/data/list-view/)
- [Base-Komponente](../../basics/base.md)

# Skeleton (Platzhalter)

| Feld | Wert |
|------|------|
| **Kategorie** | `feedback` |
| **Erbt von** | `base` |
| **Varianten** | `text`, `rect`, `circle`, `card`, `list-item`, `table-row`, `avatar` |
| **Zustände** | `loading` ist der einzige Zustand |
| **Gesten** | keine — nicht bedienbar |
| **Animationen** | `pulse` |
| **Verwandt** | `spinner`, `progress`, `list-view`, `base` |
| **Status** | dokumentiert |

## Beschreibung

Ein Skeleton ist ein Platzhalter in der späteren Layoutform. Er zeigt, wo und
wie groß Inhalte erscheinen, während sie geladen werden.

## Verwendungszweck

- Ansichten sofort strukturieren, bevor Daten eintreffen
- Listen, Tabellen und Karten beim Laden andeuten
- Wahrgenommene Ladezeit verkürzen (Layout steht, Inhalte folgen)

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **text** | ein oder mehrere Textbalken |
| **rect** | Rechteck (Bild, Karte, Diagramm) |
| **circle** | Kreis (Avatar, Statuspunkt) |
| **card** | kombinierter Platzhalter im Kartenlayout |
| **list-item** | Zeile mit Icon, Text und Meta |
| **table-row** | Tabellenzeile mit Zellenbreiten |
| **avatar** | Kreis plus zwei Textbalken |

## Features

- Zwei Animationsarten: `shimmer` (wandernder Glanz) und `pulse` (Atmen)
- Kombinierbar zu ganzen Gerüsten (ein Skeleton-Layout pro Ansicht)
- Breite und Höhe frei setzbar, damit das spätere Layout nicht springt

## Abgrenzung

- **Nicht verwechseln mit** [spinner](../spinner/): ein Spinner ist ein Signal,
  ein Skeleton ist ein Platzhalter mit Form.

- **Nicht verwechseln mit** empty-state (geplant): empty-state zeigt „keine Daten“,
  Skeleton zeigt „Daten kommen noch“.

- **Nicht verwechseln mit** [progress](../progress/): Progress begleitet eine
  begonnene Aktion, Skeleton nur das Warten auf Anzeige.

## Best Practices

- Skeleton-Formate entsprechen dem echten Layout – sonst springt die Ansicht.
- Höchstens zwei bis drei Wiederholungen einer Zeile, sonst wird die Liste
  als Inhalt missverstanden.

- Nach dem Laden ohne Sprung ersetzen (Höhe beibehalten).
- Bei reduzierter Bewegung Animation auf `none` stellen.

## Siehe auch

- [Spinner](../spinner/)
- [Progress](../progress/)
- [List View](../../data/list-view/)
- [Basiskomponente](../../basics/base/)

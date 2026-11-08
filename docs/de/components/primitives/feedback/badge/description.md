# Badge (Abzeichen)

| Feld | Wert |
|------|------|
| **Kategorie** | `feedback` |
| **Erbt von** | `base` |
| **Varianten** | `status`, `counter`, `dot`, `outline` |
| **Zustände** | `versteckt` (Zähler 0) |
| **Gesten** | keine – nicht bedienbar |
| **Animationen** | `pop-in` (Zähleränderung) |
| **Verwandt** | `bottom-navigation`, `avatar`, `tags-input`, `alert`, `progress`, `base` |
| **Status** | dokumentiert |

## Beschreibung

Ein Badge ist ein kleines Anzeigeelement für Status, Zähler oder Kategorie.
Es wird auf oder neben anderen Elementen platziert und ist selbst nicht bedienbar.

## Verwendungszweck

- Zähler an Navigation und Werkzeugleisten (neue Nachrichten, offene Aufgaben)
- Status an Einträgen in Listen und Tabellen (offen, erledigt, blockiert)
- Einträge kategorisieren (Tags in der Anzeige, nicht in der Eingabe)

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **status** | einfarbige Fläche mit Text, z. B. „offen“ |
| **counter** | ein Zähler, z. B. an [bottom-navigation](../../../widgets/navigation/bottom-navigation/) |
| **dot** | nur ein Punkt, wenn der Platz minimal ist |
| **outline** | Rahmen statt Füllung, für schwache Hinweise |

## Funktionen

- Obergrenze der Zählung wird als „99+“ angezeigt
- Fünf Statusfarben, unabhängig vom Theme lesbar
- Kombinierbar mit [avatar](../../../widgets/data/avatar/) und Icons

## Abgrenzung

- **Nicht verwechseln mit** [tags-input](../../fields/tags-input/): Dort werden Tags
  eingegeben und gelöscht. Ein Badge zeigt nur an.

- **Nicht verwechseln mit** [alert](../alert/): Eine Meldung ist ein Textblock, ein Badge ist
  eine kurze Markierung.

- **Nicht verwechseln mit** [avatar](../../../widgets/data/avatar/): Ein Avatar steht für eine
  Person oder ein Objekt.

## Best Practices

- Höchstens 20 Zeichen. Lange Zustände als Wort ausschreiben, nicht nur über die Farbe.
- Ein Zähler darf nie der einzige Hinweis auf neuen Inhalt sein. Screenreader brauchen Text.
- Ein Status pro Eintrag. Mehrere Status als Liste unter dem Eintrag.

## Siehe auch

- [Progress](../progress/)
- [Alert](../alert/)
- [Avatar](../../../widgets/data/avatar/)
- [Base-Komponente](../../basics/base.md)

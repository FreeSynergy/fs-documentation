# Badge (Abzeichen)

| Feld | Wert |
|------|------|
| **Kategorie** | `feedback` |
| **Erbt von** | `base` |
| **Varianten** | `status`, `counter`, `dot`, `outline` |
| **Zustände** | - |
| **Gesten** | - |
| **Animationen** | - |
| **Verwandt** | `bottom-navigation`, `avatar`, `tags-input`, `alert`, `progress`, `base` |
| **Status** | dokumentiert |

## Beschreibung

Ein Badge ist ein kleines Anzeigeelement für Status, Zähler oder Kategorie.
Es wird anderen Elementen auf- oder beigestellt und ist selbst nicht bedienbar.

## Verwendungszweck

- Zähler an Navigation und Werkzeugleisten (neue Nachrichten, offene Aufgaben)
- Status an Einträgen in Listen und Tabellen (offen, erledigt, blockiert)
- Kategorisierung von Einträgen (Tags in der Anzeige, nicht in der Eingabe)

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **status** | Einfarbige Fläche mit Text, z. B. „offen“ |
| **counter** | Zähler, z. B. an [bottom-navigation](../../navigation/bottom-navigation/) |
| **dot** | nur ein Punkt, wenn der Platz minimal ist |
| **outline** | Rahmen statt Füllung, für schwache Hinweise |

## Features

- Zählerobergrenze mit „99+“-Darstellung
- Fünf Statusfarben, unabhängig vom Theme lesbar
- Kombinierbar mit [avatar](../../data/avatar/) und Icons

## Abgrenzung

- **Nicht verwechseln mit** [tags-input](../../fields/tags-input/): dort werden Tags
  eingegeben und gelöscht, ein Badge zeigt nur an.

- **Nicht verwechseln mit** [alert](../alert/): eine Meldung ist ein
  Textblock, ein Badge ein Kurzmarker.

- **Nicht verwechseln mit** [avatar](../../data/avatar/): ein Avatar stellt eine
  Person oder ein Objekt dar.

## Best Practices

- Höchstens 20 Zeichen; lange Zustände als Wort, nicht als Farbe allein.
- Zähler niemals der einzige Hinweis auf Neue Inhalte (Screenreader brauchen Text).
- Ein Status pro Eintrag; mehrere Status als Liste unter dem Eintrag.

## Siehe auch

- [Progress](../progress/)
- [Alert](../alert/)
- [Avatar](../../data/avatar/)
- [Basiskomponente](../../basics/base/)

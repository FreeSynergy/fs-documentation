# special (Spezielle Elemente)

Band [workbenches](../) – erhält Inhalte erst zur Laufzeit.

Zusammengesetzte Elemente mit eigener Datenstruktur: Editoren, Einbettungen, Karten und Ansichten, die es bei generischen Bibliotheken nicht gibt.

## Elemente

- [**code-editor**](./code-editor/) – Ein Code Editor ist ein Editor für Quellcode.
- [**dashboard**](./dashboard/) – Ein Dashboard ist eine Übersichtsseite mit Widgets.
- [**embed**](./embed/) – Ein **Embed** bindet fremden Inhalt in eine FreeSynergy-Oberfläche ein: ein anderes FreeSynergy-Programm, ein Widget oder eine externe Seite.
- [**whiteboard**](./whiteboard/) – Ein Whiteboard ist eine Zeichenfläche für Kollaboration.

## Steckbriefe

| Komponente | Erbt von | Varianten | Rolle | Status |
|------------|----------|-----------|-------|--------|
| [code-editor](./code-editor/) | `base` | `voll`, `nur-lesen`, `vergleich` | - | dokumentiert |
| [dashboard](./dashboard/) | `base` | `vorlage`, `anordbar`, `bericht` | - | dokumentiert |
| [embed](./embed/) | `base` | `app`, `widget`, `iframe` | - | dokumentiert |
| [whiteboard](./whiteboard/) | `base` | `zeichnung`, `formen`, `notizen`, `vorlage` | - | dokumentiert |

## Siehe auch

- [Komponenten-Übersicht](../../index.md)
- [Band workbenches](../)
- [Basiskomponente](../../primitives/basics/base.md)

# special

Band [workbenches](../) – erhält Inhalte erst zur Laufzeit.

Zusammengesetzte Elemente mit eigener Datenstruktur: Editoren, Einbettungen, Karten und Ansichten, die es bei generischen Bibliotheken nicht gibt.

## Elements

- [**code-editor**](./code-editor/) – Ein Code Editor ist ein Editor für Quellcode.
- [**dashboard**](./dashboard/) – Ein Dashboard ist eine Übersichtsseite mit Widgets.
- [**embed**](./embed/) – Ein **Embed** bindet fremden Inhalt in eine FreeSynergy-Oberfläche ein: ein anderes FreeSynergy-Programm, ein Widget oder eine externe Seite.
- [**whiteboard**](./whiteboard/) – Ein Whiteboard ist eine Zeichenfläche für Kollaboration.

## Profiles

| Component | Inherits from | Variants | Role | State |
| ------------ | ---------- | ----------- | ------- | -------- |
| [code-editor](./code-editor/) | `base` | `voll`, `nur-lesen`, `vergleich` | - | documented |
| [dashboard](./dashboard/) | `base` | `vorlage`, `anordbar`, `bericht` | - | documented |
| [embed](./embed/) | `base` | `app`, `widget`, `iframe` | - | documented |
| [whiteboard](./whiteboard/) | `base` | `zeichnung`, `formen`, `notizen`, `vorlage` | - | documented |

## See also

- [Component overview](../../index.md)
- [Band workbenches](../)
- [Base component](../../primitives/basics/base.md)

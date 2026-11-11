# fields (Felder)

Band [widgets](../) – kennt seine Inhalte beim Bauen.

Elemente zum Eingeben und Auswählen von Werten. Das Feld (`field`) hält dabei Beschriftung, Hilfetext und Fehlermeldung zusammen.

## Elemente

- [**date-picker**](./date-picker/) – Der Datumswähler öffnet ein Kalenderoverlay, in dem ein Datum oder ein Bereich ausgewählt wird.
- [**emoji-picker**](./emoji-picker/) – Ein Emoji Picker ist eine Emoji-Auswahl für Chat und Kommentare.
- [**file-upload**](./file-upload/) – Ein File Upload ist ein Element zum Auswählen und Hochladen von Dateien.
- [**range-calendar**](./range-calendar/) – Der Range Calendar wählt einen zusammenhängenden Zeitraum.
- [**rule-editor**](./rule-editor/) – Ein Regeleditor bearbeitet Regeln der Form „wenn ...
- [**time-picker**](./time-picker/) – Der Time Picker wählt eine Uhrzeit aus einer Liste möglicher Zeiten.

## Steckbriefe

| Komponente | Erbt von | Varianten | Rolle | Status |
|------------|----------|-----------|-------|--------|
| [date-picker](./date-picker/) | `base`, `date-input` | `einzeln`, `bereich`, `wiederkehrend` | `dialog` | dokumentiert |
| [emoji-picker](./emoji-picker/) | `base` | `inline`, `overlay`, `reaktion` | - | dokumentiert |
| [file-upload](./file-upload/) | `base` | `File Picker`, `Drag & Drop`, `Image Preview` | - | dokumentiert |
| [range-calendar](./range-calendar/) | `base`, `date-picker` | `zwei-monate`, `ein-monat` | `dialog` | dokumentiert |
| [rule-editor](./rule-editor/) | `base` | `list`, `simple` | - | Skizze |
| [time-picker](./time-picker/) | `base`, `date-input` | `liste`, `ziffernblatt` | `listbox` | dokumentiert |

## Siehe auch

- [Komponenten-Übersicht](../../index.md)
- [Band widgets](../)
- [Basiskomponente](../../primitives/basics/base.md)

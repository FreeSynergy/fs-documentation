# overlays (Overlays)

Elemente, die über anderem Inhalt erscheinen und eigenen Fokus bekommen. Sie haben eine eigene Lebensdauer und schließen mit `Esc` oder Klick außerhalb.

## Elemente

- [**alert-dialog**](./alert-dialog/) – Ein Bestätigungsdialog fragt nach, bevor eine Aktion ausgeführt wird.
- [**context-menu**](./context-menu/) – Ein Context Menu (Kontextmenü) wird durch Rechtsklick oder lange Touch-Aktion geöffnet und bietet kontextbezogene Optionen.
- [**drawer**](./drawer/) – Ein Drawer ist ein seitliches Overlay-Fenster (einklappbar).
- [**hover-card**](./hover-card/) – Die Vorschaukarte zeigt zu einem Verweis die wichtigsten Informationen zum Ziel — ohne die Adresse zu wechseln.
- [**modal**](./modal/) – Ein Modal ist ein Overlay-Fenster mit Fokus auf Inhalt.
- [**popover**](./popover/) – Ein Popover ist ein kleines Overlay mit interaktivem Inhalt: Aktionen, eine Vorschau oder ein kurzes Formular.
- [**tooltip**](./tooltip/) – Ein Tooltip zeigt eine kurze Erklärung zu einem Element – als Text, ohne interaktiven Inhalt.

## Steckbriefe

| Komponente | Erbt von | Varianten | Rolle | Status |
|------------|----------|-----------|-------|--------|
| [alert-dialog](./alert-dialog/) | `base`, `modal` | `bestaetigung`, `zerstoererisch` | `alertdialog` | dokumentiert |
| [context-menu](./context-menu/) | `base`, `menu` | `Standard`, `Long Press`, `Overflow Menu` | - | dokumentiert |
| [drawer](./drawer/) | `base` | `Left Drawer`, `Right Drawer`, `Bottom Drawer`, `Full Drawer` | - | dokumentiert |
| [hover-card](./hover-card/) | `base`, `popover` | `profil`, `dokument`, `vorschau` | `tooltip` | dokumentiert |
| [modal](./modal/) | `base` | `Small`, `Medium`, `Large`, `Fullscreen` | - | dokumentiert |
| [popover](./popover/) | `base` | `inhalt`, `aktionen`, `formular` | - | dokumentiert |
| [tooltip](./tooltip/) | `base` | keine | - | dokumentiert |

## Siehe auch

- [Komponenten-Übersicht](../index.md)
- [Basiskomponente](../basics/base/)

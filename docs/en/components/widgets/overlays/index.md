# overlays

Band [widgets](../) – kennt seine Inhalte beim Bauen.

Elemente, die über anderem Inhalt erscheinen und eigenen Fokus bekommen. Sie haben eine eigene Lebensdauer und schließen mit `Esc` oder Klick außerhalb.

## Elements

- [**alert-dialog**](./alert-dialog/) – Ein Bestätigungsdialog fragt nach, bevor eine Aktion ausgeführt wird.
- [**context-menu**](./context-menu/) – Ein Context Menu (Kontextmenü) wird durch Rechtsklick oder lange Touch-Aktion geöffnet und bietet kontextbezogene Optionen.
- [**drawer**](./drawer/) – Ein Drawer ist ein seitliches Overlay-Fenster (einklappbar).
- [**hover-card**](./hover-card/) – Die Vorschaukarte zeigt zu einem Verweis die wichtigsten Informationen zum Ziel — ohne die Adresse zu wechseln.
- [**modal**](./modal/) – Ein Modal ist ein Overlay-Fenster mit Fokus auf Inhalt.
- [**popover**](./popover/) – Ein Popover ist ein kleines Overlay mit interaktivem Inhalt: Aktionen, eine Vorschau oder ein kurzes Formular.
- [**tooltip**](./tooltip/) – Ein Tooltip zeigt eine kurze Erklärung zu einem Element – als Text, ohne interaktiven Inhalt.

## Profiles

| Component | Inherits from | Variants | Role | State |
| ------------ | ---------- | ----------- | ------- | -------- |
| [alert-dialog](./alert-dialog/) | `base`, `modal` | `bestaetigung`, `zerstoererisch` | `alertdialog` | documented |
| [context-menu](./context-menu/) | `base`, `menu` | `Standard`, `Long Press`, `Overflow Menu` | - | documented |
| [drawer](./drawer/) | `base` | `Left Drawer`, `Right Drawer`, `Bottom Drawer`, `Full Drawer` | - | documented |
| [hover-card](./hover-card/) | `base`, `popover` | `profil`, `dokument`, `vorschau` | `tooltip` | documented |
| [modal](./modal/) | `base` | `Small`, `Medium`, `Large`, `Fullscreen` | - | documented |
| [popover](./popover/) | `base` | `inhalt`, `aktionen`, `formular` | - | documented |
| [tooltip](./tooltip/) | `base` | `top`, `bottom`, `left`, `right`, `auto` | - | documented |

## See also

- [Component overview](../../index.md)
- [Band widgets](../)
- [Base component](../../primitives/basics/base.md)

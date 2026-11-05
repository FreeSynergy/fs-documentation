# overlays

Band [widgets](../) – knows its contents when it is built.

Elements that appear above other content and get their own focus. They have a lifetime of their own and close with `Esc` or a click outside.

## Elements

- [**alert-dialog**](./alert-dialog/) – A confirmation dialog asks before an action is carried out.
- [**context-menu**](./context-menu/) – A context menu is opened by right-click or a long touch action and offers context-related options.
- [**drawer**](./drawer/) – A drawer is a side overlay window (collapsible).
- [**hover-card**](./hover-card/) – The preview card shows the most important information about the target of a reference — without changing the address.
- [**key-verification**](./key-verification/) – A key verification lets a person check the key or device of a counterpart and confirm trust.
- [**modal**](./modal/) – A modal is an overlay window with focus on content.
- [**popover**](./popover/) – A popover is a small overlay with interactive content: actions, a preview or a short form.
- [**tooltip**](./tooltip/) – A tooltip shows a short explanation of an element — as text, without interactive content.

## Profiles

| Component | Inherits from | Variants | Role | Status |
|------------|----------|-----------|-------|--------|
| [alert-dialog](./alert-dialog/) | `base`, `modal` | `bestaetigung`, `zerstoererisch` | `alertdialog` | documented |
| [context-menu](./context-menu/) | `base`, `menu` | `Standard`, `Long Press`, `Overflow Menu` | - | documented |
| [drawer](./drawer/) | `base` | `Left Drawer`, `Right Drawer`, `Bottom Drawer`, `Full Drawer` | - | documented |
| [hover-card](./hover-card/) | `base`, `popover` | `profil`, `dokument`, `vorschau` | `tooltip` | documented |
| [key-verification](./key-verification/) | `base` | `fingerprint`, `qr`, `device-list` | - | skeleton |
| [modal](./modal/) | `base` | `Small`, `Medium`, `Large`, `Fullscreen` | - | documented |
| [popover](./popover/) | `base` | `inhalt`, `aktionen`, `formular` | - | documented |
| [tooltip](./tooltip/) | `base` | `top`, `bottom`, `left`, `right`, `auto` | - | documented |

## See also

- [Component overview](../../index.md)
- [Band widgets](../)
- [Base component](../../primitives/basics/base.md)

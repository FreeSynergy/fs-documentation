# navigation (Navigation)

Band [widgets](../) – knows its contents when it is built.

Elements that show or switch the way through the program: menus, bars, tabs,
sidebars and path indications.

## Elements

- [**bottom-navigation**](./bottom-navigation/) – Bottom navigation is navigation at the bottom of the screen, typical for mobile-first design.
- [**breadcrumb**](./breadcrumb/) – A breadcrumb is a path navigation (Home > Wiki > Page).
- [**command**](./command/) – The command palette is an overlay with an input field and a list of matches.
- [**language-switcher**](./language-switcher/) – A language switcher is a UI element for changing the application language.
- [**menu**](./menu/) – A menu is an ordered list of menu items that trigger actions or switch views.
- [**pagination**](./pagination/) – Pagination splits a long list into portions and offers switching between them.
- [**radial-menu**](./radial-menu/) – A radial menu (circular menu) arranges menu items around a centre point.
- [**sidebar**](./sidebar/) – The sidebar is a vertical navigation column, normally positioned on the left or right edge of the application.
- [**tabs**](./tabs/) – Tabs are tabs for switching between views.
- [**toolbar**](./toolbar/) – A toolbar is a row of buttons/icons for frequent actions.

## Profiles

| Component | Inherits from | Variants | Role | Status |
|-----------|---------------|----------|------|--------|
| [bottom-navigation](./bottom-navigation/) | `base` | `Active Icon`, `Text Labels`, `Icon Only` | - | documented |
| [breadcrumb](./breadcrumb/) | `base` | `pfad`, `gestutzt`, `zurueck` | - | documented |
| [command](./command/) | `base` | `palette`, `inline` | `dialog` | documented |
| [language-switcher](./language-switcher/) | `base` | `dropdown`, `knopetreihe`, `flaggen`, `kombiniert` | - | documented |
| [menu](./menu/) | `base` | `horizontal`, `vertical`, `dropdown`, `menubar`, `hamburger` | `menubar` | documented |
| [pagination](./pagination/) | `base` | `zahlen`, `vor-zurueck`, `nachladen`, `endlos` | - | documented |
| [radial-menu](./radial-menu/) | `base`, `menu` | `ring`, `sektoren`, `facher`, `launcher`, `kontext` | `menu` | documented |
| [sidebar](./sidebar/) | `base` | `angeheftet`, `ikonenleiste`, `einklappbar` | - | documented |
| [tabs](./tabs/) | `base` | `reiter`, `pille`, `karte` | - | documented |
| [toolbar](./toolbar/) | `base` | `standard`, `kontext`, `ribbon` | - | documented |

## See also

- [Component overview](../../index.md)
- [Band widgets](../)
- [Base component](../../primitives/basics/base.md)

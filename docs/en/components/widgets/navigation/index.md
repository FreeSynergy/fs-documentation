# navigation

Band [widgets](../) – kennt seine Inhalte beim Bauen.

Elemente, die den Weg durch das Programm zeigen oder umschalten: Menüs, Leisten, Reiter, Seitenleisten und Pfadangaben.

## Elements

- [**bottom-navigation**](./bottom-navigation/) – Bottom Navigation ist eine Navigation unten am Bildschirm, typisch für Mobile-First-Design.
- [**breadcrumb**](./breadcrumb/) – Ein Breadcrumb ist eine Pfadnavigation (Home > Wiki > Seite).
- [**command**](./command/) – Die Befehlspalette ist ein Overlay mit einem Eingabefeld und einer Trefferliste.
- [**language-switcher**](./language-switcher/) – Ein Language Switcher ist ein UI-Element zum Wechseln der Anwendungssprache.
- [**menu**](./menu/) – Ein Menü ist eine geordnete Liste von Menüpunkten, die Aktionen auslösen oder Ansichten wechseln.
- [**pagination**](./pagination/) – Seitennavigation teilt eine lange Liste in Portionen und bietet den Wechsel zwischen ihnen.
- [**radial-menu**](./radial-menu/) – Ein Radial Menu (Kreismenü) ordnet Menüpunkte um einen Mittelpunkt herum an.
- [**sidebar**](./sidebar/) – Die Sidebar ist eine vertikale Navigationssäule, die normalerweise links oder rechts am Rand der Anwendung positioniert ist.
- [**tabs**](./tabs/) – Tabs sind Reiter zum Umschalten zwischen Ansichten.
- [**toolbar**](./toolbar/) – Eine Toolbar ist eine Reihe von Buttons/Icons für häufige Aktionen.

## Profiles

| Component | Inherits from | Variants | Role | State |
| ------------ | ---------- | ----------- | ------- | -------- |
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

# navigation (Navigation)

Elemente, die den Weg durch das Programm zeigen oder umschalten: Menüs, Leisten, Reiter, Seitenleisten und Pfadangaben.

## Elemente

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

## Steckbriefe

| Komponente | Erbt von | Varianten | Rolle | Status |
|------------|----------|-----------|-------|--------|
| [bottom-navigation](./bottom-navigation/) | `base` | `Active Icon`, `Text Labels`, `Icon Only` | - | dokumentiert |
| [breadcrumb](./breadcrumb/) | `base` | `pfad`, `gestutzt`, `zurueck` | - | dokumentiert |
| [command](./command/) | `base` | `palette`, `inline` | `dialog` | dokumentiert |
| [language-switcher](./language-switcher/) | `base` | `dropdown`, `knopetreihe`, `flaggen`, `kombiniert` | - | dokumentiert |
| [menu](./menu/) | `base` | `horizontal`, `vertical`, `dropdown`, `menubar`, `hamburger` | `menubar` | dokumentiert |
| [pagination](./pagination/) | `base` | `zahlen`, `vor-zurueck`, `nachladen`, `endlos` | - | dokumentiert |
| [radial-menu](./radial-menu/) | `base`, `menu` | `ring`, `sektoren`, `facher`, `launcher`, `kontext` | `menu` | dokumentiert |
| [sidebar](./sidebar/) | `base` | `angeheftet`, `ikonenleiste`, `einklappbar` | - | dokumentiert |
| [tabs](./tabs/) | `base` | `reiter`, `pille`, `karte` | - | dokumentiert |
| [toolbar](./toolbar/) | `base` | `standard`, `kontext`, `ribbon` | - | dokumentiert |

## Siehe auch

- [Komponenten-Übersicht](../index.md)
- [Basiskomponente](../basics/base/)

# navigation (Navigation)

Band [widgets](../) – kennt seine Inhalte beim Bauen.

Elemente, die den Weg durch das Programm zeigen oder umschalten: Menüs, Leisten, Reiter, Seitenleisten und Pfadangaben.

## Elemente

- [**bottom-navigation**](./bottom-navigation/) – Die Bottom Navigation ist eine Navigation am unteren Bildschirmrand, typisch für Mobile-first-Design.
- [**breadcrumb**](./breadcrumb/) – Ein Breadcrumb ist eine Pfadnavigation (Start > Wiki > Seite).
- [**command**](./command/) – Die Befehlspalette ist ein Overlay mit einem Eingabefeld und einer Trefferliste.
- [**language-switcher**](./language-switcher/) – Ein Sprachumschalter ist ein Bedienelement zum Wechseln der Sprache der Anwendung.
- [**menu**](./menu/) – Ein Menü ist eine geordnete Liste von Menüeinträgen, die Aktionen auslösen oder Ansichten wechseln.
- [**pagination**](./pagination/) – Pagination teilt eine lange Liste in Abschnitte auf und bietet den Wechsel zwischen ihnen an.
- [**radial-menu**](./radial-menu/) – Ein Radial Menu (Kreismenü) ordnet Menüpunkte um einen Mittelpunkt herum an.
- [**sidebar**](./sidebar/) – Die Sidebar ist eine vertikale Navigationsspalte, meist am linken oder rechten Rand der Anwendung.
- [**tabs**](./tabs/) – Tabs (Reiter) dienen dazu, zwischen Ansichten zu wechseln.
- [**toolbar**](./toolbar/) – Eine Toolbar ist eine Reihe von Schaltflächen/Icons für häufige Aktionen.

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

- [Komponenten-Übersicht](../../index.md)
- [Band widgets](../)
- [Basiskomponente](../../primitives/basics/base.md)

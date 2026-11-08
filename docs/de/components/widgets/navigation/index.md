# navigation

Band [widgets](../) – kennt seinen Inhalt, wenn es gebaut wird.

Elemente, die den Weg durch das Programm zeigen oder umschalten: Menüs, Leisten, Reiter, Seitenleisten und Pfadanzeigen.

## Elemente

- [**bottom-navigation**](./bottom-navigation/) – Die untere Navigation liegt am unteren Bildschirmrand und ist typisch für Mobile-first-Design.
- [**breadcrumb**](./breadcrumb/) – Ein Breadcrumb ist eine Pfadnavigation (Start > Wiki > Seite).
- [**command**](./command/) – Die Befehlspalette ist ein Overlay mit einem Eingabefeld und einer Trefferliste.
- [**language-switcher**](./language-switcher/) – Ein Sprachumschalter ist ein Bedienelement zum Ändern der Anwendungssprache.
- [**menu**](./menu/) – Ein Menü ist eine geordnete Liste von Menüpunkten, die Aktionen auslösen oder Ansichten umschalten.
- [**pagination**](./pagination/) – Die Seitennummerierung teilt eine lange Liste in Abschnitte und bietet das Wechseln zwischen ihnen.
- [**radial-menu**](./radial-menu/) – Ein Kreismenü ordnet Menüpunkte um einen Mittelpunkt an.
- [**sidebar**](./sidebar/) – Die Seitenleiste ist eine vertikale Navigationsspalte, meist am linken oder rechten Rand der Anwendung.
- [**tabs**](./tabs/) – Reiter sind Tabs zum Wechseln zwischen Ansichten.
- [**toolbar**](./toolbar/) – Eine Werkzeugleiste ist eine Reihe von Buttons/Icons für häufige Aktionen.

## Profile

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

- [Komponentenübersicht](../../index.md)
- [Band Widgets](../)
- [Basiskomponente](../../primitives/basics/base.md)

# basics (Grundlagen)

Band [primitives](../) – nicht weiter zerlegbar.

Grundlagen, von denen alle anderen Komponenten ausgehen: die Basisklasse mit ihren geerbten Attributen, Zuständen und Tokens sowie die kleinsten Bausteine.

## Elemente

- [**kbd**](./kbd/) – Kbd zeigt eine einzelne Taste oder eine Tastenkombination optisch an – so, wie sie auf einer Tastenkappe steht.
- [**label**](./label/) – Ein Label ist die Beschriftung eines Steuerelements oder Feldes.
- [**link**](./link/) – Ein Link ändert die Adresse – er führt zu einer anderen Seite, einem anderen Objekt oder einer Stelle innerhalb der aktuellen Ansicht.
- [**separator**](./separator/) – Ein Separator trennt Inhalte voneinander: waagerecht zwischen Blöcken, senkrecht zwischen Spalten oder Werkzeuggruppen.

## Steckbriefe

| Komponente | Erbt von | Varianten | Rolle | Status |
|------------|----------|-----------|-------|--------|
| [kbd](./kbd/) | `base` | `einzeln`, `kombination` | - | dokumentiert |
| [label](./label/) | `base` | `ueber-feld`, `inline`, `versteckt`, `pflicht` | - | dokumentiert |
| [link](./link/) | `base` | `standard`, `muted`, `icon`, `unterstrichen` | - | dokumentiert |
| [separator](./separator/) | `base` | `horizontal`, `vertical`, `mit-beschriftung`, `dekorativ`, `inset` | - | dokumentiert |

## Siehe auch

- [Komponenten-Übersicht](../../index.md)
- [Band primitives](../)

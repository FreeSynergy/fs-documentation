# actions

Band [primitives](../) – lässt sich nicht weiter aufteilen.

Aktionselemente lösen eine einzelne Aktion aus oder bündeln zusammengehörige Aktionen. Sie ändern Daten oder Zustände, aber nicht die Adresse.

## Elemente

- [**button**](./button/) – Ein Button löst eine einzelne Aktion aus.
- [**button-group**](./button-group/) – Eine Button-Gruppe fasst zusammengehörige Buttons zu einer optischen und logischen Einheit zusammen.
- [**floating-action-button**](./floating-action-button/) – Ein Floating Action Button (FAB) ist ein runder Hauptaktions-Button, meist unten rechts platziert.

## Profile

| Komponente | Erbt von | Varianten | Rolle | Status |
|------------|----------|-----------|-------|--------|
| [button](./button/) | `base` | `primary`, `secondary`, `outline`, `ghost`, `danger`, `link` | - | dokumentiert |
| [button-group](./button-group/) | `base` | `verbund`, `segment`, `split` | - | dokumentiert |
| [floating-action-button](./floating-action-button/) | `base` | `standard FAB`, `mini FAB`, `extended FAB` | - | dokumentiert |

## Siehe auch

- [Komponentenübersicht](../../index.md)
- [Band primitives](../)
- [Basiskomponente](../basics/base.md)

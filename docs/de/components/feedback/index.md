# feedback (Rückmeldung)

Elemente, die den Zustand einer Anwendung sichtbar machen: Meldungen, Fortschritt, Ladezustände und Kennzeichnungen.

## Elemente

- [**alert**](./alert/) – Ein Alert ist eine Status-Meldung (Info, Warning, Error, Success).
- [**badge**](./badge/) – Ein Badge ist ein kleines Anzeigeelement für Status, Zähler oder Kategorie.
- [**empty-state**](./empty-state/) – Ein leerer Zustand erklärt, warum eine Fläche ohne Inhalt ist, und zeigt den Weg zum ersten Inhalt.
- [**progress**](./progress/) – Eine Progress-Anzeige zeigt, wie weit eine begonnene Aktion fortgeschritten ist – oder dass sie läuft, ohne dass der Wert bekannt ist.
- [**skeleton**](./skeleton/) – Ein Skeleton ist ein Platzhalter in der späteren Layoutform.
- [**spinner**](./spinner/) – Ein Spinner zeigt an, dass das System arbeitet, ohne dass ein Fortschrittswert bekannt ist.
- [**toast**](./toast/) – Ein Toast ist eine Pop-up-Benachrichtigung, die meist oben rechts erscheint.

## Steckbriefe

| Komponente | Erbt von | Varianten | Rolle | Status |
|------------|----------|-----------|-------|--------|
| [alert](./alert/) | `base` | `inline`, `banner` | `alert` | dokumentiert |
| [badge](./badge/) | `base` | `status`, `counter`, `dot`, `outline` | - | dokumentiert |
| [empty-state](./empty-state/) | `base` | `leer`, `kein-treffer`, `fehler` | `status` | dokumentiert |
| [progress](./progress/) | `base` | `linear`, `circular`, `mit-label`, `unbestimmt` | - | dokumentiert |
| [skeleton](./skeleton/) | `base` | `text`, `rect`, `circle`, `card`, `list-item`, `table-row`, `avatar` | - | dokumentiert |
| [spinner](./spinner/) | `base` | `einfach`, `mit-text`, `inline` | - | dokumentiert |
| [toast](./toast/) | `base` | `Info`, `Success`, `Warning`, `Error` | - | dokumentiert |

## Siehe auch

- [Komponenten-Übersicht](../index.md)
- [Basiskomponente](../basics/base/)

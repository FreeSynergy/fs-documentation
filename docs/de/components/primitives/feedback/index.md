# feedback (Rückmeldung)

Band [primitives](../) – nicht weiter zerlegbar.

Elemente, die den Zustand einer Anwendung sichtbar machen: Meldungen, Fortschritt, Ladezustände und Kennzeichnungen.

## Elemente

- [**alert**](./alert/) – Ein Alert ist eine Statusmeldung (Info, Warnung, Fehler, Erfolg).
- [**badge**](./badge/) – Ein Badge ist ein kleines Anzeigeelement für Status, Zähler oder Kategorie.
- [**empty-state**](./empty-state/) – Ein Empty State erklärt, warum eine Fläche keinen Inhalt hat.
- [**encryption-state**](./encryption-state/) – Ein Verschlüsselungsstatus zeigt, wie eine Nachricht oder Unterhaltung geschützt ist (MLS, OpenPGP, Megolm, nur Transport, keine).
- [**message-status**](./message-status/) – Ein Nachrichtenstatus zeigt, wie weit eine gesendete Nachricht gekommen ist: wird gesendet, gesendet, zugestellt, gelesen oder fehlgeschlagen.
- [**progress**](./progress/) – Eine Fortschrittsanzeige zeigt, wie weit eine gestartete Aktion ist.
- [**skeleton**](./skeleton/) – Ein Skeleton ist ein Platzhalter in der späteren Form des Layouts.
- [**spinner**](./spinner/) – Ein Spinner zeigt, dass das System arbeitet, ohne dass ein Fortschrittswert bekannt ist.
- [**toast**](./toast/) – Ein Toast ist eine Benachrichtigung als Pop-up.

## Steckbriefe

| Komponente | Erbt von | Varianten | Rolle | Status |
|------------|----------|-----------|-------|--------|
| [alert](./alert/) | `base` | `inline`, `banner` | - | dokumentiert |
| [badge](./badge/) | `base` | `status`, `counter`, `dot`, `outline` | - | dokumentiert |
| [empty-state](./empty-state/) | `base` | `leer`, `kein-treffer`, `fehler` | `status` | dokumentiert |
| [encryption-state](./encryption-state/) | `base` | `icon`, `icon-text`, `warning` | - | Skizze |
| [message-status](./message-status/) | `base` | `icon`, `icon-text` | - | Skizze |
| [progress](./progress/) | `base` | `linear`, `circular`, `mit-label`, `unbestimmt` | - | dokumentiert |
| [skeleton](./skeleton/) | `base` | `text`, `rect`, `circle`, `card`, `list-item`, `table-row`, `avatar` | - | dokumentiert |
| [spinner](./spinner/) | `base` | `einfach`, `mit-text`, `inline` | - | dokumentiert |
| [toast](./toast/) | `base` | `info`, `success`, `warning`, `error` | - | dokumentiert |

## Siehe auch

- [Komponenten-Übersicht](../../index.md)
- [Band primitives](../)
- [Basiskomponente](../basics/base.md)

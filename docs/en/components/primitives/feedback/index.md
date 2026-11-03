# feedback

Band [primitives](../) – cannot be broken down further.

Elements that make the state of an application visible: messages, progress,
loading states and markings.

## Elements

- [**alert**](./alert/) – an alert is a status message (info, warning, error, success).
- [**badge**](./badge/) – a badge is a small display element for status, counts or category.
- [**empty-state**](./empty-state/) – an empty state explains why a surface has no content and shows the way to the first content.
- [**progress**](./progress/) – a progress indicator shows how far a started action has come – or that it is running without the value being known.
- [**skeleton**](./skeleton/) – a skeleton is a placeholder in the later layout shape.
- [**spinner**](./spinner/) – a spinner indicates that the system is working without a progress value being known.
- [**toast**](./toast/) – a toast is a pop-up notification that usually appears top right.

## Profiles

| Component | Inherits from | Variants | Role | Status |
|-----------|---------------|----------|------|--------|
| [alert](./alert/) | `base` | `inline`, `banner` | `alert` | documented |
| [badge](./badge/) | `base` | `status`, `counter`, `dot`, `outline` | - | documented |
| [empty-state](./empty-state/) | `base` | `leer`, `kein-treffer`, `fehler` | `status` | documented |
| [progress](./progress/) | `base` | `linear`, `circular`, `mit-label`, `unbestimmt` | - | documented |
| [skeleton](./skeleton/) | `base` | `text`, `rect`, `circle`, `card`, `list-item`, `table-row`, `avatar` | - | documented |
| [spinner](./spinner/) | `base` | `einfach`, `mit-text`, `inline` | - | documented |
| [toast](./toast/) | `base` | `info`, `success`, `warning`, `error` | - | documented |

## See also

- [Component overview](../../index.md)
- [Band primitives](../)
- [Base component](../basics/base.md)

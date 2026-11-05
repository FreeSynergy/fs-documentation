# feedback

Band [primitives](../) – cannot be broken down further.

Elements that make the state of an application visible: messages, progress, loading states and markers.

## Elements

- [**alert**](./alert/) – An alert is a status message (info, warning, error, success).
- [**badge**](./badge/) – A badge is a small display element for status, counts or category.
- [**empty-state**](./empty-state/) – An empty state explains why a surface has no content and shows the way to the first content.
- [**encryption-state**](./encryption-state/) – An encryption state shows how a message or conversation is protected (MLS, OpenPGP, Megolm, transport only, none).
- [**message-status**](./message-status/) – A message status shows how far a sent message has come: being sent, sent, delivered, read or failed.
- [**progress**](./progress/) – A progress indicator shows how far a started action has come – or that it is running, without the value being known.
- [**skeleton**](./skeleton/) – A skeleton is a placeholder in the later layout shape.
- [**spinner**](./spinner/) – A spinner indicates that the system is working, without a progress value being known.
- [**toast**](./toast/) – A toast is a pop-up notification that usually appears top right.

## Profiles

| Component | Inherits from | Variants | Role | Status |
|------------|----------|-----------|-------|--------|
| [alert](./alert/) | `base` | `inline`, `banner` | `alert` | documented |
| [badge](./badge/) | `base` | `status`, `counter`, `dot`, `outline` | - | documented |
| [empty-state](./empty-state/) | `base` | `leer`, `kein-treffer`, `fehler` | `status` | documented |
| [encryption-state](./encryption-state/) | `base` | `icon`, `icon-text`, `warning` | - | skeleton |
| [message-status](./message-status/) | `base` | `icon`, `icon-text` | - | skeleton |
| [progress](./progress/) | `base` | `linear`, `circular`, `mit-label`, `unbestimmt` | - | documented |
| [skeleton](./skeleton/) | `base` | `text`, `rect`, `circle`, `card`, `list-item`, `table-row`, `avatar` | - | documented |
| [spinner](./spinner/) | `base` | `einfach`, `mit-text`, `inline` | - | documented |
| [toast](./toast/) | `base` | `info`, `success`, `warning`, `error` | - | documented |

## See also

- [Component overview](../../index.md)
- [Band primitives](../)
- [Base component](../basics/base.md)

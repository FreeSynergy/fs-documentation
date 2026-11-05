# FreeSynergy Simple 0.1 — Dependencies (our components)

| Region / feature | Component | Level |
|------------------|-----------|-------|
| full-screen message | `mail-view` / `message-bubble` (NEW) | widget |
| encryption state | `encryption-state` (NEW) | primitive |
| top bar icons | `button` (icon) | primitive |
| list screen | `list-view` (needs swipe/selection changes) | widget |
| composer | `composer` with the simple text editor (ADR 0039) | workbench |
| recipient picker | `search-field` + `list-view` | primitive + widget |
| new contact form | `field`, `text-input`, `form` (cn backlog bf7c901) | primitive / widget |
| undo after delete/cancel | `toast` | primitive |
| gestures | swipe, double tap, long press (`interactions/gestures/`) | — |

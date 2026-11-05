# FreeSynergy Simple 0.1 — Interaction

Gestures belong to the frontend, not to the program or the composer (ADR 0037).

## Reading screen
| Gesture | Action | Capability |
|---------|--------|------------|
| swipe left | next unread message | `conversation.open` / `message.open` |
| swipe right | previous unread message ⚠️ direction proposed | `message.open` |
| swipe up | forward | `message.forward` |
| swipe down | delete (toast with undo) | `message.delete` |
| double tap | reply | `message.reply` |

## Compose screen
| Gesture | Action | Capability |
|---------|--------|------------|
| swipe up | send | `message.send` |
| swipe down | cancel (toast with undo; draft kept until the undo time ends) | — |
| swipe left | save as draft and close ⚠️ proposed | `draft.save` |
| swipe right | attach (photo, file) ⚠️ proposed | `attachment.add` |
| tap 👤+ | add recipients → recipient picker | — |

## Accessibility (every gesture has an equivalent)
- **Visible hints** on first use (arrows at the edges), fading out.
- **Long press** → menu with the same actions as the gestures.
- **Keyboard:** ← → next/previous unread, ↑ forward, Del delete, Enter reply; in compose Ctrl+Enter send, Esc cancel.
- **Screen readers:** the actions are exposed as named actions on the message (needs accessibility support in Blinc — `todo/upstream.md`).
- Gestures are recognised for finger, mouse (drag) and pen alike (ADR 0015).

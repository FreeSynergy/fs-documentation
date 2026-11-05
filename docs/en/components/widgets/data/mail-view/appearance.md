# Mail View - Appearance

## Base layout

```
┌─────────────────────────────────────────┐
│ From     anna@example.org   🔒 ✔ signed │
│ To       team@example.org               │
│ Subject  Meeting notes                  │
│ Date     05 Nov 2026, 10:42             │
├─────────────────────────────────────────┤
│ body (text or sanitised HTML)           │
├─────────────────────────────────────────┤
│ 📎 notes.pdf   📎 plan.png              │
└─────────────────────────────────────────┘
```

## Variants

| Variant | Appearance |
|---|---|
| **full** | header block, divider, body, attachment row |
| **compact** | two lines: sender + subject, excerpt |
| **source** | monospace original text ⚠️ |

## Sizes

| Size | Height | Use |
|---|---|---|
| `small` | 200 px | list preview |
| `medium` | 400 px | standard |
| `full` | 100% | reading pane |

## Colours and states

| State | Appearance |
|---|---|
| Default | theme surface |
| Unencrypted | error-toned marker via [encryption-state](../../../primitives/feedback/encryption-state/) |
| Signature invalid | error marker in the header |
| Remote content blocked | info bar above the body |

## Hover and focus effects

| Effect | Description |
|---|---|
| `background` | header rows highlight for address actions |
| `tooltip` | full address and signature details |

## Responsive

- The header collapses to sender and subject; the rest expands on tap.
- Attachments wrap below the body.

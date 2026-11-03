# Alert - Appearance

## Base layout
An alert is a status message (info, warning, error, success).

```
┌─────────────────────────────────────────┐
│ [✕]                                     │
│ 📢 Title                                │
│ Description text...                     │
│                                         │
│ [Action]                                │
└─────────────────────────────────────────┘
```

## Variants

| Variant | Appearance |
|---------|------------|
| **inline** | borderless surface inside the content, an icon on the left |
| **banner** | full width above the view, offset background, fixed |

## Sizes

| Size | Width | Use |
|------|-------|-----|
| small | 200px | inline |
| medium | 400px | standard |
| large | 600px | featured |
| full | 100% | full width |

## Colours and states

| Status | Colour | Description |
|--------|--------|-------------|
| **info** | blue | information message |
| **success** | green | success message |
| **warning** | orange | warning message |
| **error** | red | error message |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `shadow` | shadow becomes stronger |
| `border-left` | the line lights up |

## Responsive

An inline message flows along with the content; the banner variant stays at the top
(`sticky`) while the content moves on. When closing, the message shrinks to its
line height (`fade-out`, `collapse`) so the rest of the content moves up. At narrow
widths the actions stack below each other.

```css
.alert--banner { position: sticky; top: 0; z-index: 20; }
.alert-message { overflow-wrap: anywhere; }
.alert--dismissing { opacity: 0; max-height: 0; }   /* fade-out + collapse */

@media (max-width: 600px) {
  .alert-actions { flex-direction: column; }        /* actions stacked */
}
```

## Types

| Type | Colour | Description |
|------|--------|-------------|
| `info` | blue | information message |
| `success` | green | success message |
| `warning` | orange/yellow | warning message |
| `error` | red | error message |

## Dismissible

```
┌─────────────────────────────────────────┐
│ [✕]                                     │
│ 📢 Title                                │
│ Description text...                     │
└─────────────────────────────────────────┘
```

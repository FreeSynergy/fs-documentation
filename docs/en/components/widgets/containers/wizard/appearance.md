# Wizard - Appearance

## Base layout
A wizard is a step-by-step form for complex tasks.

```
┌─────────────────────────────────────────┐
│ Step 1 of 5                             │
├─────────────────────────────────────────┤
│                                         │
│   Content of the step                   │
│                                         │
├─────────────────────────────────────────┤
│ [Back]                 [Next →]         │
└─────────────────────────────────────────┘
```

## Variants

| Variant | Description |
|---------|-------------|
| **Horizontal** | horizontal step indicator |
| **Vertical** | vertical step indicator |
| **Stepper** | with a visual progress display |
| **schrittanzeige** | only showing the steps, without guidance |

## Sizes

| Size | Width | Use |
|------|-------|-----|
| small | 300px | small wizards |
| medium | 500px | standard |
| large | 700px | large wizards |
| full | 100% | full width |

## Colours and states

| Status | Colour | Description |
|--------|--------|-------------|
| **Active step** | primary colour | current step |
| **Completed step** | green | finished step |
| **Pending step** | grey | outstanding step |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `color` | the colour changes |
| `border-bottom` | an underline appears |

## Responsive

Changing steps is a sliding transition: forwards from the right (`slide-in`), backwards
mirrored; the step indicator follows with `progress`. On a narrow surface the vertical
indicator becomes a row of counter and bar, the content stays in one column.

```css
.wizard-step        { transition: transform 200ms, opacity 200ms; }
.wizard-step--in-next { transform: translateX(24px); opacity: 0; }
.wizard-step--in-prev { transform: translateX(-24px); opacity: 0; }

@media (max-width: 600px) {
  .wizard--vertical .step-indicator { flex-direction: row; }  /* counter + bar */
}
```

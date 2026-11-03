# Wizard

| Field | Value |
|-------|-------|
| **Category** | `containers` |
| **Inherits from** | `base` |
| **Variants** | `Horizontal`, `Vertical`, `Stepper`, `schrittanzeige` |
| **States** | `completed` |
| **Gestures** | `tap`, `swipe` |
| **Animations** | `slide-in`, `progress`, `highlight` |
| **Related** | `modal`, `tabs`, `progress`, `field` |
| **Status** | documented |

!!! info "Standardisation"
    The former component `stepper` became a variant of `wizard`: `assistent` (with
    guidance) and `schrittanzeige` (only showing the steps).

## Description
A wizard is a step-by-step form for complex tasks.

## Purpose

- Step-by-step instructions
- Complex forms
- Setup assistants
- Onboarding

## Variants

| Variant | Description |
|---------|-------------|
| **Horizontal** | horizontal step indicator |
| **Vertical** | vertical step indicator |
| **Stepper** | with a visual progress display |
| **schrittanzeige** | only showing the steps, without guidance |

## Features

- Step indicator (progress display)
- Back/next navigation
- Validation (per step)
- Save draft (intermediate saving)

## Distinction

- **Do not confuse with** [modal](../../overlays/modal/): a wizard *can* run inside a
  modal, but it is defined by its ordered sequence of steps and the check per step,
  the modal by the overlay itself.
- **Do not confuse with** [tabs](../../navigation/tabs/): tabs are freely switchable, the
  wizard guides through a sequence and validates before moving on.
- **Do not confuse with** [progress](../../../primitives/feedback/progress/): the progress bar
  component only shows a share; the step indicator shows position, what is done and
  what is outstanding per step.
- The variant `schrittanzeige` (formerly `stepper`) does not guide — it only displays steps.

## Best Practices

- Clarity
- Feedback
- Progress
- Flexibility

## Structure

```
┌─────────────────────────────────────────┐
│ Step 1 of 5                             │  ← step indicator
├─────────────────────────────────────────┤
│                                         │
│   Content of the step                   │
│                                         │  ← body
├─────────────────────────────────────────┤
│ [Back]                 [Next →]         │  ← footer
└─────────────────────────────────────────┘
```

## See also

- [containers – overview](../index.md)
- [Base component](../../../primitives/basics/base.md)

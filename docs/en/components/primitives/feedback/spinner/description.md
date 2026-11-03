# Spinner

| Field | Value |
|-------|-------|
| **Category** | `feedback` |
| **Inherits from** | `base` |
| **Variants** | `einfach`, `mit-text`, `inline` |
| **States** | `loading` is the only state |
| **Gestures** | none – not operable |
| **Animations** | `spin`, `pulse` |
| **Related** | `button`, `progress`, `skeleton`, `base` |
| **Status** | documented |

## Description

A spinner indicates that the system is working, without a progress value being
known. It is the smallest form of feedback.

## Purpose

- Waiting for a response (saving, loading, checking)
- Loading state in [button](../../actions/button/) and fields
- Activity indicator in bars and cards

## Variants

| Variant | Description |
|---------|-------------|
| **einfach** | only the rotating graphic |
| **mit-text** | spinner plus accompanying text ("Loading…") |
| **inline** | small enough to sit in a line of text or in a field |

## Features

- Background ring (`track`) for better perceptibility
- Rotation speed adjustable
- In buttons it replaces the label without changing the width much

## Distinction

- **Do not confuse with** [progress](../progress/): progress shows an amount,
  a spinner only activity.

- **Do not confuse with** [skeleton](../skeleton/): a skeleton fills a
  placeholder, a spinner marks a process.

- **Do not confuse with** the loading state of [button](../../actions/button/):
  that one uses a spinner internally.

## Best Practices

- Never leave a spinner for more than a few seconds without additional info –
  otherwise show [progress](../progress/) or a message.

- The waiting area gets `aria-busy`; the spinner itself needs no text.
- At most one spinner per screen area.

## See also

- [Progress](../progress/)
- [Skeleton](../skeleton/)
- [Button](../../actions/button/)
- [Base component](../../basics/base.md)

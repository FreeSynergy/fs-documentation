# OTP Input (one-time password)

| Field | Value |
|-------|-------|
| **Category** | `fields` |
| **Inherits from** | `base`, `text-input` |
| **Variants** | `einzelboxen`, `block` |
| **States** | `error`, `loading`, `filled` |
| **Gestures** | `tap`, `type` |
| **Animations** | `shake` |
| **Related** | `text-input`, `button`, `alert` |
| **Role** | `group` |
| **Status** | documented |

## Description

The one-time-password field takes a short numeric code – one field per
character. It supports pasting from the clipboard and autofill from the
operating system.

## Purpose

- Sign-in with a second factor
- Confirming a dangerous action
- Verifying an email address or phone number

## Variants

| Variant | Description |
|---------|-------------|
| **einzelboxen** | one box per character, standard |
| **block** | one field with character spacing, for narrow surfaces |

## Features

- Completes automatically when the code is pasted
- Autofill from the operating system (`autocomplete = one-time-code`)
- It checks after the last character, not after every one
- Error: clear the fields and shake briefly, enter the code again

## Distinction

- **Do not confuse with** [text-input](../text-input/) with `password`: a password
  is long-term and freely chosen, the code is short and machine-generated.
- **Do not confuse with** [tags-input](../tags-input/): there several values are
  created, here each character forms part of one value.

## Best Practices

- Take the length from the provider (usually 6), do not guess it.
- Only request a new code after the deadline expires, with a countdown.
- Do not mask any characters – the code is short and gets checked.

## See also

- [Text Input](../text-input/)
- [Base component](../../basics/base.md)

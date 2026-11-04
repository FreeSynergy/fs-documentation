# Language Switcher

| Field | Value |
|-------|-------|
| **Category** | `navigation` |
| **Inherits from** | `base` |
| **Variants** | `dropdown`, `knopetreihe`, `flaggen`, `kombiniert` |
| **States** | `aktiv` |
| **Gestures** | `tap` |
| **Animations** | `expand`, `fade-in` |
| **Related** | `select`, `menu`, `toolbar`, `bottom-navigation` |
| **State** | documented |

## Description
A language switcher is a UI element for changing the application language.

## Purpose

- Changing language settings
- Multilingualism
- Regional adaptation

## Variants

| Variant | Description |
|---------|-------------|
| **dropdown** | current language plus a drop-down list |
| **knopetreihe** | each language as its own button (up to three languages) |
| **flaggen** | only symbols, with a tooltip |
| **kombiniert** | row of buttons with a `…` drop-down for further languages |

## Features

- Automatic detection
- Persistent setting
- Live switching
- No reload needed

## Distinction

- **Do not confuse with** [select](../../../primitives/fields/select/): a field value stays in the
  form, the language applies to the whole application and is remembered permanently.
- **Do not confuse with** [menu](../menu/): a menu invokes actions, this switch only changes one
  setting.
- Flags do not stand for languages: English is spoken in many countries.

## Best Practices

- Write language names in the language itself ("Deutsch", "English", "Français").
- Show language codes (`de`, `en`) instead of flags when it is about language and not region.
- Take the default language from the system, remember the selection in the profile and on the device.
- Switch without reloading; mark headings missing in the secondary language.
- Account for right-to-left languages (mirrored layout), do not only translate.

## Size variants

| Size | Use |
|------|-----|
| Small | in the header bar |
| Medium | in the settings |
| Large | on the start page |

## Colour variants

| State | Colour | Description |
|-------|--------|-------------|
| **Default** | normal | standard style |
| **Active** | primary colour | active language |

## Languages

| Language | Code | Flag |
|----------|------|------|
| Deutsch | de | 🇩🇪 |
| English | en | 🇬🇧 |
| Français | fr | 🇫🇷 |
| **Español** | es | 🇪🇸 |
| Italiano | it | 🇮🇹 |

## See also

- [navigation – overview](../index.md)
- [Select](../../../primitives/fields/select/) — a value in a form
- [Toolbar](../toolbar/) — the usual place for the switch
- [Base component](../../../primitives/basics/base.md)

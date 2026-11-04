# Code Editor

| Field | Value |
| ------ | ------ |
| **Category** | `special` |
| **Inherits from** | `base` |
| **Variants** | `voll`, `nur-lesen`, `vergleich` |
| **States** | `ungespeichert`, `fehler` |
| **Gestures** | `tap`, `double-tap`, `long-press`, `drag` |
| **Animations** | `highlight`, `fade-in` |
| **Related** | `rich-text-editor`, `textarea`, `whiteboard`, `dashboard` |
| **State** | documented |

## Description
A code editor is an editor for source code.

## Purpose

- Code
- Programming
- Scripts

## Variants

| Variant | Description |
| ---------- | -------------- |
| **voll** | editing with highlighting, completion and error marking |
| **nur-lesen** | highlighted code for viewing and copying |
| **vergleich** | two versions side by side, differences marked |

## Features

- Syntax Highlighting
- Line Numbers
- Auto-completion
- Error Detection

## Distinction

- **Do not confuse with** [rich-text-editor](../../fields/rich-text-editor/): there formatted
  text is created, here source code. Wiki syntax is a variant of the text editor, not of this one.
- **Do not confuse with** [textarea](../../../primitives/fields/textarea/): without line numbers,
  highlighting and bracket closing it is simply a text field.
- Output of programs is not an editor task — it belongs in a result view.

## Best Practices

- Always state the language explicitly, otherwise the highlighting is missing and the indentation is wrong.
- `Tab` indents; offer `Esc` or `Ctrl+Tab` to leave the editor.
- Line numbers and a horizontal ruler only from multi-line content onwards.
- Mark unsaved changes clearly, ask before closing.
- Document shortcuts in the usual place (`Ctrl+/`, `Ctrl+F`, `Ctrl+D`).

## See also

- [special – overview](../index.md)
- [Rich Text Editor](../../fields/rich-text-editor/) — formatted text
- [Whiteboard](../whiteboard/) — sketches instead of code
- [Base component](../../../primitives/basics/base.md)

# Rich Text Editor

| Field | Value |
|-------|-------|
| **Category** | `fields` |
| **Inherits from** | `base`, `textarea` |
| **Variants** | `wysiwyg`, `wiki-syntax` |
| **States** | `unspeichert`, `error` |
| **Gestures** | `tap`, `double-tap`, `long-press`, `drag` |
| **Animations** | `fade-in`, `highlight` |
| **Related** | `textarea`, `code-editor`, `whiteboard`, `emoji-picker` |
| **Status** | documented |

!!! info "Standardisation"
    The former component `wiki-editor` became a variant of `rich-text-editor`:
    `wysiwyg` and `wiki-syntax`.

## Description
A rich text editor is an editor for formatted text.

## Purpose

- Documents
- Articles
- Messages

## Variants

| Variant | Description |
|---------|-------------|
| **wysiwyg** | formatting as in the printed layout (standard) |
| **wiki-syntax** | editor with wiki syntax (Markdown) and preview |

## Features

- Bold/Italic/Underline
- Headings
- Lists
- Links
- Images

## Distinction

- **Do not confuse with** [textarea](../../../primitives/fields/textarea/): the multi-line field stores
  plain text, this editor stores formatting as structure.
- **Do not confuse with** [code-editor](../../special/code-editor/): there source code with syntax
  highlighting is in the foreground, here the printed layout.
- **Do not confuse with** [whiteboard](../../special/whiteboard/): a free drawing surface instead of
  text flow.

## Best Practices

- Only show tools the content really knows (no `Tabelle` in a comment field).
- Offer shortcuts in parallel (`Ctrl+B`, `Ctrl+I`, `Ctrl+K` for links).
- Paste foreign text cleaned up (take the formatting from other applications, not everything).
- Save the intermediate state automatically and make the save point visible (`unspeichert`).
- `wiki-syntax` always with a preview switch, so the syntax stays readable.

## See also

- [fields – overview](../index.md)
- [Textarea](../../../primitives/fields/textarea/) — editing plain text
- [Code Editor](../../special/code-editor/) — source code
- [Base component](../../../primitives/basics/base.md)

# Message Composer

| Field | Value |
|-------|-------|
| **Category** | `special` |
| **Inherits from** | `base` |
| **Variants** | `chat`, `mail`, `reply` |
| **States** | `empty`, `draft`, `sending`, `error` |
| **Gestures** | none – gestures are added by the frontend, not by the component (ADR 0037) |
| **Animations** | `fade-in` |
| **Related** | `code-editor`, `tags-input`, `mention-input`, `emoji-picker`, `file-upload`, `embed` |
| **Status** | skeleton |

## Description

The message composer is the workbench for writing a message: recipients, subject, a simple text editor, attachments, emoji and mentions.

## Purpose

- Write chat messages and mails
- Reply field in embedded views (ADR 0037)
- Drafts that survive restarts

## Variants

| Variant | Description |
|---|---|
| **chat** | single field with send button |
| **mail** | recipients, subject, editor, attachments |
| **reply** | only a reply field (compact) |

## Features

- Recipients via [tags-input](../../../primitives/fields/tags-input/) variant `recipients` (contact suggestion, key state per chip)
- Subject (mail)
- Simple text editor = [code-editor](../code-editor/) (Markdown), ADR 0039
- Attachments via [file-upload](../../../widgets/fields/file-upload/)
- [emoji-picker](../../../widgets/fields/emoji-picker/) and [mention-input](../../../primitives/fields/mention-input/)
- Encryption hint before sending

## Data binding

Binds a message draft: ActivityStreams `Note` (draft) plus recipients and `$draft` keyword. Output: `text/plain`, `text/markdown` and (mail) `text/html`. Band decided 2026-11-05: **workbench**, because it contains the editor, itself a workbench; the children are chosen at run time.

## Distinction

- **Do not confuse with** [code-editor](../code-editor/): the editor is one part of the composer.
- **Do not confuse with** [rich-text-editor](../../fields/rich-text-editor/): the composer uses the simple editor (ADR 0039); the extended one can replace it for mail ⚠️.
- **Do not confuse with** an app: the app adds menu, gestures and settings around the composer (ADR 0037).

## Best Practices

- Keep drafts automatically.
- Show the encryption state before sending; explain if no encrypted path exists.
- Do not hide attachments from the screen reader.

## Blinc note

Built in our layer on Blinc parts (`textarea`, `button`, `rich_text_editor`, `selection_toolbar`). IME and pre-edit input for CJK and mobile: Blinc backlog **e864f0c** (mandatory for a messenger). Combobox hover for recipient suggestions: **8115bf5**.

## Open points

- ⚠️ Composer decomposition for the plain chat case (textarea + button) versus this workbench
- ⚠️ Undo send / schedule send placement

## See also

- [special – overview](../index.md)
- [Code Editor](../code-editor/)
- [Rich Text Editor](../../fields/rich-text-editor/)
- [Embed](../embed/)
- [Messenger requirements](../../../../programs/apps/messenger/requirements.md)
- [Base component](../../../primitives/basics/base.md)

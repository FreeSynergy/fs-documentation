# Block Editor

| Field | Value |
|-------|-------|
| **Category** | `fields` |
| **Inherits from** | `base` |
| **Variants** | `edit`, `read`, `template` |
| **States** | `unsaved`, `readonly`, `error` |
| **Gestures** | none – gestures are added by the frontend, not by the component (ADR 0037) |
| **Animations** | `reorder`, `fade-in` |
| **Related** | `code-editor`, `rich-text-editor`, `dashboard`, `repeater` |
| **Status** | skeleton |

## Description

The block editor edits structured documents as a tree of blocks (like Notion). Each block has a data type. It is the third of the three text editors (ADR 0039).

## Purpose

- Structured documents and wiki pages
- Documents made of text plus layers (ADR 0042)
- Templates with fixed parts and placeholders

## Variants

| Variant | Description |
|---|---|
| **edit** | edit blocks |
| **read** | read-only |
| **template** | fixed parts with placeholders |

## Features

- Block tree with insert, move, convert
- Each block binds a data type from the representation register (ADR 0023)
- Layers (formatting, names, links, variables, own explanations) over the text as marks (ADR 0033), stored only in the database
- Link table: moving rewrites links
- Persistent, limited undo (ADR 0042)

## Data binding

Binds a block document (own block specification, ADR 0034). A `.md` or code file is a block document with **one** block pointing to the text; code mode and block mode are two views of one model (ADR 0042). `fs-store` is the truth, files are exports.

## Distinction

- **Do not confuse with** [code-editor](../../special/code-editor/): the simple editor for Markdown and code files.
- **Do not confuse with** [rich-text-editor](../rich-text-editor/): extended WYSIWYG editor for office-style documents (ODF).
- **Do not confuse with** [dashboard](../../special/dashboard/): a dashboard arranges widgets.

## Best Practices

- Use block mode when a document is structured; plain files stay in the code editor.
- Show where layers (marks) exist.
- Remind on saving that the undo history can be reset (ADR 0042).

## Blinc note

Not in Blinc; built in our layer on `rich_text_editor` parts ⚠️. Backlog id: none ⚠️.

## Open points

- ⚠️ Block specification (ADR 0034) status
- ⚠️ Relation to rich-text-editor (same model or separate)

## See also

- [fields – overview](../index.md)
- [Code Editor](../../special/code-editor/)
- [Rich Text Editor](../rich-text-editor/)
- [Base component](../../../primitives/basics/base.md)

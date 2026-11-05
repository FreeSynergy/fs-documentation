# special

Band [workbenches](../) – receives its content only at runtime.

Composite elements with a data structure of their own: editors, embeds, maps and views that generic libraries do not offer.

## Elements

- [**code-editor**](./code-editor/) – A code editor is an editor for source code.
- [**dashboard**](./dashboard/) – A dashboard is an overview page with widgets.
- [**embed**](./embed/) – An **embed** includes foreign content in a FreeSynergy surface: another FreeSynergy program, a widget or an external page.
- [**html-view**](./html-view/) – An HTML view shows foreign HTML (for example a mail body) in cleaned form and without loading anything remote.
- [**message-composer**](./message-composer/) – The message composer is the workbench for writing a message: recipients, subject, a simple text editor, attachments, emoji and mentions.
- [**whiteboard**](./whiteboard/) – A whiteboard is a drawing surface for collaboration.

## Profiles

| Component | Inherits from | Variants | Role | Status |
|------------|----------|-----------|-------|--------|
| [code-editor](./code-editor/) | `base` | `voll`, `nur-lesen`, `vergleich` | - | documented |
| [dashboard](./dashboard/) | `base` | `vorlage`, `anordbar`, `bericht` | - | documented |
| [embed](./embed/) | `base` | `app`, `widget`, `iframe` | - | documented |
| [html-view](./html-view/) | `base` | `sanitised`, `remote-allowed` | - | skeleton |
| [message-composer](./message-composer/) | `base` | `chat`, `mail`, `reply` | - | skeleton |
| [whiteboard](./whiteboard/) | `base` | `zeichnung`, `formen`, `notizen`, `vorlage` | - | documented |

## See also

- [Component overview](../../index.md)
- [Band workbenches](../)
- [Base component](../../primitives/basics/base.md)

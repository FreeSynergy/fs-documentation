# special (Special elements)

Band [workbenches](../) – receives its content only at runtime.

Composite elements with their own data structure: editors, embeddings, cards and views
that generic libraries do not offer.

## Elements

- [**code-editor**](./code-editor/) – A code editor is an editor for source code.
- [**dashboard**](./dashboard/) – A dashboard is an overview page with widgets.
- [**embed**](./embed/) – An **embed** includes foreign content in a FreeSynergy surface: another FreeSynergy program, a widget or an external page.
- [**whiteboard**](./whiteboard/) – A whiteboard is a drawing surface for collaboration.

## Profiles

| Component | Inherits from | Variants | Role | State |
|-----------|---------------|----------|------|-------|
| [code-editor](./code-editor/) | `base` | `voll`, `nur-lesen`, `vergleich` | - | documented |
| [dashboard](./dashboard/) | `base` | `vorlage`, `anordbar`, `bericht` | - | documented |
| [embed](./embed/) | `base` | `app`, `widget`, `iframe` | - | documented |
| [whiteboard](./whiteboard/) | `base` | `zeichnung`, `formen`, `notizen`, `vorlage` | - | documented |

## See also

- [Component overview](../../index.md)
- [Band workbenches](../)
- [Base component](../../primitives/basics/base.md)

# fields (Fields)

Band [workbenches](../) – receives its content only at runtime.

Elements for entering and selecting values. The field (`field`) holds the label, help
text and error message together.

## Elements

- [**block-editor**](./block-editor/) – The block editor edits structured documents as a tree of blocks (like Notion).
- [**rich-text-editor**](./rich-text-editor/) – A rich text editor is an editor for formatted text.

## Profiles

| Component | Inherits from | Variants | Role | State |
|-----------|---------------|----------|------|-------|
| [block-editor](./block-editor/) | `base` | `edit`, `read`, `template` | - | skeleton |
| [rich-text-editor](./rich-text-editor/) | `base`, `textarea` | `wysiwyg`, `wiki-syntax` | - | documented |

## See also

- [Component overview](../../index.md)
- [Band workbenches](../)
- [Base component](../../primitives/basics/base.md)

# Loading

Loading animations bridge a waiting time and answer three different questions:
*What is happening right now?* (dots), *how much longer?* (progress) and *what
is coming?* (skeleton).

## Elements

- **progress** - measurable progress (bar, circle)
- **skeleton** - placeholder shapes in the layout of the later content
- **typing** - typing indicator (three dots in chats)
- **dots** - three dotted loading balls as a compact activity indicator

## Which one first?

| Case | Animation |
|------|-----------|
| layout of the content known | skeleton |
| progress measurable | progress |
| under 1 s of waiting | none – otherwise it flickers |
| short request, unknown extent | dots |
| answer from a chat partner | typing |

## See also

- [Animations overview](../index.md)
- [Loop](../loop/) - lasting signals without a loading reference
- [List view](../../../components/widgets/data/list-view/description.md) - skeleton in lists

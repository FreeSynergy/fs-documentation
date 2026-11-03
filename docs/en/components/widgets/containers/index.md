# containers

Band [widgets](../) – knows its contents when it is built.

Boxes and surfaces that hold other content: cards, panels, collapsible groups,
split views and assistants.

## Elements

- [**accordion**](./accordion/) – an accordion is a stack of headers that can collapse and expand content.
- [**card**](./card/) – the card is a container element that presents content in a structured box with a title, content and optional actions.
- [**panel**](./panel/) – a panel is a large container with a header, content and footer.
- [**scroll-area**](./scroll-area/) – a scroll area is a surface with a fixed measure whose content runs.
- [**split-view**](./split-view/) – a split view is a layout with two areas side by side.
- [**wizard**](./wizard/) – a wizard is a step-by-step form for complex tasks.

## Profiles

| Component | Inherits from | Variants | Role | Status |
|-----------|---------------|----------|------|--------|
| [accordion](./accordion/) | `base` | `standard`, `mehrere`, `einzel`, `deaktiviert` | - | documented |
| [card](./card/) | `base` | `standard`, `flach`, `umrandet`, `medien` | - | documented |
| [panel](./panel/) | `base` | `standard`, `einklappbar`, `verschiebbar`, `filter` | - | documented |
| [scroll-area](./scroll-area/) | `base` | `vertikal`, `horizontal`, `beides` | `group` | documented |
| [split-view](./split-view/) | `base` | `Fixed Split`, `Resizable Split`, `Responsive` | - | documented |
| [wizard](./wizard/) | `base` | `Horizontal`, `Vertical`, `Stepper`, `schrittanzeige` | - | documented |

## See also

- [Component overview](../../index.md)
- [Band widgets](../)
- [Base component](../../primitives/basics/base.md)

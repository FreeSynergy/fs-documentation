# Pull to Refresh

## Description

Pull to refresh is a combination of a **drag at the boundary** of a scrollable
area and a loading action: the user pulls the content down (or at the
respective start edge), a loading indicator appears, and releasing starts the
refresh.

Android reference: `SwipeRefreshLayout`, iOS: `UIRefreshControl`.

## Usage

- Refreshing feeds/lists (email, social, chat)
- Synchronizing data views
- A substitute for a refresh button on small screens

## Edges

| Edge | Description |
|------|-------------|
| Top (standard) | List at the start, pulling down |
| Bottom | "Load more" at the end of the list (pull for more) |
| Left/Right | Lateral refresh (calendar, chat history) |

## Duration

- Trigger distance: typically 60–100px
- Holding the indicator: until the response arrives
- Hiding the indicator after completion: 300ms

## Detection

| Method | Description |
|--------|-------------|
| **Scroll-Edge + Drag** | Drag only possible when the scroller is at the start edge |
| **Trigger-Distance** | From this distance: the indicator locks, armed state |
| **Over-Scroll Boundary** | The rubber-band area becomes the loading zone |

## States

| State | Description |
|-------|-------------|
| **Idle** | Normal list |
| **Pulling** | Indicator grows with the pull distance |
| **Armed** | Threshold reached, "release to refresh" |
| **Refreshing** | Indicator rotates, the list stays put |
| **Done** | Indicator disappears, content updated |

## Difference from Drag

- **Drag**: an element or content is moved and stays moved
- **Pull to Refresh**: movement at a fixed boundary, triggers a loading action

## Accessibility

Always offer an explicit refresh button; `prefers-reduced-motion` reduces the
rubber-band effect (WCAG 2.5.7 for the drag component).

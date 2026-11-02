# Edge Swipe (Edge Pan)

## Description

An edge swipe starts **at the screen edge**: the finger begins in a narrow zone
at the edge and swipes inwards. The start position is decisive – the same
movement in the middle of the screen is a normal swipe.

iOS knows `UIScreenEdgePanGestureRecognizer` for this, Android has the system
gesture "swipe back"; web browsers treat horizontal edge swipes as the
browser's back gesture.

## Usage

- Back navigation (standard on iOS and Android)
- Revealing a side panel / sidebar (desktop tablets, Surface)
- Pulling the control center / notifications out of the edge
- Opening radial menus at the edge (context)

## Edge Zones

| Edge | Typical function |
|------|------------------|
| Left | Back |
| Right | Back (in RTL) or side panel |
| Top | Notifications / status bar |
| Bottom | Home / app switching (full-screen navigation) |

## Duration

- Swipe duration: 100–400ms
- Start zone: 10–24px from the edge center

## Detection

| Method | Description |
|--------|-------------|
| **Edge Zone** | Touch start inside the edge zone |
| **Inward Vector** | The movement points away from the edge into the content |
| **Predictive Path** | The continuation of the swipe path predicts the target (Android) |

## Difference from Swipe

- **Swipe**: starts anywhere, the action belongs to the content
- **Edge Swipe**: starts at the edge, the action belongs to navigation/the app

## See also

- [Swipe](../swipe/description.md)
- [Navigation Sidebar](../../../../de/components/navigation/sidebar/description.md) (German)

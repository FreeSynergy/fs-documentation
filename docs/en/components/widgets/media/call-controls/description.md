# Call Controls

| Field | Value |
|-------|-------|
| **Category** | `media` |
| **Inherits from** | `base` |
| **Variants** | `bar`, `compact` |
| **States** | `idle`, `ringing`, `connected`, `muted`, `sharing` |
| **Gestures** | none – gestures are added by the frontend, not by the component (ADR 0037) |
| **Animations** | `pop-in` |
| **Related** | `button-group`, `media-player`, `grid-view`, `toolbar` |
| **Status** | skeleton |

## Description

Call controls are the control bar of a call: microphone, camera, screen sharing, hang up. They belong to the **separate calls program**, not to the messenger (ADR 0037).

## Purpose

- Control bar of the calls program
- Mini-bar in other programs during an ongoing call
- Reusable by streaming, SIP and normal phone calls

## Variants

| Variant | Description |
|---|---|
| **bar** | full control bar |
| **compact** | microphone and hang-up only |

## Features

- Toggle buttons with state
- Hang up as a distinct, confirming-free action
- Optional device selection
- Combines with [grid-view](../../data/grid-view/) for the tile grid

## Data binding

Binds a call session (MatrixRTC ⚠️ / no FreeSynergy standard yet). Register (ADR 0023): `CallSession → call-controls`. ADR 0037 point 6: calls are always their own program; what is visible of them are reusable components.

## Distinction

- **Do not confuse with** [media-player](../media-player/): the player controls playback; call controls control a live session.
- **Do not confuse with** [button-group](../../../primitives/actions/button-group/): the group is generic, this one binds the session.

## Best Practices

- Muted and camera-off states must be visible without colour.
- Hang up is separated from the other controls.
- The bar stays reachable during screen sharing.

## Blinc note

No direct Blinc equivalent (media controls exist for the player only). Built in our layer; generic toggle buttons from Blinc. Backlog id: none ⚠️.

## Open points

- ⚠️ Call protocol/standard (MatrixRTC, SIP, WebRTC)
- ⚠️ Name of the calls program

## See also

- [media – overview](../index.md)
- [Media Player](../media-player/)
- [Button Group](../../../primitives/actions/button-group/)
- [Messenger requirements](../../../../programs/apps/messenger/requirements.md)
- [Base component](../../../primitives/basics/base.md)

# Call Controls - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to Rust and
    Blinc, the `usage.md` examples will be replaced in a separate pass. This page is a
    skeleton (decision 2026-11-05).

## Application

Bar of controls for a running call, supplied by the calls program.

## Examples

```jsx
<CallControls session={call} onToggleMic={mute} onHangUp={endCall} />
```

## Scenarios

| Scenario | Recommendation |
|---|---|
| Calls program | `bar` |
| Another program during a call | `compact` as mini-bar |

## Embedding in other programs (ADR 0037)

The calls program shows a mini-bar in the messenger while a call runs. Per ADR 0037 every program is at least a workbench, so the same component appears compactly in project management, contacts, helpdesk and others, with fewer settings. Whoever wants more opens the messenger app. The component does not know which program hosts it; menus, gestures and mouse behaviour come from the host frontend.

## Keyboard and screen reader

- Toolbar pattern: arrow keys move, Space toggles.
- State words ("Microphone muted") are announced on change.
- A shortcut for mute is defined by the frontend, not by the component.

# Key Verification - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to Rust and
    Blinc, the `usage.md` examples will be replaced in a separate pass. This page is a
    skeleton (decision 2026-11-05).

## Application

Dialog for confirming a key or device.

## Examples

```jsx
<KeyVerification open={show} subject={contact} fingerprint={fp} onConfirm={trust} onReject={flag} />
```

## Scenarios

| Scenario | Recommendation |
|---|---|
| From encryption-state | open for an unverified key |
| New device | `device-list` after a login notice |

## Embedding in other programs (ADR 0037)

Any program showing a person can open the verification. Per ADR 0037 every program is at least a workbench, so the same component appears compactly in project management, contacts, helpdesk and others, with fewer settings. Whoever wants more opens the messenger app. The component does not know which program hosts it; menus, gestures and mouse behaviour come from the host frontend.

## Keyboard and screen reader

- Focus moves into the dialog; Esc closes without confirming.
- The fingerprint can be read group by group.
- Confirm and reject are separate, clearly named buttons.

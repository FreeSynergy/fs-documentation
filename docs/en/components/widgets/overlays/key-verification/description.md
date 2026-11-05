# Key Verification

| Field | Value |
|-------|-------|
| **Category** | `overlays` |
| **Inherits from** | `base` |
| **Variants** | `fingerprint`, `qr`, `device-list` |
| **States** | `unverified`, `comparing`, `verified`, `mismatch` |
| **Gestures** | none – gestures are added by the frontend, not by the component (ADR 0037) |
| **Animations** | `fade-in`, `pop-in` |
| **Related** | `modal`, `encryption-state`, `avatar`, `popover` |
| **Status** | skeleton |

## Description

A key verification lets a person check the key or device of a counterpart and confirm trust.

## Purpose

- Verify an OpenPGP fingerprint or MLS credential
- Confirm a new device of a contact
- Record trust (Web of Trust confirmation)

## Variants

| Variant | Description |
|---|---|
| **fingerprint** | compare fingerprint groups |
| **qr** | scan or show a QR code |
| **device-list** | list of devices with state |

## Features

- Fingerprint in readable groups, plus a QR code
- Compare on both sides, confirm or reject
- Device list with state
- Result stored with the identity

## Data binding

Binds OpenPGP fingerprint, MLS credential and Web-of-Trust confirmation (`data/identity`). Register (ADR 0023): `Key → key-verification | text`. Messenger requirements `key.verify`, `device.list`.

## Distinction

- **Do not confuse with** [modal](../modal/): the modal is a generic dialog; this one is a fixed verification flow.
- **Do not confuse with** [encryption-state](../../../primitives/feedback/encryption-state/): the state shows; the verification confirms.

## Best Practices

- Say plainly what confirming means.
- Never auto-confirm; mismatch is a clear error.
- Offer comparison over a second channel (in person, call).

## Blinc note

No Blinc equivalent. Built in our layer (binds identity data); the generic dialog part comes from `modal`. Backlog id: none ⚠️.

## Open points

- ⚠️ QR format for the exchange
- ⚠️ Ownership of trust records (identity vs. messages)

## See also

- [overlays – overview](../index.md)
- [Modal](../modal/)
- [Encryption State](../../../primitives/feedback/encryption-state/)
- [Messenger requirements](../../../../programs/apps/messenger/requirements.md)
- [Base component](../../../primitives/basics/base.md)

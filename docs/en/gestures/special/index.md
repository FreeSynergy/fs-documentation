# Special Gestures (special)

Special gestures run **without a classic touched element**: hover needs no
contact at all, and fingerprint does not target a UI element but a
biometric sensor.

Both gestures are deliberately without multipoint: hover exists only as one
hovering pointer, and the fingerprint sensor reads exactly one finger pad.

## Elements

- **hover** - pointer over element without contact (tooltip, preview)
- **fingerprint** - touching a biometric sensor (unlocking, authorising)

## Mapping

| Situation | Gesture |
|-----------|---------|
| Tooltip / preview without click | hover |
| Unlocking, authorising payments | fingerprint |

## Accessibility

Hover is unavailable on pure touchscreens – content must never be reachable
via hover only. Biometrics always need an equivalent alternative without
biometrics (PIN, pattern, password).

## See also

- [Gesture overview](../index.md)
- [Tap](../tap/tap/description.md) - contrast: a gesture on an element
- [Swipe](../swipe/swipe/description.md) - sliding across the sensor (swipe method)

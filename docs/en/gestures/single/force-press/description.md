# Force Press (Pressure Gesture)

## Description

A force press uses a **pressure sensor**: neither the time nor the distance
decides, but the force applied. Apple called this 3D Touch ("Peek & Pop"), on
trackpads it is called Force Click, Android devices with a pressure layer call
it Hard Press.

Without a pressure sensor the gesture is usually **simulated via a long press**
today (press and hold), because pressure sensors have disappeared from
smartphones. On the web: `PointerEvent.pressure` only returns values > 0 on
compatible hardware.

## Usage

- Peek & Pop: preview on light pressure, open on stronger pressure
- Context menu without waiting long
- Quick dialogs on app icons (homescreen shortcuts)
- Pressure-dependent brush size in drawing apps (pen)

## Pressure Levels

| Level | Pressure | Action |
|-------|----------|--------|
| Light Press | from ~30% | Element gives way minimally |
| Peek | from ~50% | Preview card appears |
| Pop | from ~75% | The target is opened |

## Duration

- Building up pressure: 100–500ms
- Opening the preview: 200–300ms

## Detection

| Method | Description |
|--------|-------------|
| **Pressure sensor** | Hardware measures force (older iOS, trackpad, pen) |
| **Long Press Fallback** | Without a sensor: holding replaces pressing |
| **pressure value** | `pointerdown`/`pointermove` with `pressure` 0–1 |

## Difference from Long Press

- **Long Press**: time decides
- **Force Press**: force decides (time is irrelevant)

## See also

- [Long Press](../long-press/description.md) - fallback without a pressure sensor
- [Press animation](../../../animations/feedback/press/description.md)

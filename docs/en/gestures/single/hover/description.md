# Hover (Hovering)

## Description

Hover describes **positioning the pointer over an element without contact**.
Classically with a mouse, on tablets with a precision pointer (Apple Pencil
hover over iPad, iPadOS cursor) and pens with hover detection; on pure
touchscreens there is no hover – there the first touch is already the action.

iOS provides the `UIHoverGestureRecognizer` for this, on the web:
`pointerover`/`pointerenter` with `pointerType`.

## Usage

- Showing a tooltip / help text
- Opening a preview menu under menu items
- Hover-lift: raising the element, making focus visible
- Precise selection in dense surfaces (tables, CAD, maps)
- Pen preview: showing the tool size before drawing starts

## Duration

- Showing/hiding: 100–300ms with a delay (usually 300–700ms against accidental triggering)
- As long as the pointer is over the element: active indefinitely

## Detection

| Method | Description |
|--------|-------------|
| **Mouse** | `pointermove` without a pressed button |
| **Pen Hover** | Sensor detects the pen before it touches down |
| **Touch-Pointer** | connected Bluetooth/trackpad pointer |

## Difference from Tap

- **Tap**: contact + triggering
- **Hover**: no contact, only preparing the action

## Difference from Force Press (Pen)

- **Hover**: distance > 0, no force
- **Force Press**: contact with force

## Accessibility

Hover content must also be reachable via keyboard focus and closable via
tap/escape (WCAG 1.4.13 Content on Hover or Focus). On touch, a first tap to
expand and a second to execute is allowed.

# Scale In

## Description

Scale In makes an element grow from size 0 % to 100 % without it leaving its
place in the layout. The growth point (`transformOrigin`) decides from which
direction the element appears to come.

## Use

- dialogs and popovers that "open up" when they open
- menus and tooltips that grow out of their trigger
- badges, chips and counters that newly enter the layout
- icon swap when a toggle is activated
- focus point in onboarding (the first new element)
- popover that grows out of an icon button

## Duration

- Typical: 150–300 ms
- Default value: 200 ms

## Difference from Zoom In

- Zoom In: usually starts at an intermediate value (e.g. 50–70 %) and, through
  an added depth or perspective effect, feels like approaching the element
- Scale In: begins exactly at 0 %, works without perspective and stays flat in
  the viewer plane
- Bounce In: also grows to 100 %, but ends with a springy overshoot past the
  final size

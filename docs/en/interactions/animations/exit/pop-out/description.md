# Pop Out

## Description

Pop Out is the opposite direction of Pop In: the element briefly anticipates (a
tiny enlargement), then shrinks below its final size and disappears meanwhile
through decreasing opacity. It looks "flicked away" and only gives up its place
in the layout at the end of the animation.

## Use

- remove chips and filter labels when the user deselects
- take an avatar out of a participant list (a participant leaves the room)
- dissolve a counter badge on an icon
- dissolve a list of elements that are folded away one by one
- remove deselected markers on a map
- let onboarding pins disappear after their explanation

## Duration

- Typical: 150–250 ms (exits may be shorter than entrances)
- Micro (badge, counter): 120–180 ms
- Several elements in a row: 150 ms plus a stagger, see
  [Cascade](../../organization/cascade/description.md)

## Difference from Pop In

- Pop In overshoots past the final size and ends calmly; Pop Out first briefly
  anticipates and ends at size 0.
- Pop In ends visible, Pop Out removes the element from the layout
  (`display: none` after `onAnimateEnd`).

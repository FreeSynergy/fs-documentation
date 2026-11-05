# Pop In

## Description

Pop In fades an element in both through opacity and through its size at the
same time, briefly shooting it past the final size (an overshoot of about 5 %).
That makes the element look plump and unmistakably "set down", without
neighbouring elements moving around in the layout.

## Use

- add chips and filter labels when the user makes a selection
- insert an avatar into a participant or commenter list
- let a counter badge appear on an icon (new message)
- let a selection tick "jump into" cards and lists
- drop pins and markers onto a map
- onboarding elements that should appear clearly but briefly

## Duration

- Typical: 200–300 ms
- Micro (badge, counter, tick): 150–200 ms
- Attention (onboarding pin): 300–400 ms

## Difference from Scale In

- Scale In grows exactly from 0 % to 100 % and does not change opacity; Pop In
  starts partly transparent and briefly overshoots past 100 %.
- Scale In ends without motion; Pop In lands with a short spring-back that
  emphasises the final state.

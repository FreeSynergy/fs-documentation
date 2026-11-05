# Tick Draw

## Description

Tick Draw draws a success tick as a line: the stroke follows a prepared path and
becomes visible in a short time, as though someone had set it. Usually a circle
or a surface appears first, then the tick. The animation replaces a text like
"Saved" with an unambiguous, language-independent sign.

## Use

- confirmation after saving, sending or synchronising
- ticking off a task in the list, see [checkbox](../../../../components/primitives/fields/checkbox/description.md)
- completing a step in an assistant
- confirming a selection (multi-selection, filters)
- a tick on an image or file icon (done, checked)
- a short success signal after a gesture-based control

## Duration

- Typical: 300–500 ms for the stroke
- Run-up (circle/background appears): 150–250 ms
- The signal may not take longer than 600 ms, otherwise it feels sluggish

## Difference from Ripple and Highlight

- Ripple confirms the contact itself and starts at the click point; Tick Draw
  confirms the result of the action.
- Highlight briefly colours a surface and says "something changed here"; Tick
  Draw shows a completed process and stays put.

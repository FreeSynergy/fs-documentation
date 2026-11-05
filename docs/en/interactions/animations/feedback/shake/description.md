# Shake

## Description

Shake briefly rattles an element horizontally around its position of rest and
decays as it does. It is feedback from the interface: the application uses it to
signal an error or a rejected action.

## Use

- wrong password or wrong code in the login
- a form field is rejected as invalid
- the action is not allowed at this place
- drag & drop onto an unsuitable target
- a reminder about a mandatory field that is still empty

## Duration

- Typical: 300–500 ms
- Default value: 400 ms

## Difference from Wiggle

- Wiggle: a slight rotation of a few degrees, longer or endless, as a hint at the
  edit mode
- Shake: a horizontal displacement with a larger amplitude, once, as an error
  message

## Difference from the Shake gesture

- Animation Shake: the element moves on its own – the application gives feedback
  to the user
- Shake gesture (see [shake gesture](../../../gestures/device/shake/description.md)):
  the user shakes the device – an input the application reacts to
- In short: in the animation the element moves as output, in the gesture the
  human shakes the device as input

# Feedback

Feedback animations respond directly to an input. They are short (usually under
500 ms) and never change the layout – the user should understand what their
action caused.

## Elements

- **shake** - briefly rattle horizontally (error, rejected input)
- **wiggle** - rock slightly (edit mode)
- **ripple** - let a wave spread from the point of contact
- **press** - sink minimally while pressing
- **lift** - raise on hover or focus (the shadow grows)
- **tick-draw** - draw a success tick as a line
- **highlight** - briefly let the background light up (found passage)
- **elastic** - swing past the final position
- **rubber-band** - excessive pulling springs back (over-scroll)

## Assignment

| Situation | Animation |
|-----------|-----------|
| action succeeded | ripple, tick-draw |
| a control step is active | press, lift |
| action rejected | shake, wiggle |
| content changed or found | highlight |
| boundary reached | rubber-band, elastic |

## See also

- [Animations overview](../index.md)
- [Gestures](../../gestures/) - shake and wiggle are output here, input there
- [Loop](../loop/) - lasting signals instead of a one-time response

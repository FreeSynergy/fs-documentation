# Flick (Momentum Swipe)

## Description

A flick is a fast swipe in which the finger **lifts off with momentum**. What
matters is not the distance covered, but the velocity at the moment of release:
after releasing, the content keeps moving through the impulse (momentum).

Android distinguishes in the `GestureDetector` between `onScroll` (drag,
continuously guided) and `onFling` (abrupt, with velocity). In everyday usage,
Flick and **Fling** are used as synonyms.

## Usage

- Throw/momentum scrolling in lists
- Fast paging in galleries and onboarding pages
- Tile/carousel paging (flicking one card further)
- Map views: quickly pushing the map section further

## Duration and Velocity

- Touch duration: usually under 300ms
- Velocity threshold: typically > 1000 px/s at release
- Run-out: content decelerates over 300–1500ms

## Detection

| Method | Description |
|--------|-------------|
| **Velocity** | Movement velocity of the last events at the up-event |
| **Decelerate** | Run-out with decreasing velocity |
| **Distinction from Swipe** | Flick evaluates velocity, Swipe evaluates distance |

## Difference from Swipe

- **Swipe**: distance counts (typically > 50px), content follows the finger 1:1
- **Flick**: velocity counts, content rolls out after the release

## Difference from Drag

- **Drag**: guiding, the content hangs on the finger, stops on release
- **Flick**: imparting momentum, the content keeps moving after the release

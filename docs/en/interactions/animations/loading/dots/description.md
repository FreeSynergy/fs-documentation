# Dots

## Description

Dots shows three dot-shaped elements that rise, fall or light up in a steady
rhythm. The indicator says: something is running right now, but there is no
measurable progress. It is the compact alternative to the spinner when the space
is small or the expected period is short.

## Use

- loading state inside a button ("Saving …")
- short requests in panels for which a skeleton is not worth it
- waiting for an answer in a list or a search field
- showing that a connection is currently being established
- inactive tabs whose content has not been loaded yet
- as a building block for the typing indicator, see [Typing](../typing/description.md)

## Duration

- Typical: 1200–1600 ms per cycle
- A single pulse: 400–600 ms
- From 10 s without a result, switch to [Skeleton](../skeleton/description.md) or
  [Progress](../progress/description.md)

## Difference from Typing and Spinner

- Typing imitates a human typing with an irregular rhythm and responds to a
  message; Dots runs evenly and signals system activity.
- Spin turns a surface around its axis and needs a certain size; Dots already
  works at line height and next to text.

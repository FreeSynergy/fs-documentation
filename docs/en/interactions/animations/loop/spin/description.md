# Spin

## Description

Spin turns an element permanently in an even rhythm – without a defined end
angle. The animation runs as an endless loop and signals activity for as long as
a task (loading, syncing, processing) is not yet finished.

## Use

- loading spinner while data is being fetched
- synchronisation and refresh status
- processing or upload with an unknown progress
- recording or live indicator in toolbars
- play status: a rotating icon while playing
- a progress wheel next to texts like "Saving …"

## Duration

- Per revolution: 800–1500ms
- `iterationCount: infinite` – the total duration ends with the task
- Under 800ms per revolution looks restless, over 1500ms sluggish

## Difference from Rotate

- Spin: an endless rotation without an end angle; it only stops when the work is
  done
- Rotate: a defined, one-time turn to a fixed angle with a lasting end state

# Time Picker - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to
    Rust and Blinc, the `usage.md` examples will be replaced in a separate pass.

## Application

The selection appears when tapping the time field. The start and end of an appointment
are considered together so the end never lies before the start.

## Examples

### Start of an appointment

```jsx
<TimePicker label="Start" value={start} step={15} onChange={setStart} />
```

### Hide times that are taken

```jsx
<TimePicker blocked={roomBookings} min="08:00" max="18:00" />
```

## Scenarios

| Scenario | Recommendation |
|----------|----------------|
| Creating an appointment | `step = 15`, pull the end along automatically |
| Time tracking | `step = 6`, `freeInput = true` |
| Room booking | `blocked` from the calendar of the room |

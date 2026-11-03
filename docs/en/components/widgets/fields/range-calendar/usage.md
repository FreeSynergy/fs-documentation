# Range Calendar - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to
    Rust and Blinc, the `usage.md` examples will be replaced in a separate pass.

## Application

The calendar usually sits in a filter bar or a dialog. The result is shown as a
readable period outside the calendar.

## Examples

### Filter in a list view

```jsx
<RangeCalendar from={from} to={to} months={2} onChange={applyFilter} />
```

### Entering an absence

```jsx
<RangeCalendar min={today} maxRange={90} showCount={true} onChange={save} />
```

## Scenarios

| Scenario | Recommendation |
|----------|----------------|
| Report filter | `presets` with 7, 30 and quarter |
| Entering a vacation | `min = heute`, show the day counter |
| Mobile filter bar | `months = 1`, swipe gesture to change the month |

# Calendar View - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to
    Rust and Blinc, the `usage.md` examples will be replaced in a separate pass.

## Application

A calendar view shows appointments in a calendar.

- Showing appointments
- Calendars
- Planning
- Scheduling

## Examples

### Showing appointments

```jsx
<CalendarView date="date" events={entries} onChange={action} />
```

### Calendars

```jsx
<CalendarView date="date" events={entries} interactive={false} />
```

### Planning

```jsx
<CalendarView date="date" events={entries} interactive={false} />
```

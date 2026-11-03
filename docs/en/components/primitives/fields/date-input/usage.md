# Date Input - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to
    Rust and Blinc, the `usage.md` examples will be replaced in a separate pass.

## Application

A date input is a date selection field with a calendar.

- Date of birth
- Choosing an appointment
- Giving a date

## Examples

### Date of birth

```jsx
<DateInput value="value" type="date" onChange={action} />
```

### Choosing an appointment

```jsx
<DateInput value="value" type="date" minDate="minDate" />
```

### Giving a date

```jsx
<DateInput value="value" type="date" maxDate="maxDate" />
```

## Notes

- States: `placeholder` (in addition to the states from `base`)

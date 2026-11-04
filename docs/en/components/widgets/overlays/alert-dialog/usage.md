# Alert Dialog - Usage

!!! note
    The examples are kept syntax-neutral. Once the implementation switches to Rust and
    Blinc, the `usage.md` examples will be replaced in a separate pass.

## Application

The dialog appears out of an action and holds it back until a decision is made. It is
managed once per program window, not once per button.

## Examples

### Securing a destructive action

```jsx
<AlertDialog title="Discard page?" message="Changes will be lost."
             destructive={true} confirmLabel="Discard" onConfirm={discard} />
```

### Confirmation with a typed word

```jsx
<AlertDialog title="Delete knowledge area?" confirmWord="wiki-demo"
             confirmLabel="Delete permanently" onConfirm={remove} />
```

## Scenarios

| Scenario | Recommendation |
|----------|----------------|
| action can be undone | no dialog, toast with undo |
| deleting an object with many references | `destructive` + `confirmWord` |
| leaving a form with changes | dialog with three actions (Save, Discard, Cancel) |

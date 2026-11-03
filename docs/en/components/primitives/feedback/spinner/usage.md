# Spinner - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to
    Rust and Blinc, the `usage.md` examples will be replaced in a separate pass.

## Loading state in an area

```jsx
<Panel busy={loading}>
  {loading ? <Spinner text="Loading view…" /> : content}
</Panel>
```

## A compact activity hint in a bar

```jsx
<Toolbar>
  <Spinner size="small" track={false} aria-label="Synchronising" />
</Toolbar>
```

## In a field (while checking)

```jsx
<TextInput
  value={login}
  trailing={<Spinner size="small" inline={true} />}
/>
```

## Scenarios

| Scenario | Recommendation |
|----------|----------------|
| Saving, response < 2 s | `loading` on the [button](../../actions/button/) |
| Loading a view | `mit-text` centred in the area |
| Synchronisation in the background | `small` in the status bar |
| Duration known / large data volume | [progress](../progress/) instead of a spinner |

# Kbd - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to
    Rust and Blinc, the `usage.md` examples will be replaced in a separate pass.

## Single key

```jsx
<Kbd shortcut="Esc" />
```

## Combination in a tooltip

```jsx
<Tooltip content={<>Save <Kbd keys={["Ctrl", "S"]} /></>} />
```

## Shortcut overview

```jsx
<Table>
  <Row action="Open search"><Kbd keys={["Ctrl", "K"]} /></Row>
  <Row action="Save"><Kbd keys={["Ctrl", "S"]} /></Row>
</Table>
```

## Showing the pressed state (onboarding)

```jsx
<Kbd shortcut="Enter" active={userPressed} />
```

## Scenarios

| Scenario | Recommendation |
|----------|----------------|
| Tooltip with a shortcut | `keys` combination on the right side of the text |
| Command palette (`command`) | kbd per candidate in the result list |
| Mac variants | caption `Cmd`/`Ctrl` depending on the platform |
| Coded content | `code`, not kbd |

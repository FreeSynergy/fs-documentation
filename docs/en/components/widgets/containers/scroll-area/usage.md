# Scroll Area - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to
    Rust and Blinc, the `usage.md` examples will be replaced in a separate pass.

## Application

The scroll area receives a fixed measure from outside (flexible height of the
column) and takes care of everything else: indicators, gradients, loading more,
follow.

## Examples

### A chat history that follows new content

```jsx
<ScrollArea height="100%" direction="vertikal" follow={true} onEndReached={loadOlder} />
```

### A horizontal toolbar

```jsx
<ScrollArea direction="horizontal" scrollbar="automatisch" edges={true} />
```

## Scenarios

| Scenario | Recommendation |
|----------|----------------|
| Message outbox | `follow = true`, load more at the top with `keepPosition` |
| Table inside a card | scroll area only for the body rows, the header stays put |
| Narrow toolbar | `direction = "horizontal"`, gradients as a hint |

# Hover Card - Usage

!!! note
    The examples are kept syntax-neutral. Once the implementation switches to Rust and
    Blinc, the `usage.md` examples will be replaced in a separate pass.

## Application

The card hangs on a reference. It only opens when the pointer rests steadily on the
trigger; the content comes from the already loaded record or is fetched afterwards.

## Examples

### Profile preview on a name

```jsx
<HoverCard target={user.id} variant="profil" placement="top" />
```

### Article excerpt in a list

```jsx
<HoverCard content={{ title, excerpt, updated }} openDelay={400} />
```

## Scenarios

| Scenario | Recommendation |
|----------|----------------|
| name in a chat message | `variant = "profil"`, `openDelay = 300` |
| reference in a table | `variant = "dokument"`, `size = "small"` |
| touch surface | long-press, card as a bottom bar |

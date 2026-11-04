# Command - Usage

!!! note
    The examples are kept syntax-neutral. Once the implementation switches to Rust and
    Blinc, the `usage.md` examples will be replaced in a separate pass.

## Application

The palette is created once per program window and is reachable globally via the shortcut.
It receives the commands of the currently active view.

## Examples

### Palette in the program window

```jsx
<Command commands={commands} hotkey="ctrl+k" onSelect={run} />
```

### Opening commands from a toolbar

```jsx
<Command commands={viewCommands} open={paletteOpen} onClose={close} />
```

## Scenarios

| Scenario | Recommendation |
|----------|----------------|
| desktop client | `hotkey = "ctrl+k"`, palette centred |
| mobile | `inline` in the sidebar, no shortcut |
| command not found | notice with suggestions instead of an empty list |

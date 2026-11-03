# Chart - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to
    Rust and Blinc, the `usage.md` examples will be replaced in a separate pass.

## Application

A chart is a data visualisation (diagrams).

- Statistics
- Diagrams
- Graphics

## Examples

### Statistics

```jsx
<Chart data={entries} type="line" />
```

### Diagrams

```jsx
<Chart data={entries} interactive={true} />
```

### Graphics

```jsx
<Chart data={entries} showLegend={true} />
```

## Notes

- Transitions: `highlight`

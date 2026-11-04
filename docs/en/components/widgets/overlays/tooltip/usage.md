# Tooltip - Usage

!!! note
    The examples are kept syntax-neutral. Once the implementation switches to Rust and
    Blinc, the `usage.md` examples will be replaced in a separate pass.

## Explaining an icon-only button

```jsx
<IconButton icon="settings" aria-label="Settings">
  <Tooltip content="Open settings" placement="top" />
</IconButton>
```

## Full text for a truncated value

```jsx
<TableCell value={shortTitle}>
  <Tooltip content={fullTitle} placement="top" />
</TableCell>
```

## Showing a keyboard shortcut

```jsx
<Tooltip content="Save (Ctrl + S)" delay={0} />
```

## On mobile via long-press

```jsx
<ToolbarItem icon="filter">
  <Tooltip content="Filter" trigger="longpress" />
</ToolbarItem>
```

## Scenarios

| Scenario | Recommendation |
|----------|----------------|
| icon-only button | tooltip plus `aria-label` |
| truncated table value | `placement="top"`, `delay={0}` |
| explanatory text for a field | rather [field](../../../primitives/fields/field/) with `help` |
| content with buttons or links | [popover](../popover/), no tooltip |

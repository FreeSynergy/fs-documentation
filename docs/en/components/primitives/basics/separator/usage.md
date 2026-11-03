# Separator - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to
    Rust and Blinc, the `usage.md` examples will be replaced in a separate pass.

## Separating menu groups

```jsx
<Menu>
  <MenuItem label="Rename" />
  <Separator />
  <MenuItem label="Archive" />
  <MenuItem label="Delete" variant="danger" />
</Menu>
```

## Tool groups in a bar

```jsx
<Toolbar>
  <ToolbarGroup items={formatItems} />
  <Separator orientation="vertical" />
  <ToolbarGroup items={alignItems} />
</Toolbar>
```

## Alternative with a caption

```jsx
<Separator label="or" />
<Button label="New document" variant="primary" />
```

## Decorative line under a heading

```jsx
<Separator variant="dekorativ" />
```

## Scenarios

| Scenario | Recommendation |
|----------|----------------|
| Menu with different kinds of actions | `horizontal`, role `separator` |
| Two sides of a detail view | `vertical` |
| Form sections | `horizontal` with `spacing` 16 |
| Pure appearance without structure | `dekorativ` plus `aria-hidden` |

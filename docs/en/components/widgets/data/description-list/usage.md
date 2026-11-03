# Description List - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to
    Rust and Blinc, the `usage.md` examples will be replaced in a separate pass.

## Application

The list sits in detail views and cards. Values that should be edited are opened by
clicking on a field — the list itself stays presentation.

## Examples

### Details of a contact

```jsx
<DescriptionList items={contactFields} columns={2} copyable={true} />
```

### Metadata in a card

```jsx
<DescriptionList items={docMeta} variant="gestapelt" showEmpty={false} />
```

## Scenarios

| Scenario | Recommendation |
|----------|----------------|
| Detail page of a record | `columns = 2`, groups for more than twelve values |
| Narrow sidebar | `variant = "gestapelt"` |
| Values in running text | `variant = "inline"` |

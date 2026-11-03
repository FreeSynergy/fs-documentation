# Empty State - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to
    Rust and Blinc, the `usage.md` examples will be replaced in a separate pass.

## Application

The empty state replaces the list, not a hint above the list. It only appears
once it is certain that there is no content – while loading, a skeleton stands there.

## Examples

### First content is missing

```jsx
<EmptyState title="No tasks yet" icon="task"
            actionLabel="Create your first task" hint="Ctrl N" onAction={create} />
```

### Filter without a hit

```jsx
<EmptyState variant="kein-treffer" query={q} title="No match"
            actionLabel="Reset filters" onReset={clear} />
```

## Scenarios

| Scenario | Recommendation |
|----------|----------------|
| Area opened for the first time | `variant = "leer"` with a create action |
| Search returns nothing | `variant = "kein-treffer"`, show the search term |
| Loading error | `variant = "fehler"` with a retry |

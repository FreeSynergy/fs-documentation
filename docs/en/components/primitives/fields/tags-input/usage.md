# Tags Input - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to
    Rust and Blinc, the `usage.md` examples will be replaced in a separate pass.

## Application

A tags input is a list of tags/labels.

- Hashtags
- Categories
- Keywords

## Examples

### Hashtags

```jsx
<TagsInput tags={entries} onChange={action} />
```

### Categories

```jsx
<TagsInput tags={entries} placeholder="placeholder" />
```

### Keywords

```jsx
<TagsInput tags={entries} showRemove={true} />
```

## Notes

- States: `placeholder` (in addition to the states from `base`)

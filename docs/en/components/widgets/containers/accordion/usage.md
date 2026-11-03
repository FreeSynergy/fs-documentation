# Accordion - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to
    Rust and Blinc, the `usage.md` examples will be replaced in a separate pass.

## Application

An accordion is a stack of headers that can collapse and expand content.

- Saving space by collapsing and expanding
- FAQ sections
- Settings groups
- Categories with sub-items

## Examples

### Saving space by collapsing and expanding

```jsx
<Accordion items={entries} onChange={action} />
```

### FAQ sections

```jsx
<Accordion items={entries} collapsible={true} />
```

### Settings groups

```jsx
<Accordion items={entries} animate={true} />
```

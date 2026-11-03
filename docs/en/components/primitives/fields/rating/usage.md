# Rating - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to
    Rust and Blinc, the `usage.md` examples will be replaced in a separate pass.

## Application

A rating is a star or point evaluation.

- Product ratings
- Service ratings
- Stars

## Examples

### Product rating

```jsx
<Rating onChange={action} />
```

### Service rating

```jsx
<Rating onChange={action} readonly={false} />
```

### Stars

```jsx
<Rating onChange={action} max={5} />
```

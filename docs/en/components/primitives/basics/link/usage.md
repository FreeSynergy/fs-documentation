# Link - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to
    Rust and Blinc, the `usage.md` examples will be replaced in a separate pass.

## Reference to an object

```jsx
<Link href="/crm/contact/4711">Contact Meier, Anna</Link>
```

## External reference

```jsx
<Link href="https://projects.example.org/t/205" external={true} icon="external">
  Task 205
</Link>
```

## Download

```jsx
<Link href="/api/files/attachment.pdf" download="attachment.pdf">Download attachment</Link>
```

## Jump marker inside an article

```jsx
<Link href="#chapter-3" variant="muted">to chapter 3</Link>
```

## Scenarios

| Scenario | Recommendation |
|----------|----------------|
| Jumping between objects | `standard` |
| In running text | `unterstrichen` |
| External in the web browser | `external` plus an icon |
| Action without changing the address | [button](../../actions/button/), not a link |

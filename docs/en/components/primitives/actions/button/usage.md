# Button - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to
    Rust and Blinc, the `usage.md` examples will be replaced in a separate pass.

## Standard button

```jsx
<Button label="Save" variant="primary" onClick={save} />
```

## Pair of variants in a dialog

```jsx
<Dialog title="Close page?">
  <Button label="Cancel" variant="secondary" onClick={close} />
  <Button label="Discard" variant="danger" onClick={discard} />
</Dialog>
```

## Icon button with a label for screen readers

```jsx
<Button icon="settings" iconOnly={true} aria-label="Open settings" />
```

## Loading state while saving

```jsx
<Button label="Send" variant="primary" loading={sending} onClick={send} />
```

## Submitting a form

```jsx
<Form onSubmit={save}>
  <Button label="Save" type="submit" variant="primary" />
</Form>
```

## Scenarios

| Scenario | Recommendation |
|----------|----------------|
| Save a document | one `primary`, the rest `secondary` |
| Destructive action | `danger` + confirmation dialog |
| Toolbar with many actions | [button-group](../button-group/) instead of single buttons |
| Back navigation | `link`, not a button |

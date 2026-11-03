# Field - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to
    Rust and Blinc, the `usage.md` examples will be replaced in a separate pass.

## Standard field with help text

```jsx
<Field label="Username" for="username" help="At most 30 characters.">
  <TextInput id="username" maxLength={30} />
</Field>
```

## Required field with an error

```jsx
<Field
  label="Email"
  for="email"
  required={true}
  error={emailError}
>
  <TextInput id="email" type="email" value={email} />
</Field>
```

## Dense form (label on the left)

```jsx
<Field label="Category" for="cat" variant="horizontal">
  <Select id="cat" options={categories} />
</Field>
```

## Character counter in a text field

```jsx
<Field label="Note" for="note" counter={true}>
  <TextArea id="note" maxLength={500} />
</Field>
```

## Scenarios

| Scenario | Recommendation |
|----------|----------------|
| All form fields | always a field wrapper |
| Pure caption without input | [label](../../basics/label/) is enough |
| Search in bars | `inline` without `help` |
| Detail view without input | [description-list](../../../widgets/data/description-list/) |

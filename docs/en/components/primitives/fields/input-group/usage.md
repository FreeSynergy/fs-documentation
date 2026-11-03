# Input Group - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to
    Rust and Blinc, the `usage.md` examples will be replaced in a separate pass.

## Application

The group is built around an existing field, not instead of it. Label, help text
and error message stay outside with the [field](../field/); the group contains only
the field and the parts that explain the same value.

## Examples

### An address with a protocol prefix

```jsx
<InputGroup prefix="https://" field={<TextInput value={host} onChange={setHost} />} />
```

### Amounts with a unit and a sign

```jsx
<InputGroup prefix="€" suffix="gross" field={<NumberInput value={net} onChange={setNet} />} />
```

### Search with an action

```jsx
<InputGroup action="Search" onAction={runSearch} field={<TextInput value={q} onChange={setQ} />} />
```

### A country code as a prefix selection

```jsx
<InputGroup prefixOptions={dialCodes} onPrefixChange={setDial}
            field={<NumberInput value={phone} onChange={setPhone} />} />
```

## Scenarios

| Scenario | Recommendation |
|----------|----------------|
| Unit or sign | `prefix` or `suffix`, no caption of its own |
| Action on the field | `action` plus `actionOnEnter`, give the button a label |
| Country code, protocol | `prefixOptions` instead of free text |
| Password visible/hidden | `suffix` as a toggle icon, with `aria-label` |
| Field with help text | group in the field area, [field](../field/) around it |

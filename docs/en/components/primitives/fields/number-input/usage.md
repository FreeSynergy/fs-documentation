# Number Input - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to
    Rust and Blinc, the `usage.md` examples will be replaced in a separate pass.

## Application

A number input is an input field for numbers.

- Giving an age
- Quantities
- Prices
- Values

## Examples

### Giving an age

```jsx
<NumberInput onChange={action} />
```

### Quantities

```jsx
<NumberInput onChange={action} step={1} />
```

### Prices

```jsx
<NumberInput onChange={action} showStepButtons={true} />
```

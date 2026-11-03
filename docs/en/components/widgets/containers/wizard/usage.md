# Wizard - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to
    Rust and Blinc, the `usage.md` examples will be replaced in a separate pass.

## Application

A wizard is a step-by-step form for complex tasks.

- Step-by-step instructions
- Complex forms
- Setup assistants
- Onboarding

## Examples

### Step-by-step instructions

```jsx
<Wizard steps={entries} activeStep={0} onChange={action} />
```

### Complex forms

```jsx
<Wizard steps={entries} activeStep={0} validation={false} />
```

### Setup assistants

```jsx
<Wizard steps={entries} activeStep={0} clickable={false} />
```

## Notes

- States: `completed` (in addition to the states from `base`)

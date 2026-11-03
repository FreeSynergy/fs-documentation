# Text Input - Usage

## A simple text input

```jsx
<TextInput
  label="Name"
  value={name}
  onChange={setName}
  placeholder="John Doe"
/>
```

## With an icon

```jsx
<TextInput
  label="Email"
  value={email}
  onChange={setEmail}
  prefix={<Icon name="email" />}
  placeholder="name@example.com"
/>
```

## In a form

```jsx
<Form>
  <TextInput
    label="First name"
    value={firstName}
    onChange={setFirstName}
  />
  <TextInput
    label="Last name"
    value={lastName}
    onChange={setLastName}
  />
</Form>
```

## With validation

```jsx
<TextInput
  label="Email"
  value={email}
  onChange={setEmail}
  error={emailError}
  required={true}
  pattern="email"
/>
```

## With event handlers

```jsx
<TextInput
  label="Name"
  value={name}
  onChange={setName}
  onFocus={() => console.log('Focus')}
  onBlur={() => console.log('Blur')}
  onSubmit={() => console.log('Submit:', name)}
/>
```

## Examples

## Example 1: name

```
┌─────────────────────────────────────────┐
│ Name                                    │
├─────────────────────────────────────────┤
│  John Doe                               │
│                                         │
└─────────────────────────────────────────┘
```

## Example 2: email

```
┌─────────────────────────────────────────┐
│ Email                                   │
├─────────────────────────────────────────┤
│  📧 john@example.com                    │
│                                         │
└─────────────────────────────────────────┘
```

## Example 3: with an icon

```
┌─────────────────────────────────────────┐
│ 🔍 Search                               │
├─────────────────────────────────────────┤
│  search term                            │
│                                         │
└─────────────────────────────────────────┘
```

## Example 4: password

```
┌─────────────────────────────────────────┐
│ Password                                │
├─────────────────────────────────────────┤
│  •••••••••••••••                        │
│                                         │
└─────────────────────────────────────────┘
```

## Example 5: with prefix/suffix

```
┌─────────────────────────────────────────┐
│ Price in €                              │
├─────────────────────────────────────────┤
│  € 99.99                                │
│                                         │
└─────────────────────────────────────────┘
```

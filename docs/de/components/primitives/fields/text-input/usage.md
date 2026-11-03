# Text Input (Einzeiliges Textfeld) - Verwendung

## Einfaches Text Input

```jsx
<TextInput 
  label="Name"
  value={name}
  onChange={setName}
  placeholder="Max Mustermann"
/>
```

## Mit Icon

```jsx
<TextInput 
  label="E-Mail"
  value={email}
  onChange={setEmail}
  prefix={<Icon name="email" />}
  placeholder="name@example.com"
/>
```

## In Formular

```jsx
<Form>
  <TextInput 
    label="Vorname"
    value={firstName}
    onChange={setFirstName}
  />
  <TextInput 
    label="Nachname"
    value={lastName}
    onChange={setLastName}
  />
</Form>
```

## mit Validierung

```jsx
<TextInput 
  label="E-Mail"
  value={email}
  onChange={setEmail}
  error={emailError}
  required={true}
  pattern="email"
/>
```

## Mit Event-Handlern

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

## Beispiele

## Beispiel 1: Name

```
┌─────────────────────────────────────────┐
│ Name                                    │
├─────────────────────────────────────────┤
│  Max Mustermann                         │
│                                         │
└─────────────────────────────────────────┘
```

## Beispiel 2: E-Mail

```
┌─────────────────────────────────────────┐
│ E-Mail                                  │
├─────────────────────────────────────────┤
│  📧 max@example.com                     │
│                                         │
└─────────────────────────────────────────┘
```

## Beispiel 3: mit Icon

```
┌─────────────────────────────────────────┐
│ 🔍 Suche                                │
├─────────────────────────────────────────┤
│  Suchbegriff                            │
│                                         │
└─────────────────────────────────────────┘
```

## Beispiel 4: Passwort

```
┌─────────────────────────────────────────┐
│ Passwort                                │
├─────────────────────────────────────────┤
│  •••••••••••••••                        │
│                                         │
└─────────────────────────────────────────┘
```

## Beispiel 5: mit Prefix/Suffix

```
┌─────────────────────────────────────────┐
│ Preis in €                              │
├─────────────────────────────────────────┤
│  € 99.99                                │
│                                         │
└─────────────────────────────────────────┘
```

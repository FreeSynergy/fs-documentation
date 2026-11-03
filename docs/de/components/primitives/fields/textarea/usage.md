# Textarea (Mehrzeiliges Textfeld) - Verwendung

## Einfaches Textarea

```jsx
<Textarea 
  label="Nachricht"
  value={message}
  onChange={setMessage}
  placeholder="Ihre Nachricht..."
/>
```

## Auto-Resize

```jsx
<Textarea 
  label="Kommentar"
  value={comment}
  onChange={setComment}
  autoResize={true}
  minRows={3}
  maxRows={10}
/>
```

## In Formular

```jsx
<Form>
  <TextInput 
    label="Betreff"
    value={subject}
    onChange={setSubject}
  />
  <Textarea 
    label="Nachricht"
    value={message}
    onChange={setMessage}
  />
</Form>
```

## mit Character Counter

```jsx
<Textarea 
  label="Beschreibung"
  value={description}
  onChange={setDescription}
  maxLength={500}
  showCharacterCount={true}
/>
```

## Mit Event-Handlern

```jsx
<Textarea 
  label="Nachricht"
  value={message}
  onChange={setMessage}
  onFocus={() => console.log('Focus')}
  onBlur={() => console.log('Blur')}
/>
```

## Beispiele

## Beispiel 1: Nachricht

```
┌─────────────────────────────────────────┐
│ Nachricht                               │
├─────────────────────────────────────────┤
│                                         │
│  Dies ist eine Nachricht...             │
│  Mehrzeiliger Text                      │
│                                         │
│                                         │
└─────────────────────────────────────────┘
```

## Beispiel 2: Kommentar

```
┌─────────────────────────────────────────┐
│ Kommentar                               │
├─────────────────────────────────────────┤
│  👤 John Doe                            │
│  Sehr gut!                              │
│                                         │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━    │
│  (123/500 Zeichen)                      │
└─────────────────────────────────────────┘
```

## Beispiel 3: Beschreibung

```
┌─────────────────────────────────────────┐
│ Beschreibung                            │
├─────────────────────────────────────────┤
│  Diese Anwendung...                     │
│  Sie ermöglicht...                      │
│  Mit Funktionen...                      │
│                                         │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━    │
└─────────────────────────────────────────┘
```

## Beispiel 4: mit Auto-Resize

```
┌─────────────────────────────────────────┐
│ Notizen                                 │
├─────────────────────────────────────────┤
│  Punkt 1                                │
│  Punkt 2                                │
│  Punkt 3                                │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━    │
└─────────────────────────────────────────┘
```

## Beispiel 5: mit Limit

```
┌─────────────────────────────────────────┐
│ Beschreibung (max. 200 Zeichen)         │
├─────────────────────────────────────────┤
│  Dies ist ein Text...                   │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━    │
│  (145/200 Zeichen)                      │
└─────────────────────────────────────────┘
```

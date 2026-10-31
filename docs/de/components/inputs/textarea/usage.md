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

# Textarea - Verwendung

## Ein einfaches Textarea

```jsx
<Textarea
  label="Nachricht"
  value={message}
  onChange={setMessage}
  placeholder="Deine Nachricht…"
/>
```

## Automatische Größenanpassung

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

## In einem Formular

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

## Mit Zeichenzähler

```jsx
<Textarea
  label="Beschreibung"
  value={description}
  onChange={setDescription}
  maxLength={500}
  showCharacterCount={true}
/>
```

## Mit Ereignis-Handlern

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
│  Das ist eine Nachricht...              │
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
│  👤 Max Mustermann                      │
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
│  Sie macht es möglich...                │
│  Mit Funktionen...                      │
│                                         │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━    │
└─────────────────────────────────────────┘
```

## Beispiel 4: mit automatischer Größenanpassung

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

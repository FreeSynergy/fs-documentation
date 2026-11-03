# Textarea - Usage

## A simple textarea

```jsx
<Textarea
  label="Message"
  value={message}
  onChange={setMessage}
  placeholder="Your message…"
/>
```

## Auto-resize

```jsx
<Textarea
  label="Comment"
  value={comment}
  onChange={setComment}
  autoResize={true}
  minRows={3}
  maxRows={10}
/>
```

## In a form

```jsx
<Form>
  <TextInput
    label="Subject"
    value={subject}
    onChange={setSubject}
  />
  <Textarea
    label="Message"
    value={message}
    onChange={setMessage}
  />
</Form>
```

## With a character counter

```jsx
<Textarea
  label="Description"
  value={description}
  onChange={setDescription}
  maxLength={500}
  showCharacterCount={true}
/>
```

## With event handlers

```jsx
<Textarea
  label="Message"
  value={message}
  onChange={setMessage}
  onFocus={() => console.log('Focus')}
  onBlur={() => console.log('Blur')}
/>
```

## Examples

## Example 1: message

```
┌─────────────────────────────────────────┐
│ Message                                 │
├─────────────────────────────────────────┤
│                                         │
│  This is a message...                   │
│  Multi-line text                        │
│                                         │
│                                         │
└─────────────────────────────────────────┘
```

## Example 2: comment

```
┌─────────────────────────────────────────┐
│ Comment                                 │
├─────────────────────────────────────────┤
│  👤 John Doe                            │
│  Very good!                             │
│                                         │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━    │
│  (123/500 characters)                   │
└─────────────────────────────────────────┘
```

## Example 3: description

```
┌─────────────────────────────────────────┐
│ Description                             │
├─────────────────────────────────────────┤
│  This application...                    │
│  It makes it possible...                │
│  With features...                       │
│                                         │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━    │
└─────────────────────────────────────────┘
```

## Example 4: with auto-resize

```
┌─────────────────────────────────────────┐
│ Notes                                   │
├─────────────────────────────────────────┤
│  Point 1                                │
│  Point 2                                │
│  Point 3                                │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━    │
└─────────────────────────────────────────┘
```

## Example 5: with a limit

```
┌─────────────────────────────────────────┐
│ Description (max. 200 characters)       │
├─────────────────────────────────────────┤
│  This is some text...                   │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━    │
│  (145/200 characters)                   │
└─────────────────────────────────────────┘
```

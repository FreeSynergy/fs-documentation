# Mention Input - Verwendung

!!! note
    Die Beispiele bleiben syntaxneutral. Sobald die Umsetzung auf Rust und Blinc
    wechselt, werden die Beispiele in `usage.md` in einem eigenen Durchgang ersetzt.

## Anwendung

Ein Mention Input ist ein Textfeld mit Erwähnungen von Benutzern oder Kontakten.

- Chat
- Kommentare
- Nachrichten

## Beispiele

### Chat

```jsx
<MentionInput value="value" onChange={action} />
```

### Kommentare

```jsx
<MentionInput value="value" users={entries} />
```

### Nachrichten

```jsx
<MentionInput value="value" placeholder="placeholder" />
```

## Hinweise

- Zustände: `placeholder` (zusätzlich zu den Zuständen aus `base`)

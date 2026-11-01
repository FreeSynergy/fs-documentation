# Mention Input (Erwähnungsfeld) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Anwendung

Ein Mention Input ist ein Textfeld mit Benutzer-/Kontakt-Erwähnung.

- Chat
- Kommentare
- Messages

## Beispiele

### Chat

```jsx
<MentionInput value="Wert" onChange={aktion} />
```

### Kommentare

```jsx
<MentionInput value="Wert" users={eintraege} />
```

### Messages

```jsx
<MentionInput value="Wert" placeholder="Platzhalter" />
```

## Hinweise

- Zustände: `placeholder` (zusätzlich zu den Zuständen aus `base`)

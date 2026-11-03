# Toast (Benachrichtigung) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Anwendung

Ein Toast ist eine Pop-up-Benachrichtigung, die meist oben rechts erscheint.

- Kurze Benachrichtigungen
- Erfolgs-Meldungen
- Fehler-Meldungen
- Informations-Meldungen

## Beispiele

### Kurze Benachrichtigungen

```jsx
<Toast type="info" title="Titel" message="Nachricht" />
```

### Erfolgs-Meldungen

```jsx
<Toast type="info" title="Titel" autoDismiss={true} />
```

### Fehler-Meldungen

```jsx
<Toast type="info" title="Titel" dismissDelay={3000} />
```

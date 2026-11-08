# Toast - Verwendung

!!! note
    Die Beispiele bleiben syntaxneutral. Sobald die Umsetzung auf Rust und Blinc
    wechselt, werden die Beispiele in `usage.md` in einem eigenen Durchgang ersetzt.

## Anwendung

Ein Toast ist eine Benachrichtigung als Pop-up. Sie erscheint meist oben rechts.

- Kurze Benachrichtigungen
- Erfolgsmeldungen
- Fehlermeldungen
- Informationsmeldungen

## Beispiele

### Kurze Benachrichtigungen

```jsx
<Toast type="info" title="Titel" message="Meldung" />
```

### Erfolgsmeldungen

```jsx
<Toast type="info" title="Titel" autoDismiss={true} />
```

### Fehlermeldungen

```jsx
<Toast type="info" title="Titel" dismissDelay={3000} />
```

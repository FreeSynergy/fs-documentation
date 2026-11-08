# Alert – Verwendung

!!! note
    Die Beispiele bleiben syntaxneutral. Sobald die Implementierung auf Rust und
    Blinc umstellt, werden die Beispiele in `usage.md` in einem eigenen Durchgang ersetzt.

## Anwendung

Ein Alert ist eine Statusmeldung (Info, Warnung, Fehler, Erfolg).

- Statusmeldungen anzeigen
- Fehler anzeigen
- Erfolge anzeigen
- Warnungen anzeigen

## Beispiele

### Statusmeldung anzeigen

```jsx
<Alert type="info" title="Title" message="Message" />
```

### Fehler anzeigen

```jsx
<Alert type="info" title="Title" dismissible={false} />
```

### Erfolg anzeigen

```jsx
<Alert type="info" title="Title" closable={false} />
```

## Hinweise

- Barrierefreiheit: Rolle `alert`; die Bedienelemente zusätzlich mit `label` oder `aria-label` benennen
- Gesten: `tap`
- Übergänge: `fade-in`, `collapse`
- Siehe auch: [toast](../../feedback/toast/), [badge](../../feedback/badge/), [progress](../../feedback/progress/)

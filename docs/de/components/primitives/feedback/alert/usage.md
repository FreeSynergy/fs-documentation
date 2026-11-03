# Alert (Warnung) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Anwendung

Ein Alert ist eine Status-Meldung (Info, Warning, Error, Success).

- Status-Meldungen anzeigen
- Fehler anzeigen
- Erfolge anzeigen
- Warnungen anzeigen

## Beispiele

### Status-Meldungen anzeigen

```jsx
<Alert type="info" title="Titel" message="Nachricht" />
```

### Fehler anzeigen

```jsx
<Alert type="info" title="Titel" dismissible={false} />
```

### Erfolge anzeigen

```jsx
<Alert type="info" title="Titel" closable={false} />
```

## Hinweise

- Barrierefreiheit: Rolle `alert`; Bedienelemente zusätzlich mit `label` oder `aria-label` benennen
- Gesten: `tap`
- Übergänge: `fade-in`, `collapse`
- Siehe auch: [toast](../../feedback/toast/), [badge](../../feedback/badge/), [progress](../../feedback/progress/)

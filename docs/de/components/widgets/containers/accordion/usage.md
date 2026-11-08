# Accordion - Verwendung

!!! note
    Die Beispiele bleiben syntaxneutral. Sobald die Umsetzung auf Rust und Blinc
    wechselt, werden die Beispiele in `usage.md` in einem eigenen Durchgang ersetzt.

## Anwendung

Ein Accordion ist ein Stapel von Kopfzeilen, die Inhalte ein- und ausklappen.

- Platz sparen durch Ein- und Ausklappen
- FAQ-Abschnitte
- Einstellungsgruppen
- Kategorien mit Unterpunkten

## Beispiele

### Platz sparen durch Ein- und Ausklappen

```jsx
<Accordion items={entries} onChange={action} />
```

### FAQ-Abschnitte

```jsx
<Accordion items={entries} collapsible={true} />
```

### Einstellungsgruppen

```jsx
<Accordion items={entries} animate={true} />
```

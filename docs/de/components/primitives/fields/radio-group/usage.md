# Radio Group - Verwendung

!!! note
    Die Beispiele bleiben syntaxneutral. Sobald die Umsetzung auf Rust und Blinc
    wechselt, werden die Beispiele in `usage.md` in einem eigenen Durchgang ersetzt.

## Anwendung

Eine Radio Group ist eine Gruppe von Optionsfeldern (Einfachauswahl).

- Auswahlmöglichkeiten
- Optionen
- Einstellungen

## Beispiele

### Auswahlmöglichkeiten

```jsx
<RadioGroup options={entries} onChange={action} />
```

### Optionen

```jsx
<RadioGroup options={entries} name="name" />
```

### Einstellungen

```jsx
<RadioGroup options={entries} showIcons={false} />
```

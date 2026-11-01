# Radio Group (Optionsgruppe) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Anwendung

Eine Radio Group ist eine Gruppe von Optionsfeldern (einzelfach).

- Auswahlmöglichkeiten
- Optionen
- Einstellungen

## Beispiele

### Auswahlmöglichkeiten

```jsx
<RadioGroup options={eintraege} onChange={aktion} />
```

### Optionen

```jsx
<RadioGroup options={eintraege} name="Name" />
```

### Einstellungen

```jsx
<RadioGroup options={eintraege} showIcons={false} />
```

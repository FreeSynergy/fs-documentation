# Date Input (Datumsfeld) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Anwendung

Ein Date Input ist ein Datumsauswahl-Feld mit Kalender.

- Geburtsdatum
- Terminauswahl
- Datumsangabe

## Beispiele

### Geburtsdatum

```jsx
<DateInput value="Wert" type="date" onChange={aktion} />
```

### Terminauswahl

```jsx
<DateInput value="Wert" type="date" minDate="minDate" />
```

### Datumsangabe

```jsx
<DateInput value="Wert" type="date" maxDate="maxDate" />
```

## Hinweise

- Zustände: `placeholder` (zusätzlich zu den Zuständen aus `base`)

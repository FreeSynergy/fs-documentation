# Datumsfeld – Verwendung

!!! note
    Die Beispiele bleiben syntaxneutral. Sobald die Implementierung auf Rust und
    Blinc umstellt, werden die Beispiele in `usage.md` in einem eigenen Durchgang ersetzt.

## Anwendung

Ein Datumsfeld ist ein Feld zur Datumsauswahl mit einem Kalender.

- Geburtsdatum
- Einen Termin auswählen
- Ein Datum angeben

## Beispiele

### Geburtsdatum

```jsx
<DateInput value="value" type="date" onChange={action} />
```

### Einen Termin auswählen

```jsx
<DateInput value="value" type="date" minDate="minDate" />
```

### Ein Datum angeben

```jsx
<DateInput value="value" type="date" maxDate="maxDate" />
```

## Hinweise

- Zustände: `placeholder` (zusätzlich zu den Zuständen aus `base`)

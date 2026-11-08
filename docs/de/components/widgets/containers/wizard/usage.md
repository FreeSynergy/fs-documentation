# Wizard - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden die Beispiele in `usage.md` in einem eigenen Durchlauf
    ersetzt.

## Anwendung

Ein Wizard ist ein schrittweises Formular für komplexe Aufgaben.

- Schritt-für-Schritt-Anleitungen
- Komplexe Formulare
- Einrichtungsassistenten
- Onboarding

## Beispiele

### Schritt-für-Schritt-Anleitungen

```jsx
<Wizard steps={entries} activeStep={0} onChange={aktion} />
```

### Komplexe Formulare

```jsx
<Wizard steps={entries} activeStep={0} validation={false} />
```

### Einrichtungsassistenten

```jsx
<Wizard steps={entries} activeStep={0} clickable={false} />
```

## Hinweise

- Zustände: `completed` (zusätzlich zu den Zuständen aus `base`)

# Wizard (Assistent) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Anwendung

Ein Wizard ist ein schritt-für-schritt-Formular für komplexe Aufgaben.

- Schritt-für-Schritt-Anleitungen
- Komplexe Formulare
- Einrichtungs-Assistenten
- Onboarding

## Beispiele

### Schritt-für-Schritt-Anleitungen

```jsx
<Wizard steps={eintraege} activeStep={0} onChange={aktion} />
```

### Komplexe Formulare

```jsx
<Wizard steps={eintraege} activeStep={0} validation={false} />
```

### Einrichtungs-Assistenten

```jsx
<Wizard steps={eintraege} activeStep={0} clickable={false} />
```

## Hinweise

- Zustände: `completed` (zusätzlich zu den Zuständen aus `base`)

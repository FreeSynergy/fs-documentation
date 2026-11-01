# Combobox (Kombinationsfeld) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Anwendung

Ein Combobox ist ein Textfeld + Dropdown.

- Adresssuche
- Kategorien
- Suchfeld

## Beispiele

### Adresssuche

```jsx
<Combobox value="Wert" onChange={aktion} />
```

### Kategorien

```jsx
<Combobox value="Wert" options={eintraege} />
```

### Suchfeld

```jsx
<Combobox value="Wert" placeholder="Platzhalter" />
```

## Hinweise

- Zustände: `placeholder` (zusätzlich zu den Zuständen aus `base`)

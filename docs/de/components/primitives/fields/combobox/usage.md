# Combobox – Verwendung

!!! note
    Die Beispiele bleiben syntaxneutral. Sobald die Implementierung auf Rust und
    Blinc umstellt, werden die Beispiele in `usage.md` in einem eigenen Durchgang ersetzt.

## Anwendung

Eine Combobox ist ein Textfeld plus eine Auswahlliste.

- Adresssuche
- Kategorien
- Suchfeld

## Beispiele

### Adresssuche

```jsx
<Combobox value="value" onChange={action} />
```

### Kategorien

```jsx
<Combobox value="value" options={entries} />
```

### Suchfeld

```jsx
<Combobox value="value" placeholder="placeholder" />
```

## Hinweise

- Zustände: `placeholder` (zusätzlich zu den Zuständen aus `base`)

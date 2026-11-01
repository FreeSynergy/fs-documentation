# Accordion (Akkordeon) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Anwendung

Ein Accordion ist ein Stapel von Kopfzeilen, die Inhalte ein-/ausklappen können.

- Platz sparen durch Ein-/Ausklappen
- FAQ-Sectionen
- Einstellungs-Gruppen
- Kategorien mit Unterpunkten

## Beispiele

### Platz sparen durch Ein-/Ausklappen

```jsx
<Accordion items={eintraege} onChange={aktion} />
```

### FAQ-Sectionen

```jsx
<Accordion items={eintraege} collapsible={true} />
```

### Einstellungs-Gruppen

```jsx
<Accordion items={eintraege} animate={true} />
```

# Field (Feld-Wrapper) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Standardfeld mit Hilfetext

```jsx
<Field label="Benutzername" for="username" help="Maximal 30 Zeichen.">
  <TextInput id="username" maxLength={30} />
</Field>
```

## Pflichtfeld mit Fehler

```jsx
<Field
  label="E-Mail"
  for="email"
  required={true}
  error={emailError}
>
  <TextInput id="email" type="email" value={email} />
</Field>
```

## Dichtes Formular (Label links)

```jsx
<Field label="Kategorie" for="cat" variant="horizontal">
  <Select id="cat" options={categories} />
</Field>
```

## Zeichenzähler im Textfeld

```jsx
<Field label="Notiz" for="note" counter={true}>
  <TextArea id="note" maxLength={500} />
</Field>
```

## Szenarien

| Szenario | Empfehlung |
|----------|------------|
| Alle Formularfelder | immer ein Field-Wrapper |
| Reine Beschriftung ohne Eingabe | [label](../../basics/label/) genügt |
| Suche in Leisten | `inline` ohne `help` |
| Detailansicht ohne Eingabe | description-list (geplant, Welle 2) |

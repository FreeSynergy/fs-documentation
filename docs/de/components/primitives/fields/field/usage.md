# Field - Verwendung

!!! note
    Die Beispiele bleiben syntaxneutral. Sobald die Umsetzung auf Rust und Blinc
    wechselt, werden die Beispiele in `usage.md` in einem eigenen Durchgang ersetzt.

## Standardfeld mit Hilfetext

```jsx
<Field label="Username" for="username" help="Höchstens 30 Zeichen.">
  <TextInput id="username" maxLength={30} />
</Field>
```

## Pflichtfeld mit Fehler

```jsx
<Field
  label="Email"
  for="email"
  required={true}
  error={emailError}
>
  <TextInput id="email" type="email" value={email} />
</Field>
```

## Dichtes Formular (Label links)

```jsx
<Field label="Category" for="cat" variant="horizontal">
  <Select id="cat" options={categories} />
</Field>
```

## Zeichenzähler in einem Textfeld

```jsx
<Field label="Note" for="note" counter={true}>
  <TextArea id="note" maxLength={500} />
</Field>
```

## Szenarien

| Szenario | Empfehlung |
|----------|------------|
| Alle Formularfelder | immer ein Field-Wrapper |
| Reine Beschriftung ohne Eingabe | [label](../../basics/label/) reicht |
| Suche in Leisten | `inline` ohne `help` |
| Detailansicht ohne Eingabe | [description-list](../../../widgets/data/description-list/) |

# Input Group (Feldgruppe) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Betrag mit Währungspräfix

```jsx
<InputGroup prefix={<span aria-hidden="true">€</span>}>
  <NumberInput id="amount" />
</InputGroup>
```

## URL ohne Protokoll-Wiederholung

```jsx
<InputGroup prefix="https://">
  <TextInput id="homepage" placeholder="example.org" />
</InputGroup>
```

## Telefon mit Ländercode (Nachfolger von phone-input)

```jsx
<InputGroup
  prefix={<CountrySelect value={cc} onChange={setCc} />}
>
  <TextInput id="phone" type="tel" />
</InputGroup>
```

## Suche mit Action-Button

```jsx
<InputGroup suffix={<IconButton icon="search" aria-label="Suchen" onClick={runSearch} />}>
  <TextInput id="q" placeholder="Suchen…" />
</InputGroup>
```

## Szenarien

| Szenario | Empfehlung |
|----------|------------|
| Währung/Einheit | `prefix` statisch |
| Ländercode zum Telefonfeld | `prefix` mit Select |
| In-Feld-Aktion (Suchen, Klar) | `suffix` mit Button |
| Nur Beschriftung/Hilfetext | [field](../field/), keine Gruppe |

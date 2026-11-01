# Input Group (Feldgruppe) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Anwendung

Die Gruppe wird um ein bestehendes Feld gebaut, nicht statt es. Beschriftung, Hilfetext
und Fehlermeldung bleiben außerhalb beim [field](../field/); die Gruppe enthält nur das
Feld und die Teile, die denselben Wert erklären.

## Beispiele

### Adresse mit Protokoll-Vorsatz

```jsx
<InputGroup prefix="https://" field={<TextInput value={host} onChange={setHost} />} />
```

### Beträge mit Einheit und Vorzeichen

```jsx
<InputGroup prefix="€" suffix="brutto" field={<NumberInput value={net} onChange={setNet} />} />
```

### Suche mit Aktion

```jsx
<InputGroup action="Suchen" onAction={runSearch} field={<TextInput value={q} onChange={setQ} />} />
```

### Landesvorwahl als Vorsatz-Auswahl

```jsx
<InputGroup prefixOptions={dialCodes} onPrefixChange={setDial}
            field={<NumberInput value={phone} onChange={setPhone} />} />
```

## Szenarien

| Szenario | Empfehlung |
|----------|------------|
| Einheit oder Vorzeichen | `prefix` bzw. `suffix`, keine eigene Beschriftung |
| Aktion am Feld | `action` plus `actionOnEnter`, Button beschriften |
| Landesvorwahl, Protokoll | `prefixOptions` statt Freitext |
| Passwort sichtbar/versteckt | `suffix` als Umschalt-Icon, mit `aria-label` |
| Feld mit Hilfetext | Gruppe im Feldbereich, [field](../field/) drumherum |

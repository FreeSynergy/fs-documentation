# Input Group - Verwendung

!!! note
    Die Beispiele bleiben syntaxneutral. Sobald die Umsetzung auf Rust und Blinc
    wechselt, werden die Beispiele in `usage.md` in einem eigenen Durchgang ersetzt.

## Anwendung

Die Gruppe wird um ein vorhandenes Feld gebaut, nicht anstelle davon. Label,
Hilfetext und Fehlermeldung bleiben außen beim [Field](../field/). Die Gruppe
enthält nur das Feld und die Teile, die denselben Wert erklären.

## Beispiele

### Eine Adresse mit Protokoll-Präfix

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

### Ländervorwahl als Präfix-Auswahl

```jsx
<InputGroup prefixOptions={dialCodes} onPrefixChange={setDial}
            field={<NumberInput value={phone} onChange={setPhone} />} />
```

## Szenarien

| Szenario | Empfehlung |
|----------|------------|
| Einheit oder Vorzeichen | `prefix` oder `suffix`, ohne eigene Beschriftung |
| Aktion am Feld | `action` plus `actionOnEnter`. Gib dem Button ein Label |
| Ländervorwahl, Protokoll | `prefixOptions` statt Freitext |
| Passwort sichtbar/verborgen | `suffix` als Umschalt-Icon, mit `aria-label` |
| Feld mit Hilfetext | Gruppe im Feldbereich, [field](../field/) außen herum |

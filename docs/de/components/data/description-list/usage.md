# Description List (Beschreibungsliste) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Anwendung

Die Liste steht in Detailansichten und Karten. Werte, die bearbeitet werden sollen,
führt man per Klick auf ein Feld über — die Liste selbst bleibt Darstellung.

## Beispiele

### Details eines Kontakts

```jsx
<DescriptionList items={contactFields} columns={2} copyable={true} />
```

### Metadaten in einer Karte

```jsx
<DescriptionList items={docMeta} variant="gestapelt" showEmpty={false} />
```

## Szenarien

| Szenario | Empfehlung |
|----------|------------|
| Detailseite eines Datensatzes | `columns = 2`, Gruppen für mehr als zwölf Werte |
| Schmale Seitenleiste | `variant = "gestapelt"` |
| Werte im Fließtext | `variant = "inline"` |

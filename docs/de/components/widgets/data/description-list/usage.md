# Description List - Verwendung

!!! note
    Die Beispiele bleiben syntaxneutral. Sobald die Umsetzung zu Rust und Blinc wechselt,
    werden die Beispiele in `usage.md` in einem eigenen Durchgang ersetzt.

## Anwendung

Die Liste steht in Detailansichten und Karten. Werte, die bearbeitet werden sollen, werden
durch Klick auf ein Feld geöffnet — die Liste selbst bleibt Darstellung.

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
| Detailseite eines Datensatzes | `columns = 2`, Gruppen bei mehr als zwölf Werten |
| Schmale Seitenleiste | `variant = "gestapelt"` |
| Werte im laufenden Text | `variant = "inline"` |

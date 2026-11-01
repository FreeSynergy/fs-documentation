# Range Calendar (Bereichskalender) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Anwendung

Der Kalender steht meist in einer Filterleiste oder einem Dialog. Das Ergebnis wird als
lesbarer Zeitraum außerhalb des Kalenders angezeigt.

## Beispiele

### Filter in einer Listenansicht

```jsx
<RangeCalendar from={from} to={to} months={2} onChange={applyFilter} />
```

### Abwesenheit eintragen

```jsx
<RangeCalendar min={today} maxRange={90} showCount={true} onChange={save} />
```

## Szenarien

| Szenario | Empfehlung |
|----------|------------|
| Berichtsfilter | `presets` mit 7, 30 und Quartal |
| Urlaub eintragen | `min = heute`, Tageszähler anzeigen |
| Mobile Filterleiste | `months = 1`, Wischgeste zum Monatswechsel |

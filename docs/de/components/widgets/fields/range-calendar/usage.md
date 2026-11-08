# Range Calendar - Verwendung

!!! note
    Die Beispiele bleiben syntaxneutral. Sobald die Umsetzung zu Rust und Blinc wechselt,
    werden die Beispiele in `usage.md` in einem eigenen Durchgang ersetzt.

## Anwendung

Der Kalender steht meist in einer Filterleiste oder einem Dialog. Das Ergebnis wird
außerhalb des Kalenders als lesbarer Zeitraum angezeigt.

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
| Filter für Berichte | `presets` mit 7, 30 und Quartal |
| Urlaub eintragen | `min = heute`, Tageszähler anzeigen |
| Filterleiste auf dem Smartphone | `months = 1`, Wischgeste zum Wechseln des Monats |

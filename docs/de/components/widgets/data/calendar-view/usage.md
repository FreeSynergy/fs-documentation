# Calendar View - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden die Beispiele in `usage.md` in einem eigenen Durchlauf
    ersetzt.

## Anwendung

Eine Calendar View zeigt Termine in einem Kalender.

- Termine anzeigen
- Kalender
- Planung
- Terminierung

## Beispiele

### Termine anzeigen

```jsx
<CalendarView date="date" events={entries} onChange={aktion} />
```

### Kalender

```jsx
<CalendarView date="date" events={entries} interactive={false} />
```

### Planung

```jsx
<CalendarView date="date" events={entries} interactive={false} />
```

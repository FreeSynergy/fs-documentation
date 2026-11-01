# Calendar View (Kalenderansicht) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Anwendung

Eine Calendar View zeigt Termine in einem Kalender an.

- Termine anzeigen
- Kalender
- Planung
- Scheduling

## Beispiele

### Termine anzeigen

```jsx
<CalendarView date="date" events={eintraege} onChange={aktion} />
```

### Kalender

```jsx
<CalendarView date="date" events={eintraege} interactive={false} />
```

### Planung

```jsx
<CalendarView date="date" events={eintraege} interactive={false} />
```

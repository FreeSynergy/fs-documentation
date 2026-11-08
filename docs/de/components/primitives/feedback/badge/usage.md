# Badge - Verwendung

!!! note
    Die Beispiele bleiben syntaxneutral. Sobald die Umsetzung auf Rust und Blinc
    wechselt, werden die Beispiele in `usage.md` in einem eigenen Durchgang ersetzt.

## Ein Zähler an der Navigation

```jsx
<BottomNavigationItem
  icon="mail"
  label="Posteingang"
  badge={<Badge variant="counter" value={unread} max={99} />}
/>
```

## Status an einem Listeneintrag

```jsx
<ListViewItem
  title="Anfrage 1042"
  badge={<Badge status="warning" value="in Prüfung" />}
/>
```

## Ein Punkt für neue Aktivität

```jsx
<Icon name="bell" badge={<Badge dot status="info" />} />
```

## Ein Zähler mit Text, den Screenreader verstehen

```jsx
<Badge
  variant="counter"
  value={openTasks}
  aria-label={openTasks + " offene Aufgaben"}
/>
```

## Szenarien

| Szenario | Empfehlung |
|----------|------------|
| Neue Nachrichten | `counter` an der Navigation |
| Pipeline-Status in Tabellen | `status` mit einer einheitlichen Farbpalette |
| Weniger Platz als 3 Zeichen | `dot` |
| Tags, die entfernt werden sollen | `tags-input`, kein Badge |

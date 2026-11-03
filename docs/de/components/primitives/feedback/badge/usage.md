# Badge (Abzeichen) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Zähler an der Navigation

```jsx
<BottomNavigationItem
  icon="mail"
  label="Posteingang"
  badge={<Badge variant="counter" value={unread} max={99} />}
/>
```

## Status an einem Listen-Eintrag

```jsx
<ListViewItem
  title="Antrag 1042"
  badge={<Badge status="warning" value="in Prüfung" />}
/>
```

## Punkt für neue Aktivitäten

```jsx
<Icon name="bell" badge={<Badge dot status="info" />} />
```

## Zähler mit verständlichem Text für Screenreader

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
| Pipeline-Status in Tabellen | `status` mit einheitlicher Farbpalette |
| Platz geringer als 3 Zeichen | `dot` |
| Tags, die entfernt werden sollen | `tags-input`, kein Badge |

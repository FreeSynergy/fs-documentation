# Card - Verwendung

!!! note
    Die Beispiele bleiben syntaxneutral. Sobald die Umsetzung auf Rust und Blinc
    wechselt, werden die Beispiele in `usage.md` in einem eigenen Durchgang ersetzt.

## Anwendung

Die Card ist ein Container-Element. Es zeigt Inhalte in einem strukturierten Kasten
mit Titel, Inhalt und optionalen Aktionen.

- Zusammengehörige Informationen gruppieren
- Inhalte optisch trennen
- Kleine Übersichten zeigen (z. B. Kunde, Aufgabe, Nachricht)

## Beispiele

### Zusammengehörige Informationen gruppieren

```jsx
<Card title="Title" subtitle="Subtitle" content="Content" />
```

### Inhalte optisch trennen

```jsx
<Card title="Title" subtitle="Subtitle" interactive={false} />
```

### Kleine Übersichten zeigen (z. B. Kunde, Aufgabe, Nachricht)

```jsx
<Card title="Title" subtitle="Subtitle" responsive={true} />
```

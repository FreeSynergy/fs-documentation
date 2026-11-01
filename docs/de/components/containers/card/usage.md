# Card - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Anwendung

Die Card (Karte) ist ein Container-Element, das Inhalte in einer strukturierten Box mit Titel, Inhalt und optionalen Aktionen darstellt.

- Gruppierung zusammengehöriger Informationen
- Visuelle Trennung von Inhalten
- Anzeige von Mini-Übersichten (z.B. Kunde, Aufgabe, Nachricht)

## Beispiele

### Gruppierung zusammengehöriger Informationen

```jsx
<Card title="Titel" subtitle="Untertitel" content="Inhalt" />
```

### Visuelle Trennung von Inhalten

```jsx
<Card title="Titel" subtitle="Untertitel" interactive={false} />
```

### Anzeige von Mini-Übersichten (z.B. Kunde, Aufgabe, Nachricht)

```jsx
<Card title="Titel" subtitle="Untertitel" responsive={true} />
```

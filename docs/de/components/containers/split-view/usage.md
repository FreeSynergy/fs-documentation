# Split View (Geteilter Bildschirm) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Anwendung

Ein Split View ist ein Layout mit zwei Bereichen side-by-side.

- Liste + Detailansicht
- Vergleichsansichten
- Sidebar + Hauptinhalt
- Previews

## Beispiele

### Liste + Detailansicht

```jsx
<SplitView leftContent="Inhalt" rightContent="Inhalt" />
```

### Vergleichsansichten

```jsx
<SplitView leftContent="Inhalt" collapsible={false} />
```

### Sidebar + Hauptinhalt

```jsx
<SplitView leftContent="Inhalt" responsive={true} />
```

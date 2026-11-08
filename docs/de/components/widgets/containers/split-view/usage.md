# Split View - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden die Beispiele in `usage.md` in einem eigenen Durchlauf
    ersetzt.

## Anwendung

Eine Split View ist ein Layout mit zwei nebeneinanderliegenden Bereichen.

- Listen- + Detailansicht
- Vergleichsansichten
- Sidebar + Hauptinhalt
- Vorschauen

## Beispiele

### Listen- + Detailansicht

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

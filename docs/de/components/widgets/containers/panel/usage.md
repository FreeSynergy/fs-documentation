# Panel (Container) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Anwendung

Ein Panel ist ein großer Container mit Header, Inhalt und Footer.

- Große Inhalt Blöcke
- Layout-Container
- Filter-Panel
- Dashboard-Widget

## Beispiele

### Große Inhalt Blöcke

```jsx
<Panel title="Titel" content="Inhalt" footer="footer" />
```

### Layout-Container

```jsx
<Panel title="Titel" content="Inhalt" collapsible={false} />
```

### Filter-Panel

```jsx
<Panel title="Titel" content="Inhalt" draggable={false} />
```

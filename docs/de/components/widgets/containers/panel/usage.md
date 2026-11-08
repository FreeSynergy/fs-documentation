# Panel - Verwendung

!!! note
    Die Beispiele bleiben syntaxneutral. Sobald die Umsetzung auf Rust und Blinc
    wechselt, werden die Beispiele in `usage.md` in einem eigenen Durchgang ersetzt.

## Anwendung

Ein Panel ist ein großer Container mit Kopfzeile, Inhalt und Fußzeile.

- Große Inhaltsblöcke
- Layout-Container
- Filterbereich
- Dashboard-Widget

## Beispiele

### Große Inhaltsblöcke

```jsx
<Panel title="Title" content="Content" footer="footer" />
```

### Layout-Container

```jsx
<Panel title="Title" content="Content" collapsible={false} />
```

### Filterbereich

```jsx
<Panel title="Title" content="Content" draggable={false} />
```

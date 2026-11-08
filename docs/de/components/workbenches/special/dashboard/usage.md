# Dashboard – Verwendung

!!! note
    Die Beispiele bleiben syntaxneutral. Sobald die Implementierung auf Rust und
    Blinc umstellt, werden die Beispiele in `usage.md` in einem eigenen Durchgang ersetzt.

## Anwendung

Ein Dashboard ist eine Übersichtsseite mit Widgets.

- Überblick
- Auswertung
- Projekt

## Beispiele

### Überblick

```jsx
<Dashboard widgets={items} />
```

### Auswertung

```jsx
<Dashboard widgets={items} dragAndDrop={true} />
```

### Projekt

```jsx
<Dashboard widgets={items} responsive={true} />
```

## Hinweise

- Gesten: `drag`

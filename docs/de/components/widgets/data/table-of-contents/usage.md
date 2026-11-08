# Table of Contents - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden die Beispiele in `usage.md` in einem eigenen Durchlauf
    ersetzt.

## Anwendung

Ein Inhaltsverzeichnis ist eine Übersicht über Kapitel und Abschnitte.

- Dokumentation
- Bücher
- Webseiten
- Kapitelübersicht

## Beispiele

### Dokumentation

```jsx
<TableOfContents items={entries} activeItem="activeItem" />
```

### Bücher

```jsx
<TableOfContents items={entries} collapsible={false} />
```

### Webseiten

```jsx
<TableOfContents items={entries} interactive={false} />
```

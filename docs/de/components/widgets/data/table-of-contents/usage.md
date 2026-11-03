# Table of Contents (Inhaltsverzeichnis) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Anwendung

Ein Table of Contents ist eine Übersicht über Kapitel/Sectionen.

- Dokumentation
- Bücher
- Webseiten
- Kapitelübersicht

## Beispiele

### Dokumentation

```jsx
<TableOfContents items={eintraege} activeItem="activeItem" />
```

### Bücher

```jsx
<TableOfContents items={eintraege} collapsible={false} />
```

### Webseiten

```jsx
<TableOfContents items={eintraege} interactive={false} />
```

# Scroll Area (Laufbereich) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Anwendung

Der Laufbereich bekommt ein festes Maß von außen (flexible Höhe der Spalte) und
übernimmt alles Weitere: Indikatoren, Verläufe, Nachladen, Follow.

## Beispiele

### Chatverlauf, der neuen Inhalt verfolgt

```jsx
<ScrollArea height="100%" direction="vertikal" follow={true} onEndReached={loadOlder} />
```

### Waagerechte Werkzeugleiste

```jsx
<ScrollArea direction="horizontal" scrollbar="automatisch" edges={true} />
```

## Szenarien

| Szenario | Empfehlung |
|----------|------------|
| Nachrichtenausgang | `follow = true`, Nachladen oben mit `keepPosition` |
| Tabelle in einer Karte | Laufbereich nur für die Körperzeilen, Kopf bleibt stehen |
| Werkzeugleiste schmal | `direction = "horizontal"`, Verläufe als Hinweis |

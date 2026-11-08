# Scroll Area - Verwendung

!!! note
    Die Beispiele bleiben syntaxneutral. Sobald die Umsetzung auf Rust und Blinc
    wechselt, werden die Beispiele in `usage.md` in einem eigenen Durchgang ersetzt.

## Anwendung

Der Scroll Area bekommt von außen eine feste Abmessung (flexible Höhe der
Spalte) und übernimmt alles andere: Anzeigen, Verläufe, Nachladen und Follow.

## Beispiele

### Ein Chatverlauf, der neuen Inhalten folgt

```jsx
<ScrollArea height="100%" direction="vertikal" follow={true} onEndReached={loadOlder} />
```

### Eine horizontale Werkzeugleiste

```jsx
<ScrollArea direction="horizontal" scrollbar="automatisch" edges={true} />
```

## Szenarien

| Szenario | Empfehlung |
|----------|------------|
| Nachrichtenausgang | `follow = true`, oben nachladen mit `keepPosition` |
| Tabelle in einer Card | Scroll Area nur für die Datenzeilen, die Kopfzeile bleibt stehen |
| Schmale Werkzeugleiste | `direction = "horizontal"`, Verläufe als Hinweis |

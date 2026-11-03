# Empty State (Leerer Zustand) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Anwendung

Der leere Zustand ersetzt die Liste, nicht einen Hinweis über der Liste. Er erscheint
erst, wenn feststeht, dass kein Inhalt da ist — während des Ladens steht ein Skeleton.

## Beispiele

### Erster Inhalt fehlt

```jsx
<EmptyState title="Noch keine Aufgaben" icon="task"
            actionLabel="Erste Aufgabe anlegen" hint="Strg N" onAction={create} />
```

### Filter ohne Treffer

```jsx
<EmptyState variant="kein-treffer" query={q} title="Kein Treffer"
            actionLabel="Filter zurücksetzen" onReset={clear} />
```

## Szenarien

| Szenario | Empfehlung |
|----------|------------|
| Bereich das erste Mal geöffnet | `variant = "leer"` mit Anlage-Aktion |
| Suche ergibt nichts | `variant = "kein-treffer"`, Suchbegriff anzeigen |
| Ladefehler | `variant = "fehler"` mit Wiederholen |

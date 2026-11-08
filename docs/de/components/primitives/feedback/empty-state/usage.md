# Empty State - Verwendung

!!! note
    Die Beispiele bleiben syntaxneutral. Sobald die Umsetzung auf Rust und Blinc
    wechselt, werden die Beispiele in `usage.md` in einem eigenen Durchgang ersetzt.

## Anwendung

Der Empty State ersetzt die Liste, nicht einen Hinweis über der Liste. Er erscheint
erst, wenn sicher ist, dass kein Inhalt da ist. Während des Ladens steht dort ein Skeleton.

## Beispiele

### Erster Inhalt fehlt

```jsx
<EmptyState title="Noch keine Aufgaben" icon="task"
            actionLabel="Erste Aufgabe anlegen" hint="Strg N" onAction={create} />
```

### Filter ohne Treffer

```jsx
<EmptyState variant="kein-treffer" query={q} title="Keine Treffer"
            actionLabel="Filter zurücksetzen" onReset={clear} />
```

## Szenarien

| Szenario | Empfehlung |
|----------|------------|
| Bereich wird zum ersten Mal geöffnet | `variant = "leer"` mit Aktion zum Anlegen |
| Suche liefert nichts | `variant = "kein-treffer"`, Suchbegriff anzeigen |
| Fehler beim Laden | `variant = "fehler"` mit Wiederholung |

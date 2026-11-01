# Hover Card (Vorschaukarte) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Anwendung

Die Karte hängt an einem Verweis. Sie wird nur geöffnet, wenn der Zeiger stabil auf dem
Auslöser liegt; der Inhalt kommt aus dem bereits geladenen Datensatz oder wird nachgeladen.

## Beispiele

### Profilvorschau an einem Namen

```jsx
<HoverCard target={user.id} variant="profil" placement="top" />
```

### Artikelauszug in einer Liste

```jsx
<HoverCard content={{ title, excerpt, updated }} openDelay={400} />
```

## Szenarien

| Szenario | Empfehlung |
|----------|------------|
| Name in Chatnachricht | `variant = "profil"`, `openDelay = 300` |
| Verweis in einer Tabelle | `variant = "dokument"`, `size = "small"` |
| Touch-Oberfläche | Langdruck, Karte als untere Leiste |

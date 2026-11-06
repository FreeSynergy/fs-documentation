# Link Preview (Linkvorschau) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt. Diese Seite ist eine Skizze (Entscheidung 2026-11-05).

## Anwendung

Zeigt die Vorschau eines Links innerhalb einer Nachricht.

## Beispiele

```jsx
<LinkPreview url={a.url} title={a.title} description={a.summary} image={a.image} />
```

## Szenarien

| Szenario | Empfehlung |
|---|---|
| Chat | `card` unter dem Text |
| Dichte Liste | `compact` |

## Einbettung in andere Programme (ADR 0037)

Vorschauen sind Teil der eingebetteten Nachrichtenansicht. Laut ADR 0037 ist jedes Programm mindestens eine Workbench, daher erscheint dieselbe Komponente kompakt in Projektverwaltung, Kontakten, Helpdesk und anderen, mit weniger Einstellungen. Wer mehr möchte, öffnet die Messenger-App. Die Komponente weiß nicht, welches Programm sie einbettet; Menüs, Gesten und Mausverhalten kommen vom Host-Frontend.

## Tastatur und Screenreader

- Fokussierbar als Link; Enter öffnet ihn.
- Das Bild hat einen leeren Alternativtext (dekorativ); der Titel trägt die Bedeutung.
- Das externe Ziel wird im zugänglichen Namen genannt.

# HTML View (HTML-Ansicht) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt. Diese Seite ist eine Skizze (Entscheidung 2026-11-05).

## Anwendung

Anzeige von fremdem HTML.

## Beispiele

```jsx
<HtmlView html={mail.htmlPart} baseParts={mail.inlineParts} onLinkClick={openLink} />
```

## Szenarien

| Szenario | Empfehlung |
|---|---|
| Mailtext | `sanitised` |
| Newsletter mit Einwilligung | `remote-allowed` |

## Einbettung in andere Programme (ADR 0037)

Jedes Programm, das Mails anzeigt, nutzt dieselbe Ansicht. Laut ADR 0037 ist jedes Programm mindestens eine Workbench, daher erscheint dieselbe Komponente kompakt in Projektverwaltung, Kontakten, Helpdesk und anderen, mit weniger Einstellungen. Wer mehr möchte, öffnet die Messenger-App. Die Komponente weiß nicht, welches Programm sie einbettet; Menüs, Gesten und Mausverhalten kommen vom Host-Frontend.

## Tastatur und Screenreader

- Der Inhalt ist über den Dokumentmodus des Screenreaders navigierbar.
- Links sind fokussierbar und nennen ihre Zieldomain.
- Bilder ohne Alternativtext werden übersprungen.

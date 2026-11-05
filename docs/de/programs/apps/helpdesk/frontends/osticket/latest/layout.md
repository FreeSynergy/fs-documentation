# osTicket - Struktur und UI/UX

## Seitenstruktur

```
Agentenliste:
┌────────────────────────────────────────────────────────────┐
│ Dashboard | Tickets | Kunden | Wissen | Dateien | Admin    │
│ Filter: [alle ▾][Status: offen ▾]         [+ Neues Ticket] │
├────┬──────────┬──────────────────┬────────┬───────────────┤
│ ☐  | #4711    | Zahlung fehlgesch│ Beta   | 2 h her       │
│ ☐  | #4712    | Drucker offline  | Alpha  | gestern       │
├────┴──────────┴──────────────────┴────────┴───────────────┤
│ Ticket #4711                              [⋯ Aktionen ▾]  │
│ Von: b@example.org  An: support@…  Status: open (SLA:4h)  │
│ ── Thread ──────────────────────────────────────────────── │
│ [Antwort] [Weiterleiten] [Notiz]  <editor>  [Anhang]      │
│ Interne Notiz ☐   [Ticket schließen]                      │
└────────────────────────────────────────────────────────────┘
```

## UI/UX

- funktionaler Tabellen-Stil, Grau/Blau-Standard; keine Themes ohne Template-Arbeit
- Masken sind klickpfadlastig (viele Formulare, wenige Overlays)

## Interaktionen

- **Kein Drag & Drop**, keine Live-Updates (manuell aktualisieren)
- Antwort-/Notiz-Editor: einfacher Rich-Text (HTML)
- Ticket-Aktionen als Dropdown mit Dialogen

## Responsive Design

- Portal responsive (Bootstrap-artige Breakpoints seit v1.10+), Agenten-UI nur eingeschränkt — für Mobilnutzung Portal oder API-Clients nutzen

## Accessibility

- klassische HTML-Formulare, Tab-Reihenfolge ok; Farbsignale (SLA-Fälligkeit) zusätzlich als Text
- Screenreader: Tabellenüberschriften vorhanden, aber Masken sind lang — ARIA-Ausbau unvollständig

## Performance

- MySQL-LIKE-Suche skaliert schlecht; Trennen von Archiv/Instanz empfohlen

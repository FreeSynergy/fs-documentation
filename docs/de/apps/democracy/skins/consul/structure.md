# Consul - Struktur und UI/UX

## Seitenstruktur

```
┌──────────────────────────────────────────────────────────────────┐
│ Stadtportal „Consul“   Startseite | Teilnahme | Haushalts…       │
├──────────────────────────────────────────────────────────────────┤
│ Kacheln der Beteiligungsarten (Vorschläge · Haushalt · Polls)    │
│ Vorschlagsliste: Titel | Thema | Support-Zähler | Diskussion     │
│ Detail: Text, Karte, [Unterstützen], Kommentarthemen             │
│ Haushalt: Abschnitt „250k€“ → Projekte-Grid mit ☑-Auswahl        │
└──────────────────────────────────────────────────────────────────┘
```

## UI/UX

- behördlich-freundlich; Supports als Herz-Zähler sichtbar
- Phase/Deadline-Banner pro Beteiligung

## Interaktionen

- Unterstützen (Verifizierung nötig), Kommentare (Threads), Melden (Moderation)
- Haushalts-Grid: max. n Projekte ankreuzen (Kontrolllogik inline)

## Responsive Design

- responsiv (Bürgermobil-Nutzung Standard)

## Accessibility

- Basis-Web-Standards; Kontraste je Theme

## Performance

- große Vorschlagslisten: Themen-/Statusfilter nötig; API-Caching für Stats

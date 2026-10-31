# Decidim - Struktur und UI/UX

## Seitenstruktur

```
┌──────────────────────────────────────────────────────────────────┐
│ Organisation   Prozesse …            Anmelden | Registrierung    │
├──────────────────────────────────────────────────────────────────┤
│ Prozess „Haushalt 2027“ — Phase: Priorisierung (bis 15.11)       │
│ Reiter: Vorschläge | Treffen | Budgets | Ergebnisse             │
│ Vorschlagsliste: Titel · Thema · Supports ✓128 · Kommentare 24  │
│ Detail: Text, Karte, Unterstützen-Knopf, Kommentar-Thread       │
└──────────────────────────────────────────────────────────────────┘
```

- Phase als Statusbanner; Komponenten als Reiter; Supports mit Zähler

## UI/UX

- ruhig-institutionelles Design (Tailwind-System der neuen Versionen), klare Typo
- Moderationswerkzeuge (Melden-Button) sichtbar für Teilnehmende

## Interaktionen

- Unterstützen per Klick (Verifizierung nötig); Kommentare mit Antwortbäumen
- Admin-Formulare mehrstufig (Prozess-Assistent)

## Responsive Design

- vollständig responsiv (Mobil-Beteiligung ist Ziel)

## Accessibility

- WCAG-Bemühungen dokumentiert (Kontraste, Tastaturformulare)

## Performance

- große Prozesse (tausende Vorschläge) mit Themen-Filter; Admin-Bereiche cachen wenig

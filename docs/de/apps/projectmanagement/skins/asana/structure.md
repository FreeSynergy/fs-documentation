# Asana - Struktur und UI/UX

## Seitenstruktur

```
┌──────────────────────────────────────────────────────────────────┐
│ Asana  🔍 Suche…                                  [+] [🔔] [👤]  │
├────────────────┬─────────────────────────────────────────────────┤
│ Meine Aufgaben │ Projekt „Website“ – Ansicht: Liste ▾ Timeline   │
│ Heute          │ ▸ Bereich Launch                                │
│ Heute+7        │   ☐ Copy final  👤Anna 📅 31.10 🔗2              │
│ Projekte       │   ☐ Hosting umstellen 👤Ben                    │
│ Portfolios     │ ▸ Bereich Rechtliches                          │
│ Workloads      │   ☐ Impressum …                                │
│ Goals          │        Rechtsklick → Aufgaben-Panel rechts     │
└────────────────┴─────────────────────────────────────────────────┘
```

- Aufgaben-Panel (rechts) mit Reiter-Charakter: Details | Kommentare | Abhängigkeiten

## UI/UX

- Asana-Design (Korall/Violett-Akzente), ruhige Typografie, hohe Konsistenz
- Tabs je Ansicht; Drag für Reihenfolge und Abhängigkeiten (Timeline)

## Interaktionen

- **Schnellerfassung** durch Tippen in Listen (Enter = nächste Aufgabe)
- `Tab`+Name weist schnell zu; Kommentare mit @ und Strg+Enter
- Teil-Live: neue Kommentare/Benachrichtigungen pushen in die Inbox

## Responsive Design

- Web responsiv; Mobile-Apps voll funktional (Timeline eingeschränkt)

## Accessibility

- WCAG-Berichte publiziert; Tastaturmodus `?` (siehe [shortcuts.md](shortcuts.md))

## Performance

- große Portfolios (10k Aufgaben) laden Abschnittsweise; Workload-Charts cachen

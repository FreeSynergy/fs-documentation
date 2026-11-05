# Monica - Struktur und UI/UX

## Seitenstruktur

```
┌───────────────────────────────────────────────────────────────────┐
│ Monica  [Dashboard][Contacts][Activities][Tasks][Gifts][Settings] │
├──────────────────────────┬────────────────────────────────────────┤
│ Kontaktliste (links)     │ Kontaktseite                          │
│ 🔍 Suche…                │ ┌──────────────────────────────────┐  │
│ ○ Andrea Berg ★          │ │ [Foto] Andrea Berg   ⋯           │  │
│ ○ Ben Klein              │ │ Partnerin · Berlin · 41          │  │
│ ○ Beta GmbH              │ │ ────────────────────────────────  │  │
│ + Kontakt                │ │ Reiter: About | Activities |      │  │
│                          │ │ Tasks | Relationships | Gifts     │  │
│                          │ │ ────────────────────────────────  │  │
│                          │ │ Timeline: 03.11 Wanderung (⛰)    │  │
│                          │ │           12.10 Anruf (10 min)   │  │
│                          │ └──────────────────────────────────┘  │
└──────────────────────────┴────────────────────────────────────────┘
```

- Kontaktseite = Reiter mit Timeline; „Add activity“-Form immer präsent
- Dashboard zeigt Geburtstage, ausstehende Aufgaben, „für dich wichtige Leute“

## UI/UX

- ruhige Karten-Optik, Akzentfarbe Blau; Hell/Dunkel-Theme (neuere Versionen)
- Masken folgen Laravel-Standardformularen, inline editierbar, viel „+“-Knöpfe

## Interaktionen

- **Schnellerfassung**: Aktivitäten direkt vom Dashboard („What did you do?“)
- **Drag & Drop**: ❌ nicht vorhanden
- **Animationen**: dezente Fade-Übergänge der Reiter; Timeline-Einträge blenden ein

## Responsive Design

| Breite | Verhalten |
|--------|-----------|
| Desktop | Zwei-Spalten + Reiter |
| Tablet/Mobil | einspaltig, Navigation als Dropdown |

## Accessibility

- HTML-Formulare/Tabellen, Tastaturtabellen ok, Beschriftungen vorhanden
- Timeline als Liste mit Datumsangaben — screenreader-freundlich
- Farbaccent zusätzlich textlich markiert (Stern, Typnamen)

## Performance

- Instanzen mit > 50k Aktivitäten bleiben schnell (paginierte Timeline); Cron-Läufe für Erinnerungen planen

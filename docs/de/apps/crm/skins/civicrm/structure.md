# CiviCRM - Struktur und UI/UX

## Seitenstruktur

```
┌────────────────────────────────────────────────────────────────┐
│ CMS-Leiste (Drupal/WP/Joomla)                                  │
│ Contacts | Contributions | Events | Memberships | Administer   │
├──────────────────────────────┬─────────────────────────────────┤
│ Suchergebnis / Dashboard     │ Kontakt: Andrea Berg            │
│ 🔍 Find Contacts             │ [Actions ▾]                     │
│ ┌──────────────────────────┐ │ Reiter: Activities | Mailings | │
│ │ ☐ Andrea Berg  ber…      │ │ Contributions | Events |        │
│ │ ☐ Beta GmbH              │ │ Memberships | Relationships |   │
│ └──────────────────────────┘ │ Tags | Custom                   │
│ Saved Searches               │ ── Inhalt des Reiters ──        │
│ Dashboard-Kachelen           │ (Tabellen + Add-Aktionen)       │
└──────────────────────────────┴─────────────────────────────────┘
```

- Der Charakter ist „CMS-Seite mit CRM-Inhalt“: Formulare, Tabellen, Reiter
- Öffentlich: Event-Registrierungs-/Spendenformulare als CMS-Seiten (Popup-Widget „Find Contributions“ möglich)

## UI/UX

- funktionaler backend-Stil, nicht einheitlich (historisch gewachsen); Seitenthema folgt dem CMS
- Cividashboards + SearchKit-Adminseiten moderner als Alt-Forms

## Interaktionen

- Massenaktionen über Checkboxen + Actions-Button
- Inline-Picker für Beziehungen/Tags (AJAX-Autocomplete)
- keine Live-Updates, Reload-basiert

## Responsive Design

- Verwaltungsseiten bedingt responsiv (Kernmasken okay,Report-artige Massenmasken schlecht)
- öffentliche Formulare (Events/Beiträge) responsive dank Templates

## Accessibility

- folgt CMS-Grundlagen; Formulare beschriftet, aber Autocomplete-Widgets schwach
- Tastaturtabellen ok; Actions-Menüs per Tab erreichbar

## Performance

- große Datenbestände (1 Mio.+ Kontakte) brauchen DB-Index-Tuning und Caching (Varmast); SearchKit nutzt SQL-Optimierung

# Mailchimp - Struktur und UI/UX

## Layout

```
┌───────────────────────────────────────────────────────────────┐
│ Mailchimp   Suche…                       [Create]  🐒 👤      │
├──────────┬────────────────────────────────────────────────────┤
│ Dashboard│ Audience „Newsletter“: 4.312 Kontakte              │
│ Campaigns│  Segment „Spen­der“ ▾  [Export] [Import]           │
│ Audience │  Tabelle: Email | Tags | Fields | Abwesenheit      │
│ Automations│ Journey-Builder: Trigger → [Mail] → [Delay] →   │
│ Content  │              [Condition] → [Mail/Tag]             │
│ Analytics│  Reports mit Öffnungs-/Klickkurven                 │
└──────────┴────────────────────────────────────────────────────┘
```

- Kontakte-Tabelle zentral; Journey-Builder horizontaler Fluss

## UI/UX

- freundliches Gelb-Affe-Branding; geführte Wizards („Kampagne starten“)
- Kampagnen-Editor: Blockpalette + Live-Vorschau (Desktop/Mobil)

## Interaktionen

- Tag-/Segment-Zuweisung inline; CSV-Import mit Spalten-Mapping
- Journey-Knoten per Drag, Bedingungen als Entscheidungs-Rauten

## Responsive Design

- Desktop-zentriert; Mobile-App nur Reports/Notifications

## Accessibility

- Standard-Web; Editor-Blöcke tastaturbedienbar

## Performance

- große Audiences (100k+) mit Segment-Cache; API-Pagination obligatorisch

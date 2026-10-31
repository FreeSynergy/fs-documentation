# Mautic - Struktur und UI/UX

## Layout

```
┌─────────────────────────────────────────────────────────────────┐
│ Mauticoberfläche  Suche…                    ⚙ 👤                │
├──────────┬──────────────────────────────────────────────────────┘
│ Kontakte │ Kontaktansicht: Felder links, Aktivitäten rechts,
│ Kampagnen│   Punkte-Balken, Tags (Chips)
│ E-Mails  │ Kampagnen-Canvas: (Trigger)─┬─(If/Else)─(Mail)
│ Formulare│                             └─(Wait 3d)─(Tag)
└──────────┴──────────────────────────────────────────────────────┘
Segment-/Listenfilter oben; CSV-Import-Master links
```

## UI/UX

- Standard-Admin-Optik; Canvas horizontal (Baum von links)
- Kontakt-Detail = Chronik-Log (Timeline aller Interaktionen)

## Interaktionen

- Drag im Canvas (Knoten verbinden); Segment-Regeln als Dropdown-Ketten
- Import-Master mit Vorschau-/Feldzuordnung

## Responsive Design

- Desktop; mobile Pflege nicht vorgesehen (API stattdessen)

## Accessibility

- Standard-HTML; Formulare/Buttons getaggt

## Performance

- Cron-Batches (Kampagnen, Segment-Refresh) sind der Engpass → Server-Tuning/Queue

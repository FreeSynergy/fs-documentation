# Dolibarr - Structure and UI/UX

## Page layout

```
┌──────────────────────────────────────────────────────────────────┐
│ Logo      Recherche……                    [Neu ▾]  👤 ⚙           │
├──────────┬───────────────────────────────────────────────────────┤
│ Tiers    │ Liste Kunden: Ref | Name | Status | Ort | actions 🔘  │
│ Commercial│ „Société Dupont“ (Fiche): Reiter Infos/Contacts/    │
│ Produits │ Docs/Kommentare · Links (Angebote/Rechnungen)        │
│ Compta   │ Dokument: Nummernkopf + Positionstabellen + Total    │
│ ⚙        │ Statuschip: brouillon→validée→payée                  │
└──────────┴───────────────────────────────────────────────────────┘
```

- Left: module menu; centre: lists/forms; right: columns for dashlets ("spectrum")

## UI/UX

- functional and dense, tab-based forms; colored status chips with text
- "New" menu per module for creating documents

## Interactions

- Mass selection (☑ + actions: print, e-mail dispatch …), object printing (slips), import wizard
- No drag & drop concept

## Responsive design

- Web responsive (newer versions with a mobile skin), no native app

## Accessibility

- Standard HTML forms; lists are tabular; language files (de-DE available)

## Performance

- Suitable for shared hosting; large document volumes → indexes + archive-year filter

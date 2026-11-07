# Sage - Structure and UI/UX

## Interfaces (per product)

```
Business Cloud (Web):  Kachel-Start · Belege-Liste · Bank-Feed-Reconciliation
Sage 50/100 (Windows): MDI-Fenster, Funktionsbaum links,
                       Buchungsformulare mit Kontenspalten,
                       Reports als Listen/Druckdialoge
Sage X3 (Web):         Startpages (KPI-Kacheln) → Funktionsmenüs →
                       Tabellen-Grids mit „Bearbeitungsblöcken“
```

- Cloud: modern, guided; 50/100: Windows territory with keyboard focus
- X3: function-code heavy (menus with codes such as `SALINH`), oriented to power users

## UI/UX

- German versions with tax/month-end closing wizards
- Forms table-typical (debit/credit columns), mass postings as batches

## Interactions

- Keyboard control in Windows masks is strong (account search via reference/description)
- X3: grid editing, scheduling of "flows" (batches)

## Responsive design

Only Cloud products are responsive; Windows clients are fixed to the desktop

## Accessibility

Windows base (screen readers vary by version); Cloud standard web

## Performance

On-premise scales via DB tuning; observe SaaS export limits

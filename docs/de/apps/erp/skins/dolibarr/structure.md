# Dolibarr - Struktur und UI/UX

## Seitenlayout

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

- Links das Modulmenü, Mitte Listen/Formulare, Rechts Spalten für Dashlets („spectrum“)

## UI/UX

- funktional-dicht, Tab-basierte Formulare; Statuschips farbig mit Text
- „Neu“-Menü je Modul für Dokumentanlage

## Interaktionen

- Massenauswahl (☑ + Aktionen: drucken, E-Mail-Versand …), Objektdruck (Zettel), Import-Assistent
- Kein Drag&Drop-Konzept

## Responsive Design

- Web responsive (neue Versionen mit mobilem Skin), keine native App

## Accessibility

- Standard-HTML-Formulare; Listen tabellarisch; Sprachdateien (de-DE vorhanden)

## Performance

- Shared-Hosting-tauglich; große Dokumentmassen → Indizes + Archivjahr-Filter

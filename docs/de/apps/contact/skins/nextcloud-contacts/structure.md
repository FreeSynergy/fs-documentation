# Nextcloud Contacts - Struktur und UI/UX

## Seitenstruktur

```
┌────────────────────────────────────────────────────────────────┐
│ Nextcloud-Leiste (🔍 Suche, 👤)                                │
├──────────────────┬─────────────────────────────────────────────┤
│ Adressbücher     │ Kontaktliste          │ Detail-/Editierpanel│
│ 📇 Persönlich    │ A ─ Andrea Berg       │ ✎ Andrea Berg       │
│ ★ Gelb (System)  │ B ─ Ben Klein         │ 📧 andrea…          │
│ ○ Arbeit (geteilt│ B ─ Beta GmbH         │ ☎ +49…              │
│ + Adressbuch     │ …                     │ ✚ Feld              │
│ 🗑 Gelöscht      │ [☑ Auswahl] [Import]  │ ♪ Geburtstag        │
└──────────────────┴─────────────────────────────────────────────┘
```

- Dreispaltiges Master-Detail-Layout; Auswahl-Checkboxen für Massenaktionen (Löschen, Herunterladen, Hinzufügen zu Buch)
- Editieren inline im Detailpanel, „Feld hinzufügen“-Menü nach vCard-Kategorien

## UI/UX

- follows Nextcloud-Designsystem (Team-Dialog), Hell/Dunkel je Instanz-Theme
- Initialen-Avatare, Fotos, Favoriten-Stern
- Suche in Echtzeit über Name, Organisation, Telefon, E-Mail

## Interaktionen

- **Drag & Drop**: `.vcf`-Dateien direkt in die Liste ziehen
- **Rechtsklick auf Kontakt** (neuere Versionen): Kontextmenü mit Herunterladen/Löschen
- **Animationen**: Panel-Übergänge als Cross-fade, Listenvirtualisierung ohne Sprünge

## Responsive Design

| Breite | Verhalten |
|--------|-----------|
| Desktop | drei Spalten |
| Tablet | Liste + aufklappbares Detail |
| Mobil | einspaltig, Liste → Detail-Overlay |

## Accessibility

- DOM-Formulare, Tastaturtabellen ok; Screenreader-Labels für Feldtypen vorhanden
- Massenaktionstabellen mit Checkboxen — vollständig per Tastatur bedienbar
- Farb-Badges (geteilt) zusätzlich mit Text

## Performance

- Bei > 10.000 Kontakten initial längeres Laden (Sync-Status); Versionen mit Delta-Sync verbessern das spürbar

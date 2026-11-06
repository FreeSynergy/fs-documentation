# GNOME Contacts - Struktur und UI/UX

## Fensterstruktur

```
┌────────────────────────────────────────────────────────┐
│ ⌕ Suche…            GNOME Kontakte            ⋮        │  (HeaderBar)
├───────────────────────────┬────────────────────────────┤
│ Kontaktkarten (Liste)     │ Kontakt-Karte (Detail)     │
│ ┌──────────┐ ┌──────────┐ │ ┌────────────────────────┐ │
│ │[F] Andrea│ │[F] Ben   │ │ │ [Foto] Andrea Berg     │ │
│ │ Andrea   │ │ Ben      │ │ │ 📧 a@… ✎ ☎ +49… ✎      │ │
│ └──────────┘ └──────────┘ │ │ ✚ Feld · Quelle: Persön.│ │
│ …                         │ │ [Bearbeiten]           │ │
│                           │ └────────────────────────┘ │
└───────────────────────────┴────────────────────────────┘
```

- Raster aus Kontaktkarten; Detail rechts als überlagerndes Panel (Schalter „Bearbeiten“)
- HeaderBar enthält Suche, „Neuer Kontakt“, Menü ⋮

## UI/UX

- libadwaita-Design: runde Karten, klare Typo, Hell/Dunkel nach System
- Sehr wenig sichtbare Bedienelemente — Moduswechsel „Ansicht ⇄ Bearbeiten“

## Interaktionen

- **Schnellbearbeitung**: Im Editier-Modus sind alle Felder inline; `Tab` springt weiter
- **Feld hinzufügen**: „+“-Menü mit Kategorie-Untermenüs (Telefontypen, Adresstypen)
- **Karten verknüpfen**: Auswahl zweier Kontakte → „Zusammenführen“
- **Animationen**: Karten-Transitions (libadwaita-Standard-Fades)

## Responsive Design

| Breite | Verhalten |
|--------|-----------|
| Desktop | Raster + Detail daneben |
| Mobil (GNOME Mobile/Phone) | einspaltig, Detail als Push-Navigation |

## Accessibility

- GTK4/ATK: vollständige Tastaturnavigation, Screenreader-labels, Fokus-Sichtbarkeit
- Tastaturkürzel siehe [shortcuts.md](shortcuts.md)

## Performance

- EDS-Cache: tausende Kontakte flüssig; LDAP-Quellen mit langsamem Server bremsen die Suche
